#!/usr/bin/env python3

# Solicita ao user uma sequência de DNA!
seq = input("Coloque uma sequência de DNA: ")

# Verifica se a sequência contém apenas caracteres válidos (A, T, C, G)
for nt in seq:       # Cria um loop, que testa cada nucleotídeo (caracter) inserido na sequência 
    if nt not in "ATCG":   # Se pelo menos um caracter na sequência não for um nucleotídeo ('A','G','T' ou 'C'), imprime mensagem de erro!
        print("Erro! Por favor, insira apenas os caracteres A, T, C ou G.")
        exit()  # Sai do programa caso a sequência inserida seja inválida

# Usa a função de string 'count()' para quantificar quantas vezes cada nucleotídeo aparece na sequência inserida!
contagem_nt_A = seq.count('A')
contagem_nt_T = seq.count('T')
contagem_nt_C = seq.count('C')
contagem_nt_G = seq.count('G')

# Exibe a contagem de cada nucleotídeo
print(f"A: {contagem_nt_A}")
print(f"T: {contagem_nt_T}")
print(f"C: {contagem_nt_C}")
print(f"G: {contagem_nt_G}")
