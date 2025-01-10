import pyautogui
import os
import shutil

class FilesAdd:
    def __init__(self, planilhaCustosOrigem, caminhoPropostaAddLocal, nomeOportunidadeAddRenomeadaSemCaminho, caminhoLocalSelecionado):
        self.planilhaCustosOrigem = planilhaCustosOrigem
        self.caminhoPropostaAddLocal = caminhoPropostaAddLocal
        self.nomeOportunidadeAddRenomeadaSemCaminho = nomeOportunidadeAddRenomeadaSemCaminho
        self.caminhoLocalSelecionado = caminhoLocalSelecionado
        
    def selectFilesAdd(self):
        try: 
            tipoProposta = pyautogui.prompt(
                'Por favor, informe o tipo da proposta:\n[1] Assistência Técnica\n[2] Automação Básica\n[3] Automação Completa\n[4] Painéis\n[5] Revenda\n[6] TI', 
                '❓ Tipo Proposta'
            )
            if not tipoProposta:
                pyautogui.alert('O processo foi interrompido pelo usuário.', '❌ Erro')
                exit() 
            
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
                    pyautogui.alert('Tipo de proposta inválido. O processo foi interrompido!', '❌ Erro')
                    exit()
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao selecionar os arquivos: {e}', '❌ Erro')
            exit()
    
    def copyFilesAdd(self):
        try:          
            os.makedirs(os.path.dirname(self.caminhoPropostaAddLocal), exist_ok=True)
            self.nomePropostaModeloAntigoAdd = shutil.copy2(self.propostaModeloOrigem, self.caminhoPropostaAddLocal)
            self.nomePlanilhaCustosAntigoAdd = shutil.copy2(self.planilhaCustosOrigem, self.caminhoPropostaAddLocal)
            #pyautogui.alert('Os arquivos foram copiados com sucesso!', '✅ Concluído')
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao copiar os arquivos: {e}', '❌ Erro')
            exit()

    def renameFilesAdd(self):
        try:  
            nomePropostaModeloRenomeadaAdd = os.path.join(self.caminhoPropostaAddLocal, f'{self.nomeOportunidadeAddRenomeadaSemCaminho} rev0.0.docx')
            os.rename(self.nomePropostaModeloAntigoAdd, nomePropostaModeloRenomeadaAdd)
            nomePlanilhaCustosRenomeadaAdd = os.path.join(self.caminhoPropostaAddLocal, f'{self.nomeOportunidadeAddRenomeadaSemCaminho} rev0.0.xlsx') 
            os.rename(self.nomePlanilhaCustosAntigoAdd, nomePlanilhaCustosRenomeadaAdd)      
            #pyautogui.alert('Os arquivos foram renomeados com sucesso!', '✅ Concluído')
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao renomear os arquivos: {e}', '❌ Erro')
            exit()
            
    def copyFilesLocal(self):
        try:          
            os.makedirs(os.path.dirname(self.caminhoLocalSelecionado), exist_ok=True)
            self.nomePropostaModeloAntigoAdd = shutil.copy2(self.propostaModeloOrigem, self.caminhoLocalSelecionado)
            self.nomePlanilhaCustosAntigoAdd = shutil.copy2(self.planilhaCustosOrigem, self.caminhoLocalSelecionado)
            #pyautogui.alert('Os arquivos foram copiados com sucesso!', '✅ Concluído')
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao copiar os arquivos: {e}', '❌ Erro')
            exit()

    def renameFilesLocal(self):
        try:  
            nomePropostaModeloRenomeadaAdd = os.path.join(self.caminhoLocalSelecionado, f'{self.nomeOportunidadeAddRenomeadaSemCaminho} rev0.0.docx')
            os.rename(self.nomePropostaModeloAntigoAdd, nomePropostaModeloRenomeadaAdd)
            nomePlanilhaCustosRenomeadaAdd = os.path.join(self.caminhoLocalSelecionado, f'{self.nomeOportunidadeAddRenomeadaSemCaminho} rev0.0.xlsx') 
            os.rename(self.nomePlanilhaCustosAntigoAdd, nomePlanilhaCustosRenomeadaAdd)      
            #pyautogui.alert('Os arquivos foram renomeados com sucesso!', '✅ Concluído')
        except Exception as e:
            pyautogui.alert(f'Ocorreu um erro ao renomear os arquivos: {e}', '❌ Erro')
            exit()
