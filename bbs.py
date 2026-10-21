"""
DCC075 - Segurança em Sistemas de Computação
Atividade 07 - Gerador Pseudoaleatório Blum Blum Shub (BBS) + Suite NIST

Premissas do Algoritmo Blum Blum Shub:
1. p e q devem ser números primos grandes (aqui > 10000).
2. p ≡ 3 (mod 4) e q ≡ 3 (mod 4) (Primos de Blum).
3. M = p * q (Inteiro de Blum).
4. A semente 's' deve ser coprima com M: mdc(s, M) = 1.
5. Geração:
   x_0 = (s^2) mod M
   Para cada passo i:
     x_i = (x_{i-1}^2) mod M
     bit_i = x_i mod 2 (bit menos significativo)

Valores escolhidos:
- p = 10007 (primo > 10000, 10007 % 4 == 3)
- q = 10079 (primo > 10000, 10079 % 4 == 3)
- s = 1234567 (coprimo com M = 100860553, mdc(s, M) == 1)

Como executar:
    python bbs.py
"""

import math


def eh_primo(n: int) -> bool:
    """Verifica se um número n é primo."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, int(math.isqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


def validar_parametros_bbs(p: int, q: int, s: int) -> int:
    """Valida todas as premissas matemáticas do algoritmo Blum Blum Shub."""
    assert p > 10000 and q > 10000, "Erro: p e q devem ser maiores que 10000."
    assert eh_primo(p), f"Erro: p={p} não é primo."
    assert eh_primo(q), f"Erro: q={q} não é primo."
    assert p != q, "Erro: p e q devem ser distintos."
    assert p % 4 == 3, f"Erro: p={p} não é congruente a 3 (mod 4)."
    assert q % 4 == 3, f"Erro: q={q} não é congruente a 3 (mod 4)."

    M = p * q
    assert math.gcd(s, M) == 1, f"Erro: s={s} não é coprimo com M={M}."
    return M


def blum_blum_shub(p: int, q: int, s: int, num_bits: int) -> str:
    """
    Executa o gerador Blum Blum Shub e retorna uma string de bits ('0' e '1').
    """
    M = validar_parametros_bbs(p, q, s)

    # Estado inicial: x_0 = s^2 mod M
    x = pow(s, 2, M)

    bits = []
    for _ in range(num_bits):
        # x_i = x_{i-1}^2 mod M
        x = pow(x, 2, M)
        # Extrai o bit menos significativo (LSB)
        bit = x & 1
        bits.append(str(bit))

    return "".join(bits)


if __name__ == "__main__":
    # Parâmetros escolhidos (> 10000 e congruentes a 3 mod 4)
    p = 10007
    q = 10079
    s = 1234567
    M = p * q
    QUANTIDADE_BITS = 20000  # Quantidade ideal para colar no testador online da Suite NIST

    print("=" * 65)
    print("       GERADOR PSEUDOALEATÓRIO BLUM BLUM SHUB (BBS)")
    print("=" * 65)
    print(f"Primo p escolhido : {p} (p > 10000 | p mod 4 = {p % 4})")
    print(f"Primo q escolhido : {q} (q > 10000 | q mod 4 = {q % 4})")
    print(f"Módulo M = p * q  : {M}")
    print(f"Semente s         : {s} (mdc(s, M) = {math.gcd(s, M)})")
    print(f"Total de bits     : {QUANTIDADE_BITS}")
    print("-" * 65)

    sequencia_bits = blum_blum_shub(p, q, s, QUANTIDADE_BITS)

    uns = sequencia_bits.count("1")
    zeros = sequencia_bits.count("0")
    print(f"Contagem de '0's  : {zeros} ({zeros / QUANTIDADE_BITS * 100:.2f}%)")
    print(f"Contagem de '1's  : {uns} ({uns / QUANTIDADE_BITS * 100:.2f}%)")
    print(f"Primeiros 100 bits: {sequencia_bits[:100]}...")

    # Salva os bits em arquivo para facilitar o uso no Random Bitstream Tester (NIST)
    arquivo_saida = "bitstream_nist.txt"
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(sequencia_bits)

    print(f"\n[OK] Sequência de {QUANTIDADE_BITS} bits salva em '{arquivo_saida}'.")
    print("Copie o conteúdo de 'bitstream_nist.txt' e cole em:")
    print("  https://mzsoltmolnar.github.io/random-bitstream-tester/")
