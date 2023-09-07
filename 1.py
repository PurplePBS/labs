import unittest
from Individual_task import *

class Test_Prodaza_tovarov(unittest.TestCase):

    def setUp(self):
        self.otdel_tr = Otdel("Главный","8","4",2)
        self.sotrdnik_tr = Sotrudnik("Чувикова","Сюзанна","Кирилловна","Молочные продукты","24.07.1975","1995","5 лет","заместитель директора","женский","Россия г. Курган Речная ул. д. 2 кв.60","Курган","+7 (908) 413-84-10")
        self.dolsnost_tr = Dolsnost("Заместитель директора","25000р")
        self.tovar_tr = Tovar("молоко","молочные продукты","Россия","Холодильник","Месяц")
        self.pr_tovarov_tr = Prodaza_tovarov("Иван", "15.12.1995", "14:37", "2 штуки", 68, "136р")
        self.sale_groceries = Sale_Groceries("Иван", "15.12.1995", "14:37", "2 штуки", 68, "136", "бакалеи")
        self.sale_household = Sale_Household("Иван", "15.12.1995", "14:37", "2 штуки", 68, "136р", "хоз. товары")

    def test_day_information(self):
        test_answer = 'сотрудник: Иван\nдата товара: 15.12.1995\nвремя: 14:37\nкол-во: 2 штуки\nцена: 68\nсумма: 136\nотдел: бакалеи'
        self.assertEqual(self.sale_groceries.info(),test_answer)

    def test_day_information2(self):
        test_answer = 'сотрудник: Иван\nдата товара: 15.12.1995\nвремя: 14:37\nкол-во: 2 штуки\nцена: 68\nсумма: 136р\nотдел: хоз. товары'
        self.assertEqual(self.sale_household.info(), test_answer)

    def test_discount_grocery(self):
        test_answer = 'Сегодня на товары из отдела "бакалеи" действует скидка. Нынешняя цена: 34.0'
        self.assertEqual(self.sale_groceries.discount_grocery(),test_answer)

    def test_discount_household(self):
        test_answer = 'Сегодня на товары из отдела "хоз. товары" действует скидка. Нынешняя цена: 34.0'
        self.assertEqual(self.sale_household.discount_household(),test_answer)



if __name__ == '__main__':
    unittest.main()