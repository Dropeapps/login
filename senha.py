import streamlit as st

def cadastro():
    usuario = st.text_input("Digite seu login: ")
    senha = st.text_input("Digite sua senha: ", type='password')
    st.write("Cadastro realizado com sucesso!")
    return usuario, senha

def login():
    usuario_cadastrado, senha_cadastrada = cadastro()
    usuario_digitado = st.text_input("Digite seu login: ")
    senha_digitada = st.text_input("Digite sua senha: ", type='password')

    if usuario_digitado == usuario_cadastrado and senha_digitada == senha_cadastrada:
        st.write("Login realizado com sucesso!")
    else:
        st.write("Login ou senha incorretos.")

st.title("Sistema de Login")
st.button("Fazer login", login)
