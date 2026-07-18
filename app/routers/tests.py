from fastapi import APIRouter, HTTPException

from app.schemas import (
    UnitTestRequest,
    UnitTestResponse
)

from app.services.ai_service import generate_unit_tests
from app.prompts import UNIT_TEST_PROMPT

router = APIRouter(
    prefix="/tests",
    tags=["AI Unit Test Generator"]
)


@router.post(
    "/",
    response_model=UnitTestResponse
)
async def generate_tests(request: UnitTestRequest):

    if not request.code.strip():
        raise HTTPException(
            status_code=400,
            detail="Code cannot be empty."
        )

    tests = generate_unit_tests(
        request.code,
        UNIT_TEST_PROMPT
    )

    return UnitTestResponse(
        tests=tests
    )