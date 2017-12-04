"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

import sklearn_pb2
import sklearn_pb2_grpc

def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = sklearn_pb2_grpc.iris_predictionStub(channel)
  print("works OK stub")
  X = sklearn_pb2.input_data()
  for i in  [7. ,  3.2,  4.7,  1.4]:
      X.item_features.append(i)
#  response = stub.predict_iris(sklearn_pb2.input_data(item_features=[5.1,  3.5,  1.4,  0.2]))
  response = stub.predict_iris(X)

  print("of type: " + response.pred_type)


if __name__ == '__main__':
  run()
