class Person:

    def __init__(self, name='none', id='none'):
        assert type(name) == str
        assert type(id) == str

        self.name = name
        self.id = id
