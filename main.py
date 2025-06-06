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
    venceu = False

    categoria = input('Escolha uma categoria: Objetos, Comidas ou Cidade.\n').capitalize()

    palavra_aleatoria = ''

    if categoria == 'Objetos':
        palavra_aleatoria = random.choice(objetos)
    elif categoria == 'Comidas':
        palavra_aleatoria = random.choice(comidas)
    elif categoria == 'Cidade':
        palavra_aleatoria = random.choice(cidades)

    if palavra_aleatoria != '':
        for p in palavra_aleatoria:
            if p == ' ':
                pal_secreta += ' '
            else:
                pal_secreta += '_'

        while erros < 7 and venceu == False:
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
                        venceu = True
                        resp = input('Deseja jogar novamente? (S - Sim  ||  N - Não)\n').upper()
            else:
                erros += 1
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
                    print('A palavra era:', palavra_aleatoria)
                    resp = input('Deseja iniciar? (S - Sim  ||  N - Não)\n').upper()
    else:
        print('Categoria Inválida')
        resp = input('Deseja iniciar? (S - Sim  ||  N - Não)\n').upper()

print('Que pena, até breve então')
