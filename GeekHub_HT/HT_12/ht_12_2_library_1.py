'''2. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки (включіть фантазію).
Наприклад вона може містити класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д. Можна робити по
прикладу банкомату з меню, базою даних і т.д. '''


class Human:

    def __init__(self, first_name, last_name, gender):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        print(f'Hi, my name is {self.first_name} {self.last_name}')

    def human_info(self):
        print(f'First name {self.first_name}, last name {self.last_name}')


class Accounting:

    def __init__(self, work_category):
        self.__class_salary_dict = {
            'Teaching secretary': 100,
            'Intercessor of the director of scientific work': 200,
            'Intercessor of the director of nutrition of information technologies': 500,
            'Library Director': 1000
        }

        self.__salary = self.__calculate_salary(work_category)

    def __calculate_salary(self, work_category):
        return self.__class_salary_dict.get(work_category, 0)

    @property
    def salary(self):
        if not self.__salary:
            return 'Undefined'
        return self.__salary


class Administration(Human):
    #     наслідує від класу людей
    def __init__(self, first_name, last_name, gender, work_category):
        super().__init__(first_name, last_name, gender)
        self.work_category = Accounting(work_category)

    def get_position(self):
        return self.work_category

# vlad = Administration('Vlad', 'Hotunov', 'Man', 'Library Director')
# print(vlad.work_category.salary)
