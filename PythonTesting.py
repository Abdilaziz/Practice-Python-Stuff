from bs4 import BeautifulSoup

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

print("\n")

for i in range(5):
    print(i)

print("\n")

for i in range(0,10,3):
    print(i)



# two ** means dictionary, while * means arbitrary amount of input
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print (kw, ":", keywords[kw])

        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

print (list(range(3,6)))
args = [3,6]
print (list(range(*args)))






class Dog:

    kind = 'canine'         # class variable shared by all instances
                            # if tricks is out here it would be changed
                            # by all instances

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')

print( d.kind)
print( e.kind)
print( d.name)
print( e.name)


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)










