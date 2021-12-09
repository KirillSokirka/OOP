from datetime import datetime
import threading
import time
from statistics import mean


class DigitalCounter:

    def __init__(self, min_value, max_value, value):
        self.min_value = min_value
        self.max_value = max_value
        self.value = value

    @property
    def min_value(self):
        return self.__min_value

    @min_value.setter
    def min_value(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self.__min_value = value

    @property
    def max_value(self):
        return self.__max_value

    @max_value.setter
    def max_value(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value < self.min_value:
            raise ValueError
        self.__max_value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise TypeError
        if not value >= self.min_value and value < self.min_value:
            raise ValueError
        self.__value = value

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise TypeError
        if other < 0:
            raise ValueError
        if self.__value + other > self.max_value:
            self.__value = 0
            return self
        self.__value += other
        return self

    def __isub__(self, other):
        if not isinstance(other, int):
            raise TypeError
        if other < 0:
            raise ValueError
        if self.__value - other < self.min_value:
            self.__value = 0
            return self
        self.__value -= other
        return self


class StopWatch(DigitalCounter):

    def __init__(self, min_value, max_value, initial_value):
        super(StopWatch, self).__init__(min_value, max_value, initial_value)
        self.__start_measuring = None
        self.__measured_time = None

    def start(self):
        self.__start_measuring = datetime.now()

    def stop(self):
        if not self.__start_measuring:
            return ValueError()
        self.__measured_time = datetime.now() - self.__start_measuring

    @property
    def measured_time(self):
        if not self.__measured_time:
            return 0
        return self.__measured_time


class Results:

    def __init__(self, r):
        self.results = r

    @property
    def results(self):
        return self.__results

    @results.setter
    def results(self, value):
        if not isinstance(value, list):
            raise TypeError
        if not all(isinstance(r, StopWatch) for r in value):
            raise TypeError
        self.__results = value

    def get_min(self):
        return min(w.measured_time for w in self.__results)

    def get_max(self):
        return max(w.measured_time for w in self.__results)

    def find_average(self):
        return mean(w.measured_time for w in self.__results)

    def find_top_three(self):
        res = sorted(self.__results, key= lambda r: r.measured_time, reverse=True)
        if len(res) < 3:
            return res[0]
        return res[0:3]

    def __iter__(self):
        for res in self.__results:
            yield res


if __name__ == '__main__':
    counter = DigitalCounter(0, 60, 5)
    counter += 20
    print(counter.min_value)
    print(counter.max_value)
    print(counter.value)

    stopwatcher = StopWatch(0, 60, 5)
    print(f'Initial value {stopwatcher.value}')
    stopwatcher.start()
    print("Start, Enter something to stop counting")
    time.sleep(2)
    stopwatcher.stop()
    print(stopwatcher.measured_time)
    stopwatcher2 = StopWatch(0, 60, 5)
    stopwatcher3 = StopWatch(0, 60, 5)
    stopwatcher2.start()
    stopwatcher3.start()
    time.sleep(5)
    stopwatcher2.stop()
    time.sleep(3)
    stopwatcher3.stop()
    print(stopwatcher2.measured_time)
    print(stopwatcher3.measured_time)
    res = Results([stopwatcher, stopwatcher2, stopwatcher3])
    res.find_top_three()
    print('max' + res.get_max())
    print('results:')
    for r in res:
        print(r.measured_time)
