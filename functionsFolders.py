import pyautogui
import os
import shutil

class Folders:
    
    def __init__(self, diretorioPadraoOrigem, diretorioPadraoDestino):
        self.diretorioPadraoOrigem = diretorioPadraoOrigem
        self.diretorioPadraoDestino = diretorioPadraoDestino

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
            nomeClienteAntigo = os.path.join(self.diretorioPadraoDestino, 'Cliente')
            nomeClienteRenomeado = pyautogui.prompt('Por favor, informe o nome do Cliente:')
            if not nomeClienteRenomeado:
                pyautogui.alert('O processo foi interrompido pelo usuário.')
                return
            nomeClienteRenomeado = os.path.join(self.diretorioPadraoDestino, nomeClienteRenomeado)
            os.rename(nomeClienteAntigo, nomeClienteRenomeado)

            # Renomeia o local
            nomeLocalAntigo = os.path.join(nomeClienteRenomeado, 'Local')
            nomeLocalRenomeado = pyautogui.prompt('Por favor, informe o nome do Local:')
            if not nomeLocalRenomeado:
                pyautogui.alert('O processo foi interrompido pelo usuário.')
                return
            nomeLocalRenomeado = os.path.join(nomeClienteRenomeado, nomeLocalRenomeado)
            os.rename(nomeLocalAntigo, nomeLocalRenomeado)

            # Renomeia a oportunidade
            nomeOportunidadeAntiga = os.path.join(nomeLocalRenomeado, 'Oano_mes_xx_Descrição')
            nomeOportunidadeRenomeada = pyautogui.prompt('Por favor, informe o nome da Oportunidade:')
            if not nomeOportunidadeRenomeada:
                pyautogui.alert('O processo foi interrompido pelo usuário.')
                return 
            nomeOportunidadeRenomeada = os.path.join(nomeLocalRenomeado, nomeOportunidadeRenomeada)
            os.rename(nomeOportunidadeAntiga, nomeOportunidadeRenomeada)           
            pyautogui.alert('As pastas foram renomeadas com sucesso!') 
            
            caminhoProposta = os.path.join(self.diretorioPadraoDestino, nomeClienteRenomeado, nomeLocalRenomeado, nomeOportunidadeRenomeada, 'Proposta')
            return caminhoProposta, nomeOportunidadeRenomeada                   
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao renomear os diretórios: {e}')
            exit()                    