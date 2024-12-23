import threading
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Крокодизм № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Взятие текущего времени
start_time = datetime.now()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
end_time = datetime.now()
print(f"Работа функций {end_time - start_time}")

# Взятие текущего времени
start_time_threads = datetime.now()

# Создание потоков
threads = []
threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения потоков
for thread in threads:
    thread.join()

# Взятие текущего времени
end_time_threads = datetime.now()
print(f"Работа потоков {end_time_threads - start_time_threads}")