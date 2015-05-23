"Ejemplo de menu usando listas"

menu = [
    ["perro",3000],
    ["papas",1500],
    ["gaseosa",1500],
    ["hamburguesa",4000],
    ["empanada",1000],
    ["limonada",2000]
]

def consultar_precio(menu:list, articulo:str) -> int:
    """
    Retorna el precio asociado al articulo especificado o 0 si el articulo no existe en el menu
    """
    # for elem in menu:
    #     if elem[0]==articulo:
    #         return elem[1]
    # return 0
    i = 0
    while i < len(menu):
        if menu[i][0] == articulo:
            return menu[i][1]
        i+=1
    return 0


def cuenta_a_pagar(menu:list, pedido:list) -> int:
    """
    Retorna la cantidad a pagar segun el pedido hecho y el menu dado.
    Cada elemento del pedido esta compuesto por el articulo pedido y la cantidad
    """
    total = 0
    for p in pedido:
        precio = consultar_precio(menu,p[0])
        total += p[1] * precio
    return total*1.16


def cambio_de_precio(menu:list, articulo:str, valor:int) -> list:
    "Cambia el precio del articulo especificaado por el valor dado y retorna el nuevo menu"
    for elem in menu:
        if elem[0]== articulo:
            elem[1] = valor
    return menu



def menor_precio(menu:list) -> str:
    "Retorna el nombre del articulo con menor precio en el menu dado"
    menor = menu[0]
    for elem in menu:
        print(menor)
        if elem[1] < menor[1]:
            menor = elem
    return menor[0]



# print("Precio de papas:",consultar_precio(menu,"papas"))

# print("Precio de perro+gaseosa:",consultar_precio(menu,"perro")+consultar_precio(menu,"gaseosa"))

# print("Yo quiero.... ",menor_precio(menu))

# menu = cambio_de_precio(menu,"hamburguesa", 5000)
# print(menu)

p1 = [["hamburguesa",2],["gaseosa",2],["papas",3]]

print("Total a pagar: $", cuenta_a_pagar(menu,p1))
