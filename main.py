# Faris AlTamimi, Saif Faidallah, Sameer Dawood, Samuel Oladiran

import pizza_main as tp


class main:
    __slots__ = ["_pizza1toppings", "_pizza2toppings", "_pizza2price", "_pizza2price"]

    def __init__(self):
        """a constructor to init the variables"""
        self._pizza1toppings = []
        self._pizza2toppings = []
        self._pizza2price = 5
        self._pizza2price = 5

    def getpizza1order(self):
        """Get toppings for the first pizza"""
        usertoppings = tp.Toppings()
        print("Welcome to Pizza Shelter, all orders include two pizzas")
        print("what do you want for your first pizza?")
        cheeseType = 'O'
        while cheeseType in ['O', 'o', '0']:
            print(usertoppings.get_topping_option_print_line('cheese'))
            cheeseType = input("Choose one type of cheese (O for options): ")
            for cheeseoption in cheeseType.split():
                if cheeseoption not in ['O', 'o', '0']:
                    name, price = usertoppings.get_cheese_topping_name_price(cheeseoption)
                    self._pizza1toppings.append([name, price])

        meatType = 'O'
        while meatType in ['O', 'o', '0']:
            print(usertoppings.get_topping_option_print_line('cheese'))
            meatType = input("Choose one type of meat (O for options): ")
            for meatoption in meatType.split():
                if meatoption not in ['O', 'o', '0']:
                    name, price = usertoppings.get_meat_topping_name_price(meatoption)
                    self._pizza1toppings.append([name, price])

        vegType = 'O'
        while vegType in ['O', 'o', '0']:
            print(usertoppings.get_topping_option_print_line('cheese'))
            vegType = input("Choose one type of meat (O for options): ")
            for vegoption in vegType.split():
                if vegoption not in ['O', 'o', '0']:
                    name, price = usertoppings.get_veg_topping_name_price(vegoption)
                    self._pizza1toppings.append([name, price])

    def getpizza2order(self):
        """Get toppings for the first pizza"""
        usertoppings = tp.Toppings()
        print("Welcome to Pizza Shelter, all orders include two pizzas")
        print("what do you want for your first pizza?")
        cheeseType = 'O'
        while cheeseType in ['O', 'o', '0']:
            print(usertoppings.get_topping_option_print_line('cheese'))
            cheeseType = input("Choose one type of cheese (O for options): ")
            for cheeseoption in cheeseType.split():
                if cheeseoption not in ['O', 'o', '0']:
                    name, price = usertoppings.get_cheese_topping_name_price(cheeseoption)
                    self._pizza2toppings.append([name, price])

        meatType = 'O'
        while meatType in ['O', 'o', '0']:
            print(usertoppings.get_topping_option_print_line('cheese'))
            meatType = input("Choose one type of meat (O for options): ")
            for meatoption in meatType.split():
                if meatoption not in ['O', 'o', '0']:
                    name, price = usertoppings.get_meat_topping_name_price(meatoption)
                    self._pizza2toppings.append([name, price])

        vegType = 'O'
        while vegType in ['O', 'o', '0']:
            print(usertoppings.get_topping_option_print_line('cheese'))
            vegType = input("Choose one type of meat (O for options): ")
            for vegoption in vegType.split():
                if vegoption not in ['O', 'o', '0']:
                    name, price = usertoppings.get_veg_topping_name_price(vegoption)
                    self._pizza2toppings.append([name, price])