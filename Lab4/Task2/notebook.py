import re
from datetime import datetime


from Task2.note import Note


class NoteBook:

    def __init__(self, *args):
        if args:
            self.notes = list(args)
        else:
            self.__notes = []

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value):
        if not isinstance(value, list):
            raise TypeError
        if not all(isinstance(n, Note) for n in value):
            raise TypeError
        self.__notes = value

    def __iadd__(self, other):
        if not isinstance(other, Note):
            raise TypeError
        self.__notes.append(other)
        return self

    def __isub__(self, other):
        if not isinstance(other, Note):
            raise TypeError
        if not other in self.__notes:
            return self
        self.__notes.remove(other)
        return self

    def __mul__(self, other):
        if not isinstance(other, str):
            raise TypeError
        if not re.match('(0?[1-9]|[12][0-9]|3[0-1])\/(0?[1-9]|1[0-2])\/((19[2-9][0-9]|20[0-2][0-9]))', other):
            raise ValueError
        other = datetime.strptime(other, '%d/%m/%Y')
        for note in self.__notes:
            if note.birthday == other:
                return note


if __name__ == '__main__':
    note1 = Note('Pavlik', 'Morozov', '01/03/2004', '+380(66)-523-33-92')
    note2 = Note('Petya', 'Pushkin', '02/09/2010', '+380(55)-666-77-92')
    notebook = NoteBook()
    notebook += note1
    notebook -= note1
    notebook += note1
    notebook += note2
    print(notebook * '02/09/2010')