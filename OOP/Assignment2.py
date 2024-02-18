
class Product:
    def __init__(self, name:str, price:float , quantity:int):
        self._name = name
        self._validate_price(price)
        self._price = price
        self._validate_quantity(quantity)
        self._quantity = quantity

    def display_details(self)->None:
        print(f"Name: {self._name},Price: {self.price},Quantity: {self.quantity}")


    @property
    def name(self)->str:
        return self._name
    
    @name.setter
    def name(self , name:str):
        self._name = name

    @property
    def price(self)->float:
        return self._price    
    
    @price.setter
    def price(self , price:float):
         self._validate_price(price)
         self._price = price

    @property
    def quantity(self)->int:
        return self._quantity
    
    @quantity.setter
    def quantity(self , quantity:float):
        self._validate_quantity(quantity)
        self._quantity = quantity



    @staticmethod
    def _validate_price(self,price:float):
        if price <= 0:
            raise ValueError('price cannot be last or equal to 0')

    @staticmethod
    def _validate_quantity(self,price:float):
        if price <= 0:
            raise ValueError('price cannot be last or equal to 0')

    def validate(self , price:float , quantity:int):
        self._validate_price(price)
        self._validate_quantity(quantity)


class shoppingCart:

    def __init__(self):
        self._products = []

    def add_product(self , product:Product):
        if not isinstance(product,Product):
            raise ValueError()    
        
        self._products.append(product)

    def remove_product(self , product:Product):
        try:
            self._products.remove(product)
        except ValueError:
            print(f"Product {product.name} doesn't exist")

    def view_cart(self):
        for product in self._products:
            product.display_details()

class DiscountProduct(Product):
    def __init__(self , name:str , price:float , quantity:int , discount_percentage):
        super().__init__(name , price , quantity)
        self._discount_percentage = discount_percentage
    
    def display_details(self) -> None:
        print(f"Name: {self._name},Price: {self.price},Quantity: {self.quantity} , Discount: {self._discount_percentage}")

    @property
    def price(self):
        return self._price - (self.price * self._discount_percentage*0.01)    

        
        


class Order:
    def __init__(self):
        self._products = []   
        self._total_amount = 0

    def add_product(self , product:Product):
        self._products.append(product)
        self._total_amount += product.price

    def display_order(self):
        print(f"Number of items{len(self._products)} , Total amount {self._total_amount}")     

class User:
    def __init__(self , username:str , email:str ):
        self.username = username
        self.email = email
        self.shopping_cart = shoppingCart()        

    def view_cart(self):
        self.shopping_cart.view_cart()

    def checkout(self):
        order = Order()
        for item in self.shopping_cart:
                




      