import time
import random

permissaoAquecedor = 0
permissaoAquecedor3 = 0
estadoRele = 0
temp = 35

def temperatura():
    return random.randrange(-5, 45)

def temperaturaExterna():
    return 10

###############################################

def controleTemperatura_1_1 (temperaturaAtual, EstufaNr):

    if (temperaturaAtual < 30):
        print ('ESTUFA',EstufaNr,': Temperatura atual BAIXA:', temperaturaAtual)
        print ('ESTUFA',EstufaNr,': Status do aquecedor: LIGADO.')
 
        temperaturaModificada = temperaturaAtual + 1
        return temperaturaModificada
    
    if (temperaturaAtual > 30):
        print ('ESTUFA',EstufaNr,': Temperatura atual ALTA:', temperaturaAtual)
        print ('ESTUFA',EstufaNr,': Status do aquecedor: DESLIGADO.')

        temperaturaModificada = temperaturaAtual - 1
        return temperaturaModificada

    if (temperaturaAtual == 30):
        print('ESTUFA',EstufaNr,': Temperatura IDEAL ATINGIDA:',temperaturaAtual)
        temperaturaModificada = temperatura()
        print('ESTUFA',EstufaNr,': Nova temperatura aleatória definida:',temperaturaModificada)
        return temperaturaModificada

def controleTemperatura_1_2 (temperaturaAtual, EstufaNr):

    temperaturaAmbiente = temperaturaExterna()
    
    if (temperaturaAtual > temperaturaAmbiente):
        print ('ESTUFA',EstufaNr,': Status do aquecedor: DESLIGADO.')
        print ('ESTUFA',EstufaNr,': Temperatura caindo...')
        print ('ESTUFA',EstufaNr,': Temperatura atual:', temperaturaAtual)
        print ('ESTUFA',EstufaNr,': Temperatura externa:', temperaturaAmbiente)

        temperaturaModificada = temperaturaAtual - 1
        return temperaturaModificada

    if (temperaturaAtual < temperaturaAmbiente):
        print ('ESTUFA',EstufaNr,': Status do aquecedor: DESLIGADO.')
        print ('ESTUFA',EstufaNr,': Temperatura aumentando...')
        print ('ESTUFA',EstufaNr,': Temperatura atual:', temperaturaAtual)
        print ('ESTUFA',EstufaNr,': Temperatura externa:', temperaturaAmbiente)

        temperaturaModificada = temperaturaAtual + 1
        return temperaturaModificada

    if (temperaturaAtual == temperaturaAmbiente):
        print('ESTUFA',EstufaNr,': Status do aquecedor: DESLIGADO.')
        print('ESTUFA',EstufaNr,': Estabilidade - TEMPERATURA EXTERNA ATINGIDA:',temperaturaAtual)
        
        temperaturaModificada = temperatura()
        print('ESTUFA',EstufaNr,': Nova temperatura aleatória definida:',temperaturaModificada)
        return temperaturaModificada

###############################################
    
def aquecedor1(estado: str):

    global permissaoAquecedor

    if estado == 'on':
        permissaoAquecedor = 1
        print('\n*****************************************')
        print('\nESTUFA 1: Permissão de funcionamento do Aquecedor: PERMITIDO.')
        return 'on'

    else:
        permissaoAquecedor = 0
        print('\n*****************************************')
        print('\nESTUFA 1: Permissão de funcionamento do Aquecedor: NÃO PERMITIDO.')
        return 'off'
    
def aquecedor3(estado3: str):

    global permissaoAquecedor3

    if estado3 == 'on':
        permissaoAquecedor3 = 1
        print('\n*****************************************')
        print('\nESTUFA 3: Permissão de funcionamento do Aquecedor: PERMITIDO.', permissaoAquecedor3)
        return 'on'

    else:
        permissaoAquecedor3 = 0
        print('\n*****************************************')
        print('\nESTUFA 3: Permissão de funcionamento do Aquecedor: NÃO PERMITIDO.', permissaoAquecedor3)
        return 'off'


