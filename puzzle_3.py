# Card Puzzle
''' You are given 5 cards from a  deck, and return one. Then, you give your four cards to your code in a 
optimal order; your code must guess the 5th card.'''

# Author : mahesh gaikwad
# www.concretesteelbond.com

# Preparing Card Deck
import os
from PIL import Image
import tkinter as tk
import time

num = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
c_type = ["C","D","H","S"]
all_cards = []
for t_each in c_type:
    for n_each in num:
        all_cards.append((t_each+n_each))
#print(all_cards)     
first_card = input("First card = ")
second_card = input("Second card = ")
third_card = input("Third card = ")
forth_card = input("Fourth card = ")
if all_cards.index(second_card) > all_cards.index(third_card):
    if all_cards.index(third_card)> all_cards.index(forth_card):
        ans = 6 #"LMS" 
    else:
        if all_cards.index(second_card)> all_cards.index(forth_card):
            ans = 5 #"LSM"
        else:
            ans = 3 #"MSL"      
else:
    if all_cards.index(third_card)> all_cards.index(forth_card):
        if all_cards.index(second_card)> all_cards.index(forth_card):
            ans = 4 #"MLS"
        else:
            ans = 2 #"SLM"
    else:
        ans = 1 #"SML"
#print(ans)
#print(ans)
ans1 = ans + (num.index(first_card[1::])) + 1
if ans1 > len(num):
    ans1 = - (len(num) - ans1)  - 1
    correct_card = first_card[0]+num[ans1]
else:
    correct_card = first_card[0]+num[ans1-1]
    
print("The Fifth card is ...... ",correct_card)   
#Img = Image.open("cards\\" + correct_card + ".png")
#Img.show()

four_card = [first_card,second_card,
             third_card,forth_card]
root = tk.Tk()
root.geometry("700x800")

image1 = tk.PhotoImage(file = "cards\\" + first_card + ".png")
image1 = image1.subsample(4,4)
tk.Label(root,image = image1).place(x = 100,y = 100)

image2 = tk.PhotoImage(file = "cards\\" + second_card + ".png")
image2 = image2.subsample(4,4)
tk.Label(root,image = image2).place(x = 130,y = 100)

image3 = tk.PhotoImage(file = "cards\\" + third_card + ".png")
image3 = image3.subsample(4,4)
tk.Label(root,image = image3).place(x = 160,y = 100)

image4 = tk.PhotoImage(file = "cards\\" + forth_card + ".png")
image4 = image4.subsample(4,4)
tk.Label(root,image = image4).place(x = 190,y = 100)

image = tk.PhotoImage(file = "cards\\" + correct_card + ".png")
image = image.subsample(3,3)
label = tk.Label(root,image = image)
label.place(x = 400,y = 100)
root.mainloop()







