1. сума списку за допомогою for та while:

a = list(range(11)) 
total =0           

for i in a: 
    total += i   
    
print(total)




my_list = list(range(101)) 
# альтернативная запись: my_list = [i for i in range(0, 101)]
i = 0 
total = 0 

while i < len(my_list): 
    total += my_list[i] 
    i += 1 

print(total) 

2. Написати програму, яка виводить сама себе

import sys
filename = sys.argv[0]
f = open(filename, 'r')

for line in f:
    print(line)
f.close()


3. Написати програму, яка виводить саму себе задом наперед


import sys
filename = sys.argv[0]
f = open(filename, 'r')

for line in f:
    print(line:, -1)
f.close()


4. Банкомат видає суму максимально можливими купюрами


prise = int(input('Введіть потрібну суму..'))
nominal = [1000, 500, 200, 100, 50, 20, 10, 5]

for i in nominal:
    print(f'Купюр по {i}: {prise // i}')
    prise %= i
    if not prise:
        break
        
        
5. Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри

price = int(input('Введіть суму: '))

my_list = [10, 20, 50, 100, 200, 500, 1000]

for i in my_list:
  if i <= 50:
    max_banknotes = 9
  else:
    max_banknotes = price // i
    if max_banknotes > 10:
        max_banknotes = 10
  print(f'Купюр по {i}: {max_banknotes}')
  price -= i * max_banknotes   #Вычитаем из введенной суммы общую стоимость выданных купюр текущего номинала.
  if price == 0:
      break
      
      
      
Fizzbuzz
with open('numbers.txt') as file:
    # Читаем первую строку и сохраняем ее в переменной
    line = file.readline()
    # Пока строка не пустая
    while line:
        # Разбиваем строку на три числа(убираем пробельные символы в начале и конце строки, и разбиваем строку на элементы, используя разделитель - пробел по умолчанию)
        nums = line.strip().split()
        # Преобразуем числа из строк в целочисленный тип
        nums = [int(num) for num in nums]
        # Для каждого числа в списке чисел
        for num in nums:
            # Если число кратно 3 и 5, выводим ' fizzbuzz'
            if num % 3 == 0 and num % 5 == 0:
               print(str(num) + ' = fizzbuzz ')
            # Если число кратно 3, выводим 'fizz'
            elif num % 3 == 0:
                print(str(num) + ' = fizz ')
            # Если число кратно 5, выводим 'buzz'
            elif num % 5 == 0:
                print(str(num) + ' = buzz ')
            # Иначе выводим само число
            else:
                  print(str(num) + ' не удовлетяворяет условиям ')
        # Читаем следующую строку
        print('\nПроверяем следующую строку: \n')
        line = file.readline()
        
        
Переробити другу задачу так, щоб результат писався в інший файл.
    
with open('numbers.txt') as file, open('results.txt', 'w') as outfile:
    line = file.readline()
    while line:
        nums = line.strip().split()
        nums = [int(num) for num in nums]+
        for num in nums:
            if num % 3 == 0 and num % 5 == 0:
               outfile.write(str(num))
               outfile.write('= fizzbuzz  ')
            elif num % 3 == 0:
                outfile.write(str(num))
                outfile.write('= fizz  ')
            elif num % 5 == 0:
                outfile.write(str(num))
                outfile.write('= buzz  ')
            else:
                  outfile.write(str(num) + ' no ')
        outfile.write('\nПроверяем следующую строку:\n')
        line = file.readline()