def parse(num):
    if num % 10 == 1:
        print(str(num) + "st")
    elif num % 10 == 2:
        print(str(num) + "nd")
    elif num % 10 == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")
