# Fidelipoints

**Fidelipoints** é um sistema de fidelidade desenvolvido em Python que permite aos usuários acumularem pontos por interações em redes sociais, como publicações de **stories** e **posts no feed**, com possibilidade de personalizar contas marcadas e gerenciar seu perfil.

---

## Funcionalidades

- **Cadastro de Usuários**: Crie seu perfil com nome, email, senha e número de seguidores.
- **Login Seguro**: Acesse o sistema utilizando email e senha.
- **Gerenciamento de Perfil**:
  - Atualize informações pessoais, como nome e senha.
  - Veja detalhes do seu perfil.
  - Exclua sua conta, se desejar.
- **Acúmulo de Pontos**:
  - Registre postagens do tipo **story** ou **feed**.
  - Acumule pontos baseados no número de seguidores e na interação com contas marcadas.
- **Histórico de Postagens**:
  - Veja o histórico de postagens realizadas, com informações como data, tipo e pontos ganhos.
- **CRUD**:
  - Cadastrar
  - Visualizar
  - Atualizar
  - Excluir informações de perfil e postagens.
- **Persistência de Dados**:
  - As informações são armazenadas em um arquivo JSON.

## Tecnologias Utilizadas 🛠️

- **Linguagem**: Python 3.13
- **Bibliotecas**:
  - `json` para armazenamento de dados.
  - `os` para manipulação da interface do sistema.
  - `datetime` para registrar a data e hora das postagens.
  - `random` para gerar o código aleatório

## Como Executar o Projeto 🚀

1. **Pré-requisitos**:

   - Certifique-se de ter o [Python 3.13](https://www.python.org/) instalado.
   - Instale um editor de texto ou IDE como [Visual Studio Code](https://code.visualstudio.com/).

2. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/fidelipoints.git
   cd fidelipoints
   ```
3. **Execute o programa**:

   ```bash
   python fidelipoints.py

   ```

4. **Navegue pelo Sistema**:
   Siga as instruções no terminal para cadastrar-se, fazer login e utilizar as funcionalidades.

## Melhorias Futuras

- Adicionar integração com redes sociais reais.
- Implementar interface gráfica.
- Introduzir níveis ou prêmios para pontos acumulados.
- Exportar relatórios de postagens e pontos.
