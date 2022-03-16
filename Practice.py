class User:
    def __init__(self, name_user, balance):
        self.name_user=name_user
        self.balance=balance
    def get_full_info(self):
            user = (f'Клиент "{self.name_user}".Баланс:{self.balance}' "руб")
            return user
client=User("Иван Петров", 50 )
print(client.get_full_info())


