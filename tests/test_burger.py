from classes.burger import Burger
from classes.bun import Bun
from classes.ingredient import Ingredient

class TestBurger:

    # проверка создания бургера
    def test_create_burger(self):
        burger = Burger()

        assert burger.bun == None
        assert burger.ingredients == []

    # проверка работы метода set_buns
    def test_method_set_buns(self):
        bun = Bun('Булочка с кунжутом', 10.00)

        burger = Burger()
        burger.set_buns(bun)

        assert burger.bun.name == 'Булочка с кунжутом'
        assert burger.bun.price == 10.00

    # проверка работы метода add_ingredient
    def test_method_add_ingredient(self):
        burger = Burger()
        burger.add_ingredient('Котлета')

        assert burger.ingredients == ['Котлета']

    # проверка работы метода remove_ingredient
    def test_method_remove_ingredient(self):
        burger = Burger()
        burger.add_ingredient('Котлета')
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    # проверка работы метода move_ingredient
    def test_method_move_ingredient(self):
        burger = Burger()
        burger.ingredients = ['Котлета', 'Огурец', 'Помидор']

        burger.move_ingredient(1, 2)

        assert burger.ingredients == ['Котлета', 'Помидор', 'Огурец']

    # проверка работы метода get_price
    def test_method_get_price(self):
        burger = Burger()

        bun = Bun('Булочка с кунжутом', 10.00)

        cutlet = Ingredient('Начинка', 'Котлета', 10.00)
        cucumber = Ingredient('Начинка', 'Огурец', 10.00)
        tomato = Ingredient('Начинка', 'Помидор', 10.00)

        burger.set_buns(bun)

        burger.add_ingredient(cutlet)
        burger.add_ingredient(cucumber)
        burger.add_ingredient(tomato)

        assert burger.get_price() == 50.00

    # проверка работы метода get_receipt
    def test_method_get_receipt(self):
        burger = Burger()

        bun = Bun('Булочка с кунжутом', 10.00)

        cutlet = Ingredient('Начинка', 'Котлета', 10.00)
        cucumber = Ingredient('Начинка', 'Огурец', 10.00)
        tomato = Ingredient('Начинка', 'Помидор', 10.00)

        burger.set_buns(bun)

        burger.add_ingredient(cutlet)
        burger.add_ingredient(cucumber)
        burger.add_ingredient(tomato)

        expected_receipt = "(==== Булочка с кунжутом ====)\n= начинка Котлета =\n= начинка Огурец =\n= начинка Помидор =\n(==== Булочка с кунжутом ====)\n\nPrice: 50.0"

        assert burger.get_receipt() == expected_receipt