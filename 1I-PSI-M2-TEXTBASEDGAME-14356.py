from colorama import Fore

###tentativas###

tentativa = 0

#Start

print(f"{'WELCOME TO' : >50}")
print(
  f"{'━╤デ╦︻⧼ [̲̅C̲̅є̲̅G̲̅σ̲̅ ̲̅α̲̅т̲̅É̲̅ ̲̅σ̲̅ ̲̅α̲̅L̲̅G̲̅α̲̅я̲̅V̲̅є̲̅] ⧽︻╦デ╤━' : >50}"
)

print("\n\nChose your language: ")
language = input(
  "\n[Portuguese]\n[More languages coming soon...]\n\n")  #escolha da linguagem
language = (language.lower())
if language == 'portuguese':
  print("\nA linguagem escolhida foi português")

start = input("\n\nComeçar um novo jogo?   [S]   [N]\n\n")
start = (start.lower())
if start == 's':
  print('\nloading...')
else:
  print('Ok, fechando o jogo...')
  quit()

nome = input("\n\nInsira o seu nome: \n\n")

print('\nOlá', nome,
      '! Bem vindo ao CEGO ATÉ AO ALGARVE para jogar lê o seguinte...\n')
print('AVISO\n\n Porfavor escreva as opções exatamente como estão escritas para evitar erros se tiver que copiar copie!!!\n SE nas escolhas estiver alguma coisa dentro de PARENTESES RETOS é essa palavra que deves escrever!!!\n    P.S. Se a resposta estiver mal escrita vai sempre te levar pelo percurso errado\n\nAVISO\n')
input()

##inventario, 

carteira = 1000
int(carteira)
inventory = []

death = 0
while death == 0:
  ded = 0
  death = 0
  if ded == 0:
    inventory.clear()
    tentativa = tentativa + 1
    print('Voçe vai em', tentativa, 'tentativas!')
  input('Clique ENTER para começar')
  print('\n\n')
  print('  ____   ____             _____  ____  _____ _______ ______ \n |  _ \ / __ \   /\      / ____|/ __ \|  __ \__   __|  ____|\n | |_) | |  | | /  \    | (___ | |  | | |__) | | |  | |__   \n |  _ <| |  | |/ /\ \    \___ \| |  | |  _  /  | |  |  __|  \n | |_) | |__| / ____ \   ____) | |__| | | \ \  | |  | |____ \n |____/ \____/_/    \_\ |_____/ \____/|_|  \_\ |_|  |______|\n\n')
  input()
  print('-------------------------------------------------------------------------------------------------------------------\n')

  input()
  print(' __     __     ______     __         ______     ______     __    __     ______ \n/\ \  _ \ \   /\  ___\   /\ \       /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   \n\ \ \/ ".\ \  \ \  __\   \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __\   \n \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\ \n  \/_/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/  \/_/   \/_____/ ')

  print(' ______   ______   \n/\__  _\ /\  __ \   \n\/_/\ \/ \ \ \/\ \ \n   \ \_\  \ \_____\  \n    \/_/   \/_____/ ')

  print(' ______   ______     ______     ______   ______    \n/\  == \ /\  __ \   /\  == \   /\__  _\ /\  __ \   \n\ \  _-/ \ \ \/\ \  \ \  __<   \/_/\ \/ \ \ \/\ \  \n \ \_\    \ \_____\  \ \_\ \_\    \ \_\  \ \_____\ \n  \/_/     \/_____/   \/_/ /_/     \/_/   \/_____/ \n\n\n')

  #INICIO

  inicio = input('Bem-vindo ao Porto, o Sr. Cego está ao pé da estrada e agora o que queres que ele faça?\n Ir de avião [AVIAO]  |  Tentar apanhar boleia [CARRO]  \n  -')
  inicio = (inicio.lower())
  if inicio == ('aviao'):
    print('\n\n\nEscolhes-te ir de avião. Tens', carteira,'€ na tua carteira.')
    travel = input('Escolhe o destino do Sr. Cego!\n\n [FARO (161€)]  |  [OHIO (424€)]  | (More cities coming soon...)\n  -')
    travel = (travel.lower())
    if travel == ('faro'):
      carteira = (carteira - 161)
      print('\n\nForam debitados da carteira dele 161€, agora tem', carteira,
            '€ ')
      print('\nA opção selecionada foi Faro mas ouve um imprevisto...')
      input()
      quedaaviao = input('\nO avião dele CAIU enquanto estava a passar no Rio Tejo e o Sr. Cego foi o unico sobrevivente mas com ferimentos graves.\nO que ele faz? Grita por ajuda ou vai a nadar?\n  [GRITA]  |  [NADA] \n  -')
      quedaaviao = (quedaaviao.lower())
      if quedaaviao == ('grita'):
        print('\nEnquanto estavas a gritar o corpo do Sr. Cego começa a deitar mais sangue e acaba por morrer...')
        input(Fore.RED + 'Morres de forma estupida!!')
        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
        reset = (reset.lower())
        if reset == ('sim'):
          print('\n\n')
        elif reset == ('nao'):
          print('Ok fechando o jogo...')
          quit()
        else:
          print('Escreves-te mal, fechando o jogo...')
          quit()
        
        
      elif quedaaviao == ('nada'):
        print('\nEnquanto estavas a nadar inesperadamente aparece um crocodilo e acabas por ser o almoço dele!')
        input(Fore.RED + 'Morres de forma estupida!!')
        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
        reset = (reset.lower())
        if reset == ('sim'):
          print('\n\n')
        elif reset == ('nao'):
          print('Ok fechando o jogo...')
          quit()
        else:
          print('Escreves-te mal, fechando o jogo...')
          quit()
        
      else:
        print('\nNão selecionaste nenhuma opção por causa disso o Sr, Cego ficou no avião a deitar sangue por todos os lados.')
        input(Fore.RED + 'Morres de forma estupida!!')
        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
        reset = (reset.lower())
        if reset == ('sim'):
          print('\n\n')
        elif reset == ('nao'):
          print('Ok fechando o jogo...')
          quit()
        else:
          print('Escreves-te mal, fechando o jogo...')
          quit()
        
    elif travel == ('ohio'):
      carteira = (carteira - 424)
      print('\n\nForam debitados da carteira dele 424€, agora tem', carteira,'€ ')
      print('\nAo ir para Ohio terás de jogar o "Cego em Ohio" e para isso aqui está o link: ')
      print(Fore.BLUE +'\n--->   https://replit.com/@Alvaro-Carneiro/Cego-em-Ohio   <---')
    else:
      print('Não escolheste nenhuma opção devido a esse acontecimento ficas no aeroporto até o fim da tua vida e morres lá.')
      input(Fore.RED + 'Morres de forma estupida!!')
      reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
      reset = (reset.lower())
      if reset == ('sim'):
        print('\n\n')
      elif reset == ('nao'):
        print('Ok fechando o jogo...')
        quit()
      else:
        print('Escreves-te mal, fechando o jogo...')
        quit()
        
  elif inicio == ('carro'):
    print('\n\nBoa escolha! Se a selecionas-te logo antes da outra fico feliz por não teres tentado chegar ao destino rápido. Se é que chegavas lá... MUAHAHAHA!!!')
    print('Continuando...')
    input()
    comermac = input("Com essa tua decisão o Sr. Cego enquanto ia para a entrada da autoestrada para tentar apanhar boleia, passa pelo McDonald's e o senhor cego está com um pouco de fome.\nQueres que ele vá lá comer?  [SIM]  [NAO]\n  -")
    comermac = (comermac.lower())
    if comermac == ('nao'):
      print('\n\nSelecionas-te (NAO). Se assim o queres assim será.')
      homemsus = input('\nEntão ele continua o seu caminho até à autoestrada e por sorte para logo um carro de um homem meio suspeito.\nQueres que o senhor cego vá com ele?  [SIM] [NAO]\n  -')
      homemsus = (homemsus.lower())
      if homemsus == ('sim'):
        print('\n\nSelecionas-te [SIM], devido a isso o Sr. Cego entra no carro mas o homem estava muito bebado...')
        input()
        print('\nEle durante o caminho acaba por se despistar e tem um acidente.')
        print(Fore.RED + 'Morres de forma estupida!!')
        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
        reset = (reset.lower())
        if reset == ('sim'):
          print('\n\n')
        elif reset == ('nao'):
          print('Ok fechando o jogo...')
          quit()
        else:
          print('Escreves-te mal, fechando o jogo...')
          quit()
      elif homemsus == ('nao'):
        print('\nSelecionas-te [NAO], passado 2h e 30 min uma mulher para e oferece-te boleia.')
        mulhersus = input(
          'Queres que o Sr. Cego vá com ela?  [SIM]  [NAO]\n  -')
        mulhersus = (mulhersus.lower())
        if mulhersus == ('sim'):
          print('\nQuando o Sr. Cego entra no carro ela dá um gazão com o carro e rapta-o.')
          print(Fore.RED + 'Morres de forma estupida!!')
          reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
          reset = (reset.lower())
          if reset == ('sim'):
            print('\n\n')
          elif reset == ('nao'):
            print('Ok fechando o jogo...')
            quit()
          else:
            print('Escreves-te mal, fechando o jogo...')
            quit()
        elif mulhersus == ('nao'):
          print('\nSelecionas-te [NAO], então o Sr. Cego ficou tanto tempo à espera de mais alguem para lhe dar boleia que acabou por morrer à fome!')
          print(Fore.RED + 'Morres de forma estupida!!')
          reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
          reset = (reset.lower())
          if reset == ('sim'):
           print('\n\n')
          elif reset == ('nao'):
           print('Ok fechando o jogo...')
           quit()
          else:
            print('Escreves-te mal, fechando o jogo...')
            quit()
        else:
          print('\nNão selecionas-te nenhuma opção!!! E com isso a mulher vai para embora e outro carro que estava a vir atrás atropela-te.')
          print(Fore.RED + 'Morres de forma estupida!!')
          reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
          reset = (reset.lower())
          if reset == ('sim'):
            print('\n\n')
          elif reset == ('nao'):
            print('Ok fechando o jogo...')
            quit()
          else:
            print('Escreves-te mal, fechando o jogo...')
          quit()
      else:
        print('\nNão selecionas-te nenhuma opção!!! Devido a isso o homem do carro pega numa arma e dá-lhe um tiro no meio da cabeça.')
        print(Fore.RED + 'Morres de forma estupida!!')
        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
        reset = (reset.lower())
        if reset == ('sim'):
         print('\n\n')
        elif reset == ('nao'):
         print('Ok fechando o jogo...')
         quit()
        else:
          print('Escreves-te mal, fechando o jogo...')
          quit()
    elif comermac == ('sim'):
      carteira = (carteira - 12)
      print('\n\nFicas-te com menos 12€ na carteira ou seja o total de',
            carteira, '€.')
      print('\nLogo depois de ir ao mac o Sr. Cego ficou satisfeito e segue o seu caminho. Enquanto ia para a autoestrada o Sr. Cego passou por um beco onde estavam lá 3 gunas...')
      input()
      glock = input('\nUma Glock-18 está a frente dele queres que ele pegue nela?   [SIM]  [NAO]\n  -')
      glock = (glock.lower())
      if glock == ('sim'):
        print('\nA opção selecionada foi [SIM]. Mas quando ele ia pegar na arma... era uma armadilha e caiu um machado no meio da cabeça dele.')
        print(Fore.RED + 'Morres de forma estupida!!')
        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
        reset = (reset.lower())
        if reset == ('sim'):
         print('\n\n')
        elif reset == ('nao'):
          print('Ok fechando o jogo...')
          quit()
        else:
         print('Escreves-te mal, fechando o jogo...')
         quit()
      elif glock == ('nao'):
        print('\nA opção selecionada foi [NAO]. Ainda bem que não pegaste! Porque um bocado mais ao lado estava um RPG!!!')
        rpg = input('Queres que ele pegue no RPG?   [SIM]  [NAO]\n  -')
        rpg = (rpg.lower())
        if rpg == ('sim'):
          print('\n\nApanhaste um RPG. \n \n Item RPG adicionado ao inventário')
          inventory.append("RPG")
          print('\n\nChegou o momento de enfrentar os 3 gunas!!!')
          luta1 = input('O que o Sr. Cego faz dispara ou recua?   [DISPARA]  [RECUA]\n  -')
          luta1 = (luta1.lower())
          if luta1 == ('dispara'):
            print('A opção selecionada foi [DISPARA]. Como o Sr. Cego estava perto deles ao disparar ele explodiu os gunas e ele próprio.')
            print(Fore.RED + 'Morres de forma estupida!!')
            reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
            reset = (reset.lower())
            if reset == ('sim'):
              print('\n\n')
            elif reset == ('nao'):
              print('Ok fechando o jogo...')
              quit()
            else:
              print('Escreves-te mal, fechando o jogo...')
              quit()
          elif luta1 == ('recua'):
            luta2 = input('\nA opção selecionada foi [RECUA]. Queres que ele dispare agora ou recue mais?   [DISPARA]  [RECUA]\n  -')
            luta2 = (luta2.lower())
            if luta2 == ('dispara'):
              print('\nA opção selecionada foi [DISPARA].')
              input('Disparaste a arma e...')
              print(
                '\n ______     ______     ______     __    __       \n/\  == \   /\  __ \   /\  __ \   /\ "-./  \      \n\ \  __<   \ \ \/\ \  \ \ \/\ \  \ \ \-./\ \     \n \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\    \n  \/_____/   \/_____/   \/_____/   \/_/  \/_/    \n'
              )
              print('\nPARABÉNS!!! DERROTAS-TE O PRIMEIRO BOSS!')
              inventory.remove("RPG")
              print('Tens agora o teu inventário vazio.')
              print('...')
              input(
                '\n\nAgora o Sr. Cego vai para a autoestrada pois já está a ficar tarde!'
              )
              print('\nPassado 30 min um carro parou.')
              boleia3 = input('É um grupo de amigos que vai para Aveiro e que te ofereceram para passares a noite com eles e no dia seguinte de manhã tomares o pequeno almoço com eles.\nQueres que o Sr. Cego vá com eles?   [SIM]  [NAO]\n  -')
              boleia3 = (boleia3.lower())
              if boleia3 == ('sim'):
                print('\nJajus! Foi mesmo uma grande sorte ter encontrado estes gajos...')
                input()
                print(
                  ' __     __     ______     __         ______     ______     __    __     ______ \n/\ \  _ \ \   /\  ___\   /\ \       /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   \n\ \ \/ ".\ \  \ \  __\   \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __\   \n \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\ \n  \/_/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/  \/_/   \/_____/ '
                )
                print(' ______   ______   \n/\__  _\ /\  __ \   \n\/_/\ \/ \ \ \/\ \ \n   \ \_\  \ \_____\  \n    \/_/   \/_____/ ')
                print(
                  " ______     __   __   ______     __     ______     ______    \n/\  __ \   /\ \ / /  /\  ___\   /\ \   /\  == \   /\  __ \   \n\ \  __ \  \ \ \ '/  \ \  __\   \ \ \  \ \  __<   \ \ \/\ \  \n \ \_\ \_\  \ \__|    \ \_____\  \ \_\  \ \_\ \_\  \ \_____\ \n  \/_/\/_/   \/_/      \/_____/   \/_/   \/_/ /_/   \/_____/ \n"
                )

                #AVEIROOOOOOOO

                aveiro = input(
                  '\nAqueles gajos deixaram-te ao lado da Ponte Laços de Amizade queres que o Sr. Cego vá aonde? \nVisitar a ponte ou ao Parque Infantil de Barrocas.   [PONTE]  [PARQUE]\n  -'
                )
                aveiro = (aveiro.lower())
                if aveiro == ('ponte'):
                  print('\nA opção selecionada foi [PONTE].')
                  print(
                    '\nEntão o Sr. Cego foi para a ponte apreciar a vista mas quando ele estava lá a ponte estava muito cheia e ele acaba por cair ao rio empurrado por uma pessoa e morre afogado.'
                  )
                  print(Fore.RED + 'Morres de forma estupida!!')
                  reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                  reset = (reset.lower())
                  if reset == ('sim'):
                    print('\n\n')
                  elif reset == ('nao'):
                    print('Ok fechando o jogo...')
                    quit()
                  else:
                    print('Escreves-te mal, fechando o jogo...')
                    quit()

                elif aveiro == ('parque'):
                  print('\nEnquanto o Sr. Cego ia para o parque começou a ficar com muita fome.')
                  comidaaveiro = input('Queres que ele vá comer ao restaurante por 30€?   [SIM]  [NAO]\n  -')
                  comidaaveiro = (comidaaveiro.lower())
                  if comidaaveiro == ('nao'):
                    print('A opção selecionada foi [NAO].')
                    print('\nMano ele tá com bué fome e queres que ele não vá comer? OH  MAI GODE mas agora é tarde demais para mudar de ideias por isso como ele não foi comer durante o resto do caminho que faltava ele desmaiou e ficou lá estendido no chão.')
                    print(Fore.RED + 'Morres de forma estupida!!')
                    reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                    reset = (reset.lower())
                    if reset == ('sim'):
                      print('\n\n')
                    elif reset == ('nao'):
                      print('Ok fechando o jogo...')
                      quit()
                    else:
                      print('Escreves-te mal, fechando o jogo...')
                      quit()
                  elif comidaaveiro == ('sim'):
                    carteira = (carteira - 30)
                    print(
                      '\n\nFicas-te com menos 30€ na carteira ou seja o total de',
                      carteira, '€.')
                    print('UI UI, que a comida tava buéda boua! ')
                    print('\nAgora é hora de ir para o parque! Quando o Sr. Cego chega lá tá cheio de crianças, o primeiro ano de uma escola estava lá a fazer uma visita de estudo e foi ao parque para comer e brincar.')
                    rapto = input('Queres que o Sr. Cego rapte uma criança?   [SIM]  [NAO]\n  -')
                    rapto = (rapto.lower())
                    if rapto == ('nao'):
                      print('\nA opção selecionada foi [NAO]. O Sr. Cego tem de voltar para a auto estrada.')
                      pingodoce = input('Antes de ir queres que ele passe no Pingo Doce?   [SIM]  [NAO]\n  -')
                      pingodoce = (pingodoce.lower())
                      if pingodoce == ('sim'):
                        print('\nA opção selecionada foi [SIM].')
                        carteira = (carteira - 10)
                        inventory.append("Tremoços")
                        inventory.append("Jola")
                        print(
                          '\nTens Tremoços e uma Jola no inventário e na carteira tens ',
                          carteira, '€ (gastou 10€).')
                        print('Quando o Sr. Cego ia para a auto estrada estava lá a policia a revistar as pessoas que passavam e quando foi a vez do Sr. Cego passou sem nenhum problema.')
                        taxiaveiro = input('Está a ficar tarde e ainda nenhum carro parou o que o Sr. Cego faz? \nChama um taxi ou continua a tentar apanhar boleia?   [TAXI(70€)]  [CONTINUA]\n  -')
                        taxiaveiro = (taxiaveiro.lower())
                        if taxiaveiro == ('taxi'):
                          carteira = (carteira - 70)
                          print('\nA opção selecionada foi [TAXI]. Agora tens',carteira, '€ na tua carteira.')
                          print('...')
                          input()

                          #COIMBRAAAAAAAAAAAA
                          
                          print(' __     __     ______     __         ______     ______     __    __     ______ \n/\ \  _ \ \   /\  ___\   /\ \       /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   \n\ \ \/ ".\ \  \ \  __\   \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __\   \n \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\ \n  \/_/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/  \/_/   \/_____/ ')
                          print(' ______   ______   \n/\__  _\ /\  __ \   \n\/_/\ \/ \ \ \/\ \ \n   \ \_\  \ \_____\  \n    \/_/   \/_____/ ')
                          print(' ______     ______     __     __    __     ______     ______     ______    \n/\  ___\   /\  __ \   /\ \   /\ "-./  \   /\  == \   /\  == \   /\  __ \   \n\ \ \____  \ \ \/\ \  \ \ \  \ \ \-./\ \  \ \  __<   \ \  __<   \ \  __ \  \n \ \_____\  \ \_____\  \ \_\  \ \_\ \ \_\  \ \_____\  \ \_\ \_\  \ \_\ \_\ \n  \/_____/   \/_____/   \/_/   \/_/  \/_/   \/_____/   \/_/ /_/   \/_/\/_/ \n')
                          input()
                          print('Estamos em Coimbra mas já está de noite.')
                          hotelcoimbra = input('Queres ir para um hotel por 64€?   [SIM]  [NAO]\n  -')
                          hotelcoimbra = (hotelcoimbra.lower())
                          if hotelcoimbra == ('sim'):
                            print('\nA opção selecionada foi [SIM].')
                            carteira = (carteira - 64)
                            print('Tens', carteira, '€ na tua carteira.')
                            comidacoimbra = input('\nAcordas-te no dia seguinte mas já está passava da hora do almoço, queres comer o que tens na mochila ou comer fora?  [MOCHILA]  [FORA]\n  -')
                            comidacoimbra = (comidacoimbra.lower())
                            if comidacoimbra == ('mochila'):
                              print('\nA opção selecionada foi [MOCHILA].')
                              inventory.remove("Tremoços")
                              inventory.remove('Jola')
                              print('Os tremoços e a jola foram removidos do inventário')
                              
                              #####################################################
                              
                              leiria = input('\n\nChegou o momento de seguir viagem queres tentar apanhar viagem para Santarém. \nPararam 2 carros um deles é um homem que vai por Leiria e o outro é uma mulher que vai por Castelo Branco, com quem queres ir?   [HOMEM]  [MULHER]\n  -')
                              leiia = (leiria.lower())
                              if leiria == ('homem'):
                                print('\n\nA opção selecionada foi [HOMEM].')
                                print('\nMas quando estavas a entrar em leiria caíste no void do mundo.')
                                print(Fore.RED + 'Perdes para Leiria! LEIRIA NÃO EXISTE!!!')
                                reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                                reset = (reset.lower())
                                if reset == ('sim'):
                                  print('\n\n')
                                elif reset == ('nao'):
                                  print('Ok fechando o jogo...')
                                  quit()
                                else:
                                  print('Escreves-te mal, fechando o jogo...')
                                  quit()

                              elif leiria == ('mulher'):
                                print('\nA opção selecionada foi [MULHER].')
                                print('...')
                                input()
                                print(' __     __     ______     __         ______     ______     __    __     ______ \n/\ \  _ \ \   /\  ___\   /\ \       /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   \n\ \ \/ ".\ \  \ \  __\   \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __\   \n \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\ \n  \/_/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/  \/_/   \/_____/ ')
                                print(' ______   ______   \n/\__  _\ /\  __ \   \n\/_/\ \/ \ \ \/\ \ \n   \ \_\  \ \_____\  \n    \/_/   \/_____/ ')
                                print(' ______     ______     __   __     ______   ______     ______     ______     __    __    \n/\  ___\   /\  __ \   /\ "-.\ \   /\__  _\ /\  __ \   /\  == \   /\  ___\   /\ "-./  \   \n\ \___  \  \ \  __ \  \ \ \-.  \  \/_/\ \/ \ \  __ \  \ \  __<   \ \  __\   \ \ \-./\ \  \n \/\_____\  \ \_\ \_\  \ \_\\"\_ \    \ \_\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \ \_\ \n  \/_____/   \/_/\/_/   \/_/ \/_/     \/_/   \/_/\/_/   \/_/ /_/   \/_____/   \/_/  \/_/ ')

                                print('\n\nAgora em Santarém a mulher foi logo para casa dela e convidou o Sr. Cego a ir lá pra dentro com ela') 
                                mulhersan = input('Queres que o Sr. Cego vá com ela?  [SIM]  [NAO]\n  -')
                                mulhersan = (mulhersan.lower())
                                if mulhersan == ('sim'):
                                  print('\nA opção selecionada foi [SIM].')
                                  print('Quando o Sr. Cego entro com a mulher começou a seduzi-lo, com isso o Sr. Cego distraiu-se do seu objtivo principal.')
                                  print(Fore.RED + ('Perdes por seres seduzido'))
                                  reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                                  reset = (reset.lower())
                                  if reset == ('sim'):
                                    print('\n\n')
                                  elif reset == ('nao'):
                                    print('Ok fechando o jogo...')
                                    quit()
                                  else:
                                    print('Escreves-te mal, fechando o jogo...')
                                    quit() 
                                    
                                elif mulhersan == ('nao'):
                                  print('\n\nA opção selecionada foi [SIM].')
                                  decathlon = input('\nQueres que o Sr. Cego vá à dechatlon e ao continente para se reforçar para a viagem que falta (o dinheiro que ele vai gastar poderá ser util)?  [SIM]  [NAO]\n  -')
                                  decathlon = (decathlon.lower())
                                  if decathlon == ('sim'):
                                    carteira = (carteira - 250)
                                    inventory.append("Tenda")
                                    inventory.append("Bolachas")
                                    inventory.append("Sumos")
                                    print('\n\nA opção selecionada foi [SIM].')
                                    print('\nNa carteira tens ', carteira,'€, e no inventário tens 4 sumos de pacote pequenos e um saco grande de bolachas.')
                                    tendanova = input('\nQueres que o Sr. Cego agora vá falar com a mulher para dormir lá na casa dela ou na sua nova tenda? [CASA]  [TENDA]\n  -')
                                    tendanova = (tendanova.lower())
                                    if tendanova == ('casa'):
                                      print('\n\nA opção selecionada foi [SIM]. Então o Sr. Cego foi lá falar com ela mas qnd ela o vi pegou numa arma e deu-lhe um tiro de raiva nele.')
                                      print(Fore.RED + 'Morres de forma estupida!!')
                                      reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                                      reset = (reset.lower())
                                      if reset == ('sim'):
                                        print('\n\n')
                                      elif reset == ('nao'):
                                        print('Ok fechando o jogo...')
                                        quit()
                                      else:
                                        print('Escreves-te mal, fechando o jogo...')
                                        quit()
                                        
                                    elif tendanova == ('tenda'):
                                      print('\n\nA opção selecionada foi [NAO].')
                                      print('\nEntão o Sr. Cego foi para o meio do monte onde montou a sua tenda e dormiu traquilamente.')
                                      print('\nNo dia seguinte ele acordou e comeu um bocado do que tinha na mochila e foi para a autoestrada tentar apanhar boleia')
                                      print('Passado um bocado parou lá um carro, era um velhinho muito simpático que te ofereceu para ires com ele vai até ao algarve.')
                                      velhinho = input('\nQueres que o Sr. Cego vá com o velhinho?  [SIM]  [NAO]\n  -')
                                      velhinho = (velhinho.lower())
                                      if velhinho == ('sim'):
                                        print('\nA viagem foi longa mas interesante pois enquanto iamsos 2 partilharam diversas histórias, entre elas uma delas foi sobre a guerra. Contou-lhe a histório da sua quase morte...')
                                        print('\nO velhinho levou o Sr. Cego até Evora onde lá eles pararam para comer algo depois retornar à sua viagem e assim foi onde em beja pararam para descansar na tenda que o Sr. Cego tem. No dia a seguir o pequeno almoço foram as bolachas e os sumos que o Sr. Cego tinha...')
                                        print('Os dois continuaram a viagem e desta vez para chegar ao destino final... Mas algo inesperado aconteceu...')
                                        print('A mulher a quem recusaste ir para casa dela esteve a segui-los o tempo todo, e mesmo quando iam passar a placa a dizer "ALGARVE" ela para-vos o carro e rapta o velhinho!')
                                        final = input('\nEscreve o numero que tem a opção que queres que o Sr. Cego faça:\n\n[1] Sacrificar a tua vida pelo velho\n[2] Resgatar o velho e fugir\n[3] Fugir sem o velho\n[4] Tentar conversar com a mulher\n\n  -')
                                        final = (final.lower())
                                        if final == ('1'):
                                          print('\nBem, que assim seja...\n')
                                          input()
                                          print(' ______   __  __     __    __    \n/\  == \ /\ \/\ \   /\ "-./  \   \n\ \  _-/ \ \ \_\ \  \ \ \-./\ \  \n \ \_\    \ \_____\  \ \_\ \ \_\ \n  \/_/     \/_____/   \/_/  \/_/ ') 
                                          print('...')
                                          input()
                                          print(Fore.GREEN + '!Final Heroíco!')
                                          print(Fore.WHITE + '\nSacrificas-te a tua vida pelo velhinho parabéns por teres um coração tão bom!')
                                          print('\n Obrigado por jogares, espero que não tenhas aziado muito!')
                                          quit()
                                        
                                        elif final == ('2'):
                                          print('\nA mulher tava a segurar o velhinho pelo pescoço e então o Sr. Cego rapidamente aprocima-se delas, d+a um murro deixa-a em coma e foje com o velhinho.')
                                          print(Fore.GREEN + '\n!Final Feliz!')
                                          print(Fore.WHITE + '\nConseguiste acabar o jogo da melhor maneira possível!')
                                          print('\n Parabéns e obrigado por jogares, espero que não tenhas aziado muito!')
                                          quit()
                                        elif final == ('3'):
                                          print('\nNão quiseste salvar o velhinho com isso o Sr. Cego simplesmente entro no carro do velhinho e pôs-se a andar.')
                                          print(Fore.GREEN + '\nFinal solitário...')
                                          print(Fore.WHITE + '\nObrigado por jogares, espero que não tenhas aziado muito!')
                                          quit()
                                        elif final == ('4'):
                                          print('\nA mulher estava a agarrar o velhinho pelo pescoço e com a tua decisão o Sr. Cego foi falar com ela... ')
                                          print('\nEle tentou mas acabou por não dar em nada e matando o Sr Cego e o velhinho...')
                                          print(Fore.RED + 'Morres de forma triste...')
                                          reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                                          reset = (reset.lower())
                                          if reset == ('sim'):
                                            print('\n\n')
                                          elif reset == ('nao'):
                                            print('Ok fechando o jogo...')
                                            quit()
                                          else:
                                            print('Escreves-te mal, fechando o jogo...')
                                            quit()
                                        else:
                                          print('\nNão selecionas-te nenhuma opção (escreves-te mal) por causa disso nesta situação com os nervos o Sr. Cego acabou por desmaiar e ser raptado.')
                                          print(Fore.RED + '\nPerdes de forma estúpida!')
                                          reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                                          reset = (reset.lower())
                                          if reset == ('sim'):
                                            print('\n\n')
                                          elif reset == ('nao'):
                                            print('Ok fechando o jogo...')
                                            quit()
                                          else:
                                            print('Escreves-te mal, fechando o jogo...')
                                            quit()





                                        
                                        print('Os dois continuaram a viagem e desta vez para chegar ao destino final...')
                                      elif velhinho == ('nao'):
                                        print('\nA opção selecionada foi [NAO]')
                                        print('\nVer o velho partir sozinho... devagar... não foi fácil...')
                                        print(Fore.RED + 'Perdes de tristeza...')
                                        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                                        reset = (reset.lower())
                                        if reset == ('sim'):
                                          print('\n\n')
                                        elif reset == ('nao'):
                                          print('Ok fechando o jogo...')
                                          quit()
                                        else:
                                          print('Escreves-te mal, fechando o jogo...')
                                          quit()
                                        print(Fore.RED + 'Perdes de tristeza...')
                                        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                                        reset = (reset.lower())
                                        if reset == ('sim'):
                                          print('\n\n')
                                        elif reset == ('nao'):
                                          print('Ok fechando o jogo...')
                                          quit()
                                        else:
                                          print('Escreves-te mal, fechando o jogo...')
                                          quit()
                                      else:
                                        print('\nNão selecionas-te nenhuma opção (escreves-te mal) por causa disso o velhinho sentiu-se ignorado, fazendo o Sr. Cego ao ver a cena chorar lágrimas e lágrimas...')
                                        print(Fore.RED + 'Perdes de tristeza...')
                                        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                                        reset = (reset.lower())
                                        if reset == ('sim'):
                                          print('\n\n')
                                        elif reset == ('nao'):
                                          print('Ok fechando o jogo...')
                                          quit()
                                        else:
                                          print('Escreves-te mal, fechando o jogo...')
                                          quit()
                                    else:
                                      print('\nNão selecionas-te nenhuma opção (escreves-te mal) devido a isso a mulher foi atrás de ti para te matar e adivinha...')
                                      input('Matou-te!')
                                      print(Fore.RED + 'Morres de forma estupida!!')
                                      reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                                      reset = (reset.lower())
                                      if reset == ('sim'):
                                        print('\n\n')
                                      elif reset == ('nao'):
                                        print('Ok fechando o jogo...')
                                        quit()
                                      else:
                                        print('Escreves-te mal, fechando o jogo...')
                                        quit()

                                  elif decathlon == ('nao'):
                                    print('\n\nA opção selecionada foi [NAO].')
                                    print('\nNão quiseste ir à compras devido a isso a tua unica opçao para dormir era na casa da mulher mas quando foste lá ela de tanta raiva que ficou da tua resposta matou-te')
                                    print(Fore.RED + 'Morres de forma estupida!!')
                                    reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                                    reset = (reset.lower())
                                    if reset == ('sim'):
                                      print('\n\n')
                                    elif reset == ('nao'):
                                      print('Ok fechando o jogo...')
                                      quit()
                                    else:
                                      print('Escreves-te mal, fechando o jogo...')
                                      quit()
                                      
                                  else:
                                    print('\nNão selecionas-te nenhuma opção (escreves-te mal) devido a isso o Sr. Cego ficou tão indeciso em qual ia primeiro que acabou por ter uma explosão cerebral.')
                                    print(Fore.RED + 'Morres de forma estupida!!')
                                    reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                                    reset = (reset.lower())
                                    if reset == ('sim'):
                                      print('\n\n')
                                    elif reset == ('nao'):
                                      print('Ok fechando o jogo...')
                                      quit()
                                    else:
                                      print('Escreves-te mal, fechando o jogo...')
                                      quit()
                                    
                                  
                                else:
                                  print('\nNão selecionas-te nenhuma opção (escreves-te mal) devido a isso a mulher zangada por não lhe teres respondido deu-lhe uma chapada bem forte que o Sr. Cego ficou em coma e logo depois morrer.')
                                  print(Fore.RED + 'Perdes de forma estupida!!')
                                  reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                                  reset = (reset.lower())
                                  if reset == ('sim'):
                                    print('\n\n')
                                  elif reset == ('nao'):
                                    print('Ok fechando o jogo...')
                                    quit()
                                  else:
                                    print('Escreves-te mal, fechando o jogo...')
                                    quit()
                              else:
                                print('\nNão selecionas-te nenhuma opção (escreves-te mal) devido a isso quando o Sr. Cego os dois carros chocam contra o Sr. Cego e morre esmagado pelos 2.')
                                print(Fore.RED + 'Perdes de forma estupida!!')
                                reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                                reset = (reset.lower())
                                if reset == ('sim'):
                                  print('\n\n')
                                elif reset == ('nao'):
                                  print('Ok fechando o jogo...')
                                  quit()
                                else:
                                  print('Escreves-te mal, fechando o jogo...')
                                  quit()
                                
                            elif comidacoimbra == ('fora'):
                              print('\nA opção selecionada foi [FORA]. Enquanto ele ia para lá reparou que todos os restaurantes tavam fechados pois já passava do horario do almoço quando ele chegou lá.')
                              print(Fore.RED + 'Perdes de forma estupida!!')
                              reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                              reset = (reset.lower())
                              if reset == ('sim'):
                                print('\n\n')
                              elif reset == ('nao'):
                                print('Ok fechando o jogo...')
                                quit()
                              else:
                                print('Escreves-te mal, fechando o jogo...')
                                quit()
                            
                          elif hotelcoimbra == ('nao'):
                            print('\nA opção selecionada foi [NAO].')
                            print('\nBruh, deixas-te o Sr Cego ao frio! Isso não se faz!!!')
                            print(Fore.RED + 'Morres de forma estupida!!')
                            reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                            reset = (reset.lower())
                            if reset == ('sim'):
                              print('\n\n')
                            elif reset == ('nao'):
                              print('Ok fechando o jogo...')
                              quit()
                            else:
                              print('Escreves-te mal, fechando o jogo...')
                              quit()

                        elif taxiaveiro == ('continua'):
                          print('\nA opção selecionada foi [CONTINUA]. Mas mais ninguém parou então com o frio que estava por causa de estar de noite o Sr. Cego morreu.')
                          print(Fore.RED + 'Perdes de forma estupida!!')
                          reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                          reset = (reset.lower())
                          if reset == ('sim'):
                            print('\n\n')
                          elif reset == ('nao'):
                            print('Ok fechando o jogo...')
                            quit()
                          else:
                            print('Escreves-te mal, fechando o jogo...')
                            quit()

                      elif pingodoce == ('nao'):  
                        print('\nA opção selecionada foi [NAO].')
                        print('Quando o Sr. Cego ia para a auto estrada estava lá a policia a revistar as pessoas que passavam e quando foi a vez do Sr. Cego passou sem nenhum problema.')
                        print('\n\n __     __     ______     __         ______     ______     __    __     ______ \n/\ \  _ \ \   /\  ___\   /\ \       /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   \n\ \ \/ ".\ \  \ \  __\   \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __\   \n \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\ \n  \/_/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/  \/_/   \/_____/ ')
                        print(' ______   ______   \n/\__  _\ /\  __ \   \n\/_/\ \/ \ \ \/\ \ \n   \ \_\  \ \_____\  \n    \/_/   \/_____/ ')
                        print(' ______     ______     __     __    __     ______     ______     ______    \n/\  ___\   /\  __ \   /\ \   /\ "-./  \   /\  == \   /\  == \   /\  __ \   \n\ \ \____  \ \ \/\ \  \ \ \  \ \ \-./\ \  \ \  __<   \ \  __<   \ \  __ \  \n \ \_____\  \ \_____\  \ \_\  \ \_\ \ \_\  \ \_____\  \ \_\ \_\  \ \_\ \_\ \n  \/_____/   \/_____/   \/_/   \/_/  \/_/   \/_____/   \/_/ /_/   \/_/\/_/ \n')
                        input()
                        print('Estamos em Coimbra mas já está de noite.')
                        hotelcoimbra = input('Queres ir para um hotel por 64€?   [SIM]  [NAO]\n  -')
                        hotelcoimbra = (hotelcoimbra.lower())
                        if hotelcoimbra == ('sim'):
                          print('\nA opção selecionada foi [SIM].')
                          carteira = (carteira - 64)
                          comidacoimbra = input('Acordas-te no dia seguinte mas já está passava da hora do almoço, queres comer o que tens na mochila ou comer fora?  [MOCHILA]  [FORA]\n  -')
                          comidacoimbra = (comidacoimbra.lower())
                          if comidacoimbra == ('mochila'):
                            print('\nA opção selecionada foi [MOCHILA]. Mas tu não tens nada na mochila porque não foste ao Pingo Doce.')
                            print(Fore.RED + 'Perdes de forma estupida!!')
                            reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                            reset = (reset.lower())
                            if reset == ('sim'):
                              print('\n\n')
                            elif reset == ('nao'):
                              print('Ok fechando o jogo...')
                              quit()
                            else:
                              print('Escreves-te mal, fechando o jogo...')
                              quit()
                            
                          elif comidacoimbra == ('fora'):
                            print('\nA opção selecionada foi [FORA]. Enquanto ele ia para lá reparou que todos os restaurantes tavam fechados pois já passava do horario do almoço quando ele chegou lá.')
                            print(Fore.RED + 'Perdes de forma estupida!!')
                            reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                            reset = (reset.lower())
                            if reset == ('sim'):
                              print('\n\n')
                            elif reset == ('nao'):
                              print('Ok fechando o jogo...')
                              quit()
                            else:
                              print('Escreves-te mal, fechando o jogo...')
                              quit()
                          else:
                            print('\nNão selecionas-te nenhuma opção (escreves-te mal) devido a isso quando o Sr. Cego estava a descer as escadas do hotel caiu nos degraus e morreu.')
                            print(Fore.RED + 'Perdes de forma estupida!!')
                            reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                            reset = (reset.lower())
                            if reset == ('sim'):
                              print('\n\n')
                            elif reset == ('nao'):
                              print('Ok fechando o jogo...')
                              quit()
                            else:
                              print('Escreves-te mal, fechando o jogo...')
                              quit()
                        else:
                          print('\nNão selecionas-te nenhuma opção (escreves-te mal) devido a isso o Sr. Cego quando ia passar a estrada para ir ver o hotel morreu atropelado.')
                          print(Fore.RED + 'Perdes de forma estupida!!')
                          reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                          reset = (reset.lower())
                          if reset == ('sim'):
                            print('\n\n')
                          elif reset == ('nao'):
                            print('Ok fechando o jogo...')
                            quit()
                          else:
                            print('Escreves-te mal, fechando o jogo...')
                            quit()
                      else:
                        print('\nNão selecionas-te nenhuma opção (escreves-te mal) devido a isso por isso quando ele ia para o pingo doce acabou por ser atropelado por um carrinho de de compras.')
                        print(Fore.RED + 'Perdes de forma estupida!!')
                        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                        reset = (reset.lower())
                        if reset == ('sim'):
                          print('\n\n')
                        elif reset == ('nao'):
                          print('Ok fechando o jogo...')
                          quit()
                        else:
                          print('Escreves-te mal, fechando o jogo...')
                          quit()

                    elif rapto == ('sim'):
                      print('\nA opção selecionada foi [SIM]. Então o Sr. Cego reparou que as suas educadoras estavam distraídas e aproveitou de uma criança que estava sozinha para a raptar.')
                      print('\nApanhaste uma Criança. \nItem Criança adicionado ao inventário')
                      inventory.append("Criança")
                      print('\nTens um RPG e uma Criança no inventário')
                      pingodoce = input('\nAntes de ir queres que ele passe no Pingo Doce?   [SIM]  [NAO]\n  -')
                      pingodoce = (pingodoce.lower())
                      if pingodoce == ('sim'):
                        print('\nA opção selecionada foi [SIM]. Mas quando o Sr. entrou lá os seguranças reparam que a sua mochila estava estranha. Então foram revistá-lo e ele foi preso por rapto. \nNão raptes crianças para a próxima!!!')
                        print(Fore.RED + 'Perdes de forma estupida!!')
                        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                        reset = (reset.lower())
                        if reset == ('sim'):
                          print('\n\n')
                        elif reset == ('nao'):
                          print('Ok fechando o jogo...')
                          quit()
                        else:
                          print('Escreves-te mal, fechando o jogo...')
                          quit()
                      elif pingodoce == ('nao'):
                        print('\nA opção selecionada foi [NAO]. Então o Sr. Cego foi indo para a autoestrada. \nQuando chegou lá estava lá a policia a revistar todos que passavam por lá e como o Sr. Cego não é diferente dos outros também foi.')
                        print('Ao ser revistado a polícia foi ver a sua mochila e encontro lá a criança.')
                        print(Fore.RED + 'Perdes de forma estupida!!')
                        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                        reset = (reset.lower())
                        if reset == ('sim'):
                          print('\n\n')
                        elif reset == ('nao'):
                          print('Ok fechando o jogo...')
                          quit()
                        else:
                          print('Escreves-te mal, fechando o jogo...')
                          quit()

                      else:
                        print('\nNão selecionas-te nenhuma opção (escreves-te mal) devido a isso enquanto estava a andar levou com uma pedra na cabeça.')
                        print(Fore.RED + 'Morres de forma estupida!!')
                        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                        reset = (reset.lower())
                        if reset == ('sim'):
                          print('\n\n')
                        elif reset == ('nao'):
                          print('Ok fechando o jogo...')
                          quit()
                        else:
                          print('Escreves-te mal, fechando o jogo...')
                          quit()
                    else:
                      print('\nNão selecionas-te nenhuma opção (escreves-te mal) devido a isso as criaças correram todas para abeira do Sr. Cego e começaram a dar-lhe pontapés.')
                      print(Fore.RED + 'Morres de forma estupida!!')
                      reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                      reset = (reset.lower())
                      if reset == ('sim'):
                        print('\n\n')
                      elif reset == ('nao'):
                        print('Ok fechando o jogo...')
                        quit()
                      else:
                        print('Escreves-te mal, fechando o jogo...')
                        quit()
                else:
                  print('\nNão selecionas-te nenhuma opção devido a isso o Sr. Cego começou a andar às voltas e caiu ao rio.')
                  print(Fore.RED + 'Morres de forma triste :(')
                  reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                  reset = (reset.lower())
                  if reset == ('sim'):
                    print('\n\n')
                  elif reset == ('nao'):
                    print('Ok fechando o jogo...')
                    quit()
                  else:
                    print('Escreves-te mal, fechando o jogo...')
                    quit()
              elif boleia3 == ('nao'):
                print('\nA opção selecionada foi [NAO]. Mas infelizmente mais nenhum carro parou e o Sr. Cego morreu ao frio. TURURU')
                print(Fore.RED + 'Morres de forma estupida!!')
                reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                reset = (reset.lower())
                if reset == ('sim'):
                  print('\n\n')
                elif reset == ('nao'):
                  print('Ok fechando o jogo...')
                  quit()
                else:
                  print('Escreves-te mal, fechando o jogo...')
                  quit()
              else:
                print('\nNão escolhes-te nenhuma opção, por isso o Sr. cego, devido a isso derrepente caiu-lhe uma garrafa de vidro na cabeça e teve um traumatismo craniano.')
                print(Fore.RED + 'Morres de forma estupida!!')
                reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
                reset = (reset.lower())
                if reset == ('sim'):
                  print('\n\n')
                elif reset == ('nao'):
                  print('Ok fechando o jogo...')
                  quit()
                else:
                  print('Escreves-te mal, fechando o jogo...')
                  quit()
            elif luta2 == ('recua'):
              print('A opção selecionada foi [RECUA]. Ele ao recuar foi tanto que acabou por sair do beco, ir para a estrada e ser atropelado.')
              print(Fore.RED + 'Morres de forma estupida!!')
              reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
              reset = (reset.lower())
              if reset == ('sim'):
                print('\n\n')
              elif reset == ('nao'):
                print('Ok fechando o jogo...')
                quit()
              else:
                print('Escreves-te mal, fechando o jogo...')
                quit()
            else:
              print('Não selecionas-te nenhuma opção devido a isso o Sr. Cego levou com o tiro na zona genital e acaba falecendo.')
              print(Fore.RED + 'Morres de forma estupida!!')
              reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
              reset = (reset.lower())
              if reset == ('sim'):
                print('\n\n')
              elif reset == ('nao'):
                print('Ok fechando o jogo...')
                quit()
              else:
                print('Escreves-te mal, fechando o jogo...')
                quit()
          else:
            print('\nNão escolhes-te nenhuma opção por isso o Sr. Cego levou um tiro no meio da cabeça.')
            print(Fore.RED + 'Morres de forma estupida!!')
            reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
            reset = (reset.lower())
            if reset == ('sim'):
              print('\n\n')
            elif reset == ('nao'):
              print('Ok fechando o jogo...')
              quit()
            else:
              print('Escreves-te mal, fechando o jogo...')
              quit()
        elif rpg == ('nao'):
          print('\nNão pegas-te em nenhuma arma o Sr. Cego foi massacrado pelos 3 gunas.')
          print(Fore.RED + 'Morres de forma estupida!!')
          reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
          reset = (reset.lower())
          if reset == ('sim'):
            print('\n\n')
          elif reset == ('nao'):
            print('Ok fechando o jogo...')
            quit()
          else:
            print('Escreves-te mal, fechando o jogo...')
            quit()
        else:
          print('Como não selecionas-te nada (escreveste mal) o Sr. Cego levou um tiro no meio da cabeça.')
          print(Fore.RED + 'Morres de forma estupida!!')
          reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
          reset = (reset.lower())
          if reset == ('sim'):
            print('\n\n')
          elif reset == ('nao'):
            print('Ok fechando o jogo...')
            quit()
          else:
            print('Escreves-te mal, fechando o jogo...')
            quit()
      else:
        print('Enquanto ficaste a pensar se pegavas na glock ou não apareceu um torcedor do Porto bué aziado!! E por ele estar à frente dele o Sr. Cego levou um morreu que faleceu.\n Mas morres de forma estúpida!!')
        print(Fore.RED + 'Morres de forma estupida!!')
        reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
        reset = (reset.lower())
        if reset == ('sim'):
          print('\n\n')
        elif reset == ('nao'):
          print('Ok fechando o jogo...')
          quit()
        else:
          print('Escreves-te mal, fechando o jogo...')
          quit()
    else:
      print('\nNão selecionas-te nenhuma opção devido a isso o Sr. Cego ficou lá parado à frente do Mac e por causa disso um funcionário de lá atirou-lhe um BigTasty à cara.\n  Morres de forma estúpida!!')
      print(Fore.RED + 'Morres de forma estupida!!')
      reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
      reset = (reset.lower())
      if reset == ('sim'):
        print('\n\n')
      elif reset == ('nao'):
        print('Ok fechando o jogo...')
        quit()
      else:
        print('Escreves-te mal, fechando o jogo...')
        quit()
  else:
    print(
      '\nNão escolheste nenhuma opção (escreveste mal) devido a esse acontecimento o Sr. Cego ficou a pensar noutra maneira...'
    )
    input()
    print(
      'Passado algum tempo começou a chover e o Sr. Cego ao olhar para cima...'
    )
    input()
    print('CAI-LHE UM RELÃMPAGO NA CEBEÇA!')
    print(Fore.RED + 'Morres de forma estupida!!')
    reset = input(Fore.WHITE + '\nComeçar um novo jogo?  [SIM]  [NAO]\n  -')
    reset = (reset.lower())
    if reset == ('sim'):
      print('\n\n')
    elif reset == ('nao'):
      print('Ok fechando o jogo...')
      quit()
    else:
      print('Escreves-te mal, fechando o jogo...')
      quit()