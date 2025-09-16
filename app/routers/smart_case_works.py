from fastapi import APIRouter
from fastapi.responses import Response
import secrets

router = APIRouter()


@router.post("/case", response_class=Response)
async def case():
    return Response(content="30038846~SGGH~ID158881")


@router.post("/document", response_class=Response)
async def document():  # accepts JSON with optional reqId
    req_id = secrets.token_hex(8)
    content = f'<?xml version="1.0" encoding="utf-8"?>OK {req_id}'
    return Response(content=content, media_type="application/xml")
