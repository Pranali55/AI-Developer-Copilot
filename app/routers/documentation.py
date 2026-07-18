from fastapi import APIRouter, HTTPException

from app.schemas import (
    DocumentationRequest,
    DocumentationResponse
)

from app.services.ai_service import generate_documentation
from app.prompts import DOCUMENTATION_PROMPT

router = APIRouter(
    prefix="/documentation",
    tags=["AI Documentation"]
)


@router.post(
    "/",
    response_model=DocumentationResponse
)
async def documentation(request: DocumentationRequest):
    """
    Generate documentation for uploaded source code.
    """

    if not request.code.strip():
        raise HTTPException(
            status_code=400,
            detail="Code cannot be empty."
        )

    documentation = generate_documentation(
        request.code,
        DOCUMENTATION_PROMPT
    )

    return DocumentationResponse(
        documentation=documentation
    )