class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
frantisek = Employee("František Novák", "konstruktér", 25)   
attr_name = "name"
hodnota_atributu = getattr(frantisek, attr_name, "Unknown atribut")
print(hodnota_atributu)
# print(frantisek.attr_name)