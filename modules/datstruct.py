import pickle


class DataChain:
    def __init__(self):
        self._head = None
        self._tail = None

    def add(self, data):
        data._next = data._prev = None
        if not self._head:
            self._head = self._tail = data
        else:
            self._tail._next = data
            data._prev = self._tail
            self._tail = data

    def search(self, search):
        for item in self:
            if search in item._data[1]:
                yield item

    def serialize(self):
        data = list()
        for item in self:
            data.append(pickle.dumps(item))
        return pickle.dumps(data)

    def load(self, data):
        data = pickle.loads(data)
        for elem in data:
            self.add(pickle.loads(elem))

    def __iter__(self):
        cur = self._head
        while True:
            yield cur
            if cur._next == None:
                break
            cur = cur._next
