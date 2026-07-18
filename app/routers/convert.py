from fastapi import APIRouter, HTTPException

from app.schemas import (
    ConvertRequest,
    ConvertResponse
)

from app.services.ai_service import convert_code
from app.prompts import CONVERT_PROMPT

router = APIRouter(
    prefix="/convert",
    tags=["AI Code Converter"]
)


@router.post(
    "/",
    response_model=ConvertResponse
)
async def convert(request: ConvertRequest):

    if not request.code.strip():
        raise HTTPException(
            status_code=400,
            detail="Code cannot be empty."
        )

    if not request.target_language.strip():
        raise HTTPException(
            status_code=400,
            detail="Target language is required."
        )

    prompt = f"""
{CONVERT_PROMPT}

Convert the following code into {request.target_language}.

Only return the converted code.
"""

    converted = convert_code(
        request.code,
        prompt
    )

    return ConvertResponse(
        converted_code=converted
    )