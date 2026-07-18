from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.ai_service import review_code
from app.prompts import REVIEW_PROMPT
from app.schemas import ReviewRequest, ReviewResponse

router = APIRouter(
    prefix="/review",
    tags=["AI Code Review"]
)



@router.post(
    "/",
    response_model=ReviewResponse
)
async def review(request: ReviewRequest):
    """
    Review source code using AI.
    """

    if not request.code.strip():
        raise HTTPException(
            status_code=400,
            detail="Code cannot be empty."
        )

    result = review_code(
        request.code,
        REVIEW_PROMPT
    )

    return ReviewResponse(
        review=result
    )