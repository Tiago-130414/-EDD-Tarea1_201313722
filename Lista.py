import sys
import os
class Nodo:
    def __init__(self,dato):
      self.dato = dato
      self.next = None
class Lista:
    def __init__(self):
        option = ""
        self.head = None
        self.menuL()

    def agregarFinal(self,nuevo_dato):
        nuevo_nodo = Nodo(nuevo_dato)
        if self.head is None:
            self.head = nuevo_nodo
            return   

        last = self.head
        while (last.next):
            last = last.next

        last.next = nuevo_nodo
   
    def mostrar(self):
        temp = self.head
        if temp != None:
            print("Valores En Lista: \n")
            while(temp):
                print(temp.dato +",")
                temp = temp.next
        else:
            print("Lista Vacia")     

    def eliminar(self,elementoB):
        temp = self.head

        if(temp is not None):
            if(temp.dato==elementoB):
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if temp.dato==elementoB:
                break
            prev = temp
            temp = temp.next

        if(temp==None):
            print("Elemento No Encontrado")
            return

        prev.next = temp.next
        temp = None    

    def modificar(self,elementoM):
        temp = self.head
        while(temp is not None):
            if temp.dato == elementoM:
                print("Ingrese nuevo valor: ")
                valNuevo = input()
                break
            
            temp = temp.next
        
        temp.dato = valNuevo

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
        print("\n Valor modificado")
        os.system("pause")
    def mostrarElemento(self):
        self.mostrar()
        os.system("pause")
    def eliminarElemento(self):
        print("\n Ingrese elemento a eliminar: ")
        elmt = input()
        self.eliminar(elmt)    
        print("Elemento eliminado") 
        os.system("pause")   
          
lista = Lista()