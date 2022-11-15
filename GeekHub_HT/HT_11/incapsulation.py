class Kettle:

    def turn_on(self):
        print('You turn the button')
        self.boil()
        self.check_temperature()
        self.beep()
        self.turn_off()

    def boil(self):
        print('Water heating')

    def check_temperature(self):
        print('Check the water temperature')

    def beep(self):
        print('Sound signal')

    def turn_off(self):
        print('Auto turn off')


my_kettle = Kettle()
my_kettle.turn_on()
# my_kettle.beep()
# my_kettle.boil()
