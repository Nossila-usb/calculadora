# inicia loop
while True:
    print(f'{'-'*20} calculadora python {'-'*20}\n')
    print('1 - soma.')
    print('2 - subtracao.')
    print('3 - multiplicacao.')
    print('4 - divisao.')
    print('5 - sair do programa.')

    # operacao escolhida
    operacao = input('operacao desejada')

    # verificacao se o usuario vai fazer o calculo ou sair do programa
    if operacao !='5':
        # informa os numeros 
        x = str(input('informe o 1 numero: ')).replace(',','.')
        y = str(input('informe o 2 numero: ')).replace(',','.')

         #conversao
        x = float(x)
        y = float(y)

        # verifica a operacao desejada
        match operacao:
            case '1':
                print(f'{x} + {y} ={x + Y}')
            case '2':
                print(f'{x} - {y} = {x - y}')
            case '3':
                print(f'{x} x {y} = {x * y}')
            case '4':
                if y != 0:
                    print(f'{x} : {y} = {x : y}')

        # renicia o loop
        continue 
    else:
        print('programa de encerramento!')
        break 
         
            

