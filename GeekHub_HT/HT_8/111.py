from time import sleep


COLOR_LIST = [('Red', 'Green'), ('Yellow', 'Red'), ('Green', 'Red')]


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
    index %= 3 
    

