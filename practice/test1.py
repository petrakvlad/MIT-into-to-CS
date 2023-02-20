x = 24
y = 10

def quotiend_and_remainder(x, y):
    q = x // y
    a = x % y
    return (q, a)

(quot, remain) = quotiend_and_remainder(x, y)
#print(quot, remain)

tup = ((7, "Jake"), (3, "Valera"), (9, "Kalus"), (400, "Tor"))

def get_data(tuple_any):
    num = ()
    names = ()
    for t in tuple_any:
        num = num + (t[0],)
        names = names + (t[1],)
        minn = min(num)
        maxx = max(num)
        leng = len(names)
    return (minn, maxx, leng)

#print(get_data(tup))

s = "val e bal"
n = list(s)
f = s.split("e")


L = ["a", "b", "c", "d"]
g = "/".join(L)


lista = [7, 6, 9, 2]

new = sorted(lista)
#print(new)

#lista.sort()
#print(lista)

lista1 = lista[:]

lista1.append(1)
#print(lista1)

#print(lista)

lista2 = [7, 6, 4, 5]
lista3 = lista[:]

for i in lista3:
    if i in lista2:
        lista.remove(i)
#print(lista)

def factorial(number):
    if number == 1:
        return 1
    else:
        return number*factorial(number - 1)

#print(factorial(10))


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(5))

grades = {"Ana" : {"math":2, "litreture":5}, "James": {"math": 1, "lireture":2}}

#print(grades["James"]["lireture"])

# using dictionary to store results 
# of computations and use those in the following computations
def fibo_with_dict(n, d):
    if n in d:
        return d[n]
    else:
        ans = fibo_with_dict(n-1, d) + fibo_with_dict(n-2, d)
        d[n] = ans
        return ans




dicty = {1:1, 2:2}
print(fibo_with_dict(8, dicty))
