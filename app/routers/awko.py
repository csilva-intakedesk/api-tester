from fastapi import APIRouter
from fastapi.responses import JSONResponse
import random
from datetime import date

router = APIRouter()


@router.post("/case", response_class=JSONResponse)
async def case():
    case_number = random.randint(1, 9999)
    year = date.today().year
    matter_number = f"{year}-{case_number}"

    payload = {"CaseID": case_number, "MATTER_NUMBER": matter_number}
    return JSONResponse(content=payload)


@router.post("/document", response_class=JSONResponse)
async def document():
    document_id = random.randint(1, 9999999)
    payload = {"DOCUMENT_ID": document_id}
    return JSONResponse(content=payload)


@router.post("/oauth", response_class=JSONResponse)
async def oauth():
    payload = {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "token_type": "Bearer",
        "expires_in": 3600,
        "refresh_token": "8xLOxBtZp8",
        "scope": "read write",
    }
    return JSONResponse(content=payload)
