# Hello World
print("Hello World")
print("\r")

# variabili
age = 35
print(type(age))
print(age)
print("\r")

pi = 3.14
print(type(pi))
print(pi)
print("\r")

name = "Rob"
print(type(name))
print(name)
print("\r")

print(age / pi)
print("\r")

number = 5
print(number * name)
print("\r")

print(int(number) * pi)
print("\r")

# stringhe
str = "My name is "
print(str[0])
print("\r")

print(str[0:5])  # non comprende il primo carattere
print("\r")

print(str[5])
print("\r")

print(str + name)
print("\r")

# array
myList = ["Rob", "kirsten", "Tommy", "Ralphie"]

print(myList)
print("\r")

print(myList[1])
print("\r")

print(myList[2:4])  # non comprende il 4 elemento
print("\r")

# lista di sola lettura
myTuple = [1, 2, 3, 4]
print(myTuple)
print("\r")

print(myTuple[1])
print("\r")

myTuple[2] = 5  # restituisce errore perchè non si possono modificare gli elementi
print(myTuple[2])
print("\r")

# array bidimensionale
dict = {}
dict["dad"] = "Rob"
dict["mum"] = "Kirsten"
dict[1] = "Tommy"
dict[2] = "Ralphie"
print(dict)
print("\r")

print(dict["mum"])
print("\r")

print(dict.keys())
print("\r")

print(dict.values())
print("\r")

# ciclo for
# stampa tutti i numeri da 0 a 10 quindi 11 caratteri
for i in range(11):
    print(i)
    print(name)
print(str)  # tutto ciò che si trova nell'indentazione del ciclo vieni ripetuto, il resto no
print("\r")

for i in range(0, 10):  # l'ultimo carattere è sempre escluso
    print(i)
print("\r")

foodList = ["Pizza", "Sushi", "Carne"]

for i in foodList:
    print("I love eating " + i)
print("\r")

# ciclo while
x = 0
while x <= 10:
    print(x)
    x += 1
print("\r")

dict = {"Alessio": 25, "Mario": 20, "Antonio": 24, "Andrea": 20}
for i in dict:
    print(i + " is ")
    print(dict[i])
print("\r")

# if
if name == "Alessio" or name == "Rob":
    print("Hello " + name)
else:
    print("I don't know you")
print("\r")

primes = 0
number = 2

while primes < 50:
    isPrime = True

    for i in range(2, number):
        if number % i == 0:
            isPrime = False

    if isPrime == True:
        print(number)
        primes += 1

    number += 1
print("\r")


# funzioni
def sayHello():
    print("hello")


sayHello()
print("\r")


def saySomethin(something):
    print(something)


saySomethin("Hi there")
print("\r")


def multiplyTwoNumbers(x, y):
    return x * y


print(multiplyTwoNumbers(4, 6))
print("\r")


def highestCommonFactor(x, y):
    for i in range(1, x + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf


print(highestCommonFactor(5, 10))
print("\r")

a = 5
b = 6


def addTwoNumbers():
    return a + b


print(addTwoNumbers())
print("\r")


def addTwoNumbers():
    a = 10
    return a + b  # il valore all'interno della funzione viene cambiato


print(addTwoNumbers())
print("\r")

print(a)  # se stampiamo il valore all'esterno della funzione notiamo che non cambia
print("\r")


def addTwoNumbers():
    c = 8
    return a + b


print(c)  # da errore perchè il valore non è accessibile dall'esterno
