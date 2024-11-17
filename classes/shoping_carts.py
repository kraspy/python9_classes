# 3. Класс для управления корзиной покупок


class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """

    def __init__(self, user, registrator):
        self.items = []
        self.user = user
        self.registrator = registrator

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})

    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total

    def get_details(self):
        """
        Возвращает детализированную информацию о содержимом корзины и общей стоимости.
        """
        details = f'Покупатель {self.user} приобрел:\n'
        for item in self.items:
            details += f"- {item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        details += f"Общая сумма: {self.get_total()} руб\n"
        details += f"Зарегистрировал покупки пользователь {self.registrator}"

        return details
