import pyautogui
import os
import shutil
from functionsFolders import Folders

class Files:
    def __init__(self):           
        self.propostaModeloOrigem = None
        self.planilhaCustosOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Planilha Venda\Planilha de Calculo\FGI 08A - Planilha de Custos rev02 - Lucro Real.xlsx'
        self.diretorioPadraoDestino = r'\\192.168.1.4\Comercial\Proposta 2025'
        self.tipoProposta = ""
        self.planilhaCustosDestino = None
        self.propostaModeloDestino = None
        self.pastaDestinoArquivos = None
        
    def selectFiles(self):
        try: 
            self.tipoProposta = pyautogui.prompt('Por favor, informe o tipo da proposta:\n[1] Assistência Técnica\n[2] Automação Básica\n[3] Automação Completa\n[4] Painéis\n[5] Revenda\n[6] TI:') 
            
            match self.tipoProposta:
                case '1':
                    self.propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Assistência Técnica - 20.12.2024.docx'
                case '2':
                    self.propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão Automação Básica - 20.12.2024.docx'
                case '3':
                    self.propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão Automação Completa - 20.12.2024.docx'
                case '4':
                    self.propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão Painéis - 20.12.2024.docx'
                case '5':
                    self.propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão Revenda de Material - 20.12.2024.docx'
                case '6':
                    self.propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão TI - 20.12.2024.docx'
                case _:
                    pyautogui.alert('Tipo de proposta inválido. O processo foi interrompido.')
                    exit()
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao selecionar os arquivos: {e}')
            exit()
            
    def copyFiles(self):
        try:             
            folders = Folders()
            nomeOportunidadeRenomeada = folders.renameFolders()   
            self.pastaDestinoArquivos = os.path.join(nomeOportunidadeRenomeada, 'Proposta')
            os.makedirs(self.pastaDestinoArquivos, exist_ok=True)
            pyautogui.alert('Os arquivos foram copiados com sucesso!')
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao copiar os arquivos: {e}')
            exit()

    def renameFiles(self):
       try:
            folders = Folders()
            nomeOportunidadeRenomeada = folders.renameFolders()
            
            self.planilhaCustosDestino = os.path.join(self.pastaDestinoArquivos, f'{nomeOportunidadeRenomeada} rev0.0.xlsx')
            shutil.copy(self.planilhaCustosOrigem, self.planilhaCustosDestino)
                
            self.propostaModeloDestino = os.path.join(self.pastaDestinoArquivos, f'{nomeOportunidadeRenomeada} rev0.0.docx')
            shutil.copy(self.propostaModeloOrigem, self.propostaModeloDestino)
            pyautogui.alert('Os arquivos foram renomeados com sucesso!')
       except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao renomear os arquivos: {e}')
            exit()      
        