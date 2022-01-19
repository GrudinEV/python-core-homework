import functools
import time

from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """

    def wrapper(func):
        # put your code here
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            allTime = 0
            for _ in range(num):
                start = time.time()
                func(*args, **kwargs)
                duration = time.time() - start
                print(duration)
                allTime += duration
            print(allTime / num)
        return wrapper_repeat
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
