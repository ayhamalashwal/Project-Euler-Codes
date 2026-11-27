from pathlib import Path
cipher_path = Path.home() / "Desktop" / "project_euler" / "assets" / "xor(59.py).txt"
cipher = [int(x) for x in cipher_path.read_text(encoding="utf-8").strip().split(",")]
def is_printable_ascii(code: int) -> bool:
    return (32 <= code <= 126) or code in (10, 13)
def score
