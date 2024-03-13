import grpc
from concurrent import futures
import server_pb2
import server_pb2_grpc

class ExampleServiceServicer(server_pb2_grpc.ExampleServiceServicer):
    def GetData(self, request, context):
        # Reverse the query string and return it in the response.
        result = request.query[::-1]
        return server_pb2.GetDataResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()