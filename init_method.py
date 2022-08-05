class Computer:

    def __init__(self, processor, ram):
        self.processor = processor
        self.ram = ram

    def config(self):
        print("Configuration: ", self.processor, self.ram)


com1 = Computer('i5', 16)
com2 = Computer('Ryzen 3', 8)

com1.config()
com2.config()
