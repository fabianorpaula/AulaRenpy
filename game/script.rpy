# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Julia", color="#153dc6")
define m = Character("Marcos Pato", color="#e109ff")
define nome = Character("Nome Jogador", color="#e109ff")

# The game starts here.

label start:
    
    $porno = True
    $direcao = False

    $ nome = renpy.input("QUAL O SEU NOME?:")

    nome "Oi como está [nome]"
    
    $ idade = renpy.input("QUAL A SUA IDADE?:")

    "O Jogador(a) [nome] têm anos"
    #Essa é uma estrutura de decisão
    $ idade = int(idade)
    if idade > 17:
        "Você é de maior"
        jump podejogar
    else:
        "Você é de menor"
        jump naopodejogar

    play music "audio/Fundo.mp3"

    scene biblioteca

    nome "Julia Aparece na historia"

    nome "Julia é uma linda e inteligente capivara"

   

    show julia at right
    
    

    e "Oi Marcos Pato"

    e "O que você faz aqui?"

    

    show marcos at left

    m "Oi Julinha, vim dar uma malhada no cerebro"

    m "Tá tudo firmeza?"

    play sound "audio/tiro.mp3"

    scene academia

    show marcos

    m "A Academia é meu templo"

    m "Vem malhar comigo Julinha"

    stop music

    menu:
        "Eu vou estudar":
            jump estudar
        "Eu vou malhar":
            jump malhar
        "Quero mais nada":
            return
        "Quero ir para praia":
            jump praia
    return


label estudar:
    
    scene biblioteca

    show julia
    
    e "Eu prefiro estudar"

    e "Sou uma capivara estudiosa"

    return

label malhar:

    scene academia

    show julia
    
    e "Acho que está na hora de ganhar uns musculos"

    e "Quero ficar no shape do verão"
    return

label podejogar:

    "Como você é de maior"

    "Você pode jogar o meu jogo"

    "Aproveite"

    if idade > 18:
        if porno == True:
            "assistir o filme adulto"
            "xuxa e os baixinhos"
        if direcao == True:
            "Levar o carro para a estrada"
        else:
            "Pegar um uber"
            "..."
    
    return

label no_pde_jogar:

    "Você é muito novo"

    "Volte quando for mais velhor"

    "... :("

    return