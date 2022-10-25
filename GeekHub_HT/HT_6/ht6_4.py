'''4. Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді коду Морзе 
та виводить декодоване значення (латинськими літерами).
   Особливості:
    - використовуються лише крапки, тире і пробіли (.- )
    - один пробіл означає нову літеру
    - три пробіли означають нове слово
    - результат може бути case-insensitive (на ваш розсуд - великими чи маленькими літерами).
    - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки тощо використовуватися не будуть. 
    Лише латинські літери.
    - додайте можливість декодування сервісного сигналу SOS (...---...)
    Приклад:
    --. . . -.- .... ..-- -...   .. ...   .... . .-. .
    результат: GEEKHUB IS HERE'''


DEF_MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', ',': '--..', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': '   '}


def transponation(my_dict):
    finnaly_dict = {}
    # for f in my_dict:
    #     print(f)
    for key, value in my_dict.items():
        print(key, value)
        finnaly_dict.update({value: key})
    return finnaly_dict


def pre_morse(my_string):
    morse_list = []
    if not my_string:
        return 'Input any message'
    else:
        my_list = my_string.split('   ')
        for val in my_list:
            morse_list.append(val.split(' '))

    return morse_list


def morse(any_str):
    if any_str == 'SOS':
        return '...---...'
    my_dict = transponation(DEF_MORSE_CODE_DICT)
    my_list = pre_morse(any_str)
    my_str = ''
    finally_str = ''
    for el in my_list:
        for i in el:
            my_str += my_dict[i]
        finally_str += (' '+ my_str)
        my_str = ''
    return finally_str


def decoder(any_str):
    finally_str = ''
    for letter in any_str:
        finally_str += DEF_MORSE_CODE_DICT[letter]
    return finally_str


print(morse('--. . . -.- .... ..- -...   .. ...   .... . .-. .'))
print(decoder('HELLO, PYTHON'))
print(morse('SOS'))
