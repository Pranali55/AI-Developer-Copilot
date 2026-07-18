from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.ai_service import explain_code
from app.prompts import EXPLAIN_PROMPT
from app.schemas import ExplainRequest, ExplainResponse


router = APIRouter(
    prefix="/explain",
    tags=["AI Code Explanation"]
)






@router.post(
    "/",
    response_model=ExplainResponse
)
async def explain(request: ExplainRequest):
    """
    Explain uploaded source code using AI.
    """

    if not request.code.strip():
        raise HTTPException(
            status_code=400,
            detail="Code cannot be empty."
        )

    explanation = explain_code(
        request.code,
        EXPLAIN_PROMPT
    )

    return ExplainResponse(
        explanation=explanation
    )