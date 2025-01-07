import pyautogui
from functionsFiles import Files
from functionsFolders import Folders

pyautogui.FAILSAFE = True  
pyautogui.PAUSE = 0.5  

resposta = pyautogui.confirm('A pasta Cliente já existe?', buttons=['Sim', 'Não'])
    
if resposta == "Não":
    folders = Folders()
    folders.copyFolders()
    folders.renameFolders()    
    files = Files()
    files.selectFiles()
    files.copyFiles()
    files.renameFiles()
    pyautogui.alert('Processo concluído com sucesso!')
    
if resposta == "Sim":
    exit() #teste
    client = Folders()
    client.search()
    client.addLocal()
    files = Files()
    client.copyFiles()
    client.renameFiles()
    pyautogui.alert('Processo concluído com sucesso!')

else:
    pyautogui.alert('Processo interrompido!')
    exit()