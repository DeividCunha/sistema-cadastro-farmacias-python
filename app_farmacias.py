import os

farmacias = [{'nome':'Vida Farma Premium', 'categoria':'Farmácia', 'ativo':False}, 
             {'nome':'Drogasil', 'categoria':'Drogaria', 'ativo':True},
             {'nome':'Farma Certeza Viva', 'categoria':'Farmácia', 'ativo':False}]

def exibir_nome_do_programa():
    """Exibe o nome do programa em formato ASCII art no terminal."""
    print("""
███╗   ███╗███████╗██████╗ ██╗ ██████╗██╗███╗   ██╗███████╗
████╗ ████║██╔════╝██╔══██╗██║██╔════╝██║████╗  ██║██╔════╝
██╔████╔██║█████╗  ██║  ██║██║██║     ██║██╔██╗ ██║█████╗  
██║╚██╔╝██║██╔══╝  ██║  ██║██║██║     ██║██║╚██╗██║██╔══╝  
██║ ╚═╝ ██║███████╗██████╔╝██║╚██████╗██║██║ ╚████║███████╗
╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝ ╚═════╝╚═╝╚═╝  ╚═══╝╚══════╝

███████╗██╗  ██╗██████╗ ██████╗ ███████╗███████╗███████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗   ╚███╔╝ ██████╔╝██████╔╝█████╗  ███████╗███████╗
██╔══╝   ██╔██╗ ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║
███████╗██╔╝ ╚██╗██║     ██║  ██║███████╗███████║███████║
╚══════╝╚═╝   ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
""")

def exibir_opcoes():
    """Exibe as opções disponíveis no menu principal do sistema."""
    print('1. Cadastrar farmacia')
    print('2. Listar farmacia')
    print('3. Alternar estado da farmacia')
    print('4. Sair\n')

def voltar_menu_principal():
    """Aguarda interação do usuário e retorna ao menu principal."""
    input('\nDigite uma tecla para voltar para o menu ')
    main()
    
def opcao_invalida():
    """Exibe mensagem de erro para opções inválidas e retorna ao menu."""
    print('Opção invalida!\n')
    voltar_menu_principal()

def finalizar_app():
    """Finaliza a aplicação exibindo mensagem de encerramento."""
    os.system('cls')
    exibir_subtitulo('Finalizando o app')
   
def exibir_subtitulo(texto):
    """Exibe um subtítulo formatado com linhas decorativas no terminal."""
    os.system('cls')
    linha = '-' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_nova_farmacia():
    """Solicita dados ao usuário e cadastra uma nova farmácia na lista."""
    os.system('cls')
    exibir_nome_do_programa()
    nome_de_farmacia = input('Digite o nome da farmacia que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria da farmacia {nome_de_farmacia}: ')
    dados_da_farmacia ={'nome':nome_de_farmacia, 'categoria':categoria, 'ativo':False}
    farmacias.append(dados_da_farmacia)
    print(f'A farmacia {nome_de_farmacia} foi cadastrado com sucesso!')

    voltar_menu_principal()

def listar_farmacia():
    """Lista todas as farmácias cadastradas com suas categorias e status."""
    os.system('cls')
    exibir_subtitulo('Listando farmacias')

    print(f'{"Nome da farmacia".ljust(22)} | {"Categoria".ljust(20)} | Status' )

    for farmacia in farmacias:
        nome_farmacia = farmacia['nome'] 
        categoria = farmacia['categoria']
        ativo = 'ativado' if farmacia['ativo'] else 'desativado'
        print(f'- {nome_farmacia.ljust(20)} | {categoria.ljust(20)} | {ativo}') 

    voltar_menu_principal()

def alternar_estado_da_farmacia():
    """Altera o estado (ativo/desativado) de uma farmácia pelo nome."""
    exibir_subtitulo('Alterando estado da farmacia')
    nome_farmacia = input('Digite o nome da farmacia que deseja altenar o estado: ')
    farmacia_encontrada = False
    
    for farmacia in farmacias:
        if nome_farmacia == farmacia['nome']:
            farmacia_encontrada = True
            farmacia['ativo'] = not farmacia['ativo']
            mensagem = f'A farmacia {nome_farmacia} foi ativado com sucesso' if farmacia['ativo'] else f'A farmacia {nome_farmacia} foi desativado com sucesso'
            print(mensagem)

    if not farmacia_encontrada:
        print('A farmacia não foi encontrado')

    voltar_menu_principal()

def escolher_opcao():
    """Recebe a opção do usuário e direciona para a função correspondente."""
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção', opcao_escolhida)

        if opcao_escolhida == 1:
           cadastrar_nova_farmacia()
        elif opcao_escolhida ==2:
            listar_farmacia()
        elif opcao_escolhida ==3:
            alternar_estado_da_farmacia()
        elif opcao_escolhida ==4:
            finalizar_app () 
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    """Função principal responsável por iniciar a aplicação e exibir o menu."""
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
