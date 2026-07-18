from pathlib import Path
import re

SUPPORTED_LANGUAGES = {
    ".py": "Python",
    ".cs": "C#",
    ".java": "Java",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".cpp": "C++",
    ".c": "C",
    ".go": "Go",
    ".php": "PHP",
    ".rb": "Ruby",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".html": "HTML",
    ".css": "CSS",
    ".json": "JSON",
    ".xml": "XML",
    ".sql": "SQL"
}


def detect_language(filename: str) -> str:
    """
    Detect programming language based on file extension.
    """
    extension = Path(filename).suffix.lower()
    return SUPPORTED_LANGUAGES.get(extension, "Unknown")


def read_code(file_path: str) -> str:
    """
    Read source code from uploaded file.
    """
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()


def count_lines(code: str) -> int:
    return len(code.splitlines())


def count_characters(code: str) -> int:
    return len(code)


def count_blank_lines(code: str) -> int:
    return sum(1 for line in code.splitlines() if line.strip() == "")


def count_comment_lines(code: str) -> int:
    comment_prefixes = (
        "#",
        "//",
        "/*",
        "*",
        "--"
    )

    count = 0

    for line in code.splitlines():
        stripped = line.strip()

        if stripped.startswith(comment_prefixes):
            count += 1

    return count


def count_functions(code: str) -> int:
    patterns = [
        r"^\s*def\s+\w+",
        r"^\s*function\s+\w+",
        r"^\s*public\s+.*\(",
        r"^\s*private\s+.*\(",
        r"^\s*protected\s+.*\(",
    ]

    total = 0

    for pattern in patterns:
        total += len(re.findall(pattern, code, re.MULTILINE))

    return total


def count_classes(code: str) -> int:
    patterns = [
        r"^\s*class\s+\w+",
        r"^\s*public\s+class\s+\w+",
    ]

    total = 0

    for pattern in patterns:
        total += len(re.findall(pattern, code, re.MULTILINE))

    return total


def analyze_code(file_path: str) -> dict:
    """
    Analyze uploaded source code and return metadata.
    """
    code = read_code(file_path)

    return {
        "language": detect_language(file_path),
        "lines": count_lines(code),
        "characters": count_characters(code),
        "blank_lines": count_blank_lines(code),
        "comments": count_comment_lines(code),
        "functions": count_functions(code),
        "classes": count_classes(code),
        "code": code,
    }