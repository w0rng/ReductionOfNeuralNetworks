from network import Network
from random import randint
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

class Gen():
    def __init__(self, 
                value: list, 
                max_count: int, 
                max_lauers: int, 
                min_lauers: int,
                k: int
        ) -> None:
        self.max_count = max_count
        self.max_lauers = max_lauers
        self.min_lauers = min_lauers
        self.k = k
        if value:
            self.value = value
        else:
            # Если не передана стурктура нейронной сети, генерируем ее
            self.value = [10]
            self.value += [randint(1, self.max_count) for _ in range(randint(min_lauers - 2, max_lauers-2))]
            self.value += [1]

    # Создание и обучение нейронной сети
    def create(self, epochs: int) -> None:
        dataset = pd.read_csv('housepricedata.csv').values
        X = dataset[:,0:10]
        Y = dataset[:,10]
        min_max_scaler = preprocessing.MinMaxScaler()
        X_scale = min_max_scaler.fit_transform(X)

        X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)
        X_val, self.X_test, Y_val, self.Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
        self.network = Network(self.value)
        self.network.compile()
        self.network.fit(X_train, Y_train, self.value[0], epochs, (X_val, Y_val))

    # Расчет значения для отбора геномов
    def check(self) -> float:
        return self.network.accuracy()*self.k/sum(self.value)

    # Мутация гена
    def mutation(self) -> None:
        operator = randint(0, 2)
        if operator == 0 and len(self.value) > 2: # Изменение занчения
            self.value[randint(1, len(self.value)-2)] = randint(1, self.max_count)
        elif operator == 1 and len(self.value) < self.max_lauers: # Добавление слоя
            self.value.insert(randint(1, len(self.value)-1), randint(1, self.max_count))
        elif operator == 2 and len(self.value) > self.min_lauers: # Удаление слоя
            del self.value[randint(1, len(self.value)-2)]

    # Получение точности сети
    def accuracy(self) -> float:
        return self.network.accuracy()

    # Получение ошибки сети
    def mse(self) -> float:
        return self.network.mse(self.X_test, self.Y_test)