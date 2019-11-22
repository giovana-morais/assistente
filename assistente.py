# -*- coding: utf-8 -*-

# bibliotecas padrão
import sys
import time
import random
import configparser

# texto para fala
import pyttsx3
from gtts import gTTS
from pygame import mixer

# reconhecimento de voz
import speech_recognition as sr

# requisicoes
import requests

# bibliotecas de projeto
import cal
import tedio
import utils
import youtube as yt

config = configparser.ConfigParser()
config.read("config.ini")

def fale(texto):
    """
    Método para ler o texto recebido

    Parâmetros
    ---
        texto : str
    """

    if config["assistente"]["engine"] == "gtts":
        fale_gtts(texto)
    elif config["assistente"]["engine"] == "pyttsx":
        fale_pyttsx(texto)

def fale_gtts(texto):
    for linha in texto.splitlines():
        print(f"lendo linha {linha}")
        texto_para_fala = gTTS(text=linha, lang='pt-br')
        texto_para_fala.save('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()
        # número COMPLETAMENTE ARBITRÁRIO de espera
        # pro gTTS conseguir falar
        numero_magico = len(linha)/11
        time.sleep(numero_magico)

def fale_pyttsx(texto):
    print(texto)
    engine = pyttsx3.init()

    engine.setProperty("rate", 95)
    engine.setProperty("voice", "brazil")
    engine.say(texto)
    engine.runAndWait()

def aguarda_comando():
    # Inicializando o reconhecimento de voz
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1

        # o recognizer precisa ajustar um limite de barulho externo pra
        # conseguir identificar o que a gente tá falando e o que é ruído
        # de fundo
        print("Ajustando para ruído de fundo")
        r.adjust_for_ambient_noise(source, duration=2)
        print("Estamos prontos")
        audio = r.listen(source)
    try:
        comando = r.recognize_google(audio, language="pt-BR").lower()
        print(f"Você disse: {comando}")
    # repete o comando até que entenda o que a gente tá tentando dizer
    except sr.UnknownValueError:
        print("Não foi possível ouvir seu último comando")
        comando = aguarda_comando();

    return comando

def executa(comando):
    erros = [ "Não entendi o que você disse",
                "Pode repetir?",
                "O que?",
                "Será que você pode parar de falar igual um animal?" ]

    if config["assistente"]["nome"] in comando:
        fale("Oi! Em que posso te ajudar?")
    elif "sentido da vida" in comando:
        fale("A resposta para a vida, o universo e tudo mais é quarenta \
                e dois")
    elif "adicionar um evento" in comando or "adicionar compromisso" in comando:
        # receber aqui o nome do evento e a data dele
        # por enquanto vamos ignorar o horário
        fale("Qual o nome seu evento?")
        while True:
            titulo = aguarda_comando()
            fale(titulo)
            fale("O nome do evento está correto?")
            confirmacao = aguarda_comando()
            if "sim" in confirmacao:
                print(f"titulo confirmado: {titulo}")
                break
            fale("Repita o nome, por favor")
        fale("Qual a data?")
        while True:
            data = aguarda_comando()
            fale(data)
            fale("A data do evento está correta?")
            confirmacao = aguarda_comando()

            if "sim" in confirmacao:
                print("data confirmada: {data}")
                break
            fale("Repita a data, por favor")

        data = utils.str_to_data(data)
        cal.adiciona_evento(titulo, data)
    elif "Harry Potter" in comando or "chapéu seletor" in comando:
        r = requests.get("https://www.potterapi.com/v1/sortingHat")
        casas = {"Gryffindor": "grifinória", "Hufflepuff": "lufa lufa",
                "Ravenclaw": "corvinal", "Slytherin": "sonserina"}
        casa = r.text.replace("\"", "")

        fale(f"Sua casa seria {casas[casa]}")
    elif "agenda" in comando or "eventos" in comando:
        qtd = utils.identifica_qtd(comando)
        fale("Aguarde enquanto checo seus eventos")
        eventos = cal.get_eventos(qtd)
        print(f"eventos {eventos}")
        fale(eventos)
        time.sleep(3)
    elif "youtube" in comando or "video" in comando:
        fale("Qual o vídeo?")
        while True:
            video = aguarda_comando()
            fale(video)
            fale("O nome está correto?")
            confirmacao = aguarda_comando()
            if "sim" in confirmacao:
                print(f"video {video}")
                break
            fale("repita o nome, por favor")
        yt.abre_video(video)
    elif "ideia" in comando or "entediada" in comando:
        fale(tedio.get_ideia())
    elif "piada" in comando:
        # https://github.com/kivson/charadas
        r = requests.get("https://us-central1-kivson.cloudfunctions.net/charada-aleatoria", headers={"Accept":"application/json"})
        r = r.json()
        fale(r["pergunta"])
        fale(r["resposta"])
        fale("rsrsrs")
    elif "qual o seu nome" in comando:
        fale(f"Meu nome é {config['assistente']['nome']}")
    elif "faça um funk" in comando or "faz um funk" in comando:
        fale ("tchum tcha tcha tum tcha tcha")
    elif "gato" in comando or "miau" in comando:
        fale("miau")
    elif "tchau" in comando:
        fale("Até mais!")
        sys.exit()
    # elif "abra" in comando and "rascunho" in comando:
    #     fale("Iniciando rascunho")
    else:
        erro = random.choice(erros)
        print(erro)
        fale(erro)

if __name__ == "__main__":
    # refs:  https://www.programmableweb.com/category/random/api


    # eventos = cal.get_eventos(3)
    # fale(eventos)
    # print(eventos)
    fale("oi gente do bem! como vocês estão nessa linda tarde de quinta?")
    fale("vem de zap")
    # print(r.text)
    # print(r.json())

