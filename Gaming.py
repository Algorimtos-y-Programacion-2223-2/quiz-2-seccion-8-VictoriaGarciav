from Productos import Productos

class Gaming(Productos):
    def __init__(self,id,name,type,stock,price):
        super().__init__(self,id,name,type,stock,price)

    def mostrar(self):
        return f"ID:{self.id}/Nombre:{self.name}/Tipo:{self.type}/Stock:{self.stock}/Precio:{self.price}"