'''Користувачем вводиться початковий і кінцевий рік. Створити цикл, 
який виведе всі високосні роки в цьому проміжку (границі включно). 
P.S. Рік є високосним, якщо він кратний 4, але не кратний 100, 
а також якщо він кратний 400.'''

def is_leap(year):
    return (year%4 == 0)and(year%100 != 0) or year%400 == 0

start, finish = map(int,input('Input start finish comma separated').split(','))

for i in range(start, finish+1):
    if is_leap(i):
        print('This is leap year = ', i)
        