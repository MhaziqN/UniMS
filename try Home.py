a=(input("Enter your name?"))
b=int(input("How old are you?"))
Price = 0
totalBook = 0

if b<18:
    print("You need to be above 18 to borrow books!")
    quit()
c=int(input("How many books have you borrowed already?"))
if c>3:
    print("You cannot borrow more than 3 books.")
    quit()
else:
    print("You can borrow more books if you need.")

d=input("Story Of Love cost, 10€")
if d.lower() == "yes":
    Price += 10
    totalBook +=1
else:
    pass

e=input("History of Estonia cost, 25€")
if e.lower() == 'yes':
    Price += 25
    totalBook +=1
else:
    pass

f=input("The war in Ukraine cost, 30€")
if f.lower() == 'yes' :
    Price += 30
    totalBook += 1
else:
    pass

print('...........................\n','Name :',a, '\nTotal Book :', str(totalBook),'\nPrice total :', str(Price) + "€")
