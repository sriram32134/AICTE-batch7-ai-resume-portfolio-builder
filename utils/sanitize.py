"""Text sanitization utilities for PDF-safe output."""


def sanitize_text(text: str) -> str:
    """Replace special/Unicode characters with PDF-safe ASCII equivalents."""
    if not text:
        return ""

    replacements = {
        "\u2013": "-",   # en-dash
        "\u2014": "-",   # em-dash
        "\u2018": "'",   # left single quote
        "\u2019": "'",   # right single quote
        "\u201c": '"',   # left double quote
        "\u201d": '"',   # right double quote
        "\u2022": "-",   # bullet
        "\u2026": "...", # ellipsis
        "\u00a0": " ",   # non-breaking space
        "\u200b": "",    # zero-width space
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text
