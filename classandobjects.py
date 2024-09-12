class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.num_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor):
                print(i)

    def __len__(self):
        return(self.num_of_floors)

    def __str__(self):
        return(f"Название: {self.name}, кол-во этажей: {self.num_of_floors}")

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(str(h1))
print(str(h2))

# __len__
print(len(h1))
print(len(h2))
