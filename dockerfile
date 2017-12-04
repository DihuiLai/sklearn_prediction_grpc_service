FROM gcr.io/google_appengine/python

RUN apt-get update && \
    apt-get install -y python2.7 python-pip && \
    apt-get clean && \
    rm /var/lib/apt/lists/*_*

ENV GRPC_PYTHON_VERSION 1.4.0

COPY ./ /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN pip install grpcio==${GRPC_PYTHON_VERSION} grpcio-tools==${GRPC_PYTHON_VERSION}

RUN python -m grpc_tools.protoc -I./sklearn_proto --python_out=. --grpc_python_out=. ./sklearn_proto/sklearn.proto

CMD [ "python", "iris_pred_server.py" ]
EXPOSE 50051