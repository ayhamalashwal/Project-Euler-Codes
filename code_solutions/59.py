import collections

from pathlib import Path

cipher_path = Path.home() / "Desktop" / "project_euler" / "assets" / "0059_cipher.txt"
raw_text = cipher_path.read_text(encoding="utf-8").strip()
message = [int(x) for x in raw_text.split(",")]
key = [collections.Counter(message[i::3]).most_common(1)[0][0]^ord(' ') for i in [0,1,2]]

print(''.join(map(chr, key)))
decrypted_codes = [code ^ key[idx % 3] for idx, code in enumerate(message)]
print("Sum of ASCII values:", sum(decrypted_codes))
