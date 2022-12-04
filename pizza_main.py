# Faris AlTamimi, Saif Faidallah, Sameer Dawood, Samuel Oladiran

class Toppings:
    """ toppings class will contain cheese, veggies and meat in a Dictionary
    with the prices they have"""
    cheesetoppingsDict = {'s': ['Shredded Cheese', 0.0], 'c': ['cheddar', 0.5], 'f': ['fresh mozzarella', 1.0]}
    vegtoppingsDict = {'m': ['Mushrooms', 1.0], 'b': ['bell peppers', 1.0], 'j': ['jalapenos', 1.0],
                       'p': ['pineapple', 1.5], 'n': ['None']}
    meattoppingsDict = {'p': ['pepperoni'], 's': ['sausage', 1.5], 'b': ['bacon', 1.0], 'n': ['None', 0.0]}

    def __init__(self):
        self.toppingCode = ''

    def get_cheese_topping_name_price(self, toppingCode):
        """this function gets the name and price of the cheese"""
        for toppingkey, toppingdetails in Toppings.cheesetoppingsDict.items():
            if toppingCode.lower() == toppingkey.lower():
                toppingName = toppingdetails[0]
                toppingprice = toppingdetails[1]
                return toppingName, toppingprice
            return None, None

    def get_veg_topping_name_price(self, toppingCode):
        """this function gets the name and price of the vegetables + the pineapple"""
        for toppingkey, toppingdetails in Toppings.vegtoppingsDict.items():
            if toppingCode.lower() == toppingkey.lower():
                toppingName = toppingdetails[0]
                toppingprice = toppingdetails[1]
                return toppingName, toppingprice
            return None, None
        
    def get_meat_topping_name_price(self, toppingCode):
        """this function gets the name and price of the vegetables + the pineapple"""
        for toppingkey, toppingdetails in Toppings.meattoppingsDict.items():
            if toppingCode.lower() == toppingkey.lower():
                toppingName = toppingdetails[0]
                toppingprice = toppingdetails[1]
                return toppingName, toppingprice
            return None, None

    def get_topping_option_print_line(self, toppingcategory):
        """Returns a line with all the topping name and price for the specific category of topping"""
        optionline = []
        toppingtypedict = []
        if toppingcategory.lower() == 'cheese':
            toppingtypedict = Toppings.cheesetoppingsDict
        elif toppingcategory.lower() == 'veg':
            toppingtypedict = Toppings.vegtoppingsDict
        elif toppingcategory.lower() == 'meat':
            toppingtypedict = Toppings.meattoppingsDict

        for toppingkey, toppingdetails in toppingtypedict.items():
            name = toppingdetails[0]
            price = toppingdetails[1]
            linedata = name +"("+ toppingkey + "): $" + str(price)
            optionsLine.append(linedata)
        return "/t".join(optionline)