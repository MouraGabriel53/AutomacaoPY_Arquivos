import pyautogui
import os
import shutil

class folders:
    
    def search(self):
        nome_cliente = pyautogui.prompt('Por favor, informe o nome do cliente:')
        if not nome_cliente:
            pyautogui.alert('O processo foi interrompido pelo usuário.')
            exit()
        caminho_cliente = None
        for root, dirs, files in os.walk(r'\\192.168.1.4\Comercial\Proposta 2025'):
            for dir in dirs:
                if nome_cliente.lower() == dir.lower():
                    caminho_cliente = os.path.join(root, dir)
                break
            if caminho_cliente:
                break
        if not caminho_cliente:
            pyautogui.alert('A pasta do cliente não foi encontrada.')
            exit()
        else:
            pastaProposta = caminho_cliente
            pyautogui.alert(f'A pasta do cliente foi encontrada: {pastaProposta}')
    
    def addLocal(self):
        resposta = pyautogui.confirm('Deseja criar um novo local ou utilizar um existente?', buttons=['Criar', 'Existente'])
        
        if resposta == 'Criar':
            nome_local = pyautogui.prompt('Por favor, informe o nome do novo local:')
            if not nome_local:
                pyautogui.alert('O processo foi interrompido pelo usuário.')
            exit()
            caminho_local = os.path.join(caminho_cliente, nome_local)
            os.makedirs(caminho_local, exist_ok=True)
        elif resposta == 'Existente':
            nome_local = pyautogui.prompt('Por favor, informe o nome do local existente:')
            if not nome_local:
                pyautogui.alert('O processo foi interrompido pelo usuário.')
            exit()
            caminho_local = None
            for root, dirs, files in os.walk(caminho_cliente):
                for dir in dirs:
                    if nome_local.lower() == dir.lower():
                        caminho_local = os.path.join(root, dir)
                    break
                if caminho_local:
                    break
                if not caminho_local:
                    pyautogui.alert('O local não foi encontrado.')
                exit()
        else:
            pyautogui.alert('Opção inválida. O processo foi interrompido.')
            exit()
    
    def copyFolders(self):        
        diretorioPadraoOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Diretório Padrão'
        diretorioPadraoDestino = r'\\192.168.1.4\Comercial\Proposta 2025'
        shutil.copytree(diretorioPadraoOrigem, diretorioPadraoDestino, dirs_exist_ok=True)
        
    def renameFolders(self):
        diretorioPadraoDestino = r'\\192.168.1.4\Comercial\Proposta 2025'
        # Renomeia o diretório padrão
        nomeClienteAntigo = os.path.join(diretorioPadraoDestino, 'Cliente')
        nomeClienteRenomeado = pyautogui.prompt('Por favor, informe o nome do cliente:')
        if not nomeClienteRenomeado:
            pyautogui.alert('O processo foi interrompido pelo usuário.')
            exit()
        diretorioPadraoRenomeado = os.path.join(diretorioPadraoDestino, nomeClienteRenomeado)
        os.rename(nomeClienteAntigo, diretorioPadraoRenomeado)
        
        # Renomeia o local
        nomeLocalAntigo = os.path.join(diretorioPadraoRenomeado, 'Local')
        nomeLocal = pyautogui.prompt('Por favor, informe o nome do local:')
        if not nomeLocal:
            pyautogui.alert('O processo foi interrompido pelo usuário.')
            exit()
        nomeLocalRenomeado = os.path.join(diretorioPadraoRenomeado, nomeLocal)
        os.rename(nomeLocalAntigo, nomeLocalRenomeado)
        
        # Renomeia a oportunidade
        nomeOportunidadeAntigo = os.path.join(nomeLocalRenomeado, 'Oano_mes_xx_Descrição')
        nomeOportunidade = pyautogui.prompt('Por favor, informe o nome da oportunidade:')
        if not nomeOportunidade:
            pyautogui.alert('O processo foi interrompido pelo usuário.')
            exit()
        nomeOportunidadeRenomeado = os.path.join(nomeLocalRenomeado, nomeOportunidade)
        os.rename(nomeOportunidadeAntigo, nomeOportunidadeRenomeado)
    