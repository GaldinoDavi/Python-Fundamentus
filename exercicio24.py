#Informar se a cidade está correta

cidade = input('Qual a cidade? ').strip()
resposta = 'Santo'

print(cidade.title()[:5] == resposta)
