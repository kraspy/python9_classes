# 1. Базовый класс Product и производные классы для различных типов продуктов


class Product:
    """
    Базовый класс, представляющий продукт.
    """

    def __init__(self, name: str, price: int | float) -> None:
        self.name = name
        self.price = price

    def get_details(self) -> str:
        return f"Продукт: {self.name}, Цера: {self.price} руб."


class Electronics(Product):
    """
    Класс, представляющий электронный продукт, наследующий класс Product.
    """

    def __init__(self, name: str, price: int | float, brand: str, warranty_period: int) -> None:
        super().__init__(name, price)
        self.brand = brand
        self.warranty_period = warranty_period

    def get_details(self):
        return (
            f"Электроника: {self.name}, "
            f"Бренд: {self.brand}, "
            f"Цена: {self.price} руб, "
            f"Гарантия: {self.warranty_period} лет"
        )


class Clothing(Product):
    """
    Класс, представляющий одежду, наследующий класс Product.
    """

    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def get_details(self):
        return f"Одежда: {self.name}, Размер: {self.size}, Материал: {self.material}, Цена: {self.price} руб."


class Сhemicals(Product):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def get_details(self):
        return f"Бытовая химия: {self.name}, Тип: {self.type}, Цена: {self.price} руб."
