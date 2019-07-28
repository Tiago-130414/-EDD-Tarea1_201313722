#importando librerias para manejo de consola
import sys
import os
#creando una clase nodo con un dato de tipo objeto por lo cual la lista puede ingresarse cualquier valor
class Nodo:
    def __init__(self,dato):
      self.dato = dato
      self.siguiente = None
#se crea una clase lista en la cual se definiran las funciones basicas como lo son insertar, eliminar, modificar y mostrar los elementos      
class Lista:
    #definiendo el constructor
    #option es la variable que guarda la opcion elegida del menu
    #cabezaLista es nuestra lista enlazada inicializada en null
    #menuL es el menu que contiene las operaciones que puede realizar nuestra lista simplemente enlazada
    def __init__(self):
        option = ""
        self.cabezaLista = None
        self.menuL()
    #se define el metodo agregarFinal el cual simplemente añade elementos al final de la lista
    def agregarFinal(self,nuevoDat):
        nuevoND = Nodo(nuevoDat)
        if self.cabezaLista is None:
            self.cabezaLista = nuevoND
            return   

        last = self.cabezaLista
        while (last.siguiente):
            last = last.siguiente

        last.siguiente = nuevoND
   #creando el metodo mostrar el cual lo unico que hace es recorrer la lista e imprimir en consola cada elemento encontrado
    def mostrar(self):
        temp = self.cabezaLista
        if temp != None:
            print("Valores En Lista: \n")
            while(temp):
                print(temp.dato +",")
                temp = temp.siguiente   
        else:
            print("Lista Vacia")     
    #eliminar como su nombre lo dice elimina un metodo mediante una referencia dada por el usuario
    def eliminar(self,elementoB):
        temp = self.cabezaLista

        if(temp is not None):
            if(temp.dato==elementoB):
                self.cabezaLista = temp.siguiente
    
                temp = None
                print("Elemento eliminado") 
                return

        while(temp is not None):
            if temp.dato==elementoB:
                break
            ant = temp
            temp = temp.siguiente

        if(temp==None):
            print("Elemento No Encontrado")
            return

        ant.siguiente = temp.siguiente
        temp = None    
        print("Elemento eliminado")
    #modificar es el metodo que mediante una referencia solicitada busca un valor y lo modifica
    def modificar(self,elementoM):
        temp = self.cabezaLista
        encontrado =False
        while(temp is not None):
            if temp.dato == elementoM:
                print("Ingrese nuevo valor: ")
                valNuevo = input() 
                encontrado = True
                break   
            temp = temp.siguiente       

        if encontrado ==True:
            temp.dato = valNuevo
            print("\n Valor modificado")
        else:
            print("Elemento no encontrado")
            return    
    #menuL es el menu de opciones que ayudara a el mejor control de las operaciones de la lista simple
    def menuL(self):
        while True:
            os.system("cls")
            print("\t--------Tarea 1 - 201313722--------")
            print("\t ------Lista Enlazada Simple------")
            print("1.- Insertar Elemento")
            print("2.- Modificar Elemento")
            print("3.- Mostrar Elementos")
            print("4.- Eliminar Elemento")
            print("5.- Salir")
            option = input()
            if option.__eq__("1"):
                self.insertarElemento()
            elif option.__eq__("2"):
                self.modificarElemento()
            elif option.__eq__("3"):
                self.mostrarElemento()
            elif option.__eq__("4"):
                self.eliminarElemento()
            elif option.__eq__("5"):
                os.system("cls")
                sys.exit()
            else:
                self.menuL()
    #funciones creadas para el mejor control del menu y para mejor visualizacion del codigo            
    #insertarElemento ayuda a control de la solicitud de valores para la insercion de datos            
    def insertarElemento(self):
        print("\n Ingrese el valor a insertar: ")
        val = input()
        self.agregarFinal(val)
        print("\n Insertado correctamente")
        os.system("pause")
    #modificarElemento ayuda a control de la modificacion de datos    
    def modificarElemento(self):
        print("\n Ingrese elemento a modificar: ")
        elmt = input()
        self.modificar(elmt)
        os.system("pause")
    #mostrarElemento ayuda a control de la visualizacion de los datos    
    def mostrarElemento(self):
        self.mostrar()
        os.system("pause")
    #eliminarElemento ayuda a control de la eliminacion de datos    
    def eliminarElemento(self):
        print("\n Ingrese elemento a eliminar: ")
        elmt = input()
        self.eliminar(elmt)    
        os.system("pause")   
          
lista = Lista()
