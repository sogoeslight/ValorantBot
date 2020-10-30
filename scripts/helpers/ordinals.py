def parse(num):
    if num % 10 == 1:
        return str(num) + "st"
    elif num % 10 == 2:
        return str(num) + "nd"
    elif num % 10 == 3:
        return str(num) + "rd"
    else:
        return str(num) + "th"
