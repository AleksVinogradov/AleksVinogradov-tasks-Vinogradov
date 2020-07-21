import numpy as np


def game_score_best(number, min_number, max_number):
    """Предполагаем число из середины загаданного интервала. В зависимости от информации больше/меньше
    далее предполагаем число из середины интервала, где находится загаданное число и т.д.
    Функция принимает загаданное число, а также минимальное и максимальное число из интервала.
    На выходе возвращает число попыток"""
    count = 1                                             # счетчик попыток
    predict = int((min_number+max_number) / 2)            # предполагаемое число в середине загаданного интервала
    
    while number != predict:                        
        count += 1
        if number > predict:                              # если загаданное число больше предполагаемого
            min_number = predict + 1                      # минимальная граница интервала сдвигется
            predict = int((min_number+max_number) / 2)    # осуществляется поиск в середине полученного интервала
        elif number < predict:                            # если загаданное число меньше предполагаемого
            max_number = predict - 1                      # максимальная граница интервала сдвигется
            predict = int((min_number+max_number) / 2)    # осуществляется поиск в середине полученного интервала
    return count                                          # выход из цикла


def score_game(game_score, min_number=1, max_number=100):  
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число.
    Аргументы min_number и max_number задают диапазон поиска"""
    count_ls = []
    np.random.seed(1)                                      # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(min_number, max_number + 1, size=1000)
    for number in random_array:
        count_ls.append(game_score(number, min_number, max_number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_score_best)
