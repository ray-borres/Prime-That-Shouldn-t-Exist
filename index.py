
# Five parts, two XOR fragments per part.
# All values are octal strings.
# Insert generated values here; do not include the generator.

FRAGMENTS = [
    ("PART_1_A_OCTAL", "PART_1_B_OCTAL"),
    ("PART_2_A_OCTAL", "PART_2_B_OCTAL"),
    ("PART_3_A_OCTAL", "PART_3_B_OCTAL"),
    ("PART_4_A_OCTAL", "PART_4_B_OCTAL"),
    ("PART_5_A_OCTAL", "PART_5_B_OCTAL"),
]

def decode_octal(text):
    return bytes(int(value, 8) for value in text.split())

def xor_bytes(a, b):
    if len(a) != len(b):
        raise ValueError("Fragment lengths do not match")
    return bytes(x ^ y for x, y in zip(a, b))

def recover_part(fragment_a, fragment_b):
    a = decode_octal(fragment_a)
    b = decode_octal(fragment_b)
    return xor_bytes(a, b)

# This function is for the solver to use once the fragments
# have been correctly discovered and ordered.
def recover_flag(fragments):
    return b"".join(
        recover_part(a, b) for a, b in fragments
    )

print("Five encrypted-looking parts are waiting to be solved.")
print("Find the fragments and determine their correct order.")

import secrets

# Organizer-only secret
flag = b"cybersurferCTF{gcd_leaks_the_prime_7f3a91c2}"

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def octal(data):
    return " ".join(format(byte, "03o") for byte in data)

# Split into exactly five parts
q, r = divmod(len(flag), 5)
parts = []
start = 0

for i in range(5):
    size = q + (i < r)
    parts.append(flag[start:start + size])
    start += size

print("# Copy only these fragments into the public challenge.")
for i, part in enumerate(parts, 1):
    a = secrets.token_bytes(len(part))
    b = xor_bytes(part, a)

    print(f"\nPART_{i}_A = {octal(a)!r}")
    print(f"PART_{i}_B = {octal(b)!r}")
