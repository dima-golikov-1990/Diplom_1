from classes.ingredient import Ingredient

class TestIngredient:

    # проверка создания ингредиента со всеми параметрами
    def test_create_ingredient_with_all_parameters(self):
        ingredient = Ingredient('Соус', 'Чесночный', 5.00)

        assert ingredient.type == 'Соус'
        assert ingredient.name == 'Чесночный'
        assert ingredient.price == 5.00

    # проверка работы метода get_type
    def test_method_get_type(self):
        ingredient = Ingredient('Соус', 'Чесночный', 5.00)

        assert ingredient.get_type() == 'Соус'

    # проверка работы метода get_name
    def test_method_get_name(self):
        ingredient = Ingredient('Соус', 'Чесночный', 5.00)

        assert ingredient.get_name() == 'Чесночный'

    # проверка работы метода get_price
    def test_method_get_price(self):
        ingredient = Ingredient('Соус', 'Чесночный', 5.00)

        assert ingredient.get_price() == 5.00