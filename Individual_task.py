from datetime import datetime
import pickle

##-----------------------------------------------------------------------------------------------------------------

class Otdel:
    """Класс отделы"""

    def __init__(self,name,count_prilavok,count_prodavec,number_zal):
        self.name = name
        self.count_prilavok = count_prilavok
        self.count_prodavec = count_prodavec
        self.number_zal = number_zal
        self.queue = []

#    def change(self, c):
#        self.number_zal += c

    def info(self):
        return('Название отдела: {}\nКоличество прилавков: {}\nКоличество продавцов: {}\n номер зала: {}\n'.format(self.name, self.count_prilavok,self.count_prodavec,self.number_zal))

#    def __str__(self):
#        return (f'Название отдела {self.name} количество прилавков {self.count_prilavok} количество продавцов {self.count_prodavec}')

    def change_number_zal(self, number_zal):
        self.number_zal = number_zal
        self.queue.append(Transaction(number_zal))

    def get_transaction(self):
        for i in range(len(self.queue)):
            item = self.queue.pop(0)
            print('when {0} : price {1}'.format(item.when, item.number_zal))

    def __del__(self):
        return('Класс Отделы был уничтожен')

##-----------------------------------------------------------------------------------------------------------------

class Sotrudnik:
    """Класс сотрудники"""

    def __init__(self, fname, name, otch, otdel, birthday, year_start, stach, dolsnost, pol, adres, city, mobile):
        self.fname = fname
        self.name = name
        self.otch = otch
        self.otdel = otdel
        self.birthday = birthday
        self.year_start = year_start
        self.stach = stach
        self.dolsnost = dolsnost
        self.pol = pol
        self.adres = adres
        self.city = city
        self.mobile = mobile
        self.queue = []

    def info(self):
        return("Фамилия: {}\nимя: {}\nотчество: {}\nотдел: {}\nгод рождения: {}\nгод поступления на работу: {}\nстаж: {}\nдолжность: {}\nпол: {}\nадрес: {}\nгород: {}\nтелефон: {}\n".format(self.fname,self.name,self.otch,self.otdel,self.birthday,self.year_start,self.stach,self.dolsnost,self.pol,self.adres,self.city,self.mobile))

    def change_birthday(self, birthday):
        self.birthday = birthday
        self.queue.append(Transaction(birthday))

    def get_transaction(self):
        for i in range(len(self.queue)):
            item = self.queue.pop(0)
            print('when {0} : price {1}'.format(item.when, item.birthday))

    def __del__(self):
        return('Класс сотрудники был уничтожен')

##-----------------------------------------------------------------------------------------------------------------

class Dolsnost:
    """Класс должлности"""

    def __init__(self,named,summ_stavka):
        self.named = named
        self.summ_stavka = summ_stavka
        self.queue = []

    

    def info(self):
        return("название должности: {}\n сумма ставки".format(self.named,self.summ_stavka))


    def change_summ_stavka(self, summ_stavka):
        self.price = summ_stavka
        self.queue.append(Transaction(summ_stavka))

    def get_transaction(self):
        for i in range(len(self.queue)):
            item = self.queue.pop(0)
            print('when {0} : price {1}'.format(item.when, item.summ_stavka))

    def __del__(self):
        return('Класс должности был уничтожен')



##-----------------------------------------------------------------------------------------------------------------

class Tovar:
    """Класс товары"""

    def __init__(self,namet,otdel,country_proizvod,yslov_xranen,srok_xranen):
        self.namet = namet
        self.otdel = otdel
        self.country_proizvod = country_proizvod
        self.yslov_xranen = yslov_xranen
        self.srok_xranen = srok_xranen
        self.queue = []

    def info(self):
        return("название товара: {}\nотдел: {}\nстрана производитель: {}\nусловия хранения: {}\nсроки хранения: {}\n".format(self.namet,self.otdel,self.country_proizvod,self.yslov_xranen,self.srok_xranen))

    def change_srok_xranen(self, srok_xranen):
        self.srok_xranen = srok_xranen
        self.queue.append(Transaction(srok_xranen))

    def get_transaction(self):
        for i in range(len(self.queue)):
            item = self.queue.pop(0)
            print('when {0} : price {1}'.format(item.when, item.srok_xranen))

    def __del__(self):
        return('Класс товары был уничтожен')

##-----------------------------------------------------------------------------------------------------------------

class Prodaza_tovarov():
    """Класс продажа товаров"""

    def __init__(self,sotrudnik,data_tovara,time,count,price,summ):
        self.sotrudnik = sotrudnik
        self.data_tovara = data_tovara
        self.time = time
        self.count = count
        self.price = price
        self.summ = summ
        self.queue = []

    def info(self):
        return("сотрудник: {}\nдата товара: {}\nвремя: {}\nкол-во: {}\nцена: {}\nсумма: {}\n".format(self.sotrudnik,self.data_tovara,self.time,self.count,self.price,self.summ))

    def change_price(self, price):
        self.price = price
        self.queue.append(Transaction(price))

    def get_transaction(self):
        for i in range(len(self.queue)):
            item = self.queue.pop(0)
            print('when {0} : price {1}'.format(item.when, item.price))

    def __del__(self):
        return('Класс продажа товаров был уничтожен')


class Sale_Groceries(Prodaza_tovarov):
    """Класс продажа товаров из отдела бакалеи"""

    def __init__(self,sotrudnik,data_tovara,time,count,price,summ, otdel):
        Prodaza_tovarov.__init__(self,sotrudnik,data_tovara,time,count,price,summ)
        self.otdel = otdel

    def info(self):
        return("сотрудник: {}\nдата товара: {}\nвремя: {}\nкол-во: {}\nцена: {}\nсумма: {}\nотдел: {}".format(self.sotrudnik,
                                                                                                    self.data_tovara,
                                                                                                    self.time,
                                                                                                    self.count,
                                                                                                    self.price,
                                                                                                    self.summ,self.otdel))



    def discount_grocery(self):
        self.price = self.price / 2
        return ('Сегодня на товары из отдела "{0}" действует скидка. Нынешняя цена: {1}'.format(self.otdel,self.price))


class Sale_Household(Prodaza_tovarov):
    """Класс продажа товаров из отдела хозяйственных продуктов"""

    def __init__(self, sotrudnik, data_tovara, time, count, price, summ, otdel):
        Prodaza_tovarov.__init__(self,sotrudnik, data_tovara, time, count, price, summ)
        self.otdel = otdel

    def info(self):
        return("сотрудник: {}\nдата товара: {}\nвремя: {}\nкол-во: {}\nцена: {}\nсумма: {}\nотдел: {}".format(
            self.sotrudnik,
            self.data_tovara,
            self.time,
            self.count,
            self.price,
            self.summ, self.otdel))

    def discount_household(self):
        self.price = self.price / 2
        return ('Сегодня на товары из отдела "{0}" действует скидка. Нынешняя цена: {1}'.format(self.otdel,self.price))
##------------------------------------------------------------------------------------------------------------------



##--------------------------------------------------------------------------------------------------------------

class PersistencePrice(object):

    @staticmethod # декоратор
    def seriailze(textfiles, name):
        with open((name + '.pkl'), 'wb') as f:
            pickle.dump(textfiles, f)
        f.closed

    @staticmethod
    def deserialize(name):
        with open((name + '.pkl'), 'rb') as f:
            textfiles = pickle.load(f)
        f.closed
        return textfiles

class Transaction():

    def __init__(self,price):
        #self.number_zal = number_zal
        #self.birthday = birthday
        #self.summ_stavka = summ_stavka
        #self.srok_xranen = srok_xranen

        # self.when = datetime.today()
        self.when = datetime(2023, 4, 4, 10, 00, 00)
        self.price = price
        self.queue = []


    def __del__(self):
        with open('transaction.txt', 'w') as f:
            f.write('when {0} : price {1} \n'.format(self.when, self.price))
        f.closed

##------------------------------------------------------------

if __name__ == "__main__":
    otdel= Otdel("Главный","8","4",2)
#    otdel.change(7)
#    otdel.info()

#    sotrudnik = Sotrudnik("Чувикова","Сюзанна","Кирилловна","Молочные продукты","24.07.1975","1995","5 лет","заместитель директора","женский","Россия г. Курган Речная ул. д. 2 кв.60","Курган","+7 (908) 413-84-10")
#    sotrudnik.info()

#    dolsnost = Dolsnost("Заместитель директора","25000р")
#    dolsnost.info()

#    tovar = Tovar("молоко","молочные продукты","Россия","Холодильник","Месяц")
#    tovar.info()

#    prodaza_tovarov = Prodaza_tovarov("Иван","15.12.1995","14:37","2 штуки",68,"136р")
#    prodaza_tovarov.info()

#    sale_groceries = Sale_Groceries('Алексей', '15.12.1995', '14:37', '2 штуки', '68р', '136р', 'Продано')
#    sale_groceries.info()

#    sale_household = Sale_Household('Алексей', '15.12.1995', '14:37', '2 штуки', '68р', '136р', 'Не продано')
#    sale_household.info()
    





        


    
                
