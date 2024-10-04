#!/bin/bash      

# Comando que mostra em qual diretório/pasta você está
echo "O diretório que você está:" # 'echo' exibe a mensagem no terminal
pwd  # o comando 'pwd' imprimirá o caminho completo da pasta/diretório onde você está

# Comando que gere uma lista com detalhes do conteúdo da sua pasta HOME e redirecione essa lista para o arquivo: lista_HOME.txt
echo "Gerando uma lista com detalhes da pasta HOME e redireciona para o arquivo lista_HOME.txt:" # 'echo' exibe a mensagem no terminal
ls -l $HOME > lista_HOME.txt # 'ls' lista o conteúdo do diretório em questão. '-l' fornce detalhes adicionais sobre cada arquivo e pasta (permissões, número de links, proprietário, tamanho e data da última modificação). '$HOME' trata do caminho do diretório HOME. '>' indica que a saída do comando deve ser enviada para o arquivo 'lista_HOME.txt'. Esse arquivo de texto será o local para a listagem.
