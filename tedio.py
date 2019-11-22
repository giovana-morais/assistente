# -*- coding: utf8 -*-
# baseado no bored api <https://www.boredapi.com/>

import random


ideias = [
    "saia para correr",
    "vá olhar o céu",
    "limpe seu armário e doe as roupas que não usa mais",
    "aprenda a usar um arduino",
    "chame uns amigos pra uma noite de jogos",
    "aprenda como a internet funciona",
    "faça um plano de dominação mundial",
    "aprenda a escrever com a sua mão não dominante",
    "veja um filme que você nunca veria",
    "lave uma louça",
    "faça carinho em um animal de rua",
    "escute uma música que você não escuta faz tempo",
    "escute um gênero novo de música",
    "comece um diário",
    "aprenda a assoviar com seus dedos",
    "ligue pra sua mãe e diga que a ama",
    "soque um nazista",
    "escute seu álbum favorito",
    "saia pra fazer uma caminhada",
    "visite um museu perto da sua casa" ]

def get_ideia():
    return random.choice(ideias)


if __name__ == "__main__":
    print(get_ideia())

