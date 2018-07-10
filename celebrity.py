# Programming for the puzzle
# The Best time to party 

sched =[(6,7),(7,9),(10,11),(10,12),(8,10),(9,11),(6,8)] # Celebrity Timing
list2 = [] #empty list to get max count
for each in sched:
    for a in range(each[0],each[1]):
        list2.append(a+0.5)

#print(list2)
ans = max(list2,key=list2.count)
print(ans)  

print("The Best Time to Party: "+
      str(ans - 0.5) + "-" + str(ans + 0.5))

        
