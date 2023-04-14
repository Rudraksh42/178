from tkinter import*
import random
root = Tk()
root.geometry("500x500")


label = Label(root , text="")
label.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)


class random_color():
    def __init__(self):
        self.__score = 0
    def update_game(self):
        self.text = ["skyblue" , "linen" , "cyan" , "orange" , "red" , "yellow" , "pink" , 'black']
        self.random_text_no =random.randint(0,7) 
        self.color = ["skyblue" , "linen" , "cyan" , "orange" , "red" , "yellow" , "pink" , 'black']
        self.random_color_no =random.randint(0,7) 
        label["text"] = self.text[self.random_text_no]
        label["fg"] = self.color[self.random_color_no]
        
    
button = Button(root)

root.mainloop()