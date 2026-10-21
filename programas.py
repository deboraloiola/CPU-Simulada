programa_equipe = [
    "LOAD R0, 5",     # Carrega 5 em R0
    "LOAD R2, 10",    # Carrega 10 em R2
    "ADD R0, R2",     # R0 = R0 + R2 (5 + 10 = 15)
    "STORE R0, 15",   # Armazena o valor de R0 (15) na posição 15 da memória
    "LOAD R1, 8",     # Carrega 8 em R1
    "SUB R0, R1",     # R0 = R0 - R1 (15 - 8 = 7)
    "STORE R0, 14",   # Armazena o valor de R0 (7) na posição 14 da memória
    "HALT"               # Termina a execução
]

programa_main_base = [
  "LOAD R0, 5",
  "JMP 4",
  "LOAD R0, 99",
  "LOAD R1, 8",
  "HALT"
]