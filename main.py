import speech_recognition as sr
import assistente as migo
import datetime
import cal

## TODO:
# 1. inserir módulo de reconhecimento de voz
# 2. spotify?


if __name__ == "__main__":

    while True:
        migo.executa(migo.aguarda_comando())

    #eventos = cal.get_eventos()

    # start = datetime.datetime(2019, 11, 8)
    # end = start
    # #cal.add_event("Evento teste", start, end)

    # name = "Lula Livre"
    # print(f"Creating {name} event")
    # cal.add_event(name, start, end)
