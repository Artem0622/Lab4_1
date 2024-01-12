#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    def __init__(self, first, second):
        if not isinstance(first, int) or not isinstance(second, int):
            raise TypeError("Оба поля (first и second) должны быть целыми числами")

        if second == 0:
            raise ValueError("Знаменатель (second) не может быть равен нулю")

        self.first = first
        self.second = second

    def ipart(self):
        """
        Возвращает целую часть от деления числителя на знаменатель.
        """
        if self.second != 0:
            return self.first // self.second
        else:
            raise ValueError("Невозможно вычислить целую часть при нулевом знаменателе")

    def display(self):
        print(f"({self.first}/{self.second})")

    @classmethod
    def read(cls):
        a = int(input("Введите числитель: "))
        b = int(input("Введите знаменатель: "))

        return cls(a, b)


def make_pair(first, second):
    try:
        return Pair(first, second)
    except (TypeError, ValueError) as e:
        print(f"Ошибка создания объекта Pair: {e}")
        exit()


if __name__ == "__main__":
    pair = Pair.read()
    pair.display()
    print("Целая часть:", pair.ipart())
