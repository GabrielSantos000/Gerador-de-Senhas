#Gerador de senhas
import random

"""
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
especiais = ['!', '@', '#', '$', '%', '&', '*', '+', '_', '?', '-']
"""

def password(quant):
    caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1', '2', '3', '4', '5', '6', '7', '8', '9', '0','!', '@', '#', '$', '%', '&', '*', '+', '_', '?', '-']

    if quant > 16 or quant < 4:
        return print("Você ultrapassou o limite de caractéres ou não chegou na quantidade necessária. Tente novamente!")
    else:
        print(f"A sua senha de {quant} dígitos é:")
        #listagem dos valores aleatórios obtidos
        caracteres_sorteadas = random.sample(caracteres, quant)
        #Embaralhar os caractéres com o shuffle do random
        random.shuffle(caracteres_sorteadas)
        #Convertendo lista para string utilizando o join
        caracteres = "".join(caracteres_sorteadas)

    return print(caracteres)

password(9)

