from gen import Gen
from random import randint
from threading import Thread, activeCount
from time import sleep


# Количество особей для размножения
SAMPLE = 5
# Шанс мутации в процентах
MUTATION = 30
# Коичетсво эпох генетического алгоритма
EPOCHS = 3
# Макимальное количество нейронов в одном слое
MAX_COUNT = 30
# Максимальное количество слоев
MAX_LAUERS = 10
# Минимальное количество слоев
MIN_LAUERS = 3
# Количество обучений на тестовых данных
COUNT_REPIT = 25
# Коэффициент для расчета пригодности
K = 250


# Метод скрещиывания особей
def selection(being_one: Gen, being_two: Gen) -> list:
    window = randint(1, min(len(being_one.value), len(being_two.value))//2)
    gen = []
    for i in range(min(len(being_one.value), len(being_two.value))):
        if i % 2:
            gen += being_one.value[i*window: (i+1)*window]
        else:
            gen += being_two.value[i*window: (i+1)*window]
    gen = Gen(gen, MAX_COUNT, MAX_LAUERS, MIN_LAUERS, K)
    if randint(1, 100) <= MUTATION:
        gen.mutation()
    gen.value[-1] = 1
    return gen


# Главный метод программы
def main() -> None:
    # Первая популяция
    population = [Gen([], MAX_COUNT, MAX_LAUERS, MIN_LAUERS, K) for _ in range(SAMPLE)]

    print("_______________________________________")
    print("| Эпоха | Ошибка | Точность | Структура")

    for epoch in range(EPOCHS):
        temp = []
        # Скрещивание особей
        for being_one in population:
            for being_two in population:
                if not being_one is being_two:
                    temp.append(selection(being_one, being_two))
        population = temp

        # Обучение нейронных сетей
        for i, gen in enumerate(population):
            print(f'\33]0;Обучение {i+1}/{len(population)} | Эпоха {epoch+1}/{EPOCHS}\a', end='', flush=True)
            gen.create(COUNT_REPIT)

        # Выбор наилучших экземплярорв
        population = sorted(population, key=lambda x: x.check())[:-SAMPLE-1:-1]

        print("_______________________________________")
        print("| %5d | %.4f | %.6f |" % (epoch+1 ,population[0].mse(), population[0].accuracy()), population[0].value)


if __name__ == '__main__':
    main()
