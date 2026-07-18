from pathlib import Path
import shutil
import uuid

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.config import UPLOAD_FOLDER
from app.services.parser import analyze_code, detect_language

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

# Supported source code file extensions
ALLOWED_EXTENSIONS = {
    ".py",
    ".cs",
    ".java",
    ".js",
    ".ts",
    ".cpp",
    ".c",
    ".go",
    ".php",
    ".rb",
    ".swift",
    ".kt",
    ".html",
    ".css",
    ".json",
    ".xml",
    ".sql"
}

# Maximum upload size (5 MB)
MAX_FILE_SIZE = 5 * 1024 * 1024

# Ensure upload directory exists
Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)


@router.post("/")
async def upload_code(file: UploadFile = File(...)):
    """
    Upload and analyze a source code file.
    """

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file selected."
        )

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {extension}"
        )

    contents = await file.read()

    if len(contents) == 0:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File exceeds maximum size of 5 MB."
        )

    unique_name = f"{uuid.uuid4().hex}{extension}"
    save_path = Path(UPLOAD_FOLDER) / unique_name

    with open(save_path, "wb") as buffer:
        buffer.write(contents)

    analysis = analyze_code(str(save_path))

    return {
        "success": True,
        "filename": file.filename,
        "saved_as": unique_name,
        "language": detect_language(file.filename),
        "lines": analysis["lines"],
        "characters": analysis["characters"],
        "blank_lines": analysis["blank_lines"],
        "comments": analysis["comments"],
        "functions": analysis["functions"],
        "classes": analysis["classes"],
        "code": analysis["code"]
    }


@router.delete("/{filename}")
async def delete_file(filename: str):
    """
    Delete an uploaded source code file.
    """

    file_path = Path(UPLOAD_FOLDER) / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found."
        )

    file_path.unlink()

    return {
        "success": True,
        "message": "File deleted successfully."
    }


@router.get("/languages")
async def supported_languages():
    """
    Return supported programming languages.
    """

    return {
        "supported_extensions": sorted(ALLOWED_EXTENSIONS)
    }