def format_duration(seconds):
    seconds_int = [1, 1 * 60, 1 * 60 * 60, 1 * 60 * 60 * 24, 1 * 60 * 60 * 24 * 365]
    seconds_str = ['second', 'minute', 'hour', 'day', 'year']
    i = 4
    answer = []

    while seconds:
        div = seconds // seconds_int[i]
        seconds = seconds % seconds_int[i]
        if div:
            if div > 1:
                answer.append(f'{div} {seconds_str[i]}s')
            else:
                answer.append(f'{div} {seconds_str[i]}')
        i -= 1


    return ', '.join(answer[:-1]) + f' and {answer[-1]}'


print(format_duration(3662))
