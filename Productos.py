

class Productos():
    def __init__(self,id,name,type,stock,price):
        self.id=id
        self.name=name
        self.type=type
        self.stock=stock
        self.price=price

    def mostrar(self):
        return f"ID:{self.id}/Nombre:{self.name}/Tipo:{self.type}/Stock:{self.stock}/Precio:{self.price}"
        