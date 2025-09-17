"""
Copyright (c) 2025 IntakeDesk LLC. All rights reserved.
Proprietary and Confidential. Unauthorized copying, use, modification,
or distribution is prohibited.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from integrations.litify.schemas import CaseResponsePayload, DocumentResponsePayload

router = APIRouter()


@router.post("/case", response_class=JSONResponse)
async def case() -> JSONResponse:
    payload: CaseResponsePayload = {
        "intakeId": "a0CWD000044DO1l2AG",
        "message": "intake created successfully.",
    }
    return JSONResponse(content=payload)


@router.post("/document", response_class=JSONResponse)
async def document() -> JSONResponse:
    payload: DocumentResponsePayload = {
        "relatedVendorMatterId": "a0CWD000044DO1l2AG",
        "documents": [
            {
                "vendorDocumentId": "a0CWD000044DO1l2AG-20250601",
                "tekmirDocumentId": "406becd9-de05-4aa5-a36c-5061f6032836",
            }
        ],
    }
    return JSONResponse(content=payload)
