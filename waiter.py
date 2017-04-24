from menu import Menu

class Waiter:
    def __init__(self, menu):
        menu = Menu()
        self.menu = menu
    
    def greet_guest(self):
        print('yo mate, welcome to pizzahuttos')
        
    def serve_guest(self):
        print("How can I be of service?")
        print("1. Would you like to order a pizza?")
        print("2. Would you like to leave?")
        
        choice = input()
        
        self.take_order(order_number=int(choice))
        
    def take_order(self, order_number):
        if order_number == 1:
            print("Let me get the menu")
        elif order_number == 2:
            print("Thank you for your visit!")
        else:
            print("I really don't understand")
            
    def list_menu(self):
        for dish in self.menu.contents():
            print(dish)
            
    def take_order(self, order_number):
        if order_number == 1:
            answer = "Let me get the menu"
            self.list_menu()
