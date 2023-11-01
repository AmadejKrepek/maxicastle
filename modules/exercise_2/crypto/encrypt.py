from modules.exercise_2.crypto.utils.utils import chacha20_block


# Samo polovica bloka je v bistvu sporočilo, druga polovica bloka pa vsebuje KONSTANTO,
# INICIALIZACIJSKI VEKTOR, COUNTER ter KLJUČ no in potem to združimo skupaj s sporočilom.
def chacha20_encrypt_file(input_file, output_file, key, iv, position=0):
    with open(input_file, 'rb') as f:
        data = f.read()

    encrypted_data = []
    for i in range(0, len(data), 64):
        # Scramble en BLOCK znakov (512 bitov = 16 znakov, ker je en znak 32 bit)
        # Takšen scrambled blok kot ga tukaj sedaj dobimo, bi lahko z lahkoto z obratnimi operacije v nasprotnem redu,
        # pridobili originalen blok in s tem ugotovili celoten tok ter pridobili plain text!!!! NOT SO EASY!
        block = chacha20_block(key, iv, position)
        # COUNTER da vemo, pozicijo blokov, da če se kateri izgubi
        position += 1
        # Da se ne mora zgoditi to, da bi z lahkoto pridobili originalen blok in razkrili sporočilo, naredi naslednje:
        # Doda originalen (UNSCRAMBLED) blok k SCRAMBLED bloku in to WORD WISE (XOR) in to uporabi kot PSEUDO random blok

        # Zakaj to naredimo?
        # Če ne vemo vsebine začetka bloka, ni možno obrniti enačbe. Stvar je v tem, da je narejeno tako, da
        # NAPADALEC ne morem obrniti enačbe, če ne ve pol bloka. VSAJ ZA ENKRAT ŠE NE MORA! KVANTNI RAČUNALNIKI?!?
        # And so on. Each block correspond to 64 bytes of the message. For each 64 byte chunk, scramble the right block,
        # and XOR the result with the message. And that’s pretty much it.

        # And so on. Each block correspond to 64 bytes of the message. For each 64 byte chunk,
        # scramble the right block, and XOR the result with the message. And that’s pretty much it.

        # Yes, the difference between 2 blocks (SCRAMBLED BLOK and UNSCRAMBLED BLOK) is often only one bit.
        # But after the scrambling, that single bit will have wrecked so much havoc it won’t matter:
        # the scrambled blocks will look unrelated to the attacker.
        encrypted_block = bytes(a ^ b for a, b in zip(data[i:i + 64], block))
        encrypted_data.extend(encrypted_block)

    return True, encrypted_data
