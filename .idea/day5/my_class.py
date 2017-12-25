class ee:
    def gg(self):
        print(id(self))
    @classmethod
    def dd(self):
        print(id(self))
    @staticmethod
    def ss():
        print(123)

d = ee()
e = ee()
d.gg()
e.gg()
d.dd()
e.dd()
d.ss()
