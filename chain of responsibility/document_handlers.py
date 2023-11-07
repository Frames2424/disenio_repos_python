class ApprovalHandler:
    def __init__(self, successor=None):
        self._successor = successor

    def set_successor(self, successor):
        self._successor = successor

    def process_document(self, document):
        if self._successor:
            self._successor.process_document(document)

class ApprovalHandler_A(ApprovalHandler):
    def process_document(self, document):
        if document == "Document1":
            print("El documento 1 fue aprobado por Aprobacion 'A'") 
        else:
            super().process_document(document)

class ApprovalHandler_B(ApprovalHandler):
    def process_document(self, document):
        if document == "Document2":
            print("El documento 2 fue aprobado por aprobacion 'B'")
        else:
            super().process_document(document)

class ApprovalHandler_C(ApprovalHandler):
    def process_document(self, document):
        if document == "Document3":
            print("El documento 3 fue aprobado por aprobacion 'C'")
        else:
            print("El documento fue denegado")