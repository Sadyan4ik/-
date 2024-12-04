import threading
import time
import multiprocessing
import math
import requests

# список url для АТ-01
urls = ['https://www.example.com'] * 50


def fetch_url(url):
    response = requests.get(url)
    return response.text


def sequence():
    start_time = time.perf_counter()
    for url in urls:
        fetch_url(url)
    end_time = time.perf_counter()
    print(f'sequence time: {end_time - start_time:0.2f} \n')


def threads():
    start_time = time.perf_counter()
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.perf_counter()
    print(f'threads time: {end_time - start_time:0.2f} \n')


def processes():
    start_time = time.perf_counter()
    with multiprocessing.Pool(len(urls)) as pool:
        pool.map(fetch_url, urls)
    end_time = time.perf_counter()
    print(f'processes time: {end_time - start_time:0.2f} \n')


if __name__ == '__main__':
    processes()
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):

        sequence time: 6.37 

        threads time: 0.67 

        processes time: 1.06 
    """









