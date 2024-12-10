#CADASTRO DE USUÁRIO E SENHA 
saldo = 0.0 #variavel que guardará o saldo do usuario
while True:
    #MENU
    print("bem vindo\n digite 1.cadastrar 2.login.3.encerrar")
    #ler a escolha do usuario
    escolha_menu = int(input()) #lê a escolha  coom um número

    #se usuario escolher cadastro
    if escolha_menu == 1:
        #cria um usuario e uma senha com tipo string
        usuario = input("crie um nome de usuario")
        senha = input("crie uma senha")
    elif escolha_menu == 2: #se o usuario escolher login
        #vomparar as inf. cadastradas com uma leitura
        login_usuario = input ("digite seu usuario")
        login_senha = input("digite sua senha")
        if login_usuario == usuario and login_senha == senha:
            print("login realizado com sucesso")
            #se login correto,entra no
            #menu principal do app
            print("bem vindo",usuario)
            while True: #enquanto que exibirá o menu principal
                print("1.deposito 2.sacar 3.pix 4.extrato 5.encerrar")
                escolha_principal = int(input())
                if escolha_principal == 1: #se usuario escolher deposito
                    #lê o valor depositado
                    valor_deposito = float(input())
                    saldo = saldo + valor_deposito #atualiza o valor
                    print("novo saldo é",saldo)
                elif escolha_principal == 2: #saque
                    valor_saque = float(input("digite o valor do saque"))
                    senha_saque = input("digite sua senha: ")
                    if senha_saque == senha:
                        saldo = saldo - valor_saque #subtrai o valor do saldo
                    else:
                        print("senha incorreta")
                elif escolha_principal == 3: #se usuario escolher pix
                    valor_pix = float(input("digite o valor do pix"))
                    senha_pix = input("digite sua senha")
                    if senha_pix == senha:
                        saldo = saldo - valor_pix
                    else:
                        print("senha incorreta")
                elif escolha_principal == 4: #se usuario escolher visualizar extrato
                    senha_extrato =input("digite sua senha")
                    if senha_extrato == senha:
                        print("extrato:",saldo)
                    else:
                        print("senha incorreta")
                elif escolha_principal == 5: #encerrar
                    senha_encerrar = input("digite sua senha")
                    if senha_encerrar == senha:
                      break
                    else:
                        print("senha incorreta")
                                        
    else:
        print("usuario ou senhas incorretos")