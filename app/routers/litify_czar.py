"""
Copyright (c) 2025 IntakeDesk LLC. All rights reserved.
Proprietary and Confidential. Unauthorized copying, use, modification,
or distribution is prohibited.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from integrations.litify.schemas import DocumentResponsePayload
from integrations.litify_czar.schemas import CaseResponsePayload
from integrations.oauth.schemas import OauthResponsePayload

router = APIRouter()


@router.post("/case", response_class=JSONResponse)
async def case() -> JSONResponse:
    payload: CaseResponsePayload = {
        "attempt": "0196ef15-2f6b-0f44-36d8-aa0d89679e3c",
        "id": "0196ef15-2f6b-0f44-36d8-aa0d89679e3c",
        "request_id": "0196ef15-2f6b-0f44-36d8-aa0d89679e3c",
        "status": "success",
    }
    return JSONResponse(content=payload)


@router.post("/document", response_class=JSONResponse)
async def document() -> JSONResponse:
    payload: DocumentResponsePayload = {
        "relatedVendorMatterId": "DEMOTEST-SELFREP-20250601",
        "documents": [
            {
                "vendorDocumentId": "DEMOTEST-SELFREPFILE-20250601",
                "tekmirDocumentId": "406becd9-de05-4aa5-a36c-5061f6032836",
            }
        ],
    }
    return JSONResponse(content=payload)


@router.post("/oauth", response_class=JSONResponse)
async def oauth() -> JSONResponse:
    payload: OauthResponsePayload = {
        "access_token": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
        "token_type": "Bearer",
        "expires_in": 3600,
        "scope": "user:read profile:write",
        "refresh_token": "r1t2y3u4i5o6p7q8r9s0t1u2v3w4x5y6",
    }
    return JSONResponse(content=payload)
