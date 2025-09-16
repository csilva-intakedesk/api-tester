#!/usr/bin/env bash
set -euo pipefail

# start_with_ngrok.sh
# Starts uvicorn for app.main:app, waits for health endpoint, then starts ngrok and forwards logs.

UVICORN_CMD=("uvicorn" "app.main:app" "--reload" "--host" "127.0.0.1" "--port" "8000")
NGROK_CMD=("ngrok" "http" "http://127.0.0.1:8000")

LOGDIR="./.logs"
mkdir -p "$LOGDIR"
UVICORN_LOG="$LOGDIR/uvicorn.log"
NGROK_LOG="$LOGDIR/ngrok.log"

# Start uvicorn in background
echo "Starting uvicorn..."
"${UVICORN_CMD[@]}" > "$UVICORN_LOG" 2>&1 &
UVICORN_PID=$!

echo "uvicorn started with PID $UVICORN_PID, logging to $UVICORN_LOG"

# Function to cleanup child processes on exit
cleanup() {
  echo "Shutting down..."
  if kill -0 "$NGROK_PID" 2>/dev/null; then
    echo "Killing ngrok (PID $NGROK_PID)"
    kill "$NGROK_PID" || true
  fi
  if kill -0 "$UVICORN_PID" 2>/dev/null; then
    echo "Killing uvicorn (PID $UVICORN_PID)"
    kill "$UVICORN_PID" || true
  fi
  wait 2>/dev/null || true
}
trap cleanup EXIT INT TERM

# Wait for uvicorn to be healthy
HEALTH_URL="http://127.0.0.1:8000/healthz"
MAX_RETRIES=30
SLEEP_SECONDS=1

echo "Waiting for server to respond at $HEALTH_URL..."
for i in $(seq 1 $MAX_RETRIES); do
  if curl -s --max-time 1 "$HEALTH_URL" | grep -q "status"; then
    echo "Server is up (after $i attempts)"
    break
  fi
  if ! kill -0 "$UVICORN_PID" 2>/dev/null; then
    echo "Uvicorn process exited unexpectedly. Check $UVICORN_LOG"
    exit 1
  fi
  sleep $SLEEP_SECONDS
  if [ "$i" -eq "$MAX_RETRIES" ]; then
    echo "Timed out waiting for server to become healthy. Check $UVICORN_LOG"
    exit 1
  fi
done

# Verify ngrok is available
if ! command -v ngrok >/dev/null 2>&1; then
  echo "ngrok not found in PATH. Please install ngrok: https://ngrok.com/"
  echo "Shutting down uvicorn (PID $UVICORN_PID)"
  if kill -0 "$UVICORN_PID" 2>/dev/null; then
    kill "$UVICORN_PID" || true
  fi
  exit 1
fi

# Start ngrok in background so we can monitor its exit code
echo "Starting ngrok..."
"${NGROK_CMD[@]}" > "$NGROK_LOG" 2>&1 &
NGROK_PID=$!

echo "ngrok started with PID $NGROK_PID, logging to $NGROK_LOG"

# Attempt to extract the public forwarding URL using ngrok's local API first
NGROK_PUB_URL_FILE="$LOGDIR/ngrok_url.txt"
PUBLIC_URL=""
NGROK_URL_MAX_RETRIES=30
NGROK_URL_SLEEP=0.5
NGROK_API_URL="http://127.0.0.1:4040/api/tunnels"
echo "Waiting for ngrok to publish a forwarding URL (API -> $NGROK_API_URL)..."
for j in $(seq 1 $NGROK_URL_MAX_RETRIES); do
  # Check ngrok still running
  if ! kill -0 "$NGROK_PID" 2>/dev/null; then
    echo "ngrok process exited before publishing a URL. Check $NGROK_LOG"
    break
  fi

  # Try ngrok local API
  API_OUT=$(curl -s --max-time 1 "$NGROK_API_URL" || true)
  if [ -n "$API_OUT" ]; then
    # Extract public_url fields and prefer https
    PUBLIC_URL=$(echo "$API_OUT" | grep -oE '"public_url":"https?://[^"]+' | head -n1 | sed -E 's/"public_url":"//') || true
    if [ -n "$PUBLIC_URL" ]; then
      echo "$PUBLIC_URL" > "$NGROK_PUB_URL_FILE"
      echo "Public URL (from API): $PUBLIC_URL"
      break
    fi
  fi

  # Fallback: try parsing the ngrok log for Forwarding lines
  PUBLIC_URL=$(grep -m1 'Forwarding' "$NGROK_LOG" 2>/dev/null | grep -oE 'https?://[^ ]+' | grep -m1 '^https://' || true)
  if [ -n "$PUBLIC_URL" ]; then
    echo "$PUBLIC_URL" > "$NGROK_PUB_URL_FILE"
    echo "Public URL (from log): $PUBLIC_URL"
    break
  fi

  sleep $NGROK_URL_SLEEP
done

# Tail logs to console so user can see both outputs
tail -n +1 -f "$UVICORN_LOG" &
TAIL_UV_PID=$!

tail -n +1 -f "$NGROK_LOG" &
TAIL_NG_PID=$!

# Wait for ngrok process. If ngrok exits with a non-zero code, shut down uvicorn and exit with the same code.
wait "$NGROK_PID"
NGROK_EXIT=$?
if [ "$NGROK_EXIT" -ne 0 ]; then
  echo "ngrok exited with code $NGROK_EXIT; shutting down uvicorn (PID $UVICORN_PID)"
  if kill -0 "$UVICORN_PID" 2>/dev/null; then
    kill "$UVICORN_PID" || true
  fi
fi

# Clean up tails
kill "$TAIL_UV_PID" "$TAIL_NG_PID" 2>/dev/null || true

echo "Done (ngrok exit code: $NGROK_EXIT)."
exit "$NGROK_EXIT"
