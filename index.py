
total = 0

def menu():
    print("1. Add Socks to order \n2. Remove Socks from order \n 3. View Current Order \n4. Checkout")
    number = input("Please enter your choice")
    return number

def subtract():
    global total
   
    
    while True:
        userInput = input("How many pairs would you like to remove? (type quit to exit)")
        print(userInput)
        if userInput.lower() == "quit":
            break
        if userInput.isdigit():
            socks = int(userInput)
            total = total - socks
    return total

def add():
    global total
    
       
    while True:
           userInput = input("How many pairs would you like to add? (type quit to exit)")
           print(userInput)
           if userInput.lower() == "quit":
               break
           if userInput.isdigit():
               socks = int(userInput)
               total = total + socks
    return total
    




while True:
    num =  menu()
    
    if num == "1":
        print(add())
        
    elif num == "2":
        print(subtract())
        
    