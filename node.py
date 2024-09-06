class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.prev = None
        self.next = None

class ListaDobleEnlazada:
    def __init__(self):
        self.head = None
        self.tail = None

    # Añadir un nodo al final de la lista
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.head is None:  
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            nuevo_nodo.prev = self.tail
            self.tail.next = nuevo_nodo
            self.tail = nuevo_nodo

    # Función para eliminar un nodo dado
    def eliminar_nodo(self, nodo_a_eliminar):
        # Si la lista está vacía o el nodo a eliminar es None, no hacemos nada
        if self.head is None or nodo_a_eliminar is None:
            return

        # Si el nodo a eliminar es el head
        if nodo_a_eliminar == self.head:
            self.head = nodo_a_eliminar.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None

        # Si el nodo a eliminar es el tail
        elif nodo_a_eliminar == self.tail:
            self.tail = nodo_a_eliminar.prev
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None

        # Si el nodo a eliminar está en el medio
        else:
            nodo_a_eliminar.prev.next = nodo_a_eliminar.next
            nodo_a_eliminar.next.prev = nodo_a_eliminar.prev

        # Desvincular el nodo a eliminar
        nodo_a_eliminar.prev = None
        nodo_a_eliminar.next = None

    # Función para recorrer la lista hacia atrás y mostrar los valores
    def recorrer_hacia_atras(self):
        actual = self.tail
        while actual is not None:
            print(actual.valor)
            actual = actual.prev


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.prev = None
        self.next = None

class ListaCircularDobleEnlazada:
    def __init__(self):
        self.head = None

    # Función para insertar un nodo en una posición específica
    def insertar(self, valor, posicion):
        nuevo_nodo = Nodo(valor)

        # Si la lista está vacía
        if self.head is None:
            self.head = nuevo_nodo
            nuevo_nodo.next = nuevo_nodo
            nuevo_nodo.prev = nuevo_nodo
            return

        # Si la posición es 0, insertar al inicio
        if posicion == 0:
            ultimo = self.head.prev  # Nodo actual en la posición de la cola
            nuevo_nodo.next = self.head
            nuevo_nodo.prev = ultimo
            self.head.prev = nuevo_nodo
            ultimo.next = nuevo_nodo
            self.head = nuevo_nodo
            return

        # Insertar en cualquier otra posición
        actual = self.head
        contador = 0

        # Recorrer la lista hasta la posición dada
        while contador < posicion - 1 and actual.next != self.head:
            actual = actual.next
            contador += 1

        # Inserción en la posición dada
        siguiente = actual.next
        actual.next = nuevo_nodo
        nuevo_nodo.prev = actual
        nuevo_nodo.next = siguiente
        siguiente.prev = nuevo_nodo

    # Función para eliminar un nodo dado
    def eliminar_nodo(self, nodo_a_eliminar):
        # Si la lista está vacía o el nodo a eliminar es None
        if self.head is None or nodo_a_eliminar is None:
            return

        # Si solo hay un nodo en la lista
        if nodo_a_eliminar == self.head and nodo_a_eliminar.next == self.head:
            self.head = None
            return

        # Si el nodo a eliminar es el head
        if nodo_a_eliminar == self.head:
            ultimo = self.head.prev
            self.head = self.head.next
            self.head.prev = ultimo
            ultimo.next = self.head
            return

        # Si el nodo está en cualquier otra posición
        anterior = nodo_a_eliminar.prev
        siguiente = nodo_a_eliminar.next
        anterior.next = siguiente
        siguiente.prev = anterior

    # Función para recorrer la lista hacia adelante y mostrar los valores
    def recorrer(self):
        if self.head is None:
            return

        actual = self.head
        while True:
            print(actual.valor)
            actual = actual.next
            if actual == self.head:
                break


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.prev = None
        self.next = None

class ListaCircularDobleEnlazada:
    def __init__(self):
        self.head = None

    # Función para insertar un nodo al final (para probar la lista)
    def insertar(self, valor, posicion):
        nuevo_nodo = Nodo(valor)

        # Si la lista está vacía
        if self.head is None:
            self.head = nuevo_nodo
            nuevo_nodo.next = nuevo_nodo
            nuevo_nodo.prev = nuevo_nodo
            return

        # Si la posición es 0, insertar al inicio
        if posicion == 0:
            ultimo = self.head.prev  # Nodo actual en la posición de la cola
            nuevo_nodo.next = self.head
            nuevo_nodo.prev = ultimo
            self.head.prev = nuevo_nodo
            ultimo.next = nuevo_nodo
            self.head = nuevo_nodo
            return

        # Insertar en cualquier otra posición
        actual = self.head
        contador = 0

        # Recorrer la lista hasta la posición dada
        while contador < posicion - 1 and actual.next != self.head:
            actual = actual.next
            contador += 1

        # Inserción en la posición dada
        siguiente = actual.next
        actual.next = nuevo_nodo
        nuevo_nodo.prev = actual
        nuevo_nodo.next = siguiente
        siguiente.prev = nuevo_nodo

    # Función para recorrer la lista circular varias veces (tres vueltas)
    def recorrer_varias_veces(self, vueltas=3):
        if self.head is None:
            return

        actual = self.head
        contador_vueltas = 0
        while contador_vueltas < vueltas:
            print(actual.valor)
            actual = actual.next
            
            # Si regresamos al nodo head, contamos una vuelta
            if actual == self.head:
                contador_vueltas += 1

