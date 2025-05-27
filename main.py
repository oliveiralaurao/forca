import random

objetos = ['CANETA', 'LÁPIS', 'BORRACHA']
cidades = ['HONG KONG']
comidas = ['ARROZ', 'FEIJÃO', 'MACARRÃO']


print("*********************************")
print("***Bem vindo ao jogo da Forca!***")
print("*********************************")
resp = input('Deseja iniciar? (S - Sim  ||  N - Não)\n').upper()

while resp == 'S':
    erros = 0
    letras = []
    pal_secreta = ''
    categoria = input('Escolha uma categoria: Objetos, Comidas ou Cidade.\n').capitalize()

    if categoria == 'Objetos':

        tamanho = len(objetos) - 1
        sorteio = random.randint(0, tamanho)
        palavra_aleatoria = objetos[sorteio]

    elif categoria == 'Comidas':
        tamanho = len(comidas) - 1
        sorteio = random.randint(0, tamanho)
        palavra_aleatoria = comidas[sorteio]

    elif categoria == 'Cidade':
        tamanho = len(cidades) - 1
        sorteio = random.randint(0, tamanho)
        palavra_aleatoria = cidades[sorteio]

    else:
        print('Categoria Inválida')

    for p in palavra_aleatoria:
        if p == ' ':
            pal_secreta += ' '
        else:
            pal_secreta += '_'

    while erros < 7:

        print(''.join(pal_secreta))
        letra_digitada = input('Digite somente uma letra: \n').upper()

        if letra_digitada in palavra_aleatoria:
            if letra_digitada in letras:
                print('Essa letra já foi, digite outra')
            else:
                letras.append(letra_digitada)
                for i in range(len(palavra_aleatoria)):
                    if palavra_aleatoria[i] == letra_digitada:
                        pal_secreta = pal_secreta[:i] + letra_digitada + pal_secreta[i + 1:]
                print('Letra correta!')

                if '_' not in pal_secreta:
                    print('Parabéns, você ganhou!')
                    print('A palavra era:', palavra_aleatoria)
                    resp = input('Deseja jogar novamente? (S - Sim  ||  N - Não)\n').upper()
        else:
            erros = erros + 1
            print("  _______     ")
            print(" |/      |    ")

            if erros == 1:
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")

            if erros == 2:
                print(" |      (_)   ")
                print(" |      \     ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")

            if erros == 3:
                print(" |      (_)   ")
                print(" |      \|    ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")

            if erros == 4:
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")

            if erros == 5:
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")
            if erros == 6:
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      /     ")
                print(" |            ")
                print("_|___         ")

            if erros == 7:
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")
                print(" |            ")
                print("_|___         ")
                print('Você perdeu! :(')
                resp = input('Deseja iniciar? (S - Sim  ||  N - Não)\n').upper()


print('Que pena, até breve então')
