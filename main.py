import time

import Solver
import tkinter
import time

def afficher(n1):
    if n1.etat[0][0] == 0:
        case1_1 = tkinter.Label(takin_frame, text="", font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case1_1.grid(row=1, column=1)
    else:
        case1_1 = tkinter.Label(takin_frame, text=n1.etat[0][0], font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case1_1.grid(row=1, column=1)

    if n1.etat[0][1] == 0:
        case1_2 = tkinter.Label(takin_frame, text="", font=("Arial", 40), borderwidth=3, relief="solid", width=4,
                                height=2, background="white")
        case1_2.grid(row=1, column=2)
    else:
        case1_2 = tkinter.Label(takin_frame, text=n1.etat[0][1], font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4,
                                height=2, background="white")
        case1_2.grid(row=1, column=2)

    if n1.etat[0][2] == 0:
        case1_3 = tkinter.Label(takin_frame, text="", font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case1_3.grid(row=1, column=3)
    else:
        case1_3 = tkinter.Label(takin_frame, text=n1.etat[0][2], font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case1_3.grid(row=1, column=3)

    if n1.etat[1][0] == 0:
        case2_1 = tkinter.Label(takin_frame, text="", font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case2_1.grid(row=2, column=1)
    else:
        case2_1 = tkinter.Label(takin_frame, text=n1.etat[1][0], font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case2_1.grid(row=2, column=1)

    if n1.etat[1][1] == 0:
        case2_2 = tkinter.Label(takin_frame, text="", font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case2_2.grid(row=2, column=2)
    else:
        case2_2 = tkinter.Label(takin_frame, text=n1.etat[1][1], font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case2_2.grid(row=2, column=2)

    if n1.etat[1][2] == 0:
        case2_3 = tkinter.Label(takin_frame, text="", font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case2_3.grid(row=2, column=3)
    else:
        case2_3 = tkinter.Label(takin_frame, text=n1.etat[1][2], font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case2_3.grid(row=2, column=3)

    if n1.etat[2][0] == 0:
        case3_1 = tkinter.Label(takin_frame, text="", font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case3_1.grid(row=3, column=1)
    else:
        case3_1 = tkinter.Label(takin_frame, text=n1.etat[2][0], font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case3_1.grid(row=3, column=1)

    if n1.etat[2][1] == 0:
        case3_2 = tkinter.Label(takin_frame, text="", font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case3_2.grid(row=3, column=2)
    else:
        case3_2 = tkinter.Label(takin_frame, text=n1.etat[2][1], font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case3_2.grid(row=3, column=2)

    if n1.etat[2][2] == 0:
        case3_3 = tkinter.Label(takin_frame, text="", font=("Arial", 40), borderwidth=3, relief="solid", width=4,
                                height=2, background="white")
        case3_3.grid(row=3, column=3)
    else:
        case3_3 = tkinter.Label(takin_frame, text=n1.etat[2][2], font=("Arial", 40), borderwidth=3, relief="solid",
                                width=4, height=2, background="white")
        case3_3.grid(row=3, column=3)

def melanger_takin(*args):
    n1.melanger()
    n1.afficher_noeud()
    afficher(n1)



def recherche_largeur(*args):
    l = n1.recherche_en_largeur()
    for val in l:
        afficher(val)
        val.afficher_noeud()
        app.update()
        time.sleep(2)


def recherche_profondeur(*args):
    l = n1.recherche_en_profondeur()
    for val in l:
        afficher(val)
        val.afficher_noeud()
        app.update()
        time.sleep(2)


def reset(*args):
    afficher(n1)




etat = [
        [1, 2, 3],
        [8, 6, 0],
        [7, 5, 4]
    ]
n1 = Solver.Noeud(etat)




app = tkinter.Tk("Jeu de Takin")

screen_x = int(app.winfo_screenwidth())
screen_y = int(app.winfo_screenheight())
window_x = 800
window_y = 600
pos_x = (screen_x // 2) - (window_x // 2)
pos_y = (screen_y // 2) - (window_y // 2)
geo = "{}x{}+{}+{}".format(window_x, window_y,pos_x,pos_y)
app.geometry(geo)



titre_frame = tkinter.Frame(app,background="white")
titre_frame.pack(fill="x")

titre = tkinter.Label(titre_frame,text="JEU DE TAKIN",background="white",font=("Arial", 20))
titre.pack()

takin_frame = tkinter.Frame(app,background="white")
takin_frame.pack(pady=20)
case1_1 = tkinter.Label(takin_frame,text=n1.etat[0][0],font=("Arial", 40),borderwidth=3,relief="solid",width=4,height=2,background="white")
case1_1.grid(row=1,column=1)
case1_2 = tkinter.Label(takin_frame,text=n1.etat[0][1],font=("Arial", 40),borderwidth=3,relief="solid",width=4,height=2,background="white")
case1_2.grid(row=1,column=2)
case1_3 = tkinter.Label(takin_frame,text=n1.etat[0][2],font=("Arial", 40),borderwidth=3,relief="solid",width=4,height=2,background="white")
case1_3.grid(row=1,column=3)
case2_1 = tkinter.Label(takin_frame,text=n1.etat[1][0],font=("Arial", 40),borderwidth=3,relief="solid",width=4,height=2,background="white")
case2_1.grid(row=2,column=1)
case2_2 = tkinter.Label(takin_frame,text=n1.etat[1][1],font=("Arial", 40),borderwidth=3,relief="solid",width=4,height=2,background="white")
case2_2.grid(row=2,column=2)
case2_3 = tkinter.Label(takin_frame,text="",font=("Arial", 40),borderwidth=3,relief="solid",width=4,height=2,background="white")
case2_3.grid(row=2,column=3)
case3_1 = tkinter.Label(takin_frame,text=n1.etat[2][0],font=("Arial", 40),borderwidth=3,relief="solid",width=4,height=2,background="white")
case3_1.grid(row=3,column=1)
case3_2 = tkinter.Label(takin_frame,text=n1.etat[2][1],font=("Arial", 40),borderwidth=3,relief="solid",width=4,height=2,background="white")
case3_2.grid(row=3,column=2)
case3_3 = tkinter.Label(takin_frame,text=n1.etat[2][2],font=("Arial", 40),borderwidth=3,relief="solid",width=4,height=2,background="white")
case3_3.grid(row=3,column=3)


buttons_frame = tkinter.Frame(app)
buttons_frame.pack()

melanger_button = tkinter.Button(buttons_frame,text="reset",height=2,command=reset)
melanger_button.grid(row=1,column=1,padx=20)

largeur_button = tkinter.Button(buttons_frame,text="recherche en largeur",height=2,command=recherche_largeur)
largeur_button.grid(row=1,column=2,padx=20)
profondeur_button = tkinter.Button(buttons_frame,text="recherche en profondeur",height=2,command=recherche_profondeur)
profondeur_button.grid(row=1,column=3,padx=20)

"""
a_button = tkinter.Button(buttons_frame,text="recherche en A*",height=2)
a_button.grid(row=1,column=4,padx=20)
"""
app.mainloop()

