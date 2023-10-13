#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Money:
    def __init__(self, rubles, kopecks):
        self.rubles = rubles
        self.kopecks = kopecks

    def read(self):
        try:
            self.rubles = int(input("Введите количество рублей: "))
            self.kopecks = int(input("Введите количество копеек: "))
        except ValueError:
            print("Некорректный ввод. Введите целое число.")

    def display(self):
        print(f"{self.rubles} руб. {self.kopecks} коп.")

    def __add__(self, other):
        total_kopecks = self.rubles * 100 + self.kopecks + other.rubles * 100 + other.kopecks
        new_rubles = total_kopecks // 100
        new_kopecks = total_kopecks % 100
        return Money(new_rubles, new_kopecks)

    def __sub__(self, other):
        total_kopecks = self.rubles * 100 + self.kopecks - (other.rubles * 100 + other.kopecks)
        new_rubles = total_kopecks // 100
        new_kopecks = total_kopecks % 100
        return Money(new_rubles, new_kopecks)

    def __truediv__(self, other):
        if other == 0:
            raise ValueError("Деление на ноль недопустимо.")
        total_kopecks = self.rubles * 100 + self.kopecks
        result = total_kopecks / other
        new_rubles = int(result)
        new_kopecks = round((result - new_rubles) * 100)
        return Money(new_rubles, new_kopecks)

    def __mul__(self, other):
        total_kopecks = self.rubles * 100 + self.kopecks
        result = total_kopecks * other
        new_rubles = int(result // 100)
        new_kopecks = int(result % 100)
        return Money(new_rubles, new_kopecks)

    def __eq__(self, other):
        return (self.rubles, self.kopecks) == (other.rubles, other.kopecks)

    def __lt__(self, other):
        return (self.rubles, self.kopecks) < (other.rubles, other.kopecks)

    def __le__(self, other):
        return (self.rubles, self.kopecks) <= (other.rubles, other.kopecks)

    def __str__(self):
        return f"{self.rubles} руб. {self.kopecks} коп."


if __name__ == '__main__':
    money1 = Money(10, 50)
    money2 = Money(5, 75)

    print("Деньги 1:")
    money1.display()

    print("Деньги 2:")
    money2.display()

    # Примеры операций
    print("\nОперации:")
    result = money1 + money2
    print("Сумма:")
    result.display()

    result = money1 - money2
    print("Разность:")
    result.display()

    result = money1 / 2.5
    print("Деление на число:")
    result.display()

    result = money1 * 3
    print("Умножение на число:")
    result.display()

    print("Сравнение:")
    print(f"money1 равно money2: {money1 == money2}")
    print(f"money1 меньше money2: {money1 < money2}")
