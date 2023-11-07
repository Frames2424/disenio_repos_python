from abstract_factory import AbstractFactory
from concrete_products import ProductoA_1, ProductoB_1, ProductoA_2, ProductoB_2

class ConcreteFactory_1(AbstractFactory):
    def create_product_A(self):
        return ProductoA_1()

    def create_product_B(self):
        return ProductoB_1()

class ConcreteFactory_2(AbstractFactory):
    def create_product_A(self):
        return ProductoA_2()

    def create_product_b(self):
        return ProductoB_2()