import pyautogui
from newPath.functionsFiles import Files
from newPath.functionsFolders import Folders
from newLocal.functionsAddFiles import FilesAdd
from newLocal.functionsAddFolders import FoldersAdd
from existingLocal.functionAddFilesLocal import FilesExistingLocal
from existingLocal.functionsAddFoldersLocal import FoldersExistingLocal

def configFolders():
    diretorioPadraoOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Diretório Padrão'
    diretorioPadraoDestino = r'\\192.168.1.4\Comercial\Proposta 2025'
    diretorioPadraoLocalOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Diretório Padrão\Cliente'
    diretorioPadraoOportunidadeOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Diretório Padrão\Cliente\Local'
    return diretorioPadraoOrigem, diretorioPadraoDestino, diretorioPadraoLocalOrigem, diretorioPadraoOportunidadeOrigem

def configFiles():
    planilhaCustosOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Planilha Venda\Planilha de Calculo\FGI 08A - Planilha de Custos rev02 - Lucro Real.xlsx'
    return planilhaCustosOrigem

def main():
    resposta = pyautogui.confirm('Deseja adicionar um novo Cliente?', '➕ Adicionar cliente', buttons=['Sim', 'Não'])    
    if resposta == "Sim":
        diretorioPadraoOrigem, diretorioPadraoDestino, diretorioPadraoLocalOrigem, diretorioPadraoOportunidadeOrigem = configFolders()
        folders = Folders(diretorioPadraoOrigem, diretorioPadraoDestino)
        folders.copyFolders()
        caminhoProposta, nomeDiretórioOportunidadadeRenomeada = folders.renameFolders()             
        planilhaCustosOrigem = configFiles()
        files = Files(planilhaCustosOrigem, nomeDiretórioOportunidadadeRenomeada, caminhoProposta)
        files.selectFiles() 
        files.copyFiles()
        files.renameFiles()
        pyautogui.alert('Processo concluído com sucesso!', '✅ Concluído')    
    elif resposta == "Não":
        diretorioPadraoOrigem, diretorioPadraoDestino, diretorioPadraoLocalOrigem, diretorioPadraoOportunidadeOrigem = configFolders()
        folders = FoldersAdd(diretorioPadraoDestino, diretorioPadraoLocalOrigem)
        caminhoClienteSelecionado = folders.nameClientList()
                
        respostaAddLocal = pyautogui.confirm('Deseja adicionar um novo Local?', '➕ Adicionar Local', buttons=['Sim', 'Não'])
        if not respostaAddLocal:
            pyautogui.alert('O processo foi interrompido pelo usuário.', '❌ Erro')
            exit()
        if respostaAddLocal == 'Sim':
            folders.addLocal()
            caminhoPropostaAddLocal, nomeOportunidadeAddRenomeadaSemCaminho = folders.renameAddLocalAndOportunity()
            planilhaCustosOrigem = configFiles()
            files = FilesAdd(planilhaCustosOrigem, caminhoPropostaAddLocal, nomeOportunidadeAddRenomeadaSemCaminho)
            files.selectFilesAdd()
            files.copyFilesAdd()
            files.renameFilesAdd()
        if respostaAddLocal == 'Não':
            exit()           
            folders = FoldersExistingLocal(caminhoClienteSelecionado, diretorioPadraoOportunidadeOrigem)
            folders.getLocalName()
            folders.addOportunity()
            caminhoPropostaAddLocal, nomeOportunidadeAddRenomeadaSemCaminho = folders.renameOportunity()
            planilhaCustosOrigem = configFiles()
            files = FilesExistingLocal(planilhaCustosOrigem, caminhoPropostaAddLocal, nomeOportunidadeAddRenomeadaSemCaminho)
            files.selectFilesLocal()
            exit()
            files.copyFilesLocal()
            files.renameFilesLocal()
            exit()
            
if __name__ == '__main__': 
    main()