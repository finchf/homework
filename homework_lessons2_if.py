
# 1. Користувач задає змінну вік. Якщо він старше ніж 18
# роздрукуйте що все добре, якщо ні, то роздрукуйте
# що не все добре

age = int(input('How old are you? '  ))
if age >= 18:
    print('Ласкаво просимо до Нарнії')
else:
    print('Godbye, pupsik')

# 2.Додати до першої умови, якщо вік більше ніж 100,
# роздрукувати текст що користувач вводить нас в оману

age = int(input('How old are you? '  ))
if age >= 100:
    print('Sorry we are closed')
elif age >= 18:
    print('Ласкаво просимо до Нарнії')
else:
    print('Godbye, pupsik')


# 3. Додати прінти чи є введений вік парним, чи непарним.

age = int(input('How old are you? '  ))
if age >= 100:
    print('Sorry we are closed')
elif age >= 18:
    print('Ласкаво просимо до Нарнії')
else:
    print('Godbye, pupsik')
if age % 2:
    print('your age is square')
else:
    print('your age is roundlyes')


# 4. Додати що користувач вводить ще й ім'я. І якщо в імені
# є літера 'a', то написати що ми навідь не збираємося
# його перевіряти.


name = str(input('What is your name? '))
if 'a' in name:
    print('our company does not cooperate with You')
else:
    print('Ok, lets go, ', name.capitalize())
    age = int(input('How old are you? '))
    if age >= 100:
        print('Sorry we are closed')
    elif age >= 18:
        print('Ласкаво просимо до Нарнії')
    else:
        print('Godbye, pupsik')
    if age % 2:
        print('your age is square')
    else:
        print('your age is roundlyes')


# 5.Перевірити якщо в імені є літера 'v' чи велика,
# чи маленька байдуже. І вік користувача парний,
# то написати що він виграв приз, якщо ні, то не виграв.

name = str(input('Hello! what is your name? '))
age = int(input('How old are you? '))
    if 'v' in name.lower() and not age%2:
    print('prize')
else:
    print('no prize')


# 6.  Спитати користувача вік, стать та ім'я.
# Для усіх молодше 15 ми пишемо що рекомендуємо теніс,
# для хлопців старше 15 рекомендуємо футбол, для дівчат баскетбол,
# але якщо в імені є літера 'c' або 't',
# друкуємо що ми не рекомендуємо займатися спортом

age = int(input('How old are you? '))
gender = str(input('what gender are you'))
name = str(input('what is your name?'))

if 'c' in name.lower() or 't' in name.lower():
    print('Goodbye')
elif age <= 15:
    print('Tennis')
else:
    if  'woman'  == gender:
        print('Basketball')
    elif 'man' == gender:
        print('Football')