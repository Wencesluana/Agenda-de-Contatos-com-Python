def menu():
    print("Iniciando programa...")
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
        opcao = input('''============  
            ->AGENDA DE CONTATOS<-  
            MENU:  
            [1] CADASTRAR CONTATO  
            [2] LISTAR CONTATO  
            [3] DELETAR CONTATO  
            [4] BUSCAR CONTATO PELO NOME  
            [5] ATUALIZAR CONTATO
            [6] SAIR DA APLICAÇÃO  
            ============  
            ESCOLHA UMA OPÇÃO ACIMA:  ''')

        if opcao == "1":
            cadastrarContato()
        elif opcao == "2":
            listarContato()
        elif opcao == "3":
            deletarContato()
        elif opcao == "4":
            buscarContatoPeloNome()
        elif opcao == "5":
            atualizarContato()
        elif opcao == "6":
            sair()
        else:
            print("Opção inválida, docinho.")

        voltarMenuPrincipal = input("Deseja voltar ao menu principal? (s/n) ").lower()

def cadastrarContato():
    idContato = input("Escolha o Id do contato: ")
    nome = input("Escreva o nome do seu contato: ")
    telefone = input("Escreva o telefone do contato: ")
    email = input("Escreva o e-mail de contato: ")
    try:
        with open("agenda.txt", "a") as agenda:
            dados = f'{idContato}; {nome}; {telefone}; {email}\n\n'
            agenda.write(dados)
        print(f'Contato gravado com sucesso.')
    except:
        print("Erro na gravação do contato.")

def listarContato():
    try:
        with open("agenda.txt", "r") as agenda:
            for contato in agenda:
                print(contato.strip())
    except FileNotFoundError:
        print("A agenda ainda está vazia.")

def deletarContato():
    nomeDeletado = input("Digite o nome para ser deletado: ").strip().upper()
    
    try:
        with open("agenda.txt", "r") as agenda:
            contatos = agenda.readlines()  
        
        contatos_atualizados = []
        contato_encontrado = False

        for contato in contatos:
            partes = contato.strip().split(";")  
            if len(partes) > 1 and partes[1].strip().upper() == nomeDeletado:
                contato_encontrado = True  
            else:
                contatos_atualizados.append(contato)  
        
        if not contato_encontrado:
            print("Contato não encontrado.")
        else:
            with open("agenda.txt", "w") as agenda:
                agenda.writelines(contatos_atualizados) 
            print(f'Contato deletado com sucesso.')
        listarContato()  
    except FileNotFoundError:
        print("A agenda ainda está vazia.")


def buscarContatoPeloNome():
    nome = input(f'Digite um nome a ser procurado: ').upper()
    try:
        with open("agenda.txt", "r") as agenda:
            encontrados = [contato.strip() for contato in agenda if nome in contato.split(";")[1].upper()]

        if encontrados:
            print("\n".join(encontrados))
        else:
            print("Contato não encontrado.")
    except FileNotFoundError:
        print("A agenda ainda está vazia.")

def atualizarContato():
    nomeDeletado = input("Digite o nome para ser atualizado: ").strip().upper()
    
    try:
        with open("agenda.txt", "r") as agenda:
            contatos = agenda.readlines() 
        
        contatos_atualizados = []
        contato_encontrado = False

        for contato in contatos:
            partes = contato.strip().split(";")  
            if len(partes) > 1 and partes[1].strip().upper() == nomeDeletado:
                contato_encontrado = True  
            else:
                contatos_atualizados.append(contato)  
        
        if not contato_encontrado:
            print("Contato não encontrado.")
        else:
            with open("agenda.txt", "w") as agenda:
                agenda.writelines(contatos_atualizados) 
        listarContato()  
    except FileNotFoundError:
        print("A agenda ainda está vazia.")
    idContato = input("Escolha o Id do contato atualizado: ")
    nome = input("Escreva o nome do seu contato atualizado: ")
    telefone = input("Escreva o telefone do contato atualizado: ")
    email = input("Escreva o e-mail de contato atualizado: ")
    try:
        with open("agenda.txt", "a") as agenda:
            dados = f'{idContato};{nome};{telefone};{email}\n'
            agenda.write(dados)
        print(f'Contato gravado com sucesso.')
    except:
        print("Erro na gravação do contato.")    

def sair():
    print(f'Até mais *aceno*.')
    exit()

def main():
    menu()

main()
