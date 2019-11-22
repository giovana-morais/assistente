# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import configparser
import utils

# o escopo diz respeito ao tipo de acesso que teremos ao nosso calendário
# caso mude o escopo, delete o arquivo token.pickle
SCOPES = ['https://www.googleapis.com/auth/calendar']

def inicia_servico():
    creds = None

    # o arquivo token.pickle salva os acessos do usuário e atualiza os token,
    # e é criado automaticamente quando o fluxo de autorização é completado
    # pela primeira vez
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # se não houver credenciais válidas disponíveis, faça login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # salve as credenciais para a próxima execução
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)


    return build('calendar', 'v3', credentials=creds)


def get_eventos(qtd=3):
    service = inicia_servico()

    # chamando a API do Google Agenda
    agora = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indica UTC
    print(f'Pegando os próximos {qtd} eventos')
    eventos_result = service.events().list(calendarId='primary', timeMin=agora,
                                        maxResults=qtd, singleEvents=True,
                                        orderBy='startTime').execute()
    eventos = eventos_result.get('items', [])

    eventos_str = ""
    if not eventos:
        eventos_str = 'No upcoming eventos found.'

    for evento in eventos:
        try:
            inicio = evento["start"]["dateTime"]
            tipo_data = "datetime"
        except KeyError:
            inicio = evento["start"]["date"]
            tipo_data = "date"

        inicio = utils.converte_data(inicio, tipo_data)
        eventos_str += f"{inicio}, {evento['summary']}\n"

    return eventos_str

def adiciona_evento(titulo, inicio, fim=None, use_default=True):
    """
    Parêmetros:
        titutlo: str
            nome do evento
        inicio : datetime.time
        fim  : datetime.time
    """

    service = inicia_servico()

    if fim == None:
        fim = inicio

    evento = {
            "summary": f"{titulo}",
            "description": "evento adicionado pelo assistente pessoal",
            "start" : {
                "date": inicio.date().__str__(),
                "location": "America/Sao_Paulo"
            },
            "end": {
                "date": fim.date().__str__(),
                "location": "America/Sao_Paulo"
            },
            "reminders": {
                "useDefault": use_default
            }
        }

    evento = service.events().insert(calendarId='primary', body=evento).execute()
    print(f"Evento criado {evento.get('htmlLink')}")
