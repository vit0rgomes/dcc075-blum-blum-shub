# DCC075 - Segurança em Sistemas de Computação
## Atividade 07: Gerador Pseudoaleatório Blum Blum Shub (BBS) e Suíte NIST

Implementação do algoritmo criptográfico **Blum Blum Shub (BBS)** em Python puro e validação estatística de aleatoriedade segundo os padrões do **NIST SP 800-22** (*Random Bitstream Tester*).

---

### 📐 Premissas Matemáticas e Parâmetros Escolhidos
Para garantir a segurança e as propriedades teóricas do gerador BBS:
1. **$p$ e $q$ primos grandes ($> 10000$):**
   - $p = 10007$
   - $q = 10079$
2. **Primos de Blum:** $p \equiv 3 \pmod 4$ e $q \equiv 3 \pmod 4$
   - $10007 \bmod 4 = 3$
   - $10079 \bmod 4 = 3$
3. **Módulo de Blum $M$:**
   - $M = p \cdot q = 10007 \times 10079 = 100860553$
4. **Semente $s$ coprima com $M$:**
   - $s = 1234567$ ($\text{mdc}(s, M) = 1$)

---

### ⚙️ Algoritmo de Geração
1. Estado inicial: $x_0 = (s^2) \bmod M$
2. A cada passo $i \ge 1$:
   - $x_i = (x_{i-1}^2) \bmod M$
   - $\text{bit}_i = x_i \bmod 2$ (bit menos significativo - LSB)

---

### 📊 Resultados na Suíte NIST (Random Bitstream Tester)
Avaliando a sequência gerada de 20.000 bits no [Random Bitstream Tester](https://mzsoltmolnar.github.io/random-bitstream-tester/), todos os testes estatísticos aplicáveis à amostra foram **aprovados** ($P\text{-value} \ge 0{,}01$):
- **Frequency (Monobit) Test:** P-value = 0.02545 ➔ **Passed**
- **Frequency Test within a Block:** P-value = 0.74942 ➔ **Passed**
- **Runs Test:** P-value = 0.28554 ➔ **Passed**
- **Test for the Longest Run of Ones in a Block:** P-value = 0.08732 ➔ **Passed**
- **Approximate Entropy Test:** P-value = 0.17428 ➔ **Passed**
- **Cumulative Sums (Cusum) Test:** P-value = 0.04392 / 1.00000 ➔ **Passed**

*(Nota: testes como Maurer e Linear Complexity exigem centenas de milhares ou milhões de bits pelo padrão NIST, por isso requerem amostras maiores).*

---

### 🚀 Como Executar
Requisitos: Apenas Python 3 instalado (biblioteca padrão).
```bash
python bbs.py
```
O script valida as premissas matemáticas, calcula os $20.000$ bits e salva a saída pronta em `bitstream_nist.txt`.
