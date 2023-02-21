class Author():
    def __init__(self, id, first_name=None, last_name=None) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def to_JSON(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
