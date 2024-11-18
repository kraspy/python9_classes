# 3. Класс для управления корзиной покупок
from .users import User, Admin
from .products import Product


class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """

    def __init__(self, user: User, registrator: Admin) -> None:
        self.items: list = []
        self.user = user
        self.registrator = registrator

    def add_item(self, product: Product, quantity: int):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})

    def remove_item(self, product_name: str) -> None:
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self) -> int | float:
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total: int | float = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total

    def get_details(self) -> str:
        """
        Возвращает детализированную информацию о содержимом корзины и общей стоимости.
        """
        details: str = f'Покупатель {self.user} приобрел:\n'
        for item in self.items:
            details += f"- {item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        details += f"Общая сумма: {self.get_total()} руб\n"
        details += f"Зарегистрировал покупки пользователь {self.registrator}"

        return details
