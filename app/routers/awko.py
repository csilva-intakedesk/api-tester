"""
Copyright (c) 2025 IntakeDesk LLC. All rights reserved.
Proprietary and Confidential. Unauthorized copying, use, modification,
or distribution is prohibited.
"""

from datetime import datetime, timezone
from secrets import randbelow

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/case", response_class=JSONResponse)
async def case() -> JSONResponse:
    case_number = f"{randbelow(9999) + 1:04d}"
    year = datetime.now(timezone.utc).date().year
    matter_number = f"{year}-{case_number}"

    payload = {"CaseID": case_number, "MATTER_NUMBER": matter_number}
    return JSONResponse(content=payload)


@router.post("/document", response_class=JSONResponse)
async def document() -> JSONResponse:
    document_id = f"{randbelow(999999) + 1:04d}"
    payload = {"DOCUMENT_ID": document_id}
    return JSONResponse(content=payload)


@router.post("/oauth", response_class=JSONResponse)
async def oauth() -> JSONResponse:
    payload = {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "token_type": "Bearer",
        "expires_in": 3600,
        "refresh_token": "8xLOxBtZp8",
        "scope": "read write",
    }
    return JSONResponse(content=payload)
