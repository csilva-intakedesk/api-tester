from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/case", response_class=JSONResponse)
async def case():
    payload = {
        "intakeId": "a0CWD000044DO1l2AG",
        "message": "intake created successfully.",
    }
    return JSONResponse(content=payload)
