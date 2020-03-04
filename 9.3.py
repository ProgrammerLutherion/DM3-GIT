dict1={1:"74747474J",2:"95959595H"}
dict2={"74747474J":"Pedro Perez","95959595H":"Unai Peña"}
choose=None
while choose != 0:
    print("1. Add new entries to the dictionaries")
    print("2. Enter a number and show the DNI for that student")
    print("3. Enter a DNI and show the name and surname for that student")
    print("4. Enter a number and show the name and surname for that student")
    print("5. Change the name and surname of a student")
    print("0. Exit the program")
    print()
    choose=int(input("What do you want to do next?: "))
    if choose==0:
        print("Thanks for using my program, see you next time!")
    elif choose==1:
        newID=input("Enter the new DNI: ")
        dict1.update({len(dict1)+1:newID})
        newSN=input("Enter the name and surname: ")
        dict2.update({dict1[len(dict1)]:newSN})
        #dict2.update({newID:newSN})
        print(dict1)
        print(dict2)
        print()
    elif choose==2:
        number=int(input("Input the number: "))
        data=dict1.get(number,"There's no number "+str(number))
        print(data)
    elif choose==3:
        print("The DNI's are: ",{*dict1.values()})
        ID=input("Insert the DNI of the student you are looking for: ").upper()
        data=dict2.get(ID,"There's no "+ID+" DNI")
        print(data)
    elif choose==4:
        print("This are the numbers: ",{*dict1})
        number=int(input("Input the number: "))
        data = dict1.get(number, "There's no number " + str(number))
        name = dict2.get(data)
        print(name)
    elif choose == 5:
        print(dict1)
        print(dict2)
        number=int(input("Input the number: "))
        data = dict1.get(number, "There's no number " + str(number))
        change= input("Change the name and surname: ")
        dict2[data]=change
    print()
