import sys
import os
class Nodo:
    def __init__(self,dato):
      self.dato = dato
      self.siguiente = None
      
class Lista:
    def __init__(self):
        option = ""
        self.cabezaLista = None
        self.menuL()

    def agregarFinal(self,nuevoDat):
        nuevoND = Nodo(nuevoDat)
        if self.cabezaLista is None:
            self.cabezaLista = nuevoND
            return   

        last = self.cabezaLista
        while (last.siguiente):
            last = last.siguiente

        last.siguiente = nuevoND
   
    def mostrar(self):
        temp = self.cabezaLista
        if temp != None:
            print("Valores En Lista: \n")
            while(temp):
                print(temp.dato +",")
                temp = temp.siguiente   
        else:
            print("Lista Vacia")     

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
    def insertarElemento(self):
        print("\n Ingrese el valor a insertar: ")
        val = input()
        self.agregarFinal(val)
        print("\n Insertado correctamente")
        os.system("pause")
    def modificarElemento(self):
        print("\n Ingrese elemento a modificar: ")
        elmt = input()
        self.modificar(elmt)
        os.system("pause")
    def mostrarElemento(self):
        self.mostrar()
        os.system("pause")
    def eliminarElemento(self):
        print("\n Ingrese elemento a eliminar: ")
        elmt = input()
        self.eliminar(elmt)    
        os.system("pause")   
          
lista = Lista()