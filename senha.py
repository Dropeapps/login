import streamlit as st

# Função para cadastrar um novo usuário
def register():
    username = st.text_input("Insira seu nome de usuário")
    password = st.text_input("Insira sua senha", type='password')
    confirm_password = st.text_input("Confirme sua senha", type='password')
    if password != confirm_password:
        st.error("As senhas não coincidem.")
    else:
        # Salvar o nome de usuário e a senha (NÃO FAÇA ISSO EM UM AMBIENTE DE PRODUÇÃO)
        users[username] = password
        st.success("Usuário criado com sucesso.")

# Função para fazer login
def login():
    username = st.text_input("Insira seu nome de usuário")
    password = st.text_input("Insira sua senha", type='password')
    if username in users and users[username] == password:
        st.success("Login realizado com sucesso.")
    else:
        st.error("Nome de usuário ou senha incorretos.")

# Cria dicionario vazio para armazenar usuarios e senhas
users = {}

# Adiciona título e descrição
st.title("Cadastro e Login")
st.write("Cadastre-se ou faça login para continuar.")

# Adiciona botões para escolher entre cadastro ou login
if st.button("Cadastrar"):
    register()
if st.button("Login"):
    login()

