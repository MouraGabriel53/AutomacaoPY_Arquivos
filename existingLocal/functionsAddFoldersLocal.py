import pyautogui
import os
import shutil

class FoldersExistingLocal():    
    def __init__(self, caminhoClienteSelecionado, diretorioPadraoOportunidadeOrigem):
        self.diretorioPadraoOportunidadeOrigem = caminhoClienteSelecionado
        self. diretorioPadraoOportunidadeOrigem = diretorioPadraoOportunidadeOrigem
    
    def getLocalName(self):
            try:
                locais = [item for item in os.listdir(self.caminhoClienteSelecionado) if os.path.isdir(os.path.join(self.caminhoClienteSelecionado, item))]
                if not locais:
                    pyautogui.alert("Nenhum local encontrado.", '❌ Erro')
                    return None

                if len(locais) == 1:
                    self.localName = locais[0]
                else:
                    locais_enumerados = [f"[{i+1}] {item}" for i, item in enumerate(locais)]
                    escolha = pyautogui.prompt('Escolha o Local:\n' + '\n'.join(locais_enumerados), '❓ Nome Local')
                    
                    if escolha and escolha.isdigit():
                        indice = int(escolha) - 1
                        if 0 <= indice < len(locais):
                            self.localName = locais[indice]
                        else:
                            pyautogui.alert("Escolha inválida.", '❌ Erro')
                            return None
                    else:
                        pyautogui.alert("Escolha inválida.", '❌ Erro')
                        return None
                    
                caminhoLocalSelecionado = os.path.join(self.caminhoClienteSelecionado, self.localName)
                return caminhoLocalSelecionado
            except Exception as e:
                pyautogui.alert(f"Ocorreu um erro ao buscar o nome do local: {e}", '❌ Erro')
                exit()
                
    def addOportunity(self):
        try:
            self.caminhoOportunidadeAdicionada = shutil.copytree(self.diretorioPadraoOportunidadeOrigem, self.caminhoClienteSelecionado, dirs_exist_ok=True)   
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao buscar os diretórios: {e}', '❌ Erro')
            exit()
                
    def renameOportunity(self):
        try:
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
            caminhoPropostaAddLocal = os.path.join(self.caminhoClienteSelecionado, self.caminhoOportunidadeAdicionada, nomeOportunidadeAddRenomeada, 'Proposta')
            return caminhoPropostaAddLocal, nomeOportunidadeAddRenomeadaSemCaminho
            
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao renomear os diretórios: {e}', '❌ Erro')
            exit()