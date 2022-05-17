#Utilizar escopo de variável e Return para eleger o voto opcional

def maioridade (nascimento):
    from datetime import datetime
    year = int(datetime.now().strftime('%Y')) - nascimento
    return year


voto = maioridade(int(input('Digite seu ano de nascimento: ')))
if voto >= 18:
    print(f'Você tem {voto} anos e possui voto obrigatório.')
elif voto >= 16:
    print(f'Você tem {voto} anos e seu voto é facultativo')
else:
    print(f'Você tem {voto} e ainda não possui idade suficiente para votar.')