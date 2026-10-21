"""
Este é o programa próprio solicitado para a equipe. Ele utiliza a operação STORE, ADD, SUB E LOAD.
O programa realiza as seguintes operações:
1. Carrega o valor 5 no registrador R0.
2. Carrega o valor 10 no registrador R2.
3. Adiciona o valor de R2 ao valor de R0 e armazena o resultado em R0.
4. Armazena o valor de R0 na posição 15 da memória.
5. Carrega o valor 8 no registrador R1.
6. Subtrai o valor de R1 do valor de R0 e armazena o resultado em R0.
7. Armazena o valor de R1 na posição 14 da memória.
O programa termina com a instrução HALT.

Saída esperada:
======================================
         CPU SIMULADA — 8 BITS
======================================
======================================
RESULTADO FINAL
======================================
Registradores:
  R0 = 07 (7)
  R1 = 08 (8)
  R2 = 0A (10)
  R3 = 00 (0)

Memória:
  00 = LOAD R0, 5
  01 = LOAD R2, 10
  02 = ADD R0, R2
  03 = STORE R0, 15
  04 = LOAD R1, 8
  05 = SUB R0, R1
  06 = STORE R0, 14
  07 = HALT
  08 = 0
  09 = 0
  0A = 0
  0B = 0
  0C = 0
  0D = 0
  0E = 7
  0F = 15
"""

from cpu import CPU
from programas import programa_equipe


cpu = CPU()

for i, instrucao in enumerate(programa_equipe):
    cpu.memoria[i] = instrucao



print("======================================")
print("       CPU SIMULADA — 8 BITS")
print("======================================")

cpu.executar()

print()
print("======================================")
print("RESULTADO FINAL")
print("======================================")

cpu.mostrar_estado(memoria=True)
