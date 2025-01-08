import pyautogui
from functionsFiles import Files
from functionsFolders import Folders

def configFolders():
    diretorioPadraoOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Diretório Padrão'
    diretorioPadraoDestino = r'\\192.168.1.4\Comercial\Proposta 2025'
    return diretorioPadraoOrigem, diretorioPadraoDestino

def configFiles():
    planilhaCustosOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Planilha Venda\Planilha de Calculo\FGI 08A - Planilha de Custos rev02 - Lucro Real.xlsx'
    return planilhaCustosOrigem

def main():
    resposta = pyautogui.confirm('Deseja adicionar um novo Cliente?', buttons=['Sim', 'Não'])    
    if resposta == "Sim":
        diretorioPadraoOrigem, diretorioPadraoDestino = configFolders()
        folders = Folders(diretorioPadraoOrigem, diretorioPadraoDestino)
        folders.copyFolders()
        caminhoProposta, nomeOportunidadeRenomeada = folders.renameFolders()
             
        planilhaCustosOrigem = configFiles()
        files = Files(planilhaCustosOrigem, nomeOportunidadeRenomeada, caminhoProposta)
        files.selectFiles() 
        files.copyFiles()
        files.renameFiles()
        pyautogui.alert('Processo concluído com sucesso!')    
    elif resposta == "Não":
        exit()
        diretorioPadraoOrigem, diretorioPadraoDestino = configFolders()
        client = Folders(diretorioPadraoOrigem, diretorioPadraoDestino)
        client.search()
        client.addLocal()
        
        planilhaCustosOrigem, planilhaCustosDestino = configFiles()
        files = Files(planilhaCustosOrigem, planilhaCustosDestino, client)
        client.copyFiles()
        client.renameFiles()
        pyautogui.alert('Processo concluído com sucesso!')
    else:
        pyautogui.alert('Processo interrompido!')
        exit()

if __name__ == '__main__': 
    main()