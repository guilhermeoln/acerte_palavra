secreto = 'perfume'
digitadas = []
jogar_novamente = True
chances = 3

while jogar_novamente == True:
  if chances < 0:
    print('Você perdeu!')
    break

  
  letra = input('Digite uma letra: ')

  if len(letra) > 1:
    print('Aaaaah,isso não vale!')
    continue

  digitadas.append(letra)

  if letra in secreto:
    print(f'Uhulll,a letra {letra} existe na palavra')
  else:
    print(f'Affff,a letra {letra} não existe na palavra')
    chances -= 1
    digitadas.pop()

  secreto_temporario = ''

  for letra_secreta in secreto:
    if letra_secreta in digitadas:
      secreto_temporario += letra_secreta
    else:
      secreto_temporario += '*'

  print(secreto_temporario)

  if secreto_temporario == secreto:
    print('Você venceu!')
    jogar_novamente = False