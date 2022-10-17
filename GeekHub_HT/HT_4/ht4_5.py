operation_set = {'+', '-', '*', '/', '%', '//', '**'}

def date_validate(date):
    try:
        date = float(date)
        return True
    except ValueError as err:
        print(err)
        return False

def calc():
    a, oper, b = list(input('Input an arithmetic expression with spases\n').split(' '))
    if not(date_validate(a)and date_validate(b)):
        return 'Incorrect values'
    elif oper not in operation_set:
        return 'Incorrect operations'
         
    else:
        a, b = list(map(float, (a, b)))
        match oper:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                if b != 0:
                    return a / b
                else:
                    return'Divizion by zero'
                    
            case '%':
                if b != 0:
                    return a % b
                else:
                    return 'Divizion by zero'
            case '//':
                if b != 0:
                    return a // b
                else:
                    return 'Divizion by zero'
            case '**':
                return a ** b

print(calc())
