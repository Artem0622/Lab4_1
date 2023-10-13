#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    def __init__(self, first, second):
        if not isinstance(first, int) or not isinstance(second, int):
            raise ValueError("первый и второй должны быть целыми числами ")
        if second == 0:
            raise ValueError("'Секунда не равна нулю")

        self.first = first
        self.second = second

    def ipart(self):
        return self.first // self.second

    def display(self):
        print(f"{self.first}/{self.second}")

    @classmethod
    def read(cls):
        try:
            first = int(input("Введите сначало (числитель): "))
            second = int(input("Введите  (знаменатель):: "))
            return cls(first, second)
        except ValueError:
            print("Ошибка ввода. Пожалуйста введите целочисленное число 'первое' и 'второе'")
            return None


def make_pair():
    while True:
        try:
            pair = Pair.read()
            if pair is not None:
                return pair
        except KeyboardInterrupt:
            print("Operation aborted by user.")
            return None


if __name__ == "__main__":
    fraction = make_pair()
    if fraction:
        fraction.display()
        print("Integer part:", fraction.ipart())
