#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Money:
    def __init__(self, rubles=0, kopecks=0):
        self.rubles, self.kopecks = rubles, kopecks

    def read(self):
        self.rubles, self.kopecks = map(int, input("Введите количество рублей и копеек через пробел: ").split())

    def display(self):
        print(f"{self.rubles} руб. {int(self.kopecks):02d} коп.")

    def add(self, other):
        result = Money()
        total_kopecks = self.rubles * 100 + self.kopecks + other.rubles * 100 + other.kopecks
        result.rubles, result.kopecks = divmod(total_kopecks, 100)
        return result

    def subtract(self, other):
        result = Money()
        total_kopecks = self.rubles * 100 + self.kopecks - (other.rubles * 100 + other.kopecks)
        result.rubles, result.kopecks = divmod(total_kopecks, 100)
        return result

    def divide_sum(self, num):
        result = Money()
        total_kopecks = self.rubles * 100 + self.kopecks
        result_kopecks = total_kopecks / num
        result.rubles, result.kopecks = divmod(int(result_kopecks), 100)
        return result

    def divide_by_number(self, num):
        result = Money()
        total_kopecks = self.rubles * 100 + self.kopecks
        result_kopecks = total_kopecks / num
        result.rubles, result.kopecks = divmod(int(result_kopecks), 100)
        return result

    def multiply_by_number(self, num):
        result = Money()
        total_kopecks = self.rubles * 100 + self.kopecks
        result_kopecks = total_kopecks * num
        result.rubles, result.kopecks = divmod(result_kopecks, 100)
        return result

    def compare(self, other):
        return (self.rubles == other.rubles) and (self.kopecks == other.kopecks)

    def is_less_than(self, other):
        return (self.rubles * 100 + self.kopecks) < (other.rubles * 100 + other.kopecks)


if __name__ == '__main__':
    money1 = Money()
    money1.read()
    money1.display()

    money2 = Money()
    money2.read()
    money2.display()

    sum_result = money1.add(money2)
    print("Сумма:")
    sum_result.display()

    diff_result = money1.subtract(money2)
    print("Разность:")
    diff_result.display()

    divide_sum_num = float(input("Введите число для деления суммы: "))
    div_sum_result = money1.divide_sum(divide_sum_num)
    print("Деление суммы на число:")
    div_sum_result.display()

    divide_by_num = float(input("Введите число для деления: "))
    div_result = money1.divide_by_number(divide_by_num)
    print("Деление на число:")
    div_result.display()

    multiply_by_num = float(input("Введите число для умножения: "))
    mul_result = money1.multiply_by_number(multiply_by_num)
    print("Умножение на число:")
    mul_result.display()

    comparison_result = money1.compare(money2)
    print(f"Сравнение: {comparison_result}")

    comparison_result_lt = money1.is_less_than(money2)
    print(f"Сравнение меньше: {comparison_result_lt}")
