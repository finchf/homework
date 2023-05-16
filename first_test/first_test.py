import first_test

def spam(number):
    return 'bulochka' * number


def my_sum(list_of_numbers):
    total = 0
    for i in list_of_numbers:
        total += i
    return total


def shortener(string):
    words = string.split()
    for i in range(len(words)):
        if len(words[i]) > 6:
            words[i] = words[i][:6] + "*"
    return " ".join(words)




def compare_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count
