from threading import Thread
import random
import asyncio

async def processa_inputs_user():
    print('iniciando processamento de inputs...')
    timeSleep = random.random()
    await asyncio.sleep(timeSleep)
    print('finalizando processamento de inputs')
    return 'resultado 1'

async def atualiza_outros_jogadores():
    print('iniciando atualização dos outros jogares...')
    timeSleep = random.random()
    await asyncio.sleep(timeSleep)
    print('finalizando atualização dos outros jogares')
    return 'resultado 2'

async def processa_fisica():
    print('iniciando processamento da fisica...')
    timeSleep = random.random()
    await asyncio.sleep(timeSleep)
    print('finalizando processamento da fisica')
    return 'resultado 3'

async def atualiza_texturas():
    print('iniciando Atualizando as Texturas...')
    timeSleep = random.random()
    await asyncio.sleep(timeSleep)
    print('finalizando Atualizando as Texturas')
    return 'resultado 4'

async def renderiza_imagem():
    print('iniciando renderização de imagens...')
    timeSleep = random.random()
    await asyncio.sleep(2*timeSleep)
    print('finalizando renderização de imagens')
    return 'resultado 5'

async def compoem_frame():
    print('iniciando Crianção do frame...')
    timeSleep = random.random()
    await asyncio.sleep(timeSleep)
    print('finalizando Crianção do frame')
    return 'resultado 6'

async def envia_atualizacoes_do_jogador():
    print('iniciando atualizando o mundo para os outros jogadores...')
    timeSleep = random.random()
    await asyncio.sleep(2*timeSleep)
    print('finalizando atualizando o mundo para os outros jogadores')
    return 'resultado 7'


async def mainLoop():
    while True:
        inputs, outros, fisica, texturas = await asyncio.gather(
            processa_inputs_user(),
            atualiza_outros_jogadores(),
            processa_fisica(),
            atualiza_texturas()
        )

        novo_frame = await renderiza_imagem()

        updated, enviado = await asyncio.gather(
            compoem_frame(),
            envia_atualizacoes_do_jogador()
        )

        print('-----------------')
        print('novo frame exibido')
        print('-----------------')

asyncio.run(mainLoop())
