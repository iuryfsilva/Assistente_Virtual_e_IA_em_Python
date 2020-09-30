version = "1.4.0"

def intro():
    mensagem = "Assistente - version {} / by: Fulano Beltrano Ciclano".format(version)
    print("-" * len(mensagem) + "\n{}\n".format(mensagem) + "-" * len(mensagem))

listaErros = [
    "Don't understand....",
    "Sorry, i don't understand",
    "Repeat again please"
]

conversas = {
    "Oi": "Hello, how are you?",
    " eu fine and you": "I'm fine too, thank's to ask",
}

comandos = {
    "desligar": "desligando",
    "reiniciar": "reiniciando"
}

def verificaNome(userName):
    if userName.startswith("Meu nome é"):
        userName = userName.replace("Meu nome é", "")
    if userName.startswith("Eu me chamo"):
        userName = userName.replace("Eu me chamo", "")
    if userName.startswith("Eu sou o"):
        userName = userName.replace("Eu sou o", "")
    if userName.startswith("Eu sou a"):
        userName = userName.replace("Eu sou a", "")
    
    return userName

def verificaNomeExiste(nome):
    dados = open("dados/nomes.txt", "r")
    nomeList = dados.readlines()
    
    if not nomeList:
        vazio = open("dados/nomes.txt", "r")#abre o arquivo nomes no diretorio dados no modo de leitura
        conteudo = vazio.readlines()
        conteudo.append("{}".format(nome))
        vazio = open("dados/nomes.txt", "w")#abre o arquivo nomes no diretorio dados no modo de escrita
        vazio.writelines(conteudo)
        vazio.close()
        
        return "Hello {}, nice to meet you!".format(nome)
    
    for linha in nomeList:
        if linha == nome:
            return "Hello {}, we haven been meeted!".format(nome)
    
    #abre o arquivo nomes no diretorio dados no modo de leitura    
    vazio = open("dados/nomes.txt", "r")
    conteudo = vazio.readlines()
    conteudo.append("\n{}".format(nome))
    #abre o arquivo nomes no diretorio dados no modo de escrita
    vazio = open("dados/nomes.txt", "w")
    vazio.writelines(conteudo)
    vazio.close()
    
    return "Hello {}, it's the first time than we talking".format(nome)

def nameList():
    try: 
        nomes = open("dados/nomes.txt", "r")
        nomes.close()
    
    # Cria a lista de nomes caso ela não seja encontrada
    except FileNotFoundError:
        nomes = open("dados/nomes.txt", "w")
        nomes.close()
    