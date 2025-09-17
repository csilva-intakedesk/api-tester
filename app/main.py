"""
Copyright (c) 2025 IntakeDesk LLC. All rights reserved.
Proprietary and Confidential. Unauthorized copying, use, modification,
or distribution is prohibited.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.routers import (
    awko,
    litify,
    litify_czar,
    napoli,
    saddle,
    smart_case_works,
    weitz,
)

app = FastAPI(title="api-tester")

routers = [
    (litify.router, "litify"),
    (litify_czar.router, "litify_czar"),
    (awko.router, "awko"),
    (saddle.router, "saddle"),
    (smart_case_works.router, "smart_case_works"),
    (weitz.router, "weitz"),
    (napoli.router, "napoli"),
]

for router_obj, tag in routers:
    prefix = f"/{tag}"
    app.include_router(router_obj, prefix=prefix, tags=[tag])


@app.get("/healthz", response_class=JSONResponse)
async def healthz() -> JSONResponse:
    payload = {"status": "ok"}
    return JSONResponse(content=payload)
