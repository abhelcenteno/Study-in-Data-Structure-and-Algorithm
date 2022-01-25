class Node:

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, node_data):
        print('executed')
        self._data = node_data

    @property
    def next(self):
        return  self._next

    @next.setter
    def next(self, node_next):
        self._next = node_next

    def __str__(self):
        return str(self._data)