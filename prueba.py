class Prueba:
    def __init__(self, x=2):
        self.x = x
        self.y = x * 2

    def devuelve_datos(self):
        return "Con x=%i obtenemos: y=%i" % (self.x, self.y)


if __name__ == "__main__":
    a1 = Prueba(2)
    print(a1.devuelve_datos())
    a2 = Prueba(3)
    print(a2.devuelve_datos())
