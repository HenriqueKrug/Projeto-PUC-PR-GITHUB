
# Importações

import paho.mqtt.client as mqtt
import time
from AS_hal_1 import temperatura, temperaturaExterna, aquecedor1, aquecedor3, controleTemperatura_1_1, controleTemperatura_1_2
from AS_conexao_disp_1 import user, password, client_id, client_id3, server, port

permissaoAquecedorX = 0
permissaoAquecedorX3 = 0
temperaturaAtual = temperatura()
temperaturaAtual3 = temperatura()
temperaturaAmbiente = temperaturaExterna()

# Funções

def mensagem1(client, userdata, msg):
    global permissaoAquecedorX
    vetor = msg.payload.decode().split(',')
    permissaoAquecedorX = aquecedor1 ('on' if vetor[1] == '1' else 'off')
    client.publish(f'v1/{user}/things/{client_id}/response', f'ok,{vetor[0]}')
#   print ('Vetor 1:', vetor)
 
def mensagem4(client3, userdata3, msg3):
    global permissaoAquecedorX3
    vetor3 = msg3.payload.decode().split(',')
    permissaoAquecedorX3 = aquecedor3 ('on' if vetor3[1] == '1' else 'off')
    client3.publish(f'v1/{user}/things/{client_id3}/response', f'ok,{vetor3[0]}')
#   print ('Vetor 3:', vetor3)

# Conexão Inicial - Estufa 1 e 3

client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

client.on_message = mensagem1
client.subscribe(f'v1/{user}/things/{client_id}/cmd/2')
client.loop_start() #fica rodando e monitorando possíveis mensagens

client3 = mqtt.Client(client_id3)
client3.username_pw_set(user, password)
client3.connect(server, port)

client3.on_message = mensagem4
client3.subscribe(f'v1/{user}/things/{client_id3}/cmd/2')
client3.loop_start() #fica rodando e monitorando possíveis mensagens

while True:

    temperaturaAmbiente = temperaturaExterna()
    client.publish('v1/'+user+'/things/'+client_id+'/data/3', temperaturaAmbiente)
    client3.publish('v1/'+user+'/things/'+client_id3+'/data/3', temperaturaAmbiente)
    
    if(permissaoAquecedorX == 'on'):

        EstufaNr = 1
        print('\nESTUFA 1 : Permissão de funcionamento do Aquecedor: PERMITIDO.')
        print ('ESTUFA 1 : Controle automático de temperatura: LIGADO.')
        client.publish('v1/'+user+'/things/'+client_id+'/data/0', temperaturaAtual)
        temperaturaAtual = controleTemperatura_1_1(temperaturaAtual,EstufaNr)

    if(permissaoAquecedorX == 'off'):

        EstufaNr = 1
        print('\nESTUFA 1 : Permissão de funcionamento do Aquecedor: NÃO PERMITIDO.')
        print ('ESTUFA 1 : Controle automático de temperatura: DESLIGADO.')
        client.publish('v1/'+user+'/things/'+client_id+'/data/0', temperaturaAtual)
        temperaturaAtual = controleTemperatura_1_2(temperaturaAtual,EstufaNr)
                
    if(permissaoAquecedorX == 0):

        temperaturaAtual = temperatura()
        
        print('\nESTUFA 1 : Teste do programa não iniciado.')
        print('ESTUFA 1 : Mandando temperaturas aleatórias...')
        print ('ESTUFA 1 : Temperatura Atual: ', temperaturaAtual)
        client.publish('v1/'+user+'/things/'+client_id+'/data/0', temperaturaAtual)

    if(permissaoAquecedorX3 == 'on'):

        EstufaNr = 3
        print('\nESTUFA 3 : Permissão de funcionamento do Aquecedor: PERMITIDO.')
        print ('ESTUFA 3 : Controle automático de temperatura: LIGADO.')
        client3.publish('v1/'+user+'/things/'+client_id3+'/data/0', temperaturaAtual3)
        temperaturaAtual3 = controleTemperatura_1_1(temperaturaAtual3,EstufaNr)

    if(permissaoAquecedorX3 == 'off'):

        EstufaNr = 3
        print('\nESTUFA 3 : Permissão de funcionamento do Aquecedor: NÃO PERMITIDO.')
        print ('ESTUFA 3 : Controle automático de temperatura: DESLIGADO.')
        client3.publish('v1/'+user+'/things/'+client_id3+'/data/0', temperaturaAtual3)
        temperaturaAtual3 = controleTemperatura_1_2(temperaturaAtual3,EstufaNr)

    if(permissaoAquecedorX3 == 0):

        temperaturaAtual3 = temperatura()
        print('\nESTUFA 3 : Teste do programa não iniciado.')
        print('ESTUFA 3 : Mandando temperaturas aleatórias...')
        print ('ESTUFA 3 : Temperatura Atual: ', temperaturaAtual3)    
        
        client3.publish('v1/'+user+'/things/'+client_id3+'/data/0', temperaturaAtual3)

    time.sleep(3)
    print('\n*****************************************')


#client.disconnect()

