class Order:
    def __init__(self, order, order_num):
        self.order = order
        self.order_num = order_num

class Employee:
    def __init__(self, name):
        self.name = name

class Chef(Employee):

    def __init__(self, name):
        super().__init__(name)

class Server(Employee):
    def __init__(self, name, pay, tablelist=[]):
        super().__init__(name, pay)
        self.tablelist = tablelist

    def add_table(self, table_num):
        self.table_num = table_num
        self.tablelist.append(table_num)

    def tables(self):
        return self.tablelist

class Customer:
    def __init__(self, name):
        self.name = name

class PizzaShop:

    current_order_num = 0
    orders = []

    def __init__(self, order, customer):
        PizzaShop.current_order_num += 1
        PizzaShop.orders.append(PizzaShop.current_order_num)
        self.order = Order(order, PizzaShop.orders[-1])
        self.customer = customer
        self.chef = Chef('kev').name
    

    def ticket(self):
        ticket = f'{self.order} for {self.customer} - prepared by {self.chef}'
        return ticket

    def assign_server(self):
        

 
if __name__ == '__main__':

    one = PizzaShop('mushroom', 'bill')
    two = PizzaShop('pepperoni', 'mary')
    three = PizzaShop('pepperoni', 'calvin')

    print(three.order.order_num)