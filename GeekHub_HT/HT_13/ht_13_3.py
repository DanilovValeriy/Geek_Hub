'''
3. Реалізуйте класс Transaction. Його конструктор повинен приймати такі параметри:
- amount - суму на яку було здійснено транзакцію
- date - дату переказу
- currency - валюту в якій було зроблено переказ (за замовчуванням USD)
- usd_conversion_rate - курс цієї валюти до долара (за замовчуванням 1.0)
- description - опис транзакції (за дефолтом None)
Усі параметри повинні бути записані в захищені (_attr) однойменні атрибути.
Доступ до них повинен бути забезпечений лише на читання та за допомогою механізму property.
При чому якщо description дорівнює None, то відповідне property має повертати рядок "No description provided".
Додатково реалізуйте властивість usd, що має повертати суму переказу у доларах (сума * курс)
'''


class Transaction:
    def __init__(self, amount, date, currency='USD', usd_conversion_rate=1.0, description=None):
        self._amount = amount
        self._date = date
        self._currency = currency
        self._usd_conversion_rate = usd_conversion_rate
        self._description = description

    @property
    def amount(self):
        return self._amount

    @property
    def date(self):
        return self._date

    @property
    def currency(self):
        return self._currency

    @property
    def usd_conversion_rate(self):
        return self._usd_conversion_rate

    @property
    def description(self):
        if self._description is None:
            return 'No description provided'
        return self._description

    @property
    def usd(self):
        return self.usd_conversion_rate * self.amount


my_transaction = Transaction(10000, '20-07-2020', 'UAH', 0.037, 'took out money from the nightstand')
print(my_transaction.amount)
print(my_transaction.date)
print(my_transaction.currency)
print(my_transaction.description)
print(my_transaction.usd)
# raise Exception AttributeError
# my_transaction.description = 'I am change my mind'
