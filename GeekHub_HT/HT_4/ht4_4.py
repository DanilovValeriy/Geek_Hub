'''Наприклад маємо рядок --> 
"f98neroi4nr0c3n30irn03ien3c0rfe kdno400we(nw,kowe%00koi!jn35pijnp4 6ij7k5j78p3kj546p4 65jnpoj35po6j345" 
-> просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати довільні рядки на зразок цього 
   та яка обробляє наступні випадки:
-  якщо довжина рядка в діапазоні 30-50 (включно) -> прiнтує довжину рядка, 
кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всіх чисел та окремо рядок без цифр та знаків 
лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)'''

# Я так розумію, що треба було б створити дві окремі функції для підрахунку стрінгових і цифр, але
# гадаю це вже перебор наразі
def count_digit(my_str):
    digit_count = 0
    str_count = 0
    for val in my_str:
        if val.isdigit():
            digit_count += 1
        elif val.isalpha():
            str_count += 1
    return (digit_count, str_count)


def sum_of_numbers(my_str):
    my_sum = 0
    for val in my_str:
        if val.isdigit():
            my_sum += int(val)
    return my_sum


def strng_letters_only(my_str):
    our_str = ''
    for val in my_str:
        if val.isalpha():
            our_str += val
    return our_str


def wtf(my_str):
    if len(my_str) > 50:
        return 'Oh my God! Remove the cat from the keyboard!!!'
    elif len(my_str) in range(30, 51):
        print(f'String has length = {len(my_str)}')
        print(f'Digit count = {count_digit(my_str)[0]}, letters count = {count_digit(my_str)[1]}')
    else:
        print(sum_of_numbers(my_str))
        print(strng_letters_only(my_str))

wtf('3yfyfyfyf7f7f7f7f7f7f7f7f7ff')
