from pathlib import Path
cipher_path = Path.home() / "Desktop" / "project_euler" / "assets" / "xor(59.py).txt"
cipher = [int(x) for x in cipher_path.read_text(encoding="utf-8").strip().split(",")]
def is_printable_ascii(code: int) -> bool:
    return (32 <= code <= 126) or code in (10, 13)
def score_english_byte(code: int) -> int:
    if code == 32:
        return 5
    if (65 <= code <= 90) or (97 <= code <= 122):
        return 3
    if chr(code) in ".,!?;:'\"-()":
        return 1
    return 0
def find_key(stream: list[int]) -> int:
    best_key = None
    best_score = -1
    for candidate in range(ord("a"), ord("z") + 1):
        decrypted = [b ^ candidate for b in stream]
        if not all(is_printable_ascii(code) for code in decrypted):
            continue
        score = sum(score_english_byte(code) for code in decrypted)
        if score > best_score:
            best_score = score
            best_key = candidate
        if best_key == None:
            raise ValueError("Error")
        return best_key
key = [find_best_key_byte(cipher[offset::3]) for offset in range(3)]
plain_codes = [code ^ key[i % 3] for i, code in enumerate(cipher)]
plain_text = "".join(chr(code) for code in plain_codes)
print("recovered key:", "".join(chr(k) for k in key))
print("plain_text:", plain_text)
print("ascii sum:", sum(plain_codes)
