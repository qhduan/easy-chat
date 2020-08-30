FROM tensorflow/serving
EXPOSE 8500
EXPOSE 8501
ENV MODEL_NAME=chat
COPY ./chat /models/chat
