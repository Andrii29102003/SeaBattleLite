import tkinter as tk
import random


class GAME:
    def gameEnd(self, who):
        tk.Button(text=f'{who} WINN!', command=lambda: exit(0)).grid(row=0, column=0, columnspan=5)
        window.mainloop()

    def onClick(self, trow, tcolumn):
        if compshipes[trow - 4][tcolumn - 1] == ' ': compshipes[trow - 4][tcolumn - 1] = 'O'
        if compshipes[trow - 4][tcolumn - 1] == 'x': compshipes[trow - 4][tcolumn - 1] = 'X'
        compshipesbut[trow-4][tcolumn-1]['text'] = compshipes[trow-4][tcolumn-1]
        compshipesbut[trow - 4][tcolumn - 1]['state'] = "disabled"
        global compscore
        if compshipes[trow-4][tcolumn-1]=='X' :compscore+=1
        if compscore >= 5 : Game.gameEnd('PLAYER')
        Game.compTurn()

    def compTurn(self):
        while True:
            xrow = random.randint(0, 4)
            xcolumn = random.randint(0, 4)
            global playerscore
            if playershipes[xrow][xcolumn] != 'O' and playershipes[xrow][xcolumn] != 'X':
                if playershipes[xrow][xcolumn] == ' ':playershipes[xrow][xcolumn] = 'O'
                if playershipes[xrow][xcolumn] == 'x':playershipes[xrow][xcolumn] = 'X'
                playershipesbut[xrow][xcolumn]['text'] = playershipes[xrow][xcolumn]
                if playershipes[xrow][xcolumn] == 'X':
                    playerscore+=1
                    if playerscore >= 5: Game.gameEnd('COMP')
                return


Game = GAME()
compshipes = [[' '] * 5 for i in range(5)]
playershipes = [[' '] * 5 for i in range(5)]
compshipesbut = [[0] * 5 for i in range(5)]
playershipesbut = [[0] * 5 for i in range(5)]
ltrs = 'ABCDE'
compscore = 0
playerscore = 0


for i in range(5):
    while True:
        xrow=random.randint(0,4)
        xcolumn=random.randint(0,4)
        if compshipes[xrow][xcolumn] == ' ' :
            compshipes[xrow][xcolumn]='x'
            break

for i in range(5):
    while True:
        xrow=random.randint(0,4)
        xcolumn=random.randint(0,4)
        if playershipes[xrow][xcolumn] == ' ' :
            playershipes[xrow][xcolumn]='x'
            break


window = tk.Tk()
tk.Label(text="ПОЧАТОК ГРИ").grid(row=0, column=0, columnspan=5)
tk.Label(text="МОРСЬКИЙ БІЙ").grid(row=1, column=0, columnspan=5)


tk.Label(text="ПОЛЕ КОМП'ЮТЕРА").grid(row=2, column=0, columnspan=5)
for column in range(1, 6):
    tk.Label(text=column, width=2, height=1, ).grid(row=3, column=column)
for row in range(4, 9):
    tk.Label(text=ltrs[row-4]).grid(row=row, column=0)
    for column in range(1, 6):
        compshipesbut[row-4][column-1] = tk.Button(window, text=" ", width=2, height=1, command=lambda trow=row, tcolumn=column:Game.onClick(trow,tcolumn))
        compshipesbut[row - 4][column - 1].grid(row=row, column=column)




tk.Label(text="ПОЛЕ ГРАВЦЯ").grid(row=9, column=0, columnspan=5)
for column in range(1, 6):
    tk.Label(text=column, width=2, height=1, ).grid(row=10, column=column)
for row in range(11, 16):
    tk.Label(text=ltrs[row-11]).grid(row=row, column=0)
    for column in range(1, 6):
        playershipesbut[row-11][column-1] = tk.Button(text=" ", width=2, height=1, state="disabled")
        playershipesbut[row-11][column-1].grid(row=row, column=column)

window.mainloop()
