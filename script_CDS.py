#!/usr/bin/env python3

import sys  # Permite o acesso das funções 'sys.argv[]' que funcionam pela linha de comando!

# Verifica se o comprimento adequado de argumentos na linha de comando foi ultrapassado!
if len(sys.argv) != 8:
    print("Erro: O script precisa de 7 argumentos. O primeiro deve ser uma sequência de DNA e os outros seis devem ser números inteiros.")
    sys.exit(1)

# Captura os argumentos da linha de comando
sequencia_dna = sys.argv[1]

# Confere se os seis últimos argumentos da linha de comando são números e inteiros!
if sys.argv[2].isdigit() and sys.argv[3].isdigit() and sys.argv[4].isdigit() and sys.argv[5].isdigit() and sys.argv[6].isdigit() and sys.argv[7].isdigit():
    n1, n2, n3, n4, n5, n6 = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
else:
    print("Erro: Os seis últimos argumentos devem ser números e inteiros.")
    sys.exit(1)

# Tamanho da sequência de DNA
dna_len = len(sequencia_dna)
# Verifica se os números são válidos em relação ao tamanho da sequência de DNA, ou seja, devem ser menores ou iguais ao tamanho da sequência de DNA!
if n1 > dna_len or n2 > dna_len or n3 > dna_len or n4 > dna_len or n5 > dna_len or n6 > dna_len:
    print("Erro: Todos os números inteiros devem ser menores ou iguais ao tamanho da sequência de DNA.")
    sys.exit(1)

# Extrai as CDS 1, CDS 2 e CDS 3
cds1 = sequencia_dna[n1-1:n2]
cds2 = sequencia_dna[n3-1:n4]   # O n-1 serve para acessar o elemnto corretoda sequencia, por exemplo o primeiro número 'n1-1' (index 0), já que somente n1 iria acessar o segundo (index 1)! E assim em diante para cds2 e cds3
cds3 = sequencia_dna[n5-1:n6]
# Verifica se a CDS 1 começa com o códon de início ATG
if cds1.startswith("ATG"):
    # Se começar com ATG, verifica se a CDS 3 termina com um códon de parada
    if cds3.endswith("TAG") or cds3.endswith("TAA") or cds3.endswith("TGA"):
        # Se ambas as condições forem verdadeiras, concatena e imprime as CDS
        cds_concat = cds1 + cds2 + cds3
        print("Sequência concatenada:", cds_concat)
    else:
        # Se CDS 3 não termina com um códon de parada
        print("Erro: CDS 3 não termina com um códon de parada (TAG, TAA ou TGA).")
else:
    # Se CDS 1 não começa com ATG
    print("Erro: CDS 1 não começa com o códon de início ATG.")
