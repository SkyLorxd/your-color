import matplotlib.pyplot as plt
from random import randint


# r = (
#     hex(int(input("Введите номер оттенка красного от 0 до 255: \n")))
#     .upper()[2:]
#     .zfill(2)
# )
# g = (
#     hex(int(input("Введите номер оттенка зеленого от 0 до 255: \n")))
#     .upper()[2:]
#     .zfill(2)
# )
# b = hex(int(input("Введите номер оттенка синего от 0 до 255: \n"))).upper()[2:].zfill(2)
r = hex(randint(0, 255)).upper()[2:].zfill(2)
g = hex(randint(0, 255)).upper()[2:].zfill(2)
b = hex(randint(0, 255)).upper()[2:].zfill(2)

plt.title("Ваш цвет")
plt.pie([1], colors=[f"#{r}{g}{b}"])
plt.show()
