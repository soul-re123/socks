<<<<<<< HEAD

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
        
    
=======
quantity=0
def main():
    a = int(input("Enter your action (1-4): "))
    print(action(a))
def action(data):
    if data == 1:
        return add_remove(0, "add")
    elif data == 2:
        
        return add_remove(0, "remove")
    elif data == 3:
        # Display current order details here
        return display_order()
    elif data == 4:
        # Perform checkout operations here
        return checkout()
    else:
        return "No action executed"
def add_remove(qtn, action_type):
    if action_type == "add":
        global quantity
        qtn=int(input("Enter the quantity of socks to add: "))
        quantity += qtn
        if qtn > 0:
            main()
            return f"{qtn} socks added"
        else:
            return "No socks added"
    elif action_type == "remove":        
        qtn=int(input("Enter the quantity of socks to remove: "))
        quantity -= qtn
        if qtn > 0:
            main()
            return f"{qtn} socks removed"
            
        else:
            return "No socks removed"
    else:
        return "Invalid action type"
        
def display_order():
    global quantity
    base = quantity*9.75
    shipping = 2.25
    if quantity <= 5:
        shipping = 2.25
        total = base + shipping
        print(f"Total cost for {quantity} socks: ${total:.2f}")
        main()
    else:
        shipping = (shipping)+1.25*quantity
        total = base + shipping
        print(f"Total exceeds 5 socks, total cost: ${total:.2f}")
        main()
    return f"Current order: {quantity} socks, Total: ${total:.2f}"
    
def checkout():
    global quantity
    total = display_order()
    quantity = 0
    return f"Checkout complete. {total}"
main()
>>>>>>> dac0ca5097cdbb43b45fa60f8f9eb1f6fd81112c
