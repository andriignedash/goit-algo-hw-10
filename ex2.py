import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Аналітичне обчислення
analytical_result = (b**3 / 3) - (a**3 / 3)

# Метод Монте-Карло
N = 10000  # Кількість точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, b**2, N)

# Кількість точок під кривою
points_under_curve = np.sum(y_random < f(x_random))

# Площа прямокутника
rectangle_area = (b - a) * b**2

# Обчислення інтеграла методом Монте-Карло
monte_carlo_result = (points_under_curve / N) * rectangle_area

# Обчислення за допомогою функції quad
quad_result, _ = spi.quad(f, a, b)

# Порівняння результатів
print(f"Аналітичний результат: {analytical_result}")
print(f"Результат методом Монте-Карло: {monte_carlo_result}")
print(f"Результат за допомогою quad: {quad_result}")

# Побудова графіку для наочності
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від 0 до 2')
plt.grid()
plt.show()
