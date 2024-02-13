import os

mensagens = []

nome = input("Nome: ")

while True:
  #limpando o terminal
  os.system('clear')

  if len(mensagens) > 0:
    for mensagem in mensagens:
      print(mensagem['nome'], "-", mensagem['texto'])

  print("-------------------")

  # texto
  texto = input("mensagem: ")
  if texto == "fim":
    break

  # adicionando mensagem na lista
  mensagens.append({
    'nome': nome,
    'texto': texto
  })
