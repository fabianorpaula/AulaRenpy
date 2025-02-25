# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Julia", color="#153dc6")
define m = Character("Marcos Pato", color="#e109ff")

# The game starts here.

label start:

    play music "audio/Fundo.mp3"

    scene biblioteca

    "Julia Aparece na historia"

    "Julia é uma linda e inteligente capivara"

    

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