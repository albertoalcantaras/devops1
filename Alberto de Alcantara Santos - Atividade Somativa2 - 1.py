## Alberto de Alcantara Santos - Gestão de projetos de TI"

print("ZOMBIE DICE (Protótipo Semana 8)")
print("Seja bem vindo ao jogo Zombie Dice!")

numjogadores = 0

while (numjogadores < 2):
       numjogadores = int(input("Informe a quantidade de jogadores: "))

       if numjogadores < 2:
        print("AVISO: Você precisa de pelo menos 2 jogadores!\n")


listajogadores = []
for i in range(numjogadores):
   nome = input("Informe o nome do jogador " + str(i + 1) + ":");

   listajogadores.append(nome);

print(listajogadores);


dadoVerde = ("C","P","C","T","P","C");
dadoAmarelo = ("T","P","C","T","P","C");
dadoVermelho = ("T","P","T","C","P","T");

listadados=[dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoAmarelo,dadoAmarelo,dadoAmarelo,dadoAmarelo,dadoVermelho,dadoVermelho,dadoVermelho];

print("\nINICIANDO O JOGO");
jogadorAtual=0;
dadosSorteados = [];
tiros=0;
cerebros=0;
passos=0;

listarodada = listadados.copy();
while True:
    print("\nTurno do jogador: \n", listajogadores[jogadorAtual]);


    for i in range (0, 3):
        import random

        numSorteado=random.randint(0 , (len(listarodada)-1));
        dadoSorteado=listarodada[numSorteado];

        if (dadoSorteado==("C","P","C","T","P","C")):
            corDado = 'Verde';
        elif (dadoSorteado==("T","P","C","T","P","C")):
            corDado = 'Amarelo'
        else:
            corDado = 'Vermelho';

        print("Dados sorteado: ", corDado);

        dadosSorteados.append(dadoSorteado);
        listarodada.pop(numSorteado);

        print("Dados Sorteados", dadosSorteados)


    print("\nAs faces sorteadas foram: ");
    for i in range(0,3):
        import random
        numFaceDado=random.randint(0,5);

        if dadoSorteado[numFaceDado]=="C":
            print("- CÉREBRO (Você comeu um cérebro)");
            cerebros=cerebros+1;


        elif dadoSorteado[numFaceDado]=="T":
            print("- TIRO (Você levou um tiro)");
            tiros=tiros+1;

        elif dadoSorteado[numFaceDado]=="P":
            print("- PASSOS (Uma vitima escapou)");

    if tiros >= 3:
        print("Você levou 3 tiros - GAME OVER")


        jogadorAtual = jogadorAtual + 1;

        dadosSorteados = [];
        tiros = 0;
        cerebros = 0;
        passos = 0;
        numSorteado1 = 0;
        listarodada = listadados.copy();
        if (jogadorAtual == len(listajogadores)):
            jogadorAtual = jogadorAtual - 1;
            print("\nFinalizando protótipo do jogo...")

            break

    if cerebros == 13:
        print("Parabéns, você venceu chegou a 13 cérebros");
        listarodada = listadados.copy();
        jogadorAtual = jogadorAtual + 1;
        dadosSorteados = [];
        tiros = 0;
        cerebros = 0;
        passos = 0;
        numSorteado1 = 0;
        if (jogadorAtual == len(listajogadores)):
            jogadorAtual = jogadorAtual - 1;
            print("Você perdeu")


    print("\nSCORE ATUAL: ")
    print("- CÉREBROS: ", cerebros)
    print("- TIROS: ", tiros)
    print("- Dados no Copo", len(listarodada))
    print(listarodada)


    continuarTurno=input("\nAVISO: Você deseja continuar jogando dados? (s=sim / n=não)");

    if(continuarTurno=="n"):
        listarodada = listadados.copy();
        jogadorAtual=jogadorAtual+1;
        dadosSorteados=[];
        tiros=0;
        cerebros=0;
        passos=0;
        numSorteado1 = 0;
        if(jogadorAtual==len(listajogadores)):
            print("\nFinalizando protótipo do jogo...")

            break

    elif print("\nIniciando mais uma rodada do turno atual..."):
        dadosSorteados=[];





