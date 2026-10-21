CPU SIMULADA DE 8 BITS
Arquitetura e Organização de Computadores (AOC 2026.2)
Engenharia da Computação, UFC Sobral

Equipe: Debora Monte Loiola e Anderson de Almeida Leandro


1. SOBRE O TRABALHO

Este trabalho é uma CPU simples de 8 bits feita em Python. Ela guarda os
programas na memória, lê uma instrução de cada vez e executa seguindo o ciclo
Fetch, Decode e Execute. As contas são feitas por uma ULA separada, no arquivo
ula.py.

A CPU tem:

  4 registradores: R0, R1, R2 e R3
  memória com 16 posições (endereços de 0 a 15)
  PC (Program Counter)
  ULA com ADD, SUB, AND, OR e XOR
  dados de 8 bits (valores de 0 a 255)


2. ARQUIVOS

  `cpu.py`        classe CPU (registradores, memória, PC e ciclo de instrução)
  `ula.py`        ULA e a função que limita os valores a 8 bits
  `programas.py`  programas de exemplo que rodam na CPU
  `main.py`       programa de demonstração da nossa equipe
  `testes.py`     testes das instruções e da ULA


3. COMO EXECUTAR

Precisa do Python 3 instalado. Dentro da pasta do projeto, rode:

  python main.py

Para rodar os testes:

  python testes.py


4. INSTRUÇÕES

  LOAD R0, 5      coloca o valor 5 em R0
  STORE R0, 15    guarda o valor de R0 na posição 15 da memória
  ADD R0, R1      R0 recebe R0 + R1
  SUB R0, R1      R0 recebe R0 menos R1
  AND R0, R1      R0 recebe R0 AND R1
  OR R0, R1       R0 recebe R0 OR R1
  XOR R0, R1      R0 recebe R0 XOR R1
  JMP 4           pula para a posição 4 da memória
  HALT            para a execução

Nas operações da ULA (ADD, SUB, AND, OR e XOR), o primeiro registrador é onde
o resultado fica guardado.


5. COMO FUNCIONA

A cada ciclo a CPU faz três coisas:

  Fetch: pega a instrução da memória, na posição que o PC está apontando.
  Decode: separa a operação e os operandos.
  Execute: executa a instrução e atualiza o PC.

Depois de cada instrução, o programa mostra os registradores na tela. Quando
a instrução é um STORE, ele mostra a memória também.

A execução só termina quando chega no HALT. Existe um limite de 100 ciclos
para evitar loop infinito. Se passar disso, dá erro.


6. LIMITE DE 8 BITS

Todo valor passa pela função limitar_8bits, que usa a máscara 0xFF. Então se
uma conta passar de 255 ou der negativa, o resultado volta para a faixa de
0 a 255. Exemplos:

  200 + 100 dá 44
  5 menos 10 dá 251


7. PROGRAMA DA EQUIPE

O programa que montamos usa LOAD, ADD, SUB, STORE e HALT:

  00: LOAD R0, 5
  01: LOAD R2, 10
  02: ADD R0, R2       (R0 = 5 + 10 = 15)
  03: STORE R0, 15     (memória 15 recebe 15)
  04: LOAD R1, 8
  05: SUB R0, R1       (R0 = 15 menos 8 = 7)
  06: STORE R0, 14     (memória 14 recebe 7)
  07: HALT

Resultado final esperado:

  R0 = 07 (7)
  R1 = 08 (8)
  R2 = 0A (10)
  R3 = 00 (0)

  Memória: posição 0E = 7 e posição 0F = 15. As posições de 08 a 0D ficam
  com 0, e as de 00 a 07 guardam as instruções do programa.


8. EXEMPLO DE JMP

Também deixamos no programas.py um programa que testa o salto:

  0: LOAD R0, 5
  1: JMP 4
  2: LOAD R0, 99
  3: LOAD R1, 8
  4: HALT

O JMP 4 faz a CPU pular direto da posição 1 para a 4. Por isso o LOAD R0, 99
nunca é executado e R0 continua valendo 5.


9. TESTES

O testes.py monta pequenos programas na memória, executa e confere o
resultado com assert. Os testes são:

  LOAD, JMP e HALT
  ADD, SUB, AND, OR e XOR
  STORE
  STORE usando o resultado de um ADD

Quando um teste passa aparece [OK] com o nome da instrução.


10. ERROS TRATADOS

  Instrução que não existe: erro ValueError
  STORE com endereço fora de 0 a 15: erro ValueError
  JMP com endereço fora de 0 a 15: erro ValueError
  Operação inválida na ULA: erro ValueError
  Passou de 100 ciclos: erro RuntimeError (provável loop infinito)


11. REGRAS DO PROFESSOR

Não mudamos o nome dos arquivos, a assinatura da função ula(), a estrutura
dos registradores, o tamanho da memória nem a representação de 8 bits.
