from datetime import datetime
import random   #import random function to use later in SDD option

item_code = []     #creating lists for item details
item_name = []
item_brand = []
item_price = []
item_quantity = []
item_category = []
purchased_date = []
DealersDict = {     #creating dictionary to save dealer details to display dealers' item details later in LDI option
  'KT Computers': '''Dealer Item Details
            ==================
Item-Name    Item-Brand     Item-Price      Item-Quantity
Monitor      Hp             65000           3
CPU          Dell           66000           2
Printer      Hp             45000           4''',
  'NetLanka Computers': '''Dealer Item Details
            ==================
Item-Name    Item-Brand     Item-Price      Item-Quantity
Monitor      Hp             45000           3
CPU          Samsung        80500           2
Printer      Hp             45000           4''',
  'Rsv Computers': '''Dealer Item Details
            ==================
Item-Name    Item-Brand     Item-Price      Item-Quantity
Monitor      Dell           55000           3
CPU          Hp             70000           2
Printer      Canon          52000           4''',
  'Redline technologies': '''Dealer Item Details
            ==================
Item-Name    Item-Brand     Item-Price      Item-Quantity
Monitor      Samsung        50500           3
CPU          Hp             70000           2
Printer      Dell           40000           4''',
  'Nano-Tech': '''Dealer Item Details
            ==================
Item-Name    Item-Brand     Item-Price      Item-Quantity
Monitor      Samsung        60500           3
CPU          Hp             70000           2
Printer      Dell           30000           4''',
  'ComNet Computers': '''Dealer Item Details
            ==================
Item-Name    Item-Brand     Item-Price      Item-Quantity
Monitor      Hp             60000           3
CPU          Hp             80000           2
Printer      Canon          30000           4'''
}
#creating two lists to display column names and gap in table view
titles = ['Item-Code','Item-Name','Item-Brand','Item-Price','Item-Quantity','Item-Category','Purchased-Date']
gap = ' '

f = open('Items table.txt', 'r+') #Open Items table function to read and update old saved data
def Readoldtext():
    '''Reading saved item '''
    global f,item_price,item_quantity   #making variables global
    Lines = f.readlines()   #read items table text file line by line
    temporary = []  
    for i in Lines:    #every element separated by a space in each line is appended to seperate lists
        temporary = i.split()  
        item_code.append(temporary[0])
        item_name.append((temporary[1]))
        item_brand.append((temporary[2]))
        item_price.append((temporary[3]))
        item_quantity.append((temporary[4]))
        item_category.append((temporary[5]))
        purchased_date.append((temporary[6]))

def contt():       #ask the user whether to continue or not
    go_on = input('Do you want to continue (YES/ESC) : ')
    go_on = go_on.upper()
    if go_on == 'YES':
        menu()
    elif go_on == 'ESC':
        exit()
    else:
        print('Invalid input')
        contt()

def menu():         #display main menu 
    global titles   #make variable global
    print('''            Menu

     Type AID for adding item details
     Type DID for deleting item details
     Type UID for updating item details
     Type VID for viewing the items table and print the current total
     Type SID for saving the item details to the text file
     Type SDD for selecting four dealers randomly from a file
     Type VRL for displaying all the details of the randomly selected dealers
     Type LDI for display the items of the given dealer
     Type ESC to exit the program
     ''')
    option = input('Enter the function you want to perform : ')
    Readoldtext()   #everytime read the old saved data in items table text file
    option = option.upper()   #user input is capitalized

    if option == 'AID':    #if user choose AID option
        code = input('Enter Item Code: ') 
        while code in item_code:           #check if item code already exist. 
            print('Item code already exist')
            code = input('Enter Item Code: ') #If item code exist ask for another code(item code must be unique)
        item_code.append(str(code))           #ask for other item details and append to respective list
        name = input('Enter Item Name: ')
        item_name.append(str(name))           #ask for other item details and append to respective list
        brand = input('Enter Item Brand: ')
        item_brand.append(str(brand))         #ask for other item details and append to respective list
        while True:            #check if price entered is an integer if not ask to input value again
            try:
                price =int(input('Enter price: '))
                break
            except:
                print('Invalid Input, please try again')
        item_price.append(str(price))         #ask for other item details and append to respective list         
        while True:           #check if quantity entered is an integer if not ask to input value again
            try:
                quantity = int(input('Enter Item Quantity: '))
                break
            except:    
                print('Invalid Input, please try again')
        item_quantity.append(str(quantity))    #ask for other item details and append to respective list
        category = input('Enter Category: ')
        item_category.append(str(category))    #ask for other item details and append to respective list
        date = input('Enter Purchased Date [DD-MM-YYYY] : ')
        purchased_date.append(str(date))       #ask for other item details and append to respective list
        contt()   #ask to continue or not

    elif option == 'DID':     #if user choose DID option
        delete = input('Enter item code to delete item details : ')  #ask which item to delete
        while delete not in item_code:     #check if item code already exist
            print('Item code does not exist')  #If item code does not exist ask for another code
            delete = input('Enter item code to delete item details : ')
        delete1 = item_code.index(delete)   #find the index of the entered item code in item_code list
        item_code.pop(delete1)    #delete the elements from other lists having the same index as entered item code
        item_name.pop(delete1)
        item_brand.pop(delete1)
        item_price.pop(delete1)
        item_quantity.pop(delete1)
        item_category.pop(delete1)
        purchased_date.pop(delete1)
        print('Item details deleted successfully')
        contt()    #ask to continue or not

    elif option == 'UID':     #if user choose UID option
        f = open('Items table.txt', 'r+')  #open items table text file to read and update
        update = (input('Enter item code to update item details : ')) #ask which item code to update
        while update not in item_code:    #check if item code already exist
            if update not in item_code:
                print('Item code not available')   #If item code does not exist ask for another code
                update = (input('Enter item code to update item details : '))
        update1 = item_code.index(update)     #find the index of the entered item code in item_code list
        new_code = (input('Enter New Item Code: ')) #update the elements from other lists having the same index as entered item code
        item_code[update1] = new_code
        new_name = input('Enter New Item name : ')
        item_name[update1] = new_name
        new_brand = input('Enter New Item brand : ')
        item_brand[update1] = new_brand
        while True:            #check if price entered is an integer if not ask to input value again
            try:
                new_price =int(input('Enter New price: '))
                break
            except:
                print('Invalid Input, please try again')
        item_price[update1] = str(new_price)
        while True:           #check if quantity entered is an integer if not ask to input value again
            try:
                new_quantity = int(input('Enter New Item Quantity: '))
                break
            except:    
                print('Invalid Input, please try again')
        item_quantity[update1] = str(new_quantity)
        new_category = input('Enter New Item Category: ')
        item_category[update1] = new_category
        new_purchased_date = input('Enter New Purchased Date [DD-MM-YYYY] : ')
        purchased_date[update1] = new_purchased_date
        print('Item details updated successfully')#these updates will show in VID but will get saved in text file only after SID option is selected
        contt()    #ask to continue or not

    elif option =='VID':     #if user choose VID option
        f = open('Items table.txt', 'a+')    #open items table text file
        Lines = f.readlines()       #read items table text file line by line
        count = 0
        for i in Lines:   #run for each line
            count += 1
            if count > 3:   #ignore first three lines in text file only want from first item code
                List = []
                List = i.split()          #each line split by spaces and divided to elements
                item_code.append(List[0])    #each element appended to respective list
                item_name.append(List[1])
                item_brand.append(List[2])
                item_price.append(List[3])
                item_quantity.append(List[4])
                item_category.append(List[5])
                purchased_date.append(List[6])
        l1 = []             #create a list to append all item codes 
        for i in range (1,len(item_code)):
            l1.append(int(item_code[i]))     #append all item codes as integers to 'l1' list
        li = []
        highestvalue = 0
        while len(l1) != 0:      
            for i in l1:     #find highest value from l1 then append to li and remove from l1 (repeat for all in l1)
                if i > highestvalue:
                    highestvalue = i
            li.append(highestvalue)
            l1.remove(highestvalue)
            highestvalue = 0
        #use formatted string to print column names and gaps assigned to 'titles' list and 'gap' list respectively. Replace with column names with 15 space for each column
        print(('{:15}{}{:15}{}{:15}{}{:15}{}{:15}{}{:15}{}{:15}'.format(titles[0], gap, titles[1], gap, titles[2], gap,titles[3], gap, titles[4], gap, titles[5], gap,titles[6])))
        for i in range(len(li)):   #for item code in 'li' list find its index 
            x = str(li[i])  
            findIndex = item_code.index(x)
            #Print with elements from other lists with same index
            print('{:15}{}{:15}{}{:15}{}{:15}{}{:15}{}{:15}{}{:15}'.format(item_code[findIndex], gap, item_name[findIndex], gap,item_brand[findIndex], gap, item_price[findIndex],
                                                                           gap,item_quantity[findIndex], gap, item_category[findIndex], gap,purchased_date[findIndex]))
        currenttotal = 0
        for i in range(1,len(item_quantity)): #for each quantity in 'item_quantity' list
            currenttotal += int(item_quantity[i]) * int(item_price[i]) #each quantity is multiplied with price with same index in other list and the sum is taken of all
        print('The current total of items : Rs',currenttotal)
        contt()    #ask to continue or not

    elif option == 'SID':    #if user choose SID option
        f = open('Items table.txt', 'w+')  #open items table text file 
        for i in range(len(item_code)):   #every item code is written into text file with all other elements in other lists with same indexes
            f.write('{:15}{}{:15}{}{:15}{}{:15}{}{:15}{}{:15}{}{:15}'.format(item_code[i], gap, item_name[i], gap,item_brand[i], gap, item_price[i], gap,item_quantity[i],
                                                                             gap, item_category[i],gap, purchased_date[i]))
            f.write('\n')
        f.close()    #close text file
        print('Item details saved successfully')
        contt()

    elif option == 'SDD':   #if user choose SDD option
        global txt1,txt2,txt3,txt4,pattern  #make variables global
        status = random.randint(0,1)   #generate a random number 1 or 0
        count = random.randint(0,1)
        if status == 0 and count == 0:   #if both 0 open (select) only these text files
            pattern  = 1                 #assign pattern =1 (do same for other patterns)
            txt1 = open('Dealer1','r+')
            txt2 = open('Dealer2', 'r+')
            txt3 = open('Dealer3', 'r+')
            txt4 = open('Dealer4', 'r+')
        elif status == 0 and count == 1:
            pattern = 2
            txt1 = open('Dealer3', 'r+')
            txt2 = open('Dealer4', 'r+')
            txt3 = open('Dealer5', 'r+')
            txt4 = open('Dealer6', 'r+')
        elif status == 1 and count == 1:
            pattern = 3
            txt1 = open('Dealer2', 'r+')
            txt2 = open('Dealer6', 'r+')
            txt3 = open('Dealer3', 'r+')
            txt4 = open('Dealer5', 'r+')
        else:
            pattern = 4
            txt1 = open('Dealer1', 'r+')
            txt2 = open('Dealer4', 'r+')
            txt3 = open('Dealer6', 'r+')
            txt4 = open('Dealer3', 'r+')
        print('4 Dealers are Selected Randomly')
        contt()   #ask to continue or not

    elif option == 'VRL':   #if user choose VRL option
        order = []   #create a list to store sorted locations
        locationlist = []  #create a list to store all locations
        count = 0
        for line in txt1:     #Select only location from all selected text files(ignore other details)
            count += 1
            if count == 3:
                thirdline = line
                location1 = thirdline[13:]   #(assign location to a variable)
        count = 0
        for line in txt2:
            count += 1
            if count == 3:
                thirdline = line
                location2 = thirdline[13:]
        count = 0
        for line in txt3:
            count += 1
            if count == 3:
                thirdline = line
                location3 = thirdline[13:]
        count = 0
        for line in txt4:
            count += 1
            if count == 3:
                thirdline = line
                location4 = thirdline[13:]
        locationlist = [location4, location3, location2, location1]  #append all locations to list
        x = [location4, location3, location2, location1]  #changed variable name for easy access
        order = []
        while x:
            min = x[0]
            for word in x:      #find the lowest word (acending order)
                if word < min:
                    min = word
            x.remove(min)          #Remove the lowest word from the list and append it to the 'order' list (repeat)
            order.append(min[:-1])  #remove space behind word
        print()
        if pattern == 1:         #if pattern is 1 open only these text files (repeat for all pattern)
            txt1 = open('Dealer1', 'r+')
            txt2 = open('Dealer2', 'r+')
            txt3 = open('Dealer3', 'r+')
            txt4 = open('Dealer4', 'r+')
            for i in order:  #for every element in 'order' list display only respective dealer name,contactno and location in 'order' list order (repeat)
                if i == locationlist[0][:-1]:    #if element in order list equals to element [0] of locationlist open dealer4 file and read 
                    txt4 = open('Dealer4', 'r+')
                    count = 0       
                    for i in txt4:
                        count += 1
                        if count < 4:   #display only upto line 3 (ignore item details) 
                            print(i)
                    print('..........................................................................')
                if i == locationlist[1][:-1]:    #elif element in order list equals to element [1] of locationlist open dealer3 file and read
                    txt3= open('Dealer3', 'r+')
                    count = 0
                    for i in txt3:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
                if i == locationlist[2][:-1]:
                    txt2 = open('Dealer2', 'r+')
                    count = 0
                    for i in txt2:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
                if i == locationlist[3][:-1]:
                    txt1 = open('Dealer1', 'r+')
                    count = 0
                    for i in txt1:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
        elif pattern == 2:       #if pattern is 2 open only these text files
            txt1 = open('Dealer3', 'r+')
            txt2 = open('Dealer4', 'r+')
            txt3 = open('Dealer5', 'r+')
            txt4 = open('Dealer6', 'r+')
            for i in order:        #for every element in 'order' list display only respective dealer name,contactno and location in 'order' list order (repeat)
                if i == locationlist[0][:-1]:   #if element in order list equals to element [0] of locationlist open dealer6 file and read
                    txt4 = open('Dealer6', 'r+')
                    count = 0
                    for i in txt4:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
                if i == locationlist[1][:-1]:
                    txt3 = open('Dealer5', 'r+')
                    count = 0
                    for i in txt3:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
                if i == locationlist[2][:-1]:
                    txt2 = open('Dealer4', 'r+')
                    count = 0
                    for i in txt2:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
                if i == locationlist[3][:-1]:
                    txt1 = open('Dealer3', 'r+')
                    count = 0
                    for i in txt1:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
        elif pattern == 3:
            txt1 = open('Dealer2', 'r+')
            txt2 = open('Dealer6', 'r+')
            txt3 = open('Dealer3', 'r+')
            txt4 = open('Dealer5', 'r+')
            for i in order:
                if i == locationlist[0][:-1]:
                    txt4 = open('Dealer5', 'r+')
                    count = 0
                    for i in txt4:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
                if i == locationlist[1][:-1]:
                    txt3 = open('Dealer3', 'r+')
                    count = 0
                    for i in txt3:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
                if i == locationlist[2][:-1]:
                    txt2 = open('Dealer6', 'r+')
                    count = 0
                    for i in txt2:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
                if i == locationlist[3][:-1]:
                    txt1 = open('Dealer2', 'r+')
                    count = 0
                    for i in txt1:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
        else:
            txt1 = open('Dealer1', 'r+')
            txt2 = open('Dealer4', 'r+')
            txt3 = open('Dealer6', 'r+')
            txt4 = open('Dealer3', 'r+')
            for i in order:
                if i == locationlist[0][:-1]:
                    txt4 = open('Dealer3', 'r+')
                    count = 0
                    for i in txt4:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
                if i == locationlist[1][:-1]:
                    txt3 = open('Dealer6', 'r+')
                    count = 0
                    for i in txt3:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
                if i == locationlist[2][:-1]:
                    txt2 = open('Dealer4', 'r+')
                    count = 0
                    for i in txt2:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
                if i == locationlist[3][:-1]:
                    txt1 = open('Dealer1', 'r+')
                    count = 0
                    for i in txt1:
                        count += 1
                        if count < 4:
                            print(i)
                    print('..........................................................................')
        contt()        #ask to continue or not

    elif option == 'LDI':     #if user choose SDD option
        if pattern == 1:     #if pattern is 1 open only these text files (repeat for all pattern values)
            DealerName = []   #create a list to append dealer names
            txt1 = open('Dealer1', 'r+')
            txt2 = open('Dealer2', 'r+')
            txt3 = open('Dealer3', 'r+')
            txt4 = open('Dealer4', 'r+')
            count = 0
            for i in txt1:     
                count+= 1
                if count < 2:   #display only upto line 1 (only delaer name. Ignore all other details) (repeat for all files)
                    print(i)
                    DealerName.append((i[14:-1]))  #append the letters from index 14 and ignore last space to 'DealerName' list
            count = 0
            for i in txt2:
                count += 1
                if count < 2:    #display only upto line 1 (only delaer name. Ignore all other details)
                    print(i)
                    DealerName.append((i[14:-1]))   #append the letters from index 14 and ignore last space to 'DealerName' list
            count = 0
            for i in txt3:
                count += 1
                if count < 2:
                    print(i)
                    DealerName.append((i[14:-1]))
            count = 0
            for i in txt4:
                count += 1
                if count < 2:
                    print(i)
                    DealerName.append((i[14:-1]))
        if pattern == 2:       #if pattern is 2 open only these text files
            DealerName = []    #create a list to append dealer names
            txt1 = open('Dealer3', 'r+')
            txt2 = open('Dealer4', 'r+')
            txt3 = open('Dealer5', 'r+')
            txt4 = open('Dealer6', 'r+')
            count = 0
            for i in txt1:
                count += 1
                if count < 2:   #display only upto line 1 (only delaer name. Ignore all other details)
                    print(i)
                    DealerName.append((i[14:-1]))   #append the letters from index 14 and ignore last space to 'DealerName' list
            count = 0
            for i in txt2:
                count += 1
                if count < 2:
                    print(i)
                    DealerName.append((i[14:-1]))
            count = 0
            for i in txt3:
                count += 1
                if count < 2:
                    print(i)
                    DealerName.append((i[14:-1]))
            count = 0
            for i in txt4:
                count += 1
                if count < 2:
                    print(i)
                    DealerName.append((i[14:-1]))
        if pattern == 3:
            DealerName = []
            txt1 = open('Dealer2', 'r+')
            txt2 = open('Dealer6', 'r+')
            txt3 = open('Dealer3', 'r+')
            txt4 = open('Dealer5', 'r+')
            count = 0
            for i in txt1:
                count += 1
                if count < 2:
                    print(i)
                    DealerName.append((i[14:-1]))
            count = 0
            for i in txt2:
                count += 1
                if count < 2:
                    print(i)
                    DealerName.append((i[14:-1]))
            count = 0
            for i in txt3:
                count += 1
                if count < 2:
                    print(i)
                    DealerName.append((i[14:-1]))
            count = 0
            for i in txt4:
                count += 1
                if count < 2:
                    print(i)
                    DealerName.append((i[14:-1]))
        if pattern == 4:
            DealerName = []
            txt1 = open('Dealer1', 'r+')
            txt2 = open('Dealer4', 'r+')
            txt3 = open('Dealer6', 'r+')
            txt4 = open('Dealer3', 'r+')
            count = 0
            for i in txt1:
                count += 1
                if count < 2:
                    print(i)
                    DealerName.append((i[14:-1]))
            count = 0
            for i in txt2:
                count += 1
                if count < 2:
                    print(i)
                    DealerName.append((i[14:-1]))
            count = 0
            for i in txt3:
                count += 1
                if count < 2:
                    print(i)
                    DealerName.append((i[14:-1]))
            count = 0
            for i in txt4:
                count += 1
                if count < 2:
                    print(i)
                    DealerName.append((i[14:-1]))

        choosendealer = input('Enter a Dealer name from the selected Dealer : ')  #ask user input for a dealer name
        while choosendealer not in DealerName:   #dealer name has to be from previously selected list
            print('Enter a Dealer in the selected list')
            choosendealer = input('Enter a Dealer name from the selected Dealers : ')
        print(DealersDict[choosendealer]) #find the user input dealer name in dictionary created at the top and display values
        contt()   #ask to continue or not
    
    elif option == 'ESC':   #if user choose ESC option
        exit()  #terminate program
        
    else:      #if user choose an invalid option
        print('Invalid Option. Please try again') #ask to choose another option
        
        contt()  #ask to continue or not

menu()  #call menu function
contt() #ask to continue or not

