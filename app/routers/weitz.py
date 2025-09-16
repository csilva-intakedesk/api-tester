from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response

router = APIRouter()


@router.post("/daisy_cutter/create_intake", response_class=JSONResponse)
async def create_intake():
    payload = {
        "Success": "Yes",
        "Message": "",
        "IntakeID": "123456789",
        "SystemError": None,
    }
    return JSONResponse(content=payload)


@router.post("/file_share/upload_doc", response_class=Response)
async def upload_doc():
    return Response(content="")


@router.post("/file_share/upload", response_class=Response)
async def upload():
    return Response(content="")


@router.post("/file_share/oauth", response_class=JSONResponse)
async def oauth():
    payload = {
        "access_token": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
        "token_type": "Bearer",
        "expires_in": 3600,
        "scope": "user:read profile:write",
        "refresh_token": "r1t2y3u4i5o6p7q8r9s0t1u2v3w4x5y6",
    }
    return JSONResponse(content=payload)
