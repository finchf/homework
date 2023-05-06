Завдання 1

def string_lower(s):
    return s.lower()

def string_upper(s):
    return s.upper()

list1 = 'Hello, worlD'.split()

print(list(map(string_lower, list1)))
print(list(map(string_upper, list1)))


Завдання 2
def simple(n):
    if n < 3:
        return True

    for i in range(2, int(n ** 0.5)+2):
        if not n % i:
            return False

    return True
def square(a):
    return a ** 2

l= []
for m in range(1, 51):
    if simple(m):
        l.append(square(m))


print(list(map(lambda num: num ** 2, filter(simple, range(1, 51)))))



Завдання 3
Візьміть файл, в якому є багато англійських слів у рядках. Порахуйте частоту зустрічі кожного слова та видрукуйте відсортовано.

with open('alice.txt', 'r') as f:
    text = f.read()
    words = text.lower().replace(',', '',).replace('.', '',).split()
    alice_dict = {}
    
    for word in words:
        alice_dict[word] = alice_dict.get(word, 0) + 1
    sorted_words = sorted(alice_dict.items(), key=lambda x: x[1], reverse=True)
    
    for word, count in sorted_words:
        print(word, count)
        
print(list(alice_dict))



my_zip:

def my_zip(keys, values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result