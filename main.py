import pyautogui
from functionsFiles import files
from functionsFolders import folders

pyautogui.FAILSAFE = True  
pyautogui.PAUSE = 0.5  

resposta = pyautogui.confirm('A pasta Cliente já existe?', buttons=['Sim', 'Não'])
    
if resposta == "Não":
    folders = folders()
    folders.copyfolders()
    folders.renamefolders()
    files = files()
    files.selectFiles()
    files.copyFiles()
    files.renameFiles()
    pyautogui.alert('Processo concluído com sucesso!')
    
else:
    exit()
    client = folders()
    client.search()
    client.addLocal()
    client.copyFiles()
    client.pasteFiles()
    client.renameFiles()
    pyautogui.alert('Processo concluído com sucesso!')