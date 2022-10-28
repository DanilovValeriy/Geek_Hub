'''5. Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих регістро-незалежних букв
 та цифр, які зустрічаються в рядку більше ніж 1 раз. 
 Рядок буде складатися лише з цифр та букв (великих і малих). 
 Реалізуйте обчислення за допомогою генератора в один рядок
    Example (input string -> result):
    "abcde" -> 0            # немає символів, що повторюються
    "aabbcde" -> 2          # 'a' та 'b'
    "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
    "indivisibility" -> 1   # 'i' присутнє 6 разів
    "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
    "aA11" -> 2             # 'a' і '1'
    "ABBA" -> 2             # 'A' і 'B' кожна двічі'''


def counter_repitions(my_str):
    return len({i for i in my_str if my_str.lower().count(i) > 1})

# must return 2
print(counter_repitions('Indivisibilities'))

# must return 1
print(counter_repitions("indivisibility"))

# must return 7
print(counter_repitions('abcdefgABCDEFG'))

#must return 2
print(counter_repitions("aA11"))