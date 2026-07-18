from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.ai_service import security_review
from app.prompts import SECURITY_PROMPT
from app.schemas import SecurityRequest, SecurityResponse

router = APIRouter(
    prefix="/security",
    tags=["AI Security Review"]
)




@router.post(
    "/",
    response_model=SecurityResponse
)
async def analyze_security(request: SecurityRequest):
    """
    Analyze source code for security vulnerabilities.
    """

    if not request.code.strip():
        raise HTTPException(
            status_code=400,
            detail="Code cannot be empty."
        )

    result = security_review(
        request.code,
        SECURITY_PROMPT
    )

    return SecurityResponse(
        security=result
    )