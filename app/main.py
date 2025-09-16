from fastapi import FastAPI
from app.routers import (
    litify,
    litify_czar,
    awko,
    saddle,
    smart_case_works,
    weitz,
    napoli,
)

app = FastAPI(title="api-tester")

# Register routers via a list to avoid repeating include_router calls
routers = [
    (litify.router, "/litify", ["litify"]),
    (litify_czar.router, "/litify_czar", ["litify_czar"]),
    (awko.router, "/awko", ["awko"]),
    (saddle.router, "/saddle", ["saddle"]),
    (smart_case_works.router, "/smart_case_works", ["smart_case_works"]),
    (weitz.router, "/weitz", ["weitz"]),
    (napoli.router, "/napoli", ["napoli"]),
]

for router_obj, prefix, tags in routers:
    app.include_router(router_obj, prefix=prefix, tags=tags)


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}
