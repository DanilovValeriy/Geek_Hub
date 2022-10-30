from time import sleep


COLOR_LIST = [('Red', 'Green'), ('Yellow', 'Red'), ('Green', 'Red')]


with open('my_file.txt', 'w', encoding='utf-8') as file:
    file.write('get ready to go\n')

    with open('my_file.txt', 'a+', encoding='utf-8') as file:
        index = 0
        while True:
            if index % 2:
                for _ in range(2):
                    file.write(f'{COLOR_LIST[index][0]} {COLOR_LIST[index][1]}\n')
                    sleep(1)
            else:
                for _ in range(4):
                    file.write(f'{COLOR_LIST[index][0]} {COLOR_LIST[index][1]}\n')
                    sleep(1)
            index += 1
            index %= 3 