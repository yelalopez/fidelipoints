import json

def validar_email(email):
    return "@" in email

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
    print(f'''\n
---------------------------
Dados do Usuário
  Email: {usuario['email']}
  Seguidores: {usuario['seguidores']}
  Pontos: {usuario['pontos']}\n''') 

def cadastro():
    nome = input("Digite seu nome: ").capitalize()
    email = input("Digite seu email: ")
    
    while not validar_email(email):
        print("Email inválido. Por favor, insira um email válido.")
        email = input("Digite seu email: ")
    
    senha = input("Digite a senha: ")
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
          novo_nome = input("Nome: ")
          usuario['nome'] = novo_nome.capitalize()
          
          break        
        elif opcao == 2:
          novo_seguidores = input("Seguidores: ")
          if novo_seguidores:
              try:
                usuario['seguidores'] = int(novo_seguidores)
                
              except ValueError:
                  print("Por favor insira um número válido")
          break
        elif opcao == 3:
          nova_senha = input("Nova senha: ")
          usuario['senha'] = nova_senha
          break
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

    for u in usuarios:
        if u['email'] == usuario['email']:
            u.update(usuario)
            break

    salvar_usuarios(usuarios)
    print("Perfil atualizado com sucesso!")

def encontrar_usuario(email, senha):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            return usuario
    return None

def menu_usuario(usuario):
    while True:
        print('''
===== Menu do Usuário =====
  1. Ver perfil
  2. Atualizar perfil
  3. Meus Fidelipoints
  4. Logout
---------------------------''')
    
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_dados(usuario)
        elif opcao == "2":
            atualizar_perfil(usuario)
        elif opcao == "3":
            print(f"Meus Fidelipoints: {usuario['pontos']}")
        elif opcao == "4":
            print("Logout realizado com sucesso.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def login():
    email = input("\nEmail: ")
    senha = input("Senha: ")
    usuario = encontrar_usuario(email, senha)
    if usuario:
        print(f"\nBem-vindo(a), {usuario['nome']}!")
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

print('\n=====================================')
print('Bem-vindo ao programa de Fidelipoints')

while True:
    print('''=====================================
Escolha a funcionalidade que deseja acessar:
  1. Login
  2. Cadastro
  3. Sair do programa
=====================================''')
    
    try:
        escolha = int(input('Digite a opção: '))
        
        if escolha == 1:
            login()
        elif escolha == 2:
            cadastro()  
        elif escolha == 3:
            print('Saindo do programa')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número entre 1 e 3.")
