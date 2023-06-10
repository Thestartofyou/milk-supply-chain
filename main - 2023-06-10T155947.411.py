class Supplier:
    def __init__(self, name):
        self.name = name
    
    def process_order(self, quantity):
        print(f"Processing order of {quantity} liters of milk from supplier {self.name}.")


class Manufacturer:
    def __init__(self, name, supplier):
        self.name = name
        self.supplier = supplier
    
    def produce(self, quantity):
        print(f"Producing {quantity} cartons of milk at {self.name}.")
    
    def place_order(self, quantity):
        print(f"Placing order for {quantity} liters of milk to supplier {self.supplier.name}.")
        self.supplier.process_order(quantity)


class Distributor:
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer
    
    def distribute(self, quantity):
        print(f"Distributing {quantity} cartons of milk from {self.manufacturer.name} to {self.name}.")


class Retailer:
    def __init__(self, name, distributor):
        self.name = name
        self.distributor = distributor
    
    def sell(self, quantity):
        print(f"Selling {quantity} cartons of milk at {self.name}.")


# Create supplier, manufacturer, distributor, and retailer instances
supplier = Supplier("Milk Supplier")
manufacturer = Manufacturer("Milk Manufacturer", supplier)
distributor = Distributor("Milk Distributor", manufacturer)
retailer = Retailer("Milk Retailer", distributor)

# Example supply chain process
order_quantity = 1000  # liters of milk to be ordered

manufacturer.place_order(order_quantity)
manufacturer.produce(order_quantity)
distributor.distribute(order_quantity)
retailer.sell(order_quantity)
