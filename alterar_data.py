from datetime import datetime, date
from time import sleep
from deep_translator import GoogleTranslator

data_de_hoje = datetime(date.today().year, date.today().month, date.today().day)

def mudar_data():
    data_ano_hoje = date.today().year
    data_mes_hoje = date.today().month
    data_dia_hoje = date.today().day

    pergunta = str(input('Deseja alterar o ano? (S/N) ')).upper()
    sleep(0.5)
    print()
    print('Caso tenha pressionado alguma tecla aleatória diferente de "S" será entendido como "N"')
    sleep(0.5)
    if pergunta == 'S':
        print()
        data_ano = int(input('Digite os quatro dígitos do ano que deseja verificar: '))
        sleep(0.5)
        print('Foi adicionado o ano: {}'.format(data_ano))
        sleep(0.5)
        print()
        data_ano_hoje = data_ano
    
    pergunta = str(input('Deseja alterar o mês? (S/N) ')).upper()
    print()
    print('Caso tenha pressionado alguma tecla aleatória diferente de "S" será entendido como "N"')
    print()
    if pergunta == 'S':
        sleep(0.5)
        data_mes = int(input('Digite os dois/um dígito(s) do mês que deseja verificar: '))
        sleep(0.5)
        print()
        print('Foi adicionado o mês: {}'.format(data_mes))
        sleep(0.5)
        print()
        data_mes_hoje = data_mes
    
    pergunta = str(input('Deseja alterar o dia? (S/N) ')).upper()
    print()
    print('Caso tenha pressionado alguma tecla aleatória diferente de "S" será entendido como "N"')
    print()
    if pergunta == 'S':
        sleep(0.5)
        data_dia = int(input('Digite os dois dígitos do dia que deseja verificar: '))
        sleep(0.5)
        print()
        print('Foi adicionado o dia: {}'.format(data_dia))
        sleep(0.5)
        print()
        data_dia_hoje = data_dia
    
    return datetime(data_ano_hoje, data_mes_hoje, data_dia_hoje)

# Verificação de data...
pergunta = str(input('Deseja consultar o dia de hoje? (S/N) ')).upper()
sleep(0.5)
print()
print('Caso tenha pressionado alguma tecla aleatória diferente de "N" será entendido como "S"')
print()
sleep(0.5)
if pergunta == 'N':
    print('A data de hoje é: {}/{}/{}'.format(date.today().day, date.today().month, date.today().year))
    print()
    sleep(0.5)
    data_total = mudar_data()
    print('Nova data:', data_total)
    data_nova = data_total  # Definindo a nova data
else:
    data_nova = data_de_hoje  # Se não for alterado, a nova data é a mesma que a data de hoje
print('Data configurada como {}/{}/{}'.format(data_nova.day, data_nova.month, data_nova.year))

if data_nova.year >= data_de_hoje.year:
    resultado = data_nova.year - data_de_hoje.year
    while resultado > 0:
        print('ano novo')
        resultado -= 1
elif data_nova.year <= data_de_hoje.year:
    resultado = data_de_hoje.year - data_nova.year
    while resultado > 0:
        print('ano velho')
        resultado -= 1

tradutor = GoogleTranslator(source='en',target='pt')
data_mes_trad = tradutor.translate(data_nova.strftime('%B'))
if data_mes_trad == 'Marchar':
    data_mes_trad = 'Março'
elif data_mes_trad == 'Poderia':
    data_mes_trad = 'Maio'
print(data_mes_trad)