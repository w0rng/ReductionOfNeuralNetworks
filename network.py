from keras.models import Sequential
from keras.layers import Dense


class Network:
    def __init__(self, gen: list) -> None:
        # Количество нейронов в 1 слое
        self.inp = gen[0] 
        # Создание модели нейронной сети
        self.model = Sequential() 
        # Добавление 1 слоя
        self.model.add(Dense(gen[1], input_shape=(self.inp,), activation='relu'))
        # Добавление скрытых слоев
        for count in gen[2:-1]:
            self.model.add(Dense(count, activation='relu'))
        # Добавление выходного слоя
        self.model.add(Dense(gen[-1], activation='sigmoid'))

    # Компиляция модели
    def compile(self) -> None:
        self.model.compile(
            optimizer='sgd',
            loss='binary_crossentropy',
            metrics=['accuracy']
            )

    # Обучение модели
    def fit(self, X_train, Y_train, batch_size: int, epochs: int, validation_data: tuple) -> None:
            self.history = self.model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs, validation_data=validation_data, verbose=0)
    
    # Вычисление ошибки
    def mse(self, X_test, Y_test) -> float:
        result, _ = self.model.evaluate(X_test, Y_test, batch_size=self.inp, verbose=0)
        return result

    # Точность сети
    def accuracy(self) -> float:
        return self.history.history['acc'][-1]