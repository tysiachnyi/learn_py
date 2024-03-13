import grpc
import server_pb2
import server_pb2_grpc

def run():
    # Open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051')

    # Create a stub (client)
    stub = server_pb2_grpc.ExampleServiceStub(channel)

    # Create a valid request message
    request = server_pb2.GetDataRequest(query='test query')

    # Make the call
    response = stub.GetData(request)

    # Print the response
    print(response)

if __name__ == '__main__':
    run()