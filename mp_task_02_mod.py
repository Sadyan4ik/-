import time
import asyncio
import math

# Функции для АТ-01

# запускать с n = 700008
def fibonacci(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')


# запускать с f, a, b, n равными соответственно math.sin, 0, math.pi, 20000000
def trapezoidal_rule(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')

async def async_fibonacci():
    await asyncio.to_thread(fibonacci, 700008)

async def async_trapezoidal_rule():
    await asyncio.to_thread(trapezoidal_rule, math.sin, 0, math.pi, 20000000)

async def asynchronous():
    start_time = time.time()
    await asyncio.gather(
        async_fibonacci(),
        async_trapezoidal_rule()
    )
    end_time = time.time()
    print(f'asyncio time: {end_time - start_time:0.2f} \n')

if __name__ == '__main__':
    asyncio.run(asynchronous())
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        fibonacci = 6
        trapezoidal_rule = 2.000000000000087
        asyncio time: 80.57 
    """








