from Deque_Class import Deque

def pal_checker(word):
    word_container = Deque()

    for letter in word:
        word_container.add_front(letter)

    while word_container.size() > 1:
        first_letter = word_container.remove_front()
        last_letter = word_container.remove_rear()
        if first_letter != last_letter:
            return False

    return True


print(pal_checker('shadjashdjkas'))
print(pal_checker('radar'))
print(pal_checker('nasabayabasan'))
print(pal_checker('abhelito'))
