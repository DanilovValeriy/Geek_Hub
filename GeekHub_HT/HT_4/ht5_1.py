'''Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) та яка буде повертати пору року, до якої цей мiсяць належить (зима, весна, лiто або осiнь). 
У випадку некоректного введеного значення - виводити відповідне повідомлення.'''



def what_season(month: int) -> str:
    try:
        month =  int(month)
    except ValueError as err:
        return err
    except BaseException as err:
        return err
    if month in {12, 1, 2}:
        return 'It is winter'
    elif month in {3, 4, 5}:
        return 'It is spring'
    elif month in {6, 7, 8}:
        return 'It is summer'
    elif month in {9, 10, 11}:
        return 'It is autumn'
    else:
        month2 = month%12 if month%12 else 12
        return f'Expected integer number from 1 to 12. Maybe you mean {month2}? {what_season(month2)}'
    
print(what_season(input('Input number of month\n')))
