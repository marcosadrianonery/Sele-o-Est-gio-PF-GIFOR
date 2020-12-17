

aux = 2
erro = 0
# ref_arquivo = open("qbdata.txt","r")
arquivo = open("input_1em_1.txt","r")
maximo = 32762
for i in range(2, maximo,1):

    aux = 2
    print("Entrada: ", i)
    linhas = arquivo.readline()
    print("Entrada arquivo: ", linhas)

    for j in range(1, maximo*2):

        resto = i%aux

        if resto == 0:
            linhas = arquivo.readline()

            print(aux)

            print("Aux: ", aux)
            print("Aux arquivo: ", linhas)

            if not str(aux) in str(linhas):
                erro = erro + 1
                print("erro: ", aux)
                print("Linha: ", linhas)
                print("Num erro: ", erro)

            i = i/aux
        else:
            aux = aux + 1

        if i == 1:
            break
    if not i == 1: 
        print(int(i))
        linhas = arquivo.readline()

print("ERROS: ", erro)