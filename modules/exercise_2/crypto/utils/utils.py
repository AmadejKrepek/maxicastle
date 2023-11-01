def generate_key():
    return b'SomeSecretKey12345678901234'


def rotate_left(val, n):
    return ((val << n) & 0xFFFFFFFF) | (val >> (32 - n) & 0xFFFFFFFF)


# Gre skozi 4 x 32 bitne številke (to je četrtinka bloka, celoten blok = 512 bitov)
# Hkrati deluje na 4ih znakih, da zmanjša dostop do pomnilnika, kolikor je to mogoče.
def quarter_round(state, a, b, c, d):
    # ADDITION
    state[a] = (state[a] + state[b]) & 0xFFFFFFFF
    # ROTATION and XOR
    state[d] = rotate_left(state[d] ^ state[a], 16)

    # ADDITION
    state[c] = (state[c] + state[d]) & 0xFFFFFFFF
    # ROTATION and XOR
    state[b] = rotate_left(state[b] ^ state[c], 12)

    # ADDITION
    state[a] = (state[a] + state[b]) & 0xFFFFFFFF
    # ROTATION and XOR
    state[d] = rotate_left(state[d] ^ state[a], 8)

    # ADDITION
    state[c] = (state[c] + state[d]) & 0xFFFFFFFF
    # ROTATION and XOR
    state[b] = rotate_left(state[b] ^ state[c], 7)


# Vsebuje en blok 512 bitov, 512 / 32 = 16 znakov v enem bloku
# Imamo 4x4 matriko z 32 bitnimi števili
# Ta blok ni kriptiran, to naredimo potem ko dodamo plain text.
# STRUKTURA CHACHA BLOKA:
# 1. POLOVICA bloka je napolnjena z RANDOM SECRET KEY
# 2. ČETRTINA bloka je napolnjena z NONCE (IV) IN COUNTER-jem (TO LAHKO KONTROLIRA NAPADALEC!!!)
# 3. ČETRTINA bloka je napolnjena s KONSTANTO ("expand 32-byte k")

# NONCE
# Če dodamo več prostora za NONCE, potem se ne moremo bati kolizije.

# COUNTER
# Če uporabimo kot COUNTER, veliksot sporočila postane virtualno neskončno, že zdaj v bistvu je

# POMEN KONSTANTE
# PRVA PREDNOST
# Zmanjša možnost napadalcu, število kontroliranih vnosov. Če bi bil to NONCE ali COUNTER, bi imel napadalec v kontroli
# polovico bloka. Zaradi konstante, lahko tako napadalec KONTROLIRA samo ČETRTINO bloka.
# DRUGA PREDNOST
# Preventa ALL-ZERO BLOK, če scramblaš ALL-ZERO blok, dobiš ALL-ZERO blok (ni zelo efektiven pri skrivanju podatkov)
# TRETJA PREDNOST
# Konstanta ima zelo pomembno lastnost: asimetrijo. Hkrati je ASCII tekst, zato ne more priti nekdo skozi zadnja vrata.
def chacha20_block(key, iv, position):
    # Kreiramo prazno polje za 16 znakov = 16 znakov * 32 bitov na en znak = 512 bitov (en blok)
    ctx = [0] * 16
    # Prvim štirim mestom v polju priredimo KONSTANTO
    ctx[:4] = (1634760805, 857760878, 2036477234, 1797285236)
    # Polovica bloka je ključ
    ctx[4:12] = [int.from_bytes(key[i:i + 4], 'little') for i in range(0, 32, 4)]
    # Dve mesti sta za counter
    ctx[12] = ctx[13] = position
    # Dve mesti sta za nonce (IV)
    ctx[14:16] = [int.from_bytes(iv[i:i + 4], 'little') for i in range(0, 8, 4)]

    x = list(ctx)
    # 10 DIAGONALNIH IN 10 STOLPČNIH PONOVITEV = 20 PONOVITEV
    # 2 ponovitvi v vsaki zanki

    # Kot zanimivost pri SALSA20 se je ponovilo v eni zanki 2x samo PO VRSTICAH

    # Zakaj sploh imamo PO STOLPCIH 1x pa PO DIAGONALI 1X?
    # Ker COLUMN rounds je lažje vektorizirati, bolj poceni prideš skozi.
    for _ in range(10):
        # Vsak znak se dvakrat posodobi
        # Prva posodobitev - PO STOLPCIH
        quarter_round(x, 0, 4, 8, 12)
        quarter_round(x, 1, 5, 9, 13)
        quarter_round(x, 2, 6, 10, 14)
        quarter_round(x, 3, 7, 11, 15)

        # Druga posodobitev - PO DIAGONALI
        quarter_round(x, 0, 5, 10, 15)
        quarter_round(x, 1, 6, 11, 12)
        quarter_round(x, 2, 7, 8, 13)
        quarter_round(x, 3, 4, 9, 14)

    return bytes(byte for i in range(16) for byte in x[i].to_bytes(4, 'little'))
