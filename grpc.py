import grpc
import disperse_pb2
import disperse_pb2_grpc
import base64

def run():
    # Assuming the gRPC server is running on localhost at port 50051
    channel = grpc.insecure_channel('18.191.33.157:32001')

    # Create a stub (client)
    stub = disperse_pb2_grpc.GreeterStub(channel)

    # Create a HelloRequest message
    request = disperse_pb2.EncodeStoreRequest(Duration=1, Data=base64.b64encode(open("README.md", "rb").read()).decode("utf8"), BlockNumber=17265921)

    # Make the call
    response = stub.EncodeAndDisperseStore(request)

    print(f"Received: {response.message}")

if __name__ == "__main__":
    run()