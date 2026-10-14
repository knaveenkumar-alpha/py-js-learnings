"""
md4_fallback.py
----------------
Pure-Python MD4 implementation.

"""
import struct

_MASK32 = 0xFFFFFFFF
_ROUND1_SHIFTS = (3, 7, 11, 19)
_ROUND2_SHIFTS = (3, 5, 9, 13)
_ROUND3_SHIFTS = (3, 9, 11, 15)
_ROUND2_ORDER = (0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15)
_ROUND3_ORDER = (0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15)


def _left_rotate(x: int, n: int) -> int:
    """Rotate a 32-bit integer left by ``n`` bits."""
    x &= _MASK32
    return ((x << n) | (x >> (32 - n))) & _MASK32


def _f(x: int, y: int, z: int) -> int:
    """Return MD4's choose function for one round-1 operation."""
    return (x & y) | (~x & z)


def _g(x: int, y: int, z: int) -> int:
    """Return MD4's majority function for one round-2 operation."""
    return (x & y) | (x & z) | (y & z)


def _h(x: int, y: int, z: int) -> int:
    """Return MD4's XOR function for one round-3 operation."""
    return x ^ y ^ z


def md4_hex(message: str) -> str:
    """Return the MD4 hex digest of a UTF-8 encoded string.

    MD4 is cryptographically broken and should only be used for compatibility
    with legacy systems, not for passwords, signatures, or new security code.
    """
    msg = message.encode("utf-8")
    orig_len_bits = (8 * len(msg)) & 0xFFFFFFFFFFFFFFFF

    # Padding: 0x80, zeros until length % 64 == 56, then the bit length.
    padding_length = (56 - (len(msg) + 1) % 64) % 64
    msg += b"\x80" + b"\x00" * padding_length + struct.pack("<Q", orig_len_bits)

    a0, b0, c0, d0 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476

    for chunk_start in range(0, len(msg), 64):
        chunk = msg[chunk_start:chunk_start + 64]
        X = struct.unpack("<16I", chunk)

        A, B, C, D = a0, b0, c0, d0

        # Round 1
        for i in range(16):
            k = i
            if i % 4 == 0:
                A = _left_rotate((A + _f(B, C, D) + X[k]) & _MASK32, _ROUND1_SHIFTS[0])
            elif i % 4 == 1:
                D = _left_rotate((D + _f(A, B, C) + X[k]) & _MASK32, _ROUND1_SHIFTS[1])
            elif i % 4 == 2:
                C = _left_rotate((C + _f(D, A, B) + X[k]) & _MASK32, _ROUND1_SHIFTS[2])
            else:
                B = _left_rotate((B + _f(C, D, A) + X[k]) & _MASK32, _ROUND1_SHIFTS[3])

        # Round 2
        for i, k in enumerate(_ROUND2_ORDER):
            if i % 4 == 0:
                A = _left_rotate((A + _g(B, C, D) + X[k] + 0x5A827999) & _MASK32, _ROUND2_SHIFTS[0])
            elif i % 4 == 1:
                D = _left_rotate((D + _g(A, B, C) + X[k] + 0x5A827999) & _MASK32, _ROUND2_SHIFTS[1])
            elif i % 4 == 2:
                C = _left_rotate((C + _g(D, A, B) + X[k] + 0x5A827999) & _MASK32, _ROUND2_SHIFTS[2])
            else:
                B = _left_rotate((B + _g(C, D, A) + X[k] + 0x5A827999) & _MASK32, _ROUND2_SHIFTS[3])

        # Round 3
        for i, k in enumerate(_ROUND3_ORDER):
            if i % 4 == 0:
                A = _left_rotate((A + _h(B, C, D) + X[k] + 0x6ED9EBA1) & _MASK32, _ROUND3_SHIFTS[0])
            elif i % 4 == 1:
                D = _left_rotate((D + _h(A, B, C) + X[k] + 0x6ED9EBA1) & _MASK32, _ROUND3_SHIFTS[1])
            elif i % 4 == 2:
                C = _left_rotate((C + _h(D, A, B) + X[k] + 0x6ED9EBA1) & _MASK32, _ROUND3_SHIFTS[2])
            else:
                B = _left_rotate((B + _h(C, D, A) + X[k] + 0x6ED9EBA1) & _MASK32, _ROUND3_SHIFTS[3])

        a0 = (a0 + A) & _MASK32
        b0 = (b0 + B) & _MASK32
        c0 = (c0 + C) & _MASK32
        d0 = (d0 + D) & _MASK32

    return b"".join(struct.pack("<I", v) for v in (a0, b0, c0, d0)).hex()


if __name__ == "__main__":
    # Self-test against a known MD4 vector (RFC 1320): MD4("") == 31d6cfe0d16ae931b73c59d7e0c089c0
    assert md4_hex("") == "31d6cfe0d16ae931b73c59d7e0c089c0"
    assert md4_hex("a") == "bde52cb31de33e46245e05fbdbd6fb24"
    print("md4_fallback self-test OK")