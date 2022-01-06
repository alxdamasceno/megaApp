from random import randint
from time import sleep
import PySimpleGUI as sg
import emoji


def megaJogos(n=0, msg=''):
    # Função que gerar quantidades de dezenas
    # Function that generates amounts of tens

    dezenas = []
    jogos = []
    quant = int(values['res'])

    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            num = randint(1, 60)
            if num not in dezenas:
                dezenas.append(num)
                cont += 1
            if cont >= n:
                break
        dezenas.sort()
        jogos.append(str(dezenas[:]).replace('[', '').replace(']', '').replace(',', ' '))
        dezenas.clear()
        tot += 1

    print('==' * 25)
    print(" " * 30, f'Você Gerou {quant} Jogo(os) de {msg} Dezenas.')
    print('==' * 25)
    for i, c in enumerate(jogos):
        print(" " * 3, f'Jogos {i + 1} : {c}')
        sleep(0.75)
        with open('mega.txt', 'wt+') as file:
            file.write(f'{quant} JOGOS GERADOS!' + '\n')
            for c, valor in enumerate(jogos):
                file.write(f'jogo {c + 1}:{valor}' + '\n')
            file.write('    <<<<< BOA SORTE >>>>>\n')
    print('==' * 25)
    print(" " * 40, '<<< BOA SORTE >>>', emoji.emojize(':thumbs_up:\n'))


def tratErro(n=0, msg=''):
    # Função que trata erros do usuário
    # Function that handles user errors

    try:
        if values['res']:
            megaJogos(n, msg)
        else:
            print('Preencha o campo solicitado!', emoji.emojize(":grinning_face:"))
    except(ValueError, TypeError):
        print('ERRO: Por favor, digite somente números.', emoji.emojize(":thinking_face:"))


# print(emoji.demojize(""))

sg.theme('GreenTan')

menu_def = [['&File', ['&Open', '&Save', '___', 'Properties', '&Exit']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]

layout = [[sg.Menu(menu_def)],
          [sg.T('Mega Sena(da Virada) vamos jogar!', size=(30, 1), font='Arial 19', border_width=10,
                background_color="#1F9368", justification='c', text_color='#FFF')],
          [sg.T('Quantos jogos você deseja fazer?', font='Arial 12'), sg.In(size=(10, 1), key='res')],
          [sg.T('Assinale quantos números você está marcando neste jogo:', font='Arial 12')],
          [sg.R('6', 'FD1', default=True, key='6'), sg.R('7', 'FD1', key='7'), sg.R('8', 'FD1', key='8'),
           sg.R('9', 'FD1', key='9'), sg.R('10', 'FD1', key='10'), sg.R('11', 'FD1', key='11'),
           sg.R('12', 'FD1', key='12'), sg.R('13', 'FD1', key='13'), sg.R('14', 'FD1', key='14'),
           sg.R('15', 'FD1', key='15')],
          [sg.B('Gerar Jogos', button_color='#1F9368'), sg.Button('Clear', button_color='#259FE6'), sg.B('Exit')],
          [sg.Output(font='Cambria 14', text_color='#fff', background_color='Black',
                     size=(50, 15), key='-OUTPUT-')],
          [sg.Text(size=(40, 1), key='-OUTPUT2-'), sg.B('Save')],
          [sg.T('Deus Seja Louvado !\nCriador: Alx')]]

# Create the Window
window = sg.Window('Mega Sena(Mega da Virada)', layout, icon='favicon.ico')

# Event Loop to process
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Clear':
        window['-OUTPUT-'].update('')
        window['res'].update('')
    elif event == 'Gerar Jogos':
        if values['6']:
            tratErro(6, '6')
        elif values['7']:
            tratErro(7, '7')
        elif values['8']:
            tratErro(8, '8')
        elif values['9']:
            tratErro(9, '9')
        elif values['10']:
            tratErro(10, '10')
        elif values['11']:
            tratErro(11, '11')
        elif values['12']:
            tratErro(12, '12')
        elif values['13']:
            tratErro(13, '13')
        elif values['14']:
            tratErro(14, '14')
        elif values['15']:
            tratErro(15, '15')
        window['-OUTPUT2-'].update("<<<<< BOA SORTE! >>>>>")
window.close()
