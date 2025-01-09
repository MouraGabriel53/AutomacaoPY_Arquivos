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
            pyautogui.alert('Os diretórios foram copiados com sucesso!', '✅ Concluído')
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao copiar os diretórios: {e}', '❌ Erro')
            exit()

    def renameFolders(self):
        try:
            # Renomeia o diretório padrão
            nomeClienteAntigo = os.path.join(self.diretorioPadraoDestino, 'Cliente')
            nomeClienteRenomeado = pyautogui.prompt('Por favor, informe o nome do Cliente:', '❓ Nome Cliente')
            if not nomeClienteRenomeado:
                pyautogui.alert('O processo foi interrompido pelo usuário.', '❌ Erro')
                return
            nomeClienteRenomeado = os.path.join(self.diretorioPadraoDestino, nomeClienteRenomeado)
            os.rename(nomeClienteAntigo, nomeClienteRenomeado)

            # Renomeia o local
            nomeLocalAntigo = os.path.join(nomeClienteRenomeado, 'Local')
            nomeLocalRenomeado = pyautogui.prompt('Por favor, informe o nome do Local:', '❓ Nome Local')
            if not nomeLocalRenomeado:
                pyautogui.alert('O processo foi interrompido pelo usuário.', '❌ Erro')
                return
            nomeLocalRenomeado = os.path.join(nomeClienteRenomeado, nomeLocalRenomeado)
            os.rename(nomeLocalAntigo, nomeLocalRenomeado)

            # Renomeia a oportunidade
            nomeOportunidadeAntiga = os.path.join(nomeLocalRenomeado, 'Oano_mes_xx_Descrição')
            nomeOportunidadeRenomeada = pyautogui.prompt('Por favor, informe o nome da Oportunidade:', '❓ Nome Oportunidade')
            nomeDiretórioOportunidadadeRenomeada = nomeOportunidadeRenomeada
            if not nomeOportunidadeRenomeada:
                pyautogui.alert('O processo foi interrompido pelo usuário.', '❌ Erro')
                return 
            nomeOportunidadeRenomeada = os.path.join(nomeLocalRenomeado, nomeOportunidadeRenomeada)
            os.rename(nomeOportunidadeAntiga, nomeOportunidadeRenomeada)           
            pyautogui.alert('As pastas foram renomeadas com sucesso!', '✅ Concluído') 
            
            caminhoProposta = os.path.join(self.diretorioPadraoDestino, nomeClienteRenomeado, nomeLocalRenomeado, nomeOportunidadeRenomeada, 'Proposta')
            return caminhoProposta, nomeDiretórioOportunidadadeRenomeada                   
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao renomear os diretórios: {e}', '❌ Erro')
            exit()                    