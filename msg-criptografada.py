letras_aceitas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

arquivo = open('chave.txt', 'r')
criptografia = arquivo.read()


def criarCriptografia(arquivo):
    from random import randint
    arquivo.close()
    criptografia = ''
    while len(criptografia) != len(letras_aceitas):
        caractere = letras_aceitas[randint(0, 25)]
        if caractere not in criptografia:
            criptografia += caractere
    with open('chave.txt', 'w') as file:
        file.write(criptografia)
    arquivo = open('chave.txt', 'r')

    return criptografia


def criptografar(mensagem):
    from random import randint
    global criptografia, letras_aceitas
    mensagem_criptografada = ''
    for letra in mensagem:
        if letra in letras_aceitas:
            indice = letras_aceitas.index(letra)
            mensagem_criptografada += criptografia[indice]
        else:
            mensagem_criptografada += maiusculas[randint(0, 25)]

    return mensagem_criptografada


def descriptografar(mensagem):
    global criptografia, letras_aceitas
    mensagem_descriptografada = ''
    for letra in mensagem:
        if letra in criptografia:
            indice = criptografia.index(letra)
            mensagem_descriptografada += letras_aceitas[indice]
        else:
            mensagem_descriptografada += '_'

    return mensagem_descriptografada


print('----O que deseja fazer?----')
print('[1] - Criptografar mensagem')
print('[2] - Descriptografar mensagem')
print('[3] - Criar nova chave')
print('[4] - Sair')


while True:
    opcao = str(input('Escolha: '))
    if opcao not in ['1', '2', '3']:
        break

if opcao == '1':
    print('Por favor, não digite palavras acentuadas ou caracter especial')
    mensagem = input('Mensagem para criptografar: ').lower()
    print(criptografar(mensagem))
elif opcao == '2':
    mensagem = input('Mensagem para descriptografar: ')
    print(descriptografar(mensagem))
elif opcao == '3':
    criptografia = criarCriptografia(arquivo)
    print('Nova chave criada com sucesso, cole ela no arquivo chave.txt do seu amigo.')
else:
    print('Opção inválida')
