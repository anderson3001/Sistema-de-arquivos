#Sistema para manipulação de arquivos de uma escola
#Funções utilizadas:
def adc(arquivo):
    nome = input("Nome:")
    mat = input("Número de matrícula:")
    p1 = float(input("Nota da P1:"))
    p2 = float(input("Nota da P2:"))
    trab = float(input("Nota do trabalho:"))
    with open("arquivo.csv", "a") as arquivo:
        arquivo.write(f"\n{nome}\t{mat}\t{p1}\t{p2}\t{trab}")
def exib(arquivo):
    with open("arquivo.csv", "r") as arquivo:
        for linha in arquivo:
            arq = list(linha.split("\t"))
            print(f"Nome:{arq[0]} | Matrícula: {arq[1]} | P1: {arq[2]} | P2: {arq[3]} | Trabalho: {arq[4]}")
def  ordemalfa(arquivo):
    with open("arquivo.csv", "r") as arquivo:
        x = arquivo.readlines()
        alfa = sorted(x, key=str.lower)
        for i in alfa:
            lista = list(i.split("\t"))
            P1 = float(lista[2])
            P2 = float(lista[3])
            trabalho = float(lista[4])
            media = round((4 * P1 + 4 * P2 + 2 * trabalho) / 10, 2)
            print(f"Nome: {lista[0]} | Matrícula: {lista[1]} | Nota da P1: {lista[2]} | Nota da P2: {lista[3]} | Nota do trabalho: {lista[4]} | Média: {media}")

def ordemmedia(arquivo):
    with open("arquivo.csv", "r") as arquivo:
        info = []
        arq = arquivo.readlines()
        for linha in arq:
            lista = list(linha.split("\t"))
            P1 = float(lista[2])
            P2 = float(lista[3])
            trabalho = float(lista[4])
            media = round((4 * P1 + 4 * P2 + 2 * trabalho) / 10, 2)
            lista.append(media)
            info.append(lista)
        ordem = sorted(info, key=lambda x:x[5],reverse=True)
        for i in range(len(ordem)):
            print(f"Nome: {ordem[i][0]} | Matrícula: {ordem[i][1]} | Nota da P1: {ordem[i][2]} | Nota da P2: {ordem[i][3]} | Nota do trabalho: {ordem[i][4]} | Média: {ordem[i][5]}")
def aluno(arquivo):
    with open("arquivo.csv", "r") as arquivo:
        aluno = input("Digite o nome completo do aluno:")
        x = False
        for linha in arquivo:
            lista = list(linha.split("\t"))
            if aluno in lista:
                print(f"Nome: {lista[0]} | Matrícula: {lista[1]} | Nota P1: {lista[2]} | Nota P2: {lista[3]} | Nota trbalho: {lista[4]}")
                x = True
                break
        if x == False:
            print("Aluno não está nos arquivos")
def apagar(arquivo):
    with open("arquivo.csv", "r") as arquivo:
        nome = input("Nome do aluno:")
        linhas = arquivo.readlines()
        x = False
        for linha in linhas:
            lista = list(linha.split("\t"))
            if nome in lista:
                linhas.remove(linha)
            xx = open("arquivo.csv","w")
            xx.writelines(linhas)
            xx.close()
            x = True
            break
        if x == False:
            print("Aluno não está nos arquivos")
def editar(arquivo):
    with open("arquivo.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        aluno = input("Nome do aluno a ser editado:")
        i = 0
        for linha in linhas:
            lista = list(linha.split("\t"))
            x = False
            if aluno in lista:
                nome = input("Nome atualizado:")
                mat = input("Número de matrícula atualiazado:")
                p1 = float(input("Nota da P1 atualizada:"))
                p2 = float(input("Nota da P2 atualizada:"))
                trab = float(input("Nota do trabalho atualizada:"))
                linhas[i] = f"{nome}\t{mat}\t{p1}\t{p2}\t{trab}\n"
                xx = open("arquivo.csv", "w")
                xx.writelines(linhas)
                x = True
                break
            i += 1
        if x == False:
            print("Aluno não está nos arquivos")

#criação/abertura do arquivo
with open("arquivo.csv","w") as arquivo:
    arquivo.write("Ana da Costa\t100000\t9.7\t8.8\t10.0")
    arquivo.write("\nJoão Silva\t100001\t5.0\t8.9\t10.0")
    arquivo.write("\nRicardo Pereira Peçanha\t100001\t7.5\t10.0\t10.0")
#loop que gera o menu interativo
while True:
    print("[1] Deseja adcionar aluno ao arquivo?")
    print("[2] Deseja ler o arquivo com as informações dos alunos?")
    print("[3] Deseja exibir alunos em ordem alfabetica?")
    print("[4] Deseja exibir alunos em ordem decrescente de média?")
    print("[5] Deseja verificar se um aluno está nos arquivos?")
    print("[6] Deseja editar informações de um aluno?")
    print("[7] Deseja apagar aluno dos arquivos?")
    print("[8] Deseja encerrar programa?")
#parte "interativa" do menu
    ent = input("Escolha uma opção:")
    if ent == "1":
        adc(arquivo)
    elif ent == "2":
        exib(arquivo)
    elif ent == "3":#pendente
        ordemalfa(arquivo)
    elif ent == "4":
        ordemmedia(arquivo)
    elif ent == "5":
        aluno(arquivo)
    elif ent == "6":
        editar(arquivo)
    elif ent == "7":
        apagar(arquivo)
    elif ent == "8":
        break