https://www.codewars.com/kata/56a4addbfd4a55694100001f/train/python

def validate_hello(greetings):
    return any(word in greetings.lower() for word in ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"])

