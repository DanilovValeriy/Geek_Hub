class Kettle:

    def turn_on(self):
        print('You turn the button')
        self.__boil()
        self.__check_temperature()
        self.__beep()
        self.__turn_off()

    def __boil(self):
        print('Water heating')

    def __check_temperature(self):
        print('Check the water temperature')

    def __beep(self):
        print('Sound signal')

    def __turn_off(self):
        print('Auto turn off')


my_kettle = Kettle()
my_kettle.turn_on()
# my_kettle.beep()
# my_kettle.__boil()
# my_kettle._Kettle__boil()
