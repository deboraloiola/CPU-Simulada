"""
ULA DE 8 
AOC 2026.2

Os alunos devem implementar as operações marcadas como IMPLEMENTAR.
"""

def limitar_8bits(valor):
    return valor & 0xFF


def ula(operacao, a, b=0):
    a = limitar_8bits(a)
    b = limitar_8bits(b)

    if operacao == "ADD":
        # IMPLEMENTADO
        resultado = a + b

    elif operacao == "SUB":
        # IMPLEMENTADO
        resultado = a - b

    elif operacao == "AND":
        # IMPLEMENTADO
        resultado = a & b

    elif operacao == "OR":
        # IMPLEMENTADO
        resultado = a | b

    elif operacao == "XOR":
        # IMPLEMENTADO
        resultado = a ^ b

    else:
        raise ValueError(f"Operação inválida: {operacao}")

    return limitar_8bits(resultado) #Saída também deve ser limitada a 8 bits
