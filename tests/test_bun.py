from classes.bun import Bun

class TestBun:

    # Проверка создания булочки с указанием названия и цены
    def test_create_bun_with_name_and_price(self):
        bun = Bun('Булочка с кунжутом', 10.00)

        assert bun.name == 'Булочка с кунжутом'
        assert bun.price == 10.00

    # проверка работы метода get_name
    def test_method_get_name(self):
        bun = Bun('Булочка с кунжутом', 10.00)

        assert bun.get_name() == 'Булочка с кунжутом'

    # проверка работы метода get_price
    def test_method_get_price(self):
        bun = Bun('Булочка с кунжутом', 10.00)

        assert bun.get_price() == 10.00