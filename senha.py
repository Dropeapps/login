import streamlit as st

# Criando uma função para o cadastro de login e senha
def cadastro():
    st.title("Cadastro de Login e Senha")
    login = st.text_input("Login: ")
    senha = st.text_input("Senha: ", type='password')
    if st.button("Cadastrar"):
        # Armazenando o login e a senha em um dicionário
        usuarios = {"login": login, "senha": senha}
        st.success("Usuário cadastrado com sucesso!")

# Criando uma função para o sistema de login
def login_sistema():
    st.title("Login no Sistema")
    login = st.text_input("Login: ")
    senha = st.text_input("Senha: ", type='password')
    if st.button("Entrar"):
        # Verificando se o login e a senha estão corretos
        if usuarios["login"] == login and usuarios["senha"] == senha:
            st.success("Login realizado com sucesso!")
        else:
            st.error("Login ou senha incorretos.")

# Criando o menu de opções
def menu():
    st.title("Menu de Opções")
    opcao = st.selectbox("Selecione uma opção:", ["Cadastro", "Login"])
    if opcao == "Cadastro":
        cadastro()
    elif opcao == "Login":
        login_sistema()

