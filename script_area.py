#!/usr/bin/env python3
import sys # Permite manipulação de argumentos na linha de comando

if len(sys.argv) != 3:
    print("Erro: Forneça dois inteiros positivos menores que 500.") # Se você colocar na linha de comando mais ou menos de 2 números, imprime uma mensagem de erro! Lembre-se que o índice sys.argv[0] refere-se ao nome do script! 
else:       # Se você colocar dois números na linha de comando...
    for num in range(1,3): # Para os dois números na linha de comando (não começa por 0, pois é o nome do script e a função 'range()' não abrange o último número) 
         if sys.argv[num].isdigit() and int(sys.argv[num]) > 0 and int(sys.argv[num]) < 500: # Verifica se os argumentos colocados na linha de comando possuem caracteres na forma de dígitos e os números colocados estão entre 1 e 499.  
             if num == 1:
                 a = int(sys.argv[num]) # No primeiro número colocado na linha de comando, transforme-o em inteiro
             elif num == 2: 
                 b = int(sys.argv[num]) # No segundo número colocado na linha de comando, transforme-o em inteiro
         else:
            print("Erro: Forneça dois valores inteiros positivos menores que 500.") # Se o número colocado for 0, negativo, 500 ou acima de 500, imprime mensagem de erro!
            break  # Interrompe o loop 'for'
    
    else:
        area = (a*b) / 2  # Realiza o cálculo da área de um triângulo retângulo, onde a e b são os comprimentos dos dois catetos do triângulo.
        print(f"A área do triângulo retângulo com lados a={a} e b={b}, é {area}") # Utiliza a formatação de strings para imprimir uma frase contendo os catetos do triângulo, já formatados para serem só permitidos dois dígitos de 1 a 499, e o resultado do cálculo da área do triângulo retângulo. 
