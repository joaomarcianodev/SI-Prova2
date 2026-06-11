import random

# ==========================================
# 1. FUNÇÕES MATEMÁTICAS BÁSICAS
# ==========================================

def eh_primo(num):
    """Verifica se um número é primo de forma simples."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def gerar_primo_aleatorio(min_val=100, max_val=1000):
    """Gera um número primo aleatório dentro de um intervalo."""
    primo = random.randint(min_val, max_val)
    while not eh_primo(primo):
        primo = random.randint(min_val, max_val)
    return primo

def mdc(a, b):
    """Calcula o Máximo Divisor Comum (MDC) usando o algoritmo de Euclides."""
    while b != 0:
        a, b = b, a % b
    return a

def euclides_estendido(a, b):
    """
    Algoritmo de Euclides Estendido.
    Retorna o mdc(a, b) e os coeficientes x e y tais que a*x + b*y = mdc(a, b).
    """
    if a == 0:
        return b, 0, 1
    else:
        mdc_val, x, y = euclides_estendido(b % a, a)
        return mdc_val, y - (b // a) * x, x

def inverso_modular(e, phi):
    """Calcula o inverso modular (d) de 'e' módulo 'phi'."""
    mdc_val, x, _ = euclides_estendido(e, phi)
    if mdc_val != 1:
        raise Exception('Inverso modular não existe (e e phi não são coprimos).')
    else:
        return x % phi

# ==========================================
# 2. GERAÇÃO DE CHAVES RSA
# ==========================================

def gerar_par_de_chaves():
    """Gera a chave pública e a chave privada."""
    # 1. Escolher dois números primos grandes p e q
    p = gerar_primo_aleatorio(100, 500)
    q = gerar_primo_aleatorio(100, 500)
    # Garante que p e q sejam diferentes
    while p == q:
        q = gerar_primo_aleatorio(100, 500)

    # 2. Calcular n = p * q
    n = p * q

    # 3. Calcular o Totiente de Euler: phi(n) = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)

    # 4. Escolher o expoente de cifragem (e)
    # 'e' deve ser coprimo de phi e 1 < e < phi
    e = random.randrange(2, phi)
    g = mdc(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = mdc(e, phi)

    # 5. Calcular o expoente de decifragem (d) usando o Inverso Modular
    d = inverso_modular(e, phi)

    # Chave Pública = (e, n), Chave Privada = (d, n)
    return ((e, n), (d, n))

# ==========================================
# 3. CIFRAGEM E DECIFRAGEM
# ==========================================

def cifrar(chave_publica, mensagem_clara):
    """
    Converte cada caractere para seu valor numérico (ASCII) e 
    aplica a fórmula RSA: c = (m ^ e) mod n
    """
    e, n = chave_publica
    # pow(base, exp, mod) é a função nativa do Python para aritmética modular
    mensagem_cifrada = [pow(ord(char), e, n) for char in mensagem_clara]
    return mensagem_cifrada

def decifrar(chave_privada, mensagem_cifrada):
    """
    Aplica a fórmula inversa RSA: m = (c ^ d) mod n
    e converte os números de volta para caracteres ASCII.
    """
    d, n = chave_privada
    mensagem_clara = [chr(pow(char, d, n)) for char in mensagem_cifrada]
    return ''.join(mensagem_clara)

if __name__ == '__main__':
    print("=== SISTEMA DE CRIPTOGRAFIA ASSIMÉTRICA (RSA) ===")
    
    print("\n1. Gerando par de chaves...")
    chave_publica, chave_privada = gerar_par_de_chaves()
    print(f"Chave Pública (e, n): {chave_publica}")
    print(f"Chave Privada (d, n): {chave_privada}")
    
    mensagem = input("\nDigite a mensagem secreta para cifrar: ")
    
    print("\n2. Cifrando a mensagem com a Chave Pública...")
    texto_cifrado = cifrar(chave_publica, mensagem)
    print(f"Mensagem Cifrada (blocos numéricos): {texto_cifrado}")
    
    print("\n3. Decifrando a mensagem com a Chave Privada...")
    texto_recuperado = decifrar(chave_privada, texto_cifrado)
    print(f"Mensagem Recuperada: '{texto_recuperado}'")