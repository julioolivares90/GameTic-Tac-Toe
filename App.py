from random import randrange


# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
def DisplayBoard(board):
    print(board[0]+" | "+ board[1] + " | "+board[2])
    print(board[3]+" | " + board[4] + " | "+board[5])
    print(board[6]+" | "+ board[7] + " | "+board[8])
    pass



# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
def EnterMove(board):
    position = input('Selecciona una posicion desde 1-9: ')
    
    position = int(position) - 1
    if position < 0:
        EnterMove(board=board)
        pass
    if position > 9:
        EnterMove(board=board)
        pass
    board[position] = user
    DisplayBoard(board=board)
    
    DrawMove(board=board)
    #MakelistOfFreeFields(board=board)
    pass



# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
def MakelistOfFreeFields(board):
    camposlibres = []
    for t in range(len(board)):
        if board[t]=="-":
            camposlibres.append(t)
            pass
    return camposlibres
    pass


# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
def VictoryFor(board):
    #horizontal user
    if board[0] == board[1] == board[2] == user : 
        print("gano usuario")
        pass
    if board[3] == board[4] == board[5] == user: 
        print("gano usuario")
        return
        pass
    if board[6] == board[7] == board[8] == user: 
        print("gano usuario")
        return
        pass
    #horizontal pc
    if board[0] == board[1] == board[2] == pc :
        print("gano pc!")
        return
        pass
    if board[3] == board[4] == board[5] == pc:
        print("gano pc!")
        return
        pass
    if board[6] == board[7] == board[8] == pc:
        print("gano pc!")
        return
        pass

    #diagonal pc
    if board[0] == board[4] == board[8] == pc:
        print("Gana pc!")
        pass
    if board[6] == board[4] == board[2] == pc:
        print("Gana pc!")
        pass
    #diagonal user
    if board[0] == board[4] == board[8] == user:
        print("Gana user!")
        pass
    if board[6] == board[4] == board[2] == user:
        print("Gana user!")
        pass
    #verticales user
    if board[0] == board[3] == board[6] == user : 
        print("gano usuario")
        return
        pass
    if board[1] == board[4] == board[7] == user: 
        print("gano usuario")
        return
        pass
    if board[2] == board[5] == board[8]== user: 
        print("gano usuario")
        return
        pass
    #verticales pc
    if board[0] == board[3] == board[6] == pc : 
        print("gano pc")
        return
        pass
    if board[1] == board[4] == board[7] == pc: 
        print("gano pc")
        return
        pass
    if board[2] == board[5] == board[8]== pc: 
        print("gano pc")
        return
        pass
    pass


# la función dibuja el movimiento de la maquina y actualiza el tablero
def DrawMove(board):
    print('turno de pc ')
    movimiento_pc = randrange(9)
    #si el movimiento_pc es 0 no se puede usar porque solo son validos del 1 al 9
    if movimiento_pc == 0 :
        movimiento_pc = randrange(9)
        #DrawMove(board=board)
        pass
    campos_usados = MakelistOfFreeFields(board);
    if campos_usados[0] == movimiento_pc or campos_usados[1] == movimiento_pc or campos_usados[2] == movimiento_pc:
        movimiento_pc = randrange(9)
        pass
    board[movimiento_pc] = pc
    DisplayBoard(board=board)
    #VictoryFor(board=board)
    pass


def Game():
    EnterMove(tablero)
    



tablero = [
    "-","-","-",
    "-","X","-",
    "-","-","-"
]


user = "O"
pc = "X"


if __name__ == "__main__":
    for l in range(3):
        Game()
        VictoryFor(board=tablero)
        pass
    #Game()
    pass