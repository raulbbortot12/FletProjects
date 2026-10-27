class Book(object):
    def __init__(self, title: str, author: str, desc: str, price: float, cover: str = '', id: int = None):
        self.id = id  # preenchido pelo banco (AUTOINCREMENT)
        self.title = title
        self.author = author
        self.desc = desc
        self.price = price
        self.cover = cover
    def __repr__(self):
        return f"Book(id={self.id}, title={self.title}, author={self.author}, cover={self.cover})"
