# Summary
This project is  to convert a SVM model trained on iris data set to a grpc service. The model itself is built in python's scikit learn package

# How to USE
git clone https://github.com/DihuiLai/sklearn_prediction_grpc_service.git


in one terminal: python iris_pred_server.py

in another terminal: python iris_pred_client.py

# Build docker container

docker build -t $USER/sklearn-serving -f dockerfile .

# Run docker container
docker run -it -p 50051:50051  $USER/sklearn-serving
