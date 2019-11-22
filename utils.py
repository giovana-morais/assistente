import re
import datetime

def converte_data(data_string, tipo):
    """
    Função responsável pela conversão da string de data em
    uma string que nosso assistente consiga ler melhor

    Parâmetros
    ---
        data_string : str
        tipo : str
            o tipo varia entre [date, datetime]

    Retorno
    ---
        string em formato "humano"
    """

    final_str = ""
    dia, mes, ano = None, None, None
    hora, minuto = None, None

    if tipo == "datetime":
        dia, mes, ano = separa_data(data_string.split("T")[0])
        hora, minuto = separa_horario(data_string.split("T")[1])
    elif tipo == "date":
        dia, mes, ano = separa_data(data_string)
    else:
        raise TypeError("Tipo desconhecido para data_string")

    return gera_str_data(dia, mes, ano, hora, minuto)

def gera_str_data(dia, mes, ano, hora=None, minuto=None):
    """
    Gera uma string com o melhor jeito a se dizer uma data recebida

    Parâmetros
    ---
        dia : str
        mes : str
        ano : str
        hora : str
        minuto : str

    Retorno
    ---
        str_ : str
            string com o texto gerado
    """
    meses = {"01": "Janeiro",
             "02": "Fevereiro",
             "03": "Março",
             "04": "Abril",
             "05": "Maio",
             "06": "Junho",
             "07": "Julho",
             "08": "Agosto",
             "09": "Setembro",
             "10": "Outubro",
             "11": "Novembro",
             "12": "Dezembro"}

    hoje = datetime.datetime.now()
    str_ = ""

    if hoje.day == int(dia) and hoje.month == int(mes) and hoje.year == int(ano):
        str_ += "hoje"
    elif hoje.day != int(dia) and hoje.month == int(mes) and \
         hoje.year == int(ano):
        str_ += f"Dia {dia}"
    elif hoje.month != int(mes) and hoje.year == int(ano):
        str_ += f"Dia {dia} de {meses[mes]}"
    else:
        str_ += f"Dia {dia} de {meses[mes]} de {ano}"

    if hora != None:
        str_ += f" às {hora}"

    if minuto != None:
        str_ += f" e {minuto}"

    return str_

def str_to_data(data_string):
    # TODO: descobrir como usar o NLP aqui tbm pq nem a pau que eu vou
    # ficar processando tudo na mão
    meses = {"janeiro": 1,
            "fevereiro": 2,
             "março":  3,
             "abril":  4,
             "maio":   5,
             "junho":  6,
             "julho":  7,
             "agosto": 8,
             "setembro": 9,
             "outubro": 10,
             "novembro": 11,
             "dezembro": 12}

    dias = {"primeiro": 1,
            "dois": 2,
            "três": 3,
            "quatro": 4,
            "cinco": 5,
            "seis": 6,
            "sete": 7,
            "oito": 8,
            "nove": 9,
            "dez": 10,
            "onze": 11,
            "doze": 12,
            "treze": 13,
            "quatorze": 14,
            "quinze": 15,
            "dezesseis": 16,
            "dezessete": 17,
            "dezoito": 18,
            "dezenove": 19,
            "vinte": 20,
            "vinte e um": 21,
            "vinte e dois": 22,
            "vinte e três": 23,
            "vinte e quatro": 24,
            "vinte e cinto": 25,
            "vinte e seis": 26,
            "vinte e sete": 27,
            "vinte e oito": 28,
            "vinte e nove": 29,
            "trinta": 30,
            "trinta e um": 31}

    anos = {"dois mil e vinte" : 2020,
            "dois mil e vinte e um": 2021}

    if "hoje" in data_string:
        data = datetime.datetime.now()
    elif "amanhã" in data_string or "amanha" in data_string:
        hoje = datetime.datetime.now()
        data = datetime.datetime(hoje.year, hoje.month, hoje.day + 1)
    else:
        lista_data = data_string.split(" de ")
        dia = dias[lista_data[0]]
        mes = meses[lista_data[1]]
        ano = anos[lista_data[2]]

        data = datetime.datetime(ano, mes, dia)

    return data

def separa_data(data_string):
    """
    Separa uma string em dia, mes e ano

    Parâmetros
    ---
        data_string : str
            string no formato YYYY-mm-dd

    Retorno
    ---
        dia : str
        mes : str
        ano : str
    """
    data = data_string.split('-')
    dia = data[2]
    mes = data[1]
    ano = data[0]
    return dia, mes, ano

def separa_horario(horario_string):
    """
    Separa uma string em hora e minuto, descartando as outras informações

    Parâmetros
    ---
        horario_string : str
            string no formato HH:MM:SS.FFFF

    Retorno
    ---
        hora : str
        minuto : str
    """
    horario = horario_string.split(':')
    hora = horario[0]
    minuto = horario[1]

    return hora, minuto

def identifica_qtd(comando):
    # TODO: aplicar NLP aqui pra conseguir pegar a quantidade certa?
    """
    Identifica a quantidade dita em uma frase.
    Por exemplo, "peguei três laranjas" deve retornar o inteiro 3.
    ATENÇÃO: Essa função está limitada por enquanto em até 10 unidades

    Parâmetros
    ---
        comando : str
            string com o comando de voz dado

    Retorno
    ---
        qtd : int
            inteiro com a quantidade identificada
    """
    numeros = { "um": 1,
                "dois": 2,
                "três": 3,
                "quatro": 4,
                "cinco": 5,
                "seis": 6,
                "sete": 7,
                "oito": 8,
                "nove": 9,
                "dez": 10 }

    num_str = r'.*(um|dois|três|quatro|cinco|seis|sete|oito|nove|dez).*'

    match = re.match(num_str, comando, re.M|re.I)
    qtd = None

    if match != None:
        qtd = numeros[match.group(1)]

    return qtd

if __name__ == "__main__":
    print(str_to_data("dez de agosto de dois mil e vinte e um"))

