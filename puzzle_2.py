# Programming for the puzzle
# The Best time to party 



''' There is a party to celebrate celebrities that you get to attend because you won a ticket at
your office lottery. Because of the high demand for tickets you only get to stay for one
hour but you get to pick which one since you received a special ticket. You have access
to a schedule that lists when exactly each celebrity is going to attend the party. You want
to get as many pictures with celebrities as possible to improve your social standing. This
means you wish to go for the hour when you get to hob-nob with the maximum number of
celebrities and get selfies with each of them.'''

# This question was taken from book and videos of Dr. Srini Devdas
# video link : https:// youtu.be/a1RalqkdG0c

# www.concretesteelbond.com


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

        
