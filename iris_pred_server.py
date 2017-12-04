# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import time

import grpc

import sklearn_pb2
import sklearn_pb2_grpc
import cPickle
import numpy
_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class iris_prediction(sklearn_pb2_grpc.iris_predictionServicer):

  def predict_iris(self, request, context):
    # load it again
    with open('iris_SVM_classifier.pkl', 'rb') as fid:
      clf = cPickle.load(fid)
    input_feature=[numpy.array(request.item_features)]
    y=clf.predict(input_feature)
    print input_feature, y
    return sklearn_pb2.iris_type(pred_type=str(y))


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  sklearn_pb2_grpc.add_iris_predictionServicer_to_server(iris_prediction(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
