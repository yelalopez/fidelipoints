import json
import os

def validar_email(email):
    return "@" in email

def validar_seguidores(seguidores):
    try:
        if seguidores < 0:
            print('Insira um valor válido')
            return False
        return True
    except ValueError:
        print("Por favor insira um número válido")
        return False

def carregar_usuarios(nome_arquivo="usuarios.json"):
    try:
        with open(nome_arquivo, "r") as arquivo:
            usuarios = json.load(arquivo)  
            return usuarios
    except FileNotFoundError:
        return []  

def salvar_usuarios(usuarios, nome_arquivo="usuarios.json"):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def mostrar_dados(usuario):
    os.system('cls' if os.name == 'nt' else 'clear') or None
    print(f'''\n
---------------------------
Dados do Usuário
  Email: {usuario['email']}
  Seguidores: {usuario['seguidores']}
  Pontos: {usuario['pontos']}
---------------------------''') 
    
def deletar_usuario(usuario):
    confirmar = input(f"Deseja deletar seu perfil? Essa ação é irreversivel S - Sim | N - Não: ").strip().lower()
    
    if confirmar != 's':
        print("Operaçao cancelada")
        return
    
    usuarios = carregar_usuarios()

    usuarios = [u for u in usuarios if u['email'] != usuario['email']]

    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)
    
    os.system('cls' if os.name == 'nt' else 'clear') or None
    print("Perfil deletado com sucesso")

def cadastro():
    nome = input("Digite seu nome: ").title()
    email = input("Digite seu email: ")
    
    while not validar_email(email):
        print("Email inválido. Por favor, insira um email válido.")
        email = input("Digite seu email: ")
    
    senha = input("Digite a senha: ")
    
    seguidores = int(input("Digite o número de seguidores: "))
    while not validar_seguidores(seguidores):
        seguidores = int(input("Digite o número de seguidores: "))
    pontos = 0 
    
    usuarios = carregar_usuarios()

    novo_usuario = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "seguidores": seguidores,
        "pontos": pontos
    }

    usuarios.append(novo_usuario)

    salvar_usuarios(usuarios)

    print("\n=======Cadastro realizado com sucesso!=======")
    mostrar_dados(novo_usuario)

def atualizar_perfil(usuario):
    os.system('cls' if os.name == 'nt' else 'clear') or None
    usuarios = carregar_usuarios()

    while True:
        print('''
===== Atualizar perfil =====
  1. Atualizar nome
  2. Atualizar seguidores
  3. Atualizar senha
  4. Voltar ao menu princial
-----------------------------''')
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
          os.system('cls' if os.name == 'nt' else 'clear') or None
          novo_nome = input("Atualize o nome: ")
          usuario['nome'] = novo_nome.tittle()
          print("\nNome atualizado com sucesso!")
          return
                
        elif opcao == 2:
          os.system('cls' if os.name == 'nt' else 'clear') or None
          novo_seguidores = input("Seguidores: ")
          if novo_seguidores:
              try:
                usuario['seguidores'] = int(novo_seguidores)
                print("\nSeguidores atualizado com sucesso!")
                
              except ValueError:
                  print("Por favor insira um número válido")
          return
        elif opcao == 3:
          os.system('cls' if os.name == 'nt' else 'clear') or None
          nova_senha = input("Nova senha: ")
          usuario['senha'] = nova_senha
          print("\nSenha atualizado com sucesso!")
          return
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

    for u in usuarios:
        if u['email'] == usuario['email']:
            u.update(usuario)
            break

    salvar_usuarios(usuarios)
    

def encontrar_usuario(email, senha):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            return usuario
    return None

def menu_usuario(usuario):
    os.system('cls' if os.name == 'nt' else 'clear') or None
    print(f"\nBem-vindo(a), {usuario['nome']}!")
    while True:
        print('''
===== Menu do Usuário =====
  1. Ver perfil
  2. Atualizar perfil
  3. Meus Fidelipoints
  4. Deletar perfil           
  0. Logout
---------------------------''')
    
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_dados(usuario)
        elif opcao == "2":
            atualizar_perfil(usuario)
        elif opcao == "3":
            os.system('cls' if os.name == 'nt' else 'clear') or None
            print(f'''
-----------------------------
Meus Fidelipoints: {usuario['pontos']}
-----------------------------''')
        elif opcao == "4":
            os.system('cls' if os.name == 'nt' else 'clear') or None
            deletar_usuario(usuario)
            break
        elif opcao == "0":
            os.system('cls' if os.name == 'nt' else 'clear') or None
            print('''---------------------------------
| Logout realizado com sucesso |
---------------------------------''')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear') or None
            print("Opção inválida. Tente novamente.")


def login():
    os.system('cls' if os.name == 'nt' else 'clear') or None
    email = input("Email: ")
    senha = input("Senha: ")
    usuario = encontrar_usuario(email, senha)
    if usuario:
        menu_usuario(usuario)
    else:
        print("\nEmail ou senha incorretos.")


def adicionar_usuario(nome, email, senha, seguidores, pontos=0):
    usuarios = carregar_usuarios()
    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "seguidores": seguidores,
        "pontos": pontos
    }
    usuarios.append(usuario)
    salvar_usuarios(usuarios)


####################
##### PROGRAMA #####
####################

usuarios = carregar_usuarios()
os.system('cls' if os.name == 'nt' else 'clear') or None
print('\n=====================================')
print('Bem-vindo ao programa de Fidelipoints')

while True:
    print('''=====================================
Escolha a funcionalidade que deseja acessar:
  1. Login
  2. Cadastro
  0. Sair do programa
=====================================''')
    
    try:
        escolha = int(input('Digite a opção: '))
        
        if escolha == 1:
            login()
        elif escolha == 2:
            cadastro()  
        elif escolha == 0:
            os.system('cls' if os.name == 'nt' else 'clear') or None
            print('''---------------------------------
|       Saindo do programa       |
---------------------------------''')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')
            
    except ValueError:
        print("Entrada inválida")
