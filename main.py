import pyautogui
import os
import shutil

pyautogui.FAILSAFE = True  # Habilita a função de segurança para interromper o script movendo o mouse para o canto superior esquerdo
pyautogui.PAUSE = 0.5  # Define um intervalo de pausa de 0.5 segundos entre cada chamada de função

# Pergunta ao usuário se a pasta Cliente já existe
resposta = pyautogui.confirm('A pasta Cliente já existe?', buttons=['Sim', 'Não'])

if resposta == 'Sim':
    caminho_cliente = pyautogui.prompt('Por favor, informe o caminho da pasta Cliente:')
    if not caminho_cliente:
        pyautogui.alert('O processo foi interrompido pelo usuário.')
        exit()
    else:
        pastaProposta = caminho_cliente
        
elif resposta == 'Não':
    # Copia o diretório padrão
    diretorioPadraoOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Diretório Padrão'
    diretorioPadraoDestino = r'\\192.168.1.4\Comercial\Proposta 2025'
    shutil.copytree(diretorioPadraoOrigem, diretorioPadraoDestino, dirs_exist_ok=True)

    # Renomeia o diretório padrão
    nomeClienteAntigo = os.path.join(diretorioPadraoDestino, 'Cliente')
    nomeClienteRenomeado = pyautogui.prompt('Por favor, informe o nome do cliente:')
    if not nomeClienteRenomeado:
        pyautogui.alert('O processo foi interrompido pelo usuário.')
        exit()
    diretorioPadraoRenomeado = os.path.join(diretorioPadraoDestino, nomeClienteRenomeado)
    os.rename(nomeClienteAntigo, diretorioPadraoRenomeado)
    
    # Renomeia o local
    nomeLocalAntigo = os.path.join(diretorioPadraoRenomeado, 'Local')
    nomeLocal = pyautogui.prompt('Por favor, informe o nome do local:')
    if not nomeLocal:
        pyautogui.alert('O processo foi interrompido pelo usuário.')
        exit()
    nomeLocalRenomeado = os.path.join(diretorioPadraoRenomeado, nomeLocal)
    os.rename(nomeLocalAntigo, nomeLocalRenomeado)
    
    # Renomeia a oportunidade
    nomeOportunidadeAntigo = os.path.join(nomeLocalRenomeado, 'Oano_mes_xx_Descrição')
    nomeOportunidade = pyautogui.prompt('Por favor, informe o nome da oportunidade:')
    if not nomeOportunidade:
        pyautogui.alert('O processo foi interrompido pelo usuário.')
        exit()
    nomeOportunidadeRenomeado = os.path.join(nomeLocalRenomeado, nomeOportunidade)
    os.rename(nomeOportunidadeAntigo, nomeOportunidadeRenomeado)

    # Procura a proposta modelo e a planilha de custos 
    tipoProposta = pyautogui.prompt('Por favor, informe tipo da proposta\n[1] Assistência Técnica\n[2] Automação Básica\n[3] Automação Completa\n[4] Painéis\n[5] Revenda\n[6] TI:') 
    
    if tipoProposta == '1':
        propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Assistência Técnica - 20.12.2024.docx'
    elif tipoProposta == '2':
        propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão Automação Básica - 20.12.2024.docx'
    elif tipoProposta == '3':
        propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão Automação Completa - 20.12.2024.docx'
    elif tipoProposta == '4':
        propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão Painéis - 20.12.2024.docx'
    elif tipoProposta == '5':
        propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão Revenda de Material - 20.12.2024.docx'
    elif tipoProposta == '6':
        propostaModeloOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Proposta Modelo\PROPOSTA - 2025\Proposta - Padrão TI - 20.12.2024.docx'
    else:
        pyautogui.alert('Tipo de proposta inválido. O processo foi interrompido.')
        exit()

    if not os.path.exists(propostaModeloOrigem):
        pyautogui.alert(f'O caminho {propostaModeloOrigem} não foi encontrado. O processo foi interrompido.')
        exit()
    
    planilhaCustosOrigem = r'\\192.168.1.4\Comercial\Proposta 2025\A_Planilha Venda\Planilha de Calculo\FGI 08A - Planilha de Custos rev02 - Lucro Real.xlsx'
    if not os.path.exists(planilhaCustosOrigem):
        pyautogui.alert(f'O caminho {planilhaCustosOrigem} não foi encontrado. O processo foi interrompido.')
        exit()
            
    # Copia a proposta modelo e a planilha de custos para a pasta do cliente
    pastaPropostaDestino = os.path.join(diretorioPadraoDestino, nomeClienteRenomeado, nomeLocal, nomeOportunidade)
    diretorioCliente = os.path.join(pastaPropostaDestino, 'Proposta')
    os.makedirs(diretorioCliente, exist_ok=True)
    
    planilhaCustosDestino = os.path.join(diretorioCliente, f'{nomeOportunidade} rev0.0.xlsx')
    shutil.copy(planilhaCustosOrigem, planilhaCustosDestino)
    
    propostaModeloDestino = os.path.join(diretorioCliente, f'{nomeOportunidade} rev0.0.docx')
    shutil.copy(propostaModeloOrigem, propostaModeloDestino)

    pyautogui.alert('Processo concluído com sucesso!')