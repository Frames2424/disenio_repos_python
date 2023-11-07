from abstract_products import AbstractProduct_A, AbstractProduct_B

class Producto_A_1(AbstractProduct_A):
    def operation_A(self):
        return "Operación A1 de producto_A_1."

class Producto_A_2(AbstractProduct_A):
    def operation_A(self):
        return "Operación A2 de producto_A_2."

class Producto_B_1(AbstractProduct_B):
    def operation_B(self):
        return "Operación B1 de producto_B_1."

class Producto_B_2(AbstractProduct_B):
    def operation_B(self):
        return "Operación B2 de producto_B_2."
    
    