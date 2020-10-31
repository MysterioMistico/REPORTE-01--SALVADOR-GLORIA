#Estudiante: Salvador Gloria Abad

#Carga de listas
from lifestore_file import lifestore_searches
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products

#Bienvenida

print("##################### Bienvenido ##################")
print('\n')

#Usuarios Dirección y Operaciones 
usuario_direc = "Salvador_Gloria"
pwd_direc = "321"
usuario_opera = "Operaciones"
pwd_opera = "123"

#Login
user = input("Ingrese Usuario: ")
pwd = input("\nIngrese Contraseña: ")

#Limpieza pantalla
import os, sys

def cleaning():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')
        
if __name__ == '__main__':
    cleaning()

#Menú usuario Dirección
if user == usuario_direc and pwd == pwd_direc:
  print("\n ***** Bienvenido su excelencia *****")
  print("\n ***1. Productos & Top Productos ***")
  print("\n ***2. Reseña de productos ***")
  print("\n ***3. Inventario ***\n")
  opc=input("Seleccione una opción:")
  if opc == "1":
    print("\n * Productos & Top Productos *")

#Encontrar categorias participantes
    categories = [lifestore_products[0][3]]
    for product in lifestore_products:
      new_category = 0
      for category in categories:
        if product[3] == category:
          continue
        else:
          new_category +=1
        if new_category+1 > len(categories):
          categories.append(product[3])
    print("\n # Categorias Participantes #\n")
    for total_category in categories:
      print(total_category)
    #join id_product y category para venta
    for category in categories:
      top_list = []
      for product in lifestore_products:
        sales_product = 0
        for sale in lifestore_sales:
          if product[0] == sale[1] and product[3] == category:
            sales_product +=1
        if product[3] == category:
          top_list.append([sales_product, product])
    top_list.sort(reverse=True)
    print("\n # Top 50 Articulos #\n")
    print(top_list[:50])
    print("\n # Top Articulos menos vendidos #\n")
    desc = top_list
    desc.sort()
    print(desc[0:5])
      

# productos participantes
  elif opc == "2":
    print("\n * Reseña de prodcutos *\n")
    print("\n")
    products = [lifestore_products[0][1]]
    for total_product in lifestore_products:
      new_product = 0
      for product in products:
        if total_product[1] == product:
          continue
        else:
          new_product +=1
        if new_product+1 > len(products):
          products.append(total_product[1])
    print("\n # Productos Participantes #")
    for all_products in products:
      print(all_products)
  
  #Estrellas
    for product in products:
      top_list = []
      for total_product in lifestore_products:
        sales_product = 0
        for sale in lifestore_sales:
          if total_product[0] == sale[1] and total_product[2] == total_product:
            sales_product +=1
        if product[2] == total_product:
          top_list.append([sales_product, product])
          top_list.sort(reverse=True)
          print("\n # Top 10 Articulos #\n")
          print(top_list[:10])


  elif opc == "3":
    print("\n * Inventario *\n")
    products = [lifestore_products[0][1]]
    for product in lifestore_products:
      new_product = 0
      for product_inv in products:
        if product[1] == product_inv:
          continue
        else:
          new_product +=1
        if new_product+1 > len(products):
          products.append(product[1])
          print("\n ")
          for w in products:
            print(w)
            #Inventario total
            filas = len (lifestore_products)
            columnas = len (lifestore_products[0])
            print(filas, columnas)
  
            nueva_fila = []
            for j in range(columnas):
              suma = int(sum(fila[j] for fila in lifestore_products))
              nueva_fila.append(suma)
              print(nueva_fila)

  else:
    print("\n * Opción no valida, Verifique *")

#menú usuario operaciones
elif user == usuario_opera and pwd == pwd_opera:
  print("\n ***Bienvenido su excelencia***")
  print("\n ***1. Top de productos ***")
  opc=input("Seleccione una opción:")
  if opc == "1":
    print("\n * Top de Productos \n*")
    #Encontrar categorias participantes
    categories = [lifestore_products[0][3]]
    for product in lifestore_products:
      new_category = 0
      for category in categories:
        if product[3] == category:
          continue
        else:
          new_category +=1
        if new_category+1 > len(categories):
          categories.append(product[3])
    print("\n # Categorias Participantes #")
    for total_category in categories:
      print(total_category)
    #join id_product y category para venta
    for category in categories:
      top_list = []
      for product in lifestore_products:
        sales_product = 0
        for sale in lifestore_sales:
          if product[0] == sale[1] and product[3] == category:
            sales_product +=1
        
        if product[3] == category:
          top_list.append([sales_product, product])
    top_list.sort(reverse=True)
    print("\n # Top 50 Articulos #\n")
    print(top_list[:50])
  else:
    print("\n * Opción no valida, Verifique *")
else:
  print("\n Usuario o contraseña inválido. Favor de pasar a Recursos Humanos ¡!")


