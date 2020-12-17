
"""
Problema 1:
Dado uma lista de dicionários (chave/valor) Python, 
verifique se existe a chave 'nome', e caso exista, 
salve o valor dessa chave em uma segunda lista, de 
modo que não haja repetição de valores na segunda lista.
"""

print("-"*(30))
listaPrimaria = {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'nome': '994063290', 'Marina': '8877-7788', 'nome2': '994063290', 'João': '8887-7778'}
print("Lista primaria: ", listaPrimaria)
print("-"*(30))

keyAsk = 'nome'

listaSecundaria = ['994063290']

# ------------------------------------
# Procurando uma chave especifica em uma lista
# ------------------------------------

if keyAsk in listaPrimaria:

    if not listaPrimaria[keyAsk] in listaSecundaria:
        
        listaSecundaria.append(listaPrimaria[keyAsk])

print("Lista com valor não repetido: ", listaSecundaria)
print("-"*(30))
# ------------------------------------
# Procurando diferentes valores em uma lista
# ------------------------------------

listaSecundaria = []

for chave in listaPrimaria:

    if not listaPrimaria[chave] in listaSecundaria:
        
        listaSecundaria.append(listaPrimaria[chave])

print("Lista com valores não repetidos: ", listaSecundaria)
print("-"*(30))
