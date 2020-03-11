import grpc
import protos.book_service_pb2_grpc
import protos.book_service_pb2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = protos.book_service_pb2_grpc.BookStub(channel)
        author_request = protos.book_service_pb2.AuthorRequest(id=1)
        author = stub.GetAuthor(author_request)
        print('author = ', author)


if '__main__' == __name__:
    run()
