#While and For Loop
#Concepts of "DRY" -> Don't Repeat yourself

i = 1 #intialize num
while(i<=20):
    if(i%2==0):  #Condition for even num
        print(i, end=", ")   #", " means it gave in comma sep value

    i = i+1 #updatation

print("\n-----------------------------------")

#for Loop example

for ele in range(1,10):  #not taking last value
    print(ele, end=", ")

else:  #You want to step back from loop u have to use else
    print()
    print("No elements left")

print("\n-----------------------------------")

num = 9 #table of 9th
for i in range(1,11):   
    print("{} * {} = {}".format(num, i, num*1))


