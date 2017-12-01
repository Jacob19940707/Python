restart ='Y'
while restart not in ('N', 'n', 'NO', 'no'):
    print ("Making A Cup Of Tea")
    num_orders = int(input("How many for Tea? "))
    print ("there are", num_orders, "People for tea")
    
    #This array stores the data of each person
    orders = []
    for i in range(num_orders):
        b = input ("Person %i, Would you like Sugar? YES/NO " % (i + 1))
        sugar = None
        if b in ("YES", "Y", "y", "yes", "Yes"):
            sugar = input("How many sugars? ")
        else:
            print ("Okay No sugar")
        
        milk = input("How Much Milk Would You Like? SMALL/MEDIUM/LARGE ")
        if milk in ("S", "s", "sm", "Sm", "SMALL"):
            print ("Ok you want a Small amount of cream")

        elif milk in ("m", "M", "MEDIUM"):
            print ("Ok you want a Medium amount of cream")

        elif milk in ("l","L", "LARGE"):
            print ("Ok you want a Large amount of cream")

        #\n tells the program to skip a line and start the next line of output two lines dowm
        print ("Order is being processed, next order:\n")

        #this line appends the sugar and milk variables into the array output
        orders.append({'sugar': sugar, 'milk': milk })

    print('The orders has been processed with these data:')
    for i in range(num_orders):
        order = orders[i]
        #WHAT DOES the %i DOOOOOOO????
        print (' - Person', i + 1, 'wants tea', ('with %i' % int(order['sugar']) if     
        order['sugar'] else 'without'), 'sugar and', order['milk'], 'milk') 
    print('')
    restart = input('Would you like to Re-Order? Y/N')
    if restart in ('n', 'N'):
        print('')
        print ('Okay, Thank You, Enjoy Your Tea')
