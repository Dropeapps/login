import streamlit as st

# Cadastro de login e senha
def cadastro():
    usuario = st.text_input("Insira seu login: ")
    senha = st.text_input("Insira sua senha: ", type='password')
    st.success("Cadastro realizado com sucesso!")
    return usuario, senha

# Sistema de login
def login():
    usuario_cadastrado, senha_cadastrada = cadastro()
    usuario_inserido = st.text_input("Insira seu login: ")
    senha_inserida = st.text_input("Insira sua senha: ", type='password')
    if usuario_inserido == usuario_cadastrado and senha_inserida == senha_cadastrada:
        st.success("Login realizado com sucesso!")
    else:
        st.error("Login ou senha incorretos.")

st.title("Cadastro de Login e Senha")
st.button("Cadastrar")
st.button("Fazer Login")
