import itertools

class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        return list(map(list,
            itertools.product(self.ingredients, self.toppings))
            )

if __name__ == "__main__":
    machine = IceCreamMachine(
            ["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) 
    #should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
