import os

restaurantes = [{'nome': 'praça', 'categoria': 'italiana','ativo': True},
                {'nome': 'madero', 'categoria': 'hamburgueria','ativo': True},
                {'nome': 'giraffas', 'categoria': 'fast-food','ativo': False}]


def exibir_menu():
    print('\nRestaurante Sabor Express!\n')

def exibir_opcoes():
    
    print('--------------menu-------------\n')
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('\nEncerrando o programa. Obrigado por sua visita!\n')

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ...')
    main()

def opcao_invalida():
    print('Opção inválida. Tente novamente.\n')
    voltar_menu_principal()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso"\n')
    voltar_menu_principal()

def listar_restaurantes():
    os.system('cls')
    print('Lista de restaurantes cadastrados\n')
    if len(restaurantes) == 0:
        print('Nenhum restaurante cadastrado!')
    else:    
        for restaurante in restaurantes:
            print(f'- {restaurante["nome"]} - {restaurante["categoria"]} - {"Ativo" if restaurante["ativo"] else "Inativo"}')
    
    print()
    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}\n')
        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar restaurante')
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_menu()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()