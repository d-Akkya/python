class Programmer:
    company = "Microsoft"
    def __init__(self, name, id, city):
        self.name = name
        self.id = id
        self.city = city

p = Programmer("Akkya", 20023, "Pune")
print(p.company, p.name, p.id, p.city)

r = Programmer("Prasad", 20025, "Pune")
print(r.company, r.name, r.id, r.city)