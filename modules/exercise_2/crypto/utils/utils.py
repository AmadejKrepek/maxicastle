def generate_key():
    return b'SomeSecretKey12345678901234'


def rotate_left(val, n):
    return ((val << n) & 0xFFFFFFFF) | (val >> (32 - n) & 0xFFFFFFFF)


def quarter_round(state, a, b, c, d):
    state[a] = (state[a] + state[b]) & 0xFFFFFFFF
    state[d] = rotate_left(state[d] ^ state[a], 16)
    state[c] = (state[c] + state[d]) & 0xFFFFFFFF
    state[b] = rotate_left(state[b] ^ state[c], 12)
    state[a] = (state[a] + state[b]) & 0xFFFFFFFF
    state[d] = rotate_left(state[d] ^ state[a], 8)
    state[c] = (state[c] + state[d]) & 0xFFFFFFFF
    state[b] = rotate_left(state[b] ^ state[c], 7)


def chacha20_block(key, iv, position):
    ctx = [0] * 16
    ctx[:4] = (1634760805, 857760878, 2036477234, 1797285236)
    ctx[4:12] = [int.from_bytes(key[i:i + 4], 'little') for i in range(0, 32, 4)]
    ctx[12] = ctx[13] = position
    ctx[14:16] = [int.from_bytes(iv[i:i + 4], 'little') for i in range(0, 8, 4)]

    x = list(ctx)
    for _ in range(10):
        quarter_round(x, 0, 4, 8, 12)
        quarter_round(x, 1, 5, 9, 13)
        quarter_round(x, 2, 6, 10, 14)
        quarter_round(x, 3, 7, 11, 15)
        quarter_round(x, 0, 5, 10, 15)
        quarter_round(x, 1, 6, 11, 12)
        quarter_round(x, 2, 7, 8, 13)
        quarter_round(x, 3, 4, 9, 14)

    return bytes(byte for i in range(16) for byte in x[i].to_bytes(4, 'little'))
