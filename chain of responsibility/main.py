from document_handlers import ApprovalHandler_A, ApprovalHandler_B, ApprovalHandler_C

def main():
    handler_A = ApprovalHandler_A()
    handler_B = ApprovalHandler_B()
    handler_C = ApprovalHandler_C()

    handler_A.set_successor(handler_B)
    handler_B.set_successor(handler_C)

    document_list = ["Document_1", "Document_2", "Document_3", "Document_4"]

    for doc in document_list:
        print(f"procesando!: {doc}")
        handler_A.process_document(doc)

if __name__ == "__main__":
    main()