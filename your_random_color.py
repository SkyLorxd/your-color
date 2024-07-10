import matplotlib.pyplot as plt
from random import randint

r = hex(randint(0, 255)).upper()[2:].zfill(2)
g = hex(randint(0, 255)).upper()[2:].zfill(2)
b = hex(randint(0, 255)).upper()[2:].zfill(2)

plt.title("Ваш цвет")
plt.pie([1], colors=[f"#{r}{g}{b}"])
plt.show()
