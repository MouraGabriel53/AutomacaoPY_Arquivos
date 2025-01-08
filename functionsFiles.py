import pyautogui
import os
import shutil

class Files:
    def __init__(self, planilhaCustosOrigem, nomeOportunidadeRenomeada, caminhoProposta):
        self.planilhaCustosOrigem = planilhaCustosOrigem
        self.nomeOportunidadeRenomeada = nomeOportunidadeRenomeada
        self.planilhaCustosDestino = caminhoProposta
        self.propostaModeloDestino = caminhoProposta
        self.caminhoProposta = caminhoProposta   
        
    def selectFiles(self):
        try: 
            tipoProposta = pyautogui.prompt('Por favor, informe o tipo da proposta:\n[1] Assistência Técnica\n[2] Automação Básica\n[3] Automação Completa\n[4] Painéis\n[5] Revenda\n[6] TI:') 
            
            match tipoProposta:
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
            os.makedirs(os.path.dirname(self.propostaModeloDestino), exist_ok=True)
            shutil.copy2(self.propostaModeloOrigem, self.propostaModeloDestino)
            shutil.copy2(self.planilhaCustosOrigem, self.planilhaCustosDestino)
            pyautogui.alert('Os arquivos foram copiados com sucesso!')
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao copiar os arquivos: {e}')
            exit()

    def renameFiles(self):
        try:
            pyautogui.alert('Os arquivos foram renomeados com sucesso!')
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao renomear os arquivos: {e}')
            exit()      
        