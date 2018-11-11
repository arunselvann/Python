import ctypes


class Array:
    def __init__(self, size):
        assert size > 0, "Array size must be greater than 0"
        self._size = size
        pyarraytype = ctypes.py_object * size
        self._elements = pyarraytype()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    def __init__(self, thearray):
        self._arrayRef = thearray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayref):
            entry = self._arrayred[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration