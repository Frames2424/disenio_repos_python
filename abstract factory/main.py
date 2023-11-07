from abstract_factory import AbstractFactory
from concrete_factories import ConcreteFactory_1, ConcreteFactory_2

def client_code(factory: AbstractFactory):
    product_A = factory.create_product_A()
    product_B = factory.create_product_B()
    print(f"producto A: {product_A.operation_A()} / producto B: {product_B.operation_B()}")

if __name__ == "__main__":
    factory1 = ConcreteFactory_1()
    factory2 = ConcreteFactory_2()

    client_code(factory1)
    client_code(factory2)