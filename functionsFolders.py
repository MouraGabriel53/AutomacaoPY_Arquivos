import pyautogui
import os
import shutil

class Folders:
    
    def __init__(self):
        self.diretorioPadraoDestino = r'\\192.168.1.4\Comercial\Proposta 2025'
        self.diretorioPadraoOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Diretório Padrão'
        
        self.caminho_cliente = None
        self.nome_cliente = None
        self.caminho_local = None        
        self.resposta = None
        self.nome_local = None
        
        self.nomeClienteAntigo = ""
        self.nomeClienteRenomeado = ""
        self.nomeLocalAntigo = ""
        self.nomeLocalRenomeado = ""
        self.nomeOportunidadeAntiga = ""
        self.nomeOportunidadeRenomeada = ""
        
        
    def search(self):
        self.nome_cliente = pyautogui.prompt('Por favor, informe o nome do cliente:')
        if not self.nome_cliente:
            pyautogui.alert('O processo foi interrompido pelo usuário.')
            return
        
        for root, dirs, files in os.walk(self.diretorioPadraoDestino):
            for dir in dirs:
                if self.nome_cliente.lower() == dir.lower():
                    self.caminho_cliente = os.path.join(root, dir)
                    break
            if self.caminho_cliente:
                break

        if not self.caminho_cliente:
            pyautogui.alert('A pasta do cliente não foi encontrada.')
        else:
            pyautogui.alert(f'A pasta do cliente foi encontrada: {self.caminho_cliente}')

    def addLocal(self):
        if not self.caminho_cliente:
            pyautogui.alert('Nenhum cliente foi selecionado. Execute a função "search" primeiro.')
            return
        
        self.resposta = pyautogui.confirm('Deseja criar um novo local ou utilizar um existente?', buttons=['Criar', 'Existente'])
        
        if self.resposta == 'Criar':
            self.nome_local = pyautogui.prompt('Por favor, informe o nome do novo local:')
            if not self.nome_local:
                pyautogui.alert('O processo foi interrompido pelo usuário.')
                return
            self.caminho_local = os.path.join(self.caminho_cliente, self.nome_local)
            os.makedirs(self.caminho_local, exist_ok=True)
        elif self.resposta == 'Existente':
            self.nome_local = pyautogui.prompt('Por favor, informe o nome do local existente:')
            if not self.nome_local:
                pyautogui.alert('O processo foi interrompido pelo usuário.')
                return
            for root, dirs, files in os.walk(self.caminho_cliente):
                for dir in dirs:
                    if self.nome_local.lower() == dir.lower():
                        self.caminho_local = os.path.join(root, dir)
                        break
                if self.caminho_local:
                    break
            if not self.caminho_local:
                pyautogui.alert('O local não foi encontrado.')
        else:
            pyautogui.alert('Opção inválida. O processo foi interrompido.')

    def copyFolders(self):
        try:
            shutil.copytree(self.diretorioPadraoOrigem, self.diretorioPadraoDestino, dirs_exist_ok=True)
            pyautogui.alert('Os diretórios foram copiados com sucesso!')
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao copiar os diretórios: {e}')
            exit()

    def renameFolders(self):
        try:
            # Renomeia o diretório padrão
            self.nomeClienteAntigo = os.path.join(self.diretorioPadraoDestino, 'Cliente')
            self.nomeClienteRenomeado = pyautogui.prompt('Por favor, informe o nome do cliente:')
            if not self.nomeClienteRenomeado:
                pyautogui.alert('O processo foi interrompido pelo usuário.')
                return
            self.nomeClienteRenomeado = os.path.join(self.diretorioPadraoDestino, self.nomeClienteRenomeado)
            os.rename(self.nomeClienteAntigo, self.nomeClienteRenomeado)

            # Renomeia o local
            self.nomeLocalAntigo = os.path.join(self.nomeClienteRenomeado, 'Local')
            self.nomeLocalRenomeado = pyautogui.prompt('Por favor, informe o nome do local:')
            if not self.nomeLocalRenomeado:
                pyautogui.alert('O processo foi interrompido pelo usuário.')
                return
            self.nomeLocalRenomeado = os.path.join(self.nomeClienteRenomeado, self.nomeLocalRenomeado)
            os.rename(self.nomeLocalAntigo, self.nomeLocalRenomeado)

            # Renomeia a oportunidade
            self.nomeOportunidadeAntiga = os.path.join(self.nomeLocalRenomeado, 'Oano_mes_xx_Descrição')
            self.nomeOportunidadeRenomeada = pyautogui.prompt('Por favor, informe o nome da oportunidade:')
            if not self.nomeOportunidadeRenomeada:
                pyautogui.alert('O processo foi interrompido pelo usuário.')
                return 
            self.nomeOportunidadeRenomeada = os.path.join(self.nomeLocalRenomeado, self.nomeOportunidadeRenomeada)
            os.rename(self.nomeOportunidadeAntiga, self.nomeOportunidadeRenomeada)
            pyautogui.alert('As pastas foram renomeadas com sucesso!')
            return(self.nomeOportunidadeRenomeada)
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao renomear os diretórios: {e}')
            exit()