
'''If 1 Horse = Rs. 1, 1 Elephant = Rs. 5, 20 Camels = Rs. 1/- then Find 
the combination of animals so that 100 animals = 100 rs '''

## Given Data
horse = 1 #$
elephant = 5 #$
camel = 1/20 #$
## OutPut should be
total_animal = 100
total_money = 100

x = list(range(1,97))
y = list(range(1,97))
z = list(range(1,97))
for x1 in x:
    for y1 in y:
        for z1 in z:
            if  (x1*horse + y1*elephant + z1*camel == total_money
                 and x1+y1+z1 == total_animal):
                print("Horse = "+str(x1) ,
                      "Elephant = "+str(y1),
                      "Camel = " +str(z1))
                
                
        
                
