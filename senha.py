st.title("Cadastro de Login e Senha")
username = st.text_input("Digite o seu nome de usuário: ")
password = st.text_input("Digite a sua senha: ", type='password')

if st.button("Cadastrar"):
st.write("Usuário cadastrado com sucesso!")

st.title("Sistema de Login")
username_login = st.text_input("Digite o seu nome de usuário: ")
password_login = st.text_input("Digite a sua senha: ", type='password')

if st.button("Login"):
# verifica se o login e senha digitados correspondem aos cadastrados
if username_login == username and password_login == password:
st.write("Login realizado com sucesso!")
else:
st.error("Usuário ou senha incorretos, tente novamente.")
