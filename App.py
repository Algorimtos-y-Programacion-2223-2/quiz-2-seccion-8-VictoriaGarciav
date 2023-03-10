from Hogar import Hogar
from Gaming import Gaming
from Ropa import Ropa


class App:
    products = [
        { "id": 1, "name": "Nevera", "type": "Hogar", "stock": 753, "price": 800 },
        { "id": 2, "name": "Cama", "type": "Hogar", "stock": 327, "price": 600  },
        { "id": 3, "name": "Suéter", "type": "Ropa", "stock": 260, "price": 25 },
        { "id": 4, "name": "Zapatos", "type": "Ropa", "stock": 593, "price": 5 },
        { "id": 5, "name": "Laptop Gamer", "type": "Gaming", "stock": 11, "price": 2500 },
        { "id": 6, "name": "Nintendo Switch OLED", "type": "Gaming", "stock": 25, "price": 400 }]

    new_product={"Hogar":[],"Ropa":[],"Gaming":[]}
        
    def cargar_products(self):
        products = [
        { "id": 1, "name": "Nevera", "type": "Hogar", "stock": 753, "price": 800 },
        { "id": 2, "name": "Cama", "type": "Hogar", "stock": 327, "price": 600  },
        { "id": 3, "name": "Suéter", "type": "Ropa", "stock": 260, "price": 25 },
        { "id": 4, "name": "Zapatos", "type": "Ropa", "stock": 593, "price": 5 },
        { "id": 5, "name": "Laptop Gamer", "type": "Gaming", "stock": 11, "price": 2500 },
        { "id": 6, "name": "Nintendo Switch OLED", "type": "Gaming", "stock": 25, "price": 400 }]

        for lista in range(len(products)):
            range += 1

            self.products[lista]['id']
            self.products[lista]['name']
            self.products[lista]['type']
            self.products[lista]['stock']
            self.products[lista]['price']


            for type,lista in self.products[lista].items():
                for type in lista:
                    if type=="Hogar":
                        b =type(lista['id'],lista['name'],lista['type'],lista['stock'],lista['price'])
                    elif type=="Ropa":
                        e =type(lista['id'],lista['name'],lista['type'],lista['stock'],lista['price'])
                    else:
                        d =type(lista['id'],lista['name'],lista['type'],lista['stock'],lista['price'])

            b=self.products(type["Hogar"])
            self.new_product["Hogar"].append(b)
            e=self.products(type["Ropa"])
            self.new_product["Ropa"].append(e)
            d=self.products(type["Gaming"])
            self.new_product["Gaming"].append(d)


    def ver(self):

        print("""Elija que desea ver del inventario:
              1.Hogar
              2.Ropa
              3.Gaming
              """)
        
        option_1=input("Ingrese el número de las opciones que quisiera ver:")

        while not option_1.isnumeric():
            print("Error!")
            option_1=input("Ingrese un número de las opciones")
        option_1=int(option_1)

        if option_1=="1":
            print(self.new_product["Hogar"])

        elif option_1=="2":
            print(self.new_product["Ropa"])
        
        else:
            print(self.new_product["Gaming"])

    def agregar_producto(self):

        print("""Elija que tipo de bedida quisiera agregar al inventario:
        1.Hogar
        2.Ropa
        3.Gaming
        """)

        agregar=input("Ingrese el número de las opciones:")
        while not agregar.isnumeric():
            print("Error!!")
            agregar=input("Ingrese un número de las opciones:")
        agregar=int(agregar)

        name=input("")

        if agregar == "1":


    def start(self):
        self.cargar_products
        while True:
            opcion=input("""Bienvenido a la tienda Super Samancito!
            1.Agregar Producto
            2.Ver productos
            3.Salir
            Ingrese opcion que desee:
            """)
            if opcion=="1":
                self.agregar_producto()
            elif opcion=="2":
                self.ver()
            else:
                print("Hasta pronto!")
                break
