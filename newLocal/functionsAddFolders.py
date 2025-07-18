import pyautogui
import os
import shutil

class FoldersAdd:
    def __init__(self, diretorioPadraoDestino, diretorioPadraoLocalOrigem):
        self.diretorioPadraoDestino = diretorioPadraoDestino
        self.diretorioPadraoLocalOrigem = diretorioPadraoLocalOrigem
        
        
    def nameClientList(self):
        try:
            if not os.path.exists(self.diretorioPadraoDestino):
                pyautogui.alert(f"O diretório {self.diretorioPadraoDestino} não foi encontrado.", '❌ Erro')
                return

            itens = os.listdir(self.diretorioPadraoDestino)
            self.diretorioPadraoDestinos = [item for item in itens if os.path.isdir(os.path.join(self.diretorioPadraoDestino, item))]
            if not self.diretorioPadraoDestinos:
                pyautogui.alert("Nenhum diretório encontrado.", '❌ Erro')
                return

            self.diretorioPadraoDestinos_enumeradas = [f"[{i+1}] {item}" for i, item in enumerate(self.diretorioPadraoDestinos)]
            escolha = pyautogui.prompt('Escolha o Cliente:\n' + '\n'.join(self.diretorioPadraoDestinos_enumeradas), '❓ Nome Cliente')
            
            if escolha and escolha.isdigit():
                indice = int(escolha) - 1
                if 0 <= indice < len(self.diretorioPadraoDestinos):
                    self.caminhoClienteSelecionado = os.path.join(self.diretorioPadraoDestino, self.diretorioPadraoDestinos[indice])
                    #print(f"Caminho selecionado: {self.caminhoClienteSelecionado}")
                    caminhoClienteSelecionado = self.caminhoClienteSelecionado
                    return caminhoClienteSelecionado
                else:
                    pyautogui.alert("Escolha inválida.", '❌ Erro')
                    exit()
            else:
                pyautogui.alert("Escolha inválida.", '❌ Erro')
                exit()
        except FileNotFoundError:
            pyautogui.alert(f"O diretório {self.diretorioPadraoDestino} não foi encontrado.", '❌ Erro')
            exit()
        except Exception as e:
            pyautogui.alert(f"Ocorreu um erro: {e}", '❌ Erro')
            exit()
            
    def addLocal(self):
        try:
            caminhoClienteSelecionado = self.nameClientList()
            if not caminhoClienteSelecionado:
                pyautogui.alert('Nenhum caminho de cliente selecionado.', '❌ Erro')
                exit()
            shutil.copytree(self.diretorioPadraoLocalOrigem, self.caminhoClienteSelecionado, dirs_exist_ok=True)   
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao buscar os diretórios: {e}', '❌ Erro')
            exit() 
            
    def renameAddLocalAndOportunity(self):
        try:
            if not hasattr(self, 'caminhoClienteSelecionado') or not os.path.exists(self.caminhoClienteSelecionado):
                pyautogui.alert('Caminho do cliente selecionado não é válido ou não existe.', '❌ Erro')
                exit()
            # Renomeia o local 
            nomeLocalAddAntigo = os.path.join(self.caminhoClienteSelecionado, 'Local')
            nomeLocalAddRenomeado = pyautogui.prompt('Por favor, informe o nome do Local:', '❓ Nome Local')
            if not nomeLocalAddRenomeado:
                pyautogui.alert('O processo foi interrompido pelo usuário.', '❌ Erro')
                return
            nomeLocalAddRenomeado = os.path.join(self.caminhoClienteSelecionado, nomeLocalAddRenomeado)
            os.rename(nomeLocalAddAntigo, nomeLocalAddRenomeado)

            # Renomeia a oportunidade 
            nomeOportunidadeAddAntiga = os.path.join(nomeLocalAddRenomeado, 'O25xxxx')
            nomeOportunidadeAddRenomeada = pyautogui.prompt('Por favor, informe o nome da Oportunidade:', '❓ Nome Oportunidade')
            nomeOportunidadeAddRenomeadaSemCaminho = nomeOportunidadeAddRenomeada
            if not nomeOportunidadeAddRenomeada:
                pyautogui.alert('O processo foi interrompido pelo usuário.', '❌ Erro')
                return
            nomeOportunidadeAddRenomeada = os.path.join(nomeLocalAddRenomeado, nomeOportunidadeAddRenomeada)
            os.rename(nomeOportunidadeAddAntiga, nomeOportunidadeAddRenomeada)
            #pyautogui.alert('As self.diretorioPadraoDestinos foram renomeadas com sucesso!', '✅ Concluído')
            caminhoPropostaAddLocal = os.path.join(self.caminhoClienteSelecionado, nomeLocalAddRenomeado, nomeOportunidadeAddRenomeada, 'Proposta')
            return caminhoPropostaAddLocal, nomeOportunidadeAddRenomeadaSemCaminho
        
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao renomear os diretórios: {e}', '❌ Erro')
            exit() 
                      