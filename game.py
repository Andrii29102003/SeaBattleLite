import tkinter as tk
import random


class Ship():
    def __init__(self, len, poz, direction):
        self.len=len
        self.poz=poz
        self.direction=direction
        self.ship_point_mas=[1 for i in range(len)]
    
    def on_click(self,poz):
        self.ship_point_mas[poz]=0


class Memo():
    ltrs = 'ABCDE'
    def __init__(self,h,w,player,row_zsuw):
        self.score=0
        self.h=h
        self.w=w
        self.player=player
        self.row_zsuw=row_zsuw
        self.fild_mas=[[' '] * w for i in range(h)]
        self.fild_but_mas=[[' '] * w for i in range(h)]
        self.ships=list()
        self.render()

    def on_click(self, trow, tcolumn):
        if self.fild_mas[trow - 4-self.row_zsuw][tcolumn - 1] == ' ': self.fild_mas[trow - 4-self.row_zsuw][tcolumn - 1] = 'O'
        if self.fild_mas[trow - 4-self.row_zsuw][tcolumn - 1] == 'x': self.fild_mas[trow - 4-self.row_zsuw][tcolumn - 1] = 'X'
        self.fild_but_mas[trow-4-self.row_zsuw][tcolumn-1]['text'] = self.fild_mas[trow-4-self.row_zsuw][tcolumn-1]
        self.fild_but_mas[trow - 4-self.row_zsuw][tcolumn - 1]['state'] = "disabled"
        if self.fild_mas[trow-4-self.row_zsuw][tcolumn-1]=='X' :self.score+=1
        if self.score >= self.numder_of_ships : board.game_end(self.player)

    def render(self):
        #max_len=(self.h+self.w)//1-1
        self.numder_of_ships=(self.h+self.w)//2
        for i in range(self.numder_of_ships):
            while True:
                xrow=random.randint(0,self.h-1)
                xcolumn=random.randint(0,self.w-1)
                if self.fild_mas[xrow][xcolumn] == ' ' :
                    self.fild_mas[xrow][xcolumn]='x'
                    self.ships.append(Ship(1,(xrow,xcolumn),1))
                    break
        
        tk.Label(text=f"ПОЛЕ ГРАВЦЯ {self.player}").grid(row=2+self.row_zsuw, column=0, columnspan=5)
        for column in range(1, self.w+1):
            tk.Label(text=column, width=2, height=1, ).grid(row=3+self.row_zsuw, column=column) 
        for row in range(4+self.row_zsuw, 9+self.row_zsuw):
            tk.Label(text=self.ltrs[row-4-self.row_zsuw]).grid(row=row, column=0)
            for column in range(1, 6):
                self.fild_but_mas[row-4-self.row_zsuw][column-1] = tk.Button(Board.window, text=" ", width=2, height=1, command=lambda trow=row, tcolumn=column:self.on_click(trow,tcolumn))
                self.fild_but_mas[row-4-self.row_zsuw][column-1].grid(row=row, column=column)   
        

class Board():
    window=None
    def __init__(self):
        self.window = tk.Tk()
        self.render()

    def render(self):
        tk.Label(text="ПОЧАТОК ГРИ").grid(row=0, column=0, columnspan=5)
        tk.Label(text="МОРСЬКИЙ БІЙ").grid(row=1, column=0, columnspan=5)
        self.row_zsuw=0
        self.memo1=Memo(5,5,"PLAYER1",0)
        self.row_zsuw=7
        self.memo2=Memo(5,5,"PLAYER2",7)

    def game_end(self,player):
        tk.Button(text=f'{player} WINN!', command=lambda: exit(0)).grid(row=0, column=0, columnspan=5)
        self.window.mainloop()


#MAIN
try:
  board=Board()
except:
  print("ERROR")
  exit(0)  
board.window.mainloop()