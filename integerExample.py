ten = 10
hundred = 100
thousand = 1000
million = 1000000
billion = 1000000000
wordToNum = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
             9: "nine", ten: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
             16: "sixteen",
             17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
             60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", hundred: "hundred", 1000: "thousand",
             1000000: "million", 1000000000: "billion"}

words = []
num = int(input("Enter a number: "))


def billions(number):
    next_number = number % billion
    number = (number - next_number)
    ones(int(number / billion))
    words.append(wordToNum[billion])
    return next_number


def millions(number):
    next_number = number % million
    number = (number - next_number)
    ones(int(number / million))
    words.append(wordToNum[million])
    return next_number


def thousands(number):
    next_number = number % thousand
    number = (number - next_number)
    ones(int(number / thousand))
    words.append(wordToNum[thousand])
    return next_number


def hundreds(number):
    next_number = number % hundred
    number = (number - next_number)
    ones(int(number / hundred))
    words.append(wordToNum[hundred])
    return next_number


def tens(number):
    next_number = number % ten
    number = (number - next_number)
    words.append(wordToNum[number])
    return next_number


def ones(number):
    words.append(wordToNum[number])


if num > billion:
    num = billions(num)
    
if num > million:
    num = millions(num)

if num > thousand:
    num = thousands(num)

if num > hundred:
    num = hundreds(num)

if num > 20:
    num = tens(num)

ones(num)

print(' '.join(words))
