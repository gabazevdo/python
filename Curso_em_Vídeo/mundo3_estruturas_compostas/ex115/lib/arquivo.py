from lib.utils import cabecalho


def criaArquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print('Houve uma falha na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('Houve uma falha ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        
        for linha in arq:
            dados = linha.split()
            dados[1] = dados[1].replace('\n', '')
            
            print(f'{dados[0]:<26}{dados[1]:>3}')


def arquivoExiste(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        arq = open(arquivo, 'at')
    except:
        print('Houve uma falha ao abrir o arquivo!')
    else:
        try:
            arq.write(f'{nome}: {idade}\n')
        except:
            print('Houve uma falha ao cadastrar os dados!')
        else:
            print(f'Dados cadastrados com sucesso!')
            arq.close()
