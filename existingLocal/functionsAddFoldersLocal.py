import pyautogui
import os
import shutil

class FoldersExistingLocal():    
    def __init__(self, caminhoClienteSelecionado, diretorioPadraoOportunidadeOrigem):
        self.caminhoClienteSelecionado = caminhoClienteSelecionado
        self. diretorioPadraoOportunidadeOrigem = diretorioPadraoOportunidadeOrigem
    
    def getLocalName(self):
        try:
            if not os.path.exists(self.caminhoClienteSelecionado):
                pyautogui.alert(f'O caminho {self.caminhoClienteSelecionado} não existe.', '❌ Erro')
                exit()
            
            locais = [item for item in os.listdir(self.caminhoClienteSelecionado) if os.path.isdir(os.path.join(self.caminhoClienteSelecionado, item))]
            if not locais:
                pyautogui.alert("Nenhum local encontrado.", '❌ Erro')
                exit()

            locaisEnumerados = [f'[{i+1}] {item}' for i, item in enumerate(locais)]
            escolha = pyautogui.prompt('Escolha o Local:\n' + '\n'.join(locaisEnumerados), '❓ Nome Local')

            if escolha and escolha.isdigit():
                indice = int(escolha) - 1
                if 0 <= indice < len(locais):
                    localName = locais[indice]
                else:
                    pyautogui.alert("Escolha inválida.", '❌ Erro')
                    exit()
            else:
                pyautogui.alert("Escolha inválida ou cancelada.", '❌ Erro')
                exit()

            self.caminhoClienteLocalSelecionado = os.path.join(self.caminhoClienteSelecionado, localName)
        except Exception as e:
            pyautogui.alert(f"Ocorreu um erro ao buscar o nome do local: {e}", '❌ Erro')
            exit()
                
    def addOportunity(self):
        try:
            if not os.path.exists(self.caminhoClienteLocalSelecionado):
                pyautogui.alert(f'O caminho {self.caminhoClienteLocalSelecionado} não existe.', '❌ Erro')
                exit()
            self.caminhoOportunidadeAdicionada = shutil.copytree(self.diretorioPadraoOportunidadeOrigem, self.caminhoClienteLocalSelecionado, dirs_exist_ok=True)   
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao buscar os diretórios: {e}', '❌ Erro')
            exit()
                
    def renameOportunity(self):
        try:
            if not os.path.exists(self.caminhoOportunidadeAdicionada):
                pyautogui.alert(f'O caminho {self.caminhoOportunidadeAdicionada} não existe.', '❌ Erro')
                exit()
            # Renomeia a oportunidade 
            nomeOportunidadeAddAntiga = os.path.join(self.caminhoOportunidadeAdicionada, 'Oano_mes_xx_Descrição')
            nomeOportunidadeAddRenomeada = pyautogui.prompt('Por favor, informe o nome da Oportunidade:', '❓ Nome Oportunidade')
            nomeOportunidadeAddRenomeadaSemCaminho = nomeOportunidadeAddRenomeada
            if not nomeOportunidadeAddRenomeada:
                pyautogui.alert('O processo foi interrompido pelo usuário.', '❌ Erro')
                return
            nomeOportunidadeAddRenomeada = os.path.join(self.caminhoOportunidadeAdicionada, nomeOportunidadeAddRenomeada)
            os.rename(nomeOportunidadeAddAntiga, nomeOportunidadeAddRenomeada)
            #pyautogui.alert('As self.diretorioPadraoDestinos foram renomeadas com sucesso!', '✅ Concluído')
            caminhoPropostaAddLocal = os.path.join(self.caminhoClienteLocalSelecionado, nomeOportunidadeAddRenomeada, 'Proposta')
            return caminhoPropostaAddLocal, nomeOportunidadeAddRenomeadaSemCaminho
            
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao renomear os diretórios: {e}', '❌ Erro')
            exit()