from classes.database import Database
from classes.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    # проверка создания и инициализации базы данных
    def test_create_database(self):
        database = Database()

        assert database.buns[0].name == "black bun"
        assert database.buns[1].name == "white bun"
        assert database.buns[2].name == "red bun"

        assert database.buns[0].price == 100
        assert database.buns[1].price == 200
        assert database.buns[2].price == 300

        assert database.ingredients[0].type == INGREDIENT_TYPE_SAUCE
        assert database.ingredients[1].type == INGREDIENT_TYPE_SAUCE
        assert database.ingredients[2].type == INGREDIENT_TYPE_SAUCE

        assert database.ingredients[3].type == INGREDIENT_TYPE_FILLING
        assert database.ingredients[4].type == INGREDIENT_TYPE_FILLING
        assert database.ingredients[5].type == INGREDIENT_TYPE_FILLING

        assert database.ingredients[0].name == "hot sauce"
        assert database.ingredients[1].name == "sour cream"
        assert database.ingredients[2].name == "chili sauce"
        assert database.ingredients[3].name == "cutlet"
        assert database.ingredients[4].name == "dinosaur"
        assert database.ingredients[5].name == "sausage"

        assert database.ingredients[0].price == 100
        assert database.ingredients[1].price == 200
        assert database.ingredients[2].price == 300
        assert database.ingredients[3].price == 100
        assert database.ingredients[4].price == 200
        assert database.ingredients[5].price == 300

    # проверка работы метода available_buns
    def test_method_available_buns(self):
        database = Database()

        assert database.available_buns() == database.buns

    # проверка работы метода available_ingredients
    def test_method_available_ingredients(self):
        database = Database()

        assert database.available_ingredients() == database.ingredients
