from pydantic import BaseModel


# -------------------------
# Upload
# -------------------------

class UploadResponse(BaseModel):
    success: bool
    filename: str
    saved_as: str
    language: str
    lines: int
    characters: int
    blank_lines: int
    comments: int
    functions: int
    classes: int
    code: str


# -------------------------
# Explain
# -------------------------

class ExplainRequest(BaseModel):
    code: str


class ExplainResponse(BaseModel):
    explanation: str


# -------------------------
# Review
# -------------------------

class ReviewRequest(BaseModel):
    code: str


class ReviewResponse(BaseModel):
    review: str


# -------------------------
# Security
# -------------------------

class SecurityRequest(BaseModel):
    code: str


class SecurityResponse(BaseModel):
    security: str


# -------------------------
# Documentation
# -------------------------

class DocumentationRequest(BaseModel):
    code: str


class DocumentationResponse(BaseModel):
    documentation: str


# -------------------------
# Unit Tests
# -------------------------

class UnitTestRequest(BaseModel):
    code: str


class UnitTestResponse(BaseModel):
    tests: str


# -------------------------
# Convert Code
# -------------------------

class ConvertRequest(BaseModel):
    code: str
    target_language: str


class ConvertResponse(BaseModel):
    converted_code: str


# -------------------------
# Chat
# -------------------------

class ChatRequest(BaseModel):
    code: str
    question: str


class ChatResponse(BaseModel):
    answer: str