'''1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів. 
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, 
   а в правій - пішохідного світлофора. Кожну 1 секунду виводиться поточні кольори. Ч
   ерез декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах 
   (пішоходам зелений тільки коли автомобілям червоний).
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green'''


from time import sleep


COLOR_LIST = [('Red', 'Green'), ('Yellow', 'Red'), ('Green', 'Red'), ('Yellow', 'Red')]


index = 0
while True:
    
    if index % 2:
        for _ in range(2):
            print(COLOR_LIST[index][0], COLOR_LIST[index][1])
            sleep(1)
    else:
        for _ in range(4):
            print(COLOR_LIST[index][0], COLOR_LIST[index][1])
            sleep(1)
    index += 1
    index %= 4


# with open('my_file.txt', 'w', encoding='utf-8') as file:
#     file.write('get ready to go\n')

# with open('my_file.txt', 'a+', encoding='utf-8') as file:
#     index = 0
#     while True:
#         if index % 2:
#             for _ in range(2):
#                 file.write(f'{COLOR_LIST[index][0]} {COLOR_LIST[index][1]}\n')
#                 sleep(1)
#         else:
#             for _ in range(4):
#                 file.write(f'{COLOR_LIST[index][0]} {COLOR_LIST[index][1]}\n')
#                 sleep(1)
#         index += 1
#         index %= 3 
