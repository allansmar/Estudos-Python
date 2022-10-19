'''
ATIVIDADE DE LISTA | CADASTRO USUÁRIOS

'''

usuarios = []

while True:
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    decisao = int(input(f'Digite uma opção:'
                        f'\n[1] - adicionar usuário' # append
                        f'\n[2] - visualizar cadastros' 
                        f'\n[3] - atualizar cadastros' # .index
                        f'\n[4] - deletar usuário' # .pop(INDICE) .remove("Valor")
                        f'\n[5] - sair do sistema' # Break
                        f'\n'))
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    if decisao ==1:
        cadastro = input("Adicione um usuário: ").upper()
        usuarios.append(cadastro)
        print("Cadastro realizado com sucesso! ")

    elif decisao == 2:
        print(f'{len(usuarios)} usuário(s) cadastrado(s)')
        print(f'Lista de cadastros:\n{usuarios}')

    elif decisao ==3:
        if len(usuarios) == 0:
            print('Ainda não há usuário cadastrado')
        else:
            print(usuarios)
            atualizar = input("Atualize um usuário:\n ")
            indice = usuarios.index(atualizar)
            novonome = input("Qual atualização: ").upper()
            usuarios[indice] = novonome
            print(usuarios)

    elif decisao ==4:
        print(f'Qual usuário deseja deletar?\n{usuarios}')
        deletar = input('Digite o usuário que deseja deletar: ')
        apagado = usuarios.remove(deletar)
        print(usuarios)

    elif decisao ==5:
        print("Valeu, Flws!")
        break