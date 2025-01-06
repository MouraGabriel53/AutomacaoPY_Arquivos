import pyautogui
import os
import shutil
from functionsFolders import nomeClienteRenomeado, nomeLocal, nomeOportunidade, diretorioCliente
from functionsFiles import nomeClienteRenomeado, nomeLocal, nomeOportunidade, diretorioCliente, planilhaCustosOrigem, propostaModeloOrigem

class files:
    
    def selectFiles(self):
        
        diretorioPadraoDestino = r'\\192.168.1.4\Comercial\Proposta 2025'
        
        tipoProposta = pyautogui.prompt('Por favor, informe tipo da proposta\n[1] Assistência Técnica\n[2] Automação Básica\n[3] Automação Completa\n[4] Painéis\n[5] Revenda\n[6] TI:') 
        
        match tipoProposta:
            case '1':
                propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Assistência Técnica - 20.12.2024.docx'
            case '2':
                propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão Automação Básica - 20.12.2024.docx'
            case '3':
                propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão Automação Completa - 20.12.2024.docx'
            case '4':
                propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão Painéis - 20.12.2024.docx'
            case '5':
                propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão Revenda de Material - 20.12.2024.docx'
            case '6':
                propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão TI - 20.12.2024.docx'
            case _:
                pyautogui.alert('Tipo de proposta inválido. O processo foi interrompido.')
                exit()

        if not os.path.exists(propostaModeloOrigem):
            pyautogui.alert(f'O caminho {propostaModeloOrigem} não foi encontrado. O processo foi interrompido.')
            exit()
            
    def copyFiles(self):  
        planilhaCustosOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Planilha Venda\Planilha de Calculo\FGI 08A - Planilha de Custos rev02 - Lucro Real.xlsx'
        if not os.path.exists(planilhaCustosOrigem):
            pyautogui.alert(f'O caminho {planilhaCustosOrigem} não foi encontrado. O processo foi interrompido.')
            exit()
        
        pastaPropostaDestino = os.path.join(diretorioPadraoDestino, nomeClienteRenomeado, nomeLocal, nomeOportunidade)
        diretorioCliente = os.path.join(pastaPropostaDestino, 'Proposta')
        os.makedirs(diretorioCliente, exist_ok=True)
      
    def renameFiles(self):  
        planilhaCustosDestino = os.path.join(diretorioCliente, f'{nomeOportunidade} rev0.0.xlsx')
        shutil.copy(planilhaCustosOrigem, planilhaCustosDestino)
            
        propostaModeloDestino = os.path.join(diretorioCliente, f'{nomeOportunidade} rev0.0.docx')
        shutil.copy(propostaModeloOrigem, propostaModeloDestino)

       