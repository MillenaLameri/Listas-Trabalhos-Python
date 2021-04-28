from random import randint

def forca(ten):
	hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
	print(hangman[ten])

def printapalavra(aux, letrasT):
	for x in range(len(aux)):
		if aux[x] in letrasT:
			print(aux[x] + " ", end = " ")
		else:
			print("_ ", end = " ")

print(r"""          _____                   _______                   _____                    _____                    _____          
         /\    \                 /::\    \                 /\    \                  /\    \                  /\    \         
        /::\    \               /::::\    \               /::\    \                /::\    \                /::\    \        
       /::::\    \             /::::::\    \             /::::\    \              /::::\    \              /::::\    \       
      /::::::\    \           /::::::::\    \           /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \         /:::/~~\:::\    \         /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \       /:::/    \:::\    \       /:::/__\:::\    \        /:::/  \:::\    \        /:::/__\:::\    \    
   /::::\   \:::\    \     /:::/    / \:::\    \     /::::\   \:::\    \      /:::/    \:::\    \      /::::\   \:::\    \   
  /::::::\   \:::\    \   /:::/____/   \:::\____\   /::::::\   \:::\    \    /:::/    / \:::\    \    /::::::\   \:::\    \  
 /:::/\:::\   \:::\    \ |:::|    |     |:::|    | /:::/\:::\   \:::\____\  /:::/    /   \:::\    \  /:::/\:::\   \:::\    \ 
/:::/  \:::\   \:::\____\|:::|____|     |:::|    |/:::/  \:::\   \:::|    |/:::/____/     \:::\____\/:::/  \:::\   \:::\____\
\::/    \:::\   \::/    / \:::\    \   /:::/    / \::/   |::::\  /:::|____|\:::\    \      \::/    /\::/    \:::\  /:::/    /
 \/____/ \:::\   \/____/   \:::\    \ /:::/    /   \/____|:::::\/:::/    /  \:::\    \      \/____/  \/____/ \:::\/:::/    / 
          \:::\    \        \:::\    /:::/    /          |:::::::::/    /    \:::\    \                       \::::::/    /  
           \:::\____\        \:::\__/:::/    /           |::|\::::/    /      \:::\    \                       \::::/    /   
            \::/    /         \::::::::/    /            |::| \::/____/        \:::\    \                      /:::/    /    
             \/____/           \::::::/    /             |::|  ~|               \:::\    \                    /:::/    /     
                                \::::/    /              |::|   |                \:::\    \                  /:::/    /      
                                 \::/____/               \::|   |                 \:::\____\                /:::/    /       
                                  ~~                      \:|   |                  \::/    /                \::/    /        
                                                           \|___|                   \/____/                  \/____/         
                                                                                                                             """)

palavras = ["abcdefA","abcdefB","abcdefC","abcdefD","abcdefE","abcdefF","abcdefG","abcdefH","abcdefI","abcdefJ"]

jogo = True

while jogo:

	palavrasU = []
	tentativas = 0
	letrasT = []
	ver= []
	ten = ' '
	aux2 = True
	partida = True
	while aux2:
		aux = randint(0,9)
		if aux not in palavrasU:
			aux2 = False

	palavrasU.append(aux)
	aux = palavras[aux].upper()

	while partida:
		
		printapalavra(aux,letrasT)
		print("\n")

		ten = input("Escolha uma letra >> ")
		ten = ten.upper()
		if len(ten) != 1:
			print("Tentativa inválida, escolha outra letra (uma de cada vez)")
		elif ten in letrasT:
			print("Tentativa já efetuada, tente uma nova letra")
		elif ten in aux:
			print("Acertou!")
			letrasT.append(ten)
		else:
			print("Errou!")
			letrasT.append(ten)
			forca(tentativas)
			tentativas+=1
			print("Restam %s erros!" % (7 - tentativas))
		ver3 = []
		for x in range(len(aux)):
			ver3.append(aux[x])
			if aux[x] in letrasT:
				ver.append(aux[x])

		ver2 = ver
		ver2.sort()
		ver3.sort()
		ver2 = dict.fromkeys(ver2)
		ver3 = dict.fromkeys(ver3)
		if len(ver2) == len(ver3):
			if ver2 == ver3:
				partida = False
				ganhou = True
			else:
				partida = True

		if tentativas >= 7:
				partida = False
				ganhou = False
			
	if ganhou:
		printapalavra(aux,letrasT)
		print("Parabéns, você venceu!!")
	else:
		print("Não foi dessa vez, mas vai ter mais sorte na próxima tentativa")
	denovo = input("Deseja jogar novamente? S ou N >>")
	if denovo.lower() == 'n':
		jogo = False

print("Venha Jogar mais vezes!")