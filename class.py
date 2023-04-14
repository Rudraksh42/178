from tkinter import *
from PIL import  ImageTk,Image
from tkinter import ttk
root = Tk()
root.geometry("700x700")
root.config(bg ="orange")


heading = Label(root , text = "Juice Center")
heading.place(relx = 0.5, rely=0.1 , anchor = W)


fruit_head = Label(root , text = "Select the Fruit:-")
fruit_head.place(relx = 0.7, rely=0.3 , anchor = E)

fruit_names = ["Apple" ,"Orange" , "Mango"]
fruit_dropdown = ttk.Combobox(root , state = "readonly", values = fruit_names, justify = "right")
fruit_dropdown.place(relx = 0.93, rely=0.3 , anchor = E)

quantity_j = Label(root , text = "Type the Quantity:-")
quantity_j.place(relx = 0.7, rely=0.4 , anchor = E)

Quantity = Entry(root)
Quantity.place(relx = 0.93, rely=0.4 , anchor = E)


calorie_j = Label(root , text = "")
calorie_j.place(relx = 0.5, rely=0.7 , anchor = CENTER)

total_amt = Label(root , text = "")
total_amt.place(relx = 0.5, rely=0.8 , anchor = CENTER)


juice = ImageTk.PhotoImage(Image.open("logo.png"))
juice_img = Label(root , image = juice , bg = "orange")
juice_img.place(relx = 0.2 , rely = 0.4 , anchor = CENTER)

apple = ImageTk.PhotoImage(Image.open("apple_img.png"))

mango = ImageTk.PhotoImage(Image.open("mango_img.png"))

orange = ImageTk.PhotoImage(Image.open("orange.png"))

fruit_IMG_label = Label(root , bg = "orange")
fruit_IMG_label.place(relx = 0.4, rely=0.7 , anchor = CENTER)




class Juice():
    def __init__(self , fruit_name , quantity):
        self.fruit = fruit_name
        self.quantity = int(quantity)
        self.__cost = 200
        
    def __calculate_cost(self):
        total_cost = self.quantity * self.__cost
        total_amt["text"] = "You Have To Pay " + str(total_cost) + " Rupees"
        if(self.fruit == "Apple"):
            fruit_IMG_label["image"]= apple
            calorie = self.quantity * 55
        elif(self.fruit == "Orange"):
            fruit_IMG_label["image"]= orange
            calorie = self.quantity * 60
        elif(self.fruit == "Mango"):
            fruit_IMG_label["image"]= mango
            calorie = self.quantity * 61
        calorie_j["text"] = "Calorie = " + str(calorie)
            
    def getprice(self):
        self.__calculate_cost()
        
    
def order_juice():
    fruit = fruit_dropdown.get()
    quantity = Quantity.get()
    
    obj = Juice(fruit,quantity)
    obj.getprice()
    
btn =Button(root , text = "Order juice" , command = order_juice)
btn.place(relx=0.5,rely= 0.6 , anchor = CENTER)
    
root.mainloop()