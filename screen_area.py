class Area:
    def __init__(self, coords: tuple = (0, 0, 0, 0)):
        self.coords = coords

    @property
    def width(self):
        return self.x2 - self.x1

    @property
    def height(self):
        return self.y2 - self.y1

    @property
    def geometry(self):
        return self.x1, self.y1, self.width, self.height

    @property
    def coords(self):
        return self.x1, self.y1, self.x2, self.y2

    @coords.setter
    def coords(self, coords: tuple = (0, 0, 0, 0)):
        self.x1, self.y1, self.x2, self.y2 = coords

    @staticmethod
    def from_text(text: str) -> 'Area':
        coords = text.split(", ")
        int_tup = tuple(int(number) for number in coords)
        return Area(int_tup)

    def swap_x(self):
        self.x1, self.x2 = self.x2, self.x1

    def swap_y(self):
        self.y1, self.y2 = self.y2, self.y1

    def to_text(self) -> str:
        return str.join(", ", [str(pos) for pos in self.coords])

    def __str__(self):
        return self.to_text()
