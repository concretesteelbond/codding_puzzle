# Card Puzzle
''' You are given 5 cards from a  deck, and return one. Then, you give your four cards to your code in a 
optimal order; your code must guess the 5th card.'''

# Author : mahesh gaikwad
# www.concretesteelbond.com

# Preparing Card Deck
num = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
c_type = ["C","D","H","S"]
all_cards = []
for t_each in c_type:
    for n_each in num:
        all_cards.append((t_each,n_each))
#print(all_cards)   
####
first_card = eval(input())
second_card = eval(input())
third_card = eval(input())
forth_card =  eval(input())
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
print(ans)
ans1 = ans + (num.index(first_card[1])) + 1
if ans1 > len(num):
    ans1 = - (len(num) - ans1)  - 1
    print(first_card[0], num[ans1])
else:
   print(first_card[0], num[ans1-1]) 


    
