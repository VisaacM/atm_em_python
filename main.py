import getpass
import os

os.system('cls'if os.name == 'nt' else 'clear')

y = "*  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
x = "*  S c h o o l   o f   N e t   -   C a i x a   E l e t r ô n i c o *"
vl = 5001
account_list = {
    '0001-02': {
        'password': '123456',
        'name': 'Fulano da Silva',
        'value': 100,
        'admin': False
    },
    '0002-02': {
        'password': '123456',
        'name': 'Deutrano da Silva',
        'value': 50,
        'admin': False
    },
    '1111-11': {
        'password': '123',
        'name': 'Admin da Silva',
        'value': vl,
        'admin': True
    }
}

money_slips = {
    '20': 5,
    '50': 5,
    '100': 5,
}

while True:
    print(y)
    print(x)
    print(y)

    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')
    print(account_typed)
    print(password_typed)

    a = 1
    b = 2

    while a < b:

        if account_typed in account_list and password_typed == account_list[account_typed]['password']:
            os.system('cls'if os.name == 'nt' else 'clear')

            print(y)
            print(x)
            print(y)


            print('1 - Saldo')
            print('2 - Saque')
            print('3 - Desconectar')

            if account_list[account_typed]['admin'] == True:
                print("4 - Incluir Cédulas")
            option_typed = input('Escolha uma das opções acima: ')



            if option_typed == '4' and account_list[account_typed]['admin']:
                os.system('cls'if os.name == 'nt' else 'clear')
                print(y)
                print(x)
                print(y)
                amount_typed = input('Digite a quantidade de cédulas: ')
                money_bill_typed = input('Digite a cédula a ser incluída: ')
                money_slips[money_bill_typed] += int(amount_typed)
                print(money_slips)
            elif option_typed == '1':
                print('Seu saldo é R$%s' %
                account_list[account_typed]['value'])
            elif option_typed == '3':
               print('Desconectando............')
               a = 3

            elif option_typed == '2':
                value_typed = input('Digite o valor a ser sacado:')
                
                money_slips_user = {}
                value_int = int(value_typed)
                account_list[account_typed]['value'] = account_list[account_typed]['value'] - value_int   
                

                if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                    money_slips_user['100'] = value_int // 100
                    value_int = value_int - value_int // 100 * 100

                if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
                    money_slips_user['50'] = value_int // 50
                    value_int = value_int - value_int // 50 * 50
                    

                if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                    money_slips_user['20'] = value_int // 20
                    value_int = value_int - value_int // 20 * 20
                    
                     

                if value_int != 0 and account_list['value'] != 0:
                    print('O caixa não tem cédulas ou saldo insuficiente')
                else:
                    for money_bill in money_slips_user:
                        money_slips[money_bill] -= money_slips_user[money_bill]
                                        
                        

                       
                    print('Pegue as notas:')
                    print(money_slips_user)
                    print("Valor restante na conta: %s --" %account_list[account_typed]['value'])

        else:
            print('Conta ou senha inválida...')
        input('Pressione <ENTER> para continuar')

        os.system('cls'if os.name == 'nt' else 'clear')
