# Formar linhas de titulo para um texto
def titulo(escrita):
    x = len(escrita)
    print(f'-' * x)
    print(escrita)
    print('-' * x)

titulo(input('Título: '))
