# 2. Базовый класс User и производные классы для различных типов пользователей


class User:
    """
    Базовый класс, представляющий пользователя.
    """

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def get_details(self) -> str:
        return f"Пользователь: {self.username}, Email: {self.email}"

    def __str__(self) -> str:
        return self.username


class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    """

    def __init__(self, username: str, email: str, address: str) -> None:
        super().__init__(username, email)
        self.address = address

    def get_details(self) -> str:
        return f"Клиент: {self.username}, Email: {self.email}, Адрес: {self.address}"


class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """

    def __init__(self, username: str, email: str, admin_level: int) -> None:
        super().__init__(username, email)
        self.admin_level = admin_level

    def get_details(self) -> str:
        return f"Admin: {self.username}, Email: {self.email}, Admin-Level: {self.admin_level}"
