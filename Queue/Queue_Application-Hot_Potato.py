from Queue_Class import Queue


def hot_potato(name_list, num):
    name_queue = Queue()

    for name in name_list:
        name_queue.enqueue(name)

    while name_queue.size() > 1:
        for i in range(num):
            name_queue.enqueue(name_queue.dequeue())

        name_queue.dequeue()

    return name_queue.dequeue()


print(hot_potato(['Abhel', 'Lito', 'Centeno', 'Mari', 'Cris', 'Marivic', 'Crisolito'], 14))
print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))