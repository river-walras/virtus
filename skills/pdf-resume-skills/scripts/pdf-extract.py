# /// script
# dependencies = [
#   "pypdf>=4.0.0",
# ]
# ///

"""
Extract text content from a PDF file.
Usage: uv run pdf-extract.py <path-to-pdf>
"""

import sys
from pypdf import PdfReader


def extract(path: str) -> None:
    reader = PdfReader(path)
    for i, page in enumerate(reader.pages, 1):
        text = page.extract_text()
        if text and text.strip():
            print(f"--- Page {i} ---")
            print(text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: uv run pdf-extract.py <path-to-pdf>", file=sys.stderr)
        sys.exit(1)
    extract(sys.argv[1])
