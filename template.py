class Monkey:
    all_monkeys = []
    
    def __init__(self, name, keybind, coords, upgrades):
        self.name = name.title()
        self.keybind = keybind.upper()
        self.coords = coords.lower()
        self.active = False
        self.upgrades = upgrades
        Monkey.all_monkeys.append(self)
        
    def __str__(self):
        return f'{self.name.ljust(20)} | {self.keybind.ljust(20)} | {str(self.coords.ljust(20))} | {self.upgrades.ljust(20)}'
    
    @classmethod
    def listar_macacos(cls):
       
        print(f'{"Monkey name".ljust(20)} | {"Bind".ljust(20)} | {"Coordinate".ljust(20)} | {"Active"}')
        for monkey in Monkey.all_monkeys:
            print(f'{monkey.name.ljust(20)} | {monkey.keybind.ljust(20)} | {str(monkey.coords).ljust(20)} | {monkey.active}')
    