import random  # Импортируем модуль random для возможного использования случайных событий

# Класс Hero
class Hero:
    def __init__(self, name):  # Конструктор класса Hero
        self.name = name  # Имя героя
        self.health = 100  # Здоровье героя (начальное значение 100)
        self.attack_power = 20  # Сила удара героя (начальное значение 20)

    def attack(self, other):  # Метод для атаки другого героя
        damage = self.attack_power  # Урон равен силе удара
        other.health -= damage  # Уменьшаем здоровье другого героя на величину урона
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")  # Выводим информацию об атаке

    def is_alive(self):  # Метод для проверки, жив ли герой
        return self.health > 0  # Возвращает True, если здоровье больше 0, иначе False

# Класс Game
class Game:
    def __init__(self, player_name):  # Конструктор класса Game
        self.player = Hero(player_name)  # Создаем героя для игрока
        self.computer = Hero("Компьютер")  # Создаем героя для компьютера

    def start(self):  # Метод для запуска игры
        print("Начало игры! Битва начинается!")  # Выводим сообщение о начале игры
        current_turn = 0  # Переменная для отслеживания текущего хода (0 - ход игрока, 1 - ход компьютера)

        while self.player.is_alive() and self.computer.is_alive():  # Цикл, пока оба героя живы
            if current_turn == 0:  # Если ход игрока
                print(f"\nХод игрока {self.player.name}:")  # Выводим сообщение о ходе игрока
                self.player.attack(self.computer)  # Игрок атакует компьютер
                print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")  # Выводим оставшееся здоровье компьютера
            else:  # Если ход компьютера
                print(f"\nХод компьютера {self.computer.name}:")  # Выводим сообщение о ходе компьютера
                self.computer.attack(self.player)  # Компьютер атакует игрока
                print(f"У {self.player.name} осталось {self.player.health} здоровья.")  # Выводим оставшееся здоровье игрока

            current_turn = 1 - current_turn  # Меняем ход (0 -> 1 или 1 -> 0)

        # Определение победителя
        if self.player.is_alive():  # Если игрок жив
            print(f"\n{self.player.name} побеждает! Ура!")  # Выводим сообщение о победе игрока
        else:  # Если компьютер жив
            print(f"\n{self.computer.name} побеждает. Попробуйте еще раз!")  # Выводим сообщение о победе компьютера

# Основной блок программы
if __name__ == "__main__":  # Проверяем, запущен ли скрипт напрямую
    print("Добро пожаловать в игру 'Битва героев'!")  # Приветственное сообщение
    player_name = input("Введите имя вашего героя: ")  # Запрашиваем имя игрока
    game = Game(player_name)  # Создаем экземпляр игры с именем игрока
    game.start()  # Запускаем игру