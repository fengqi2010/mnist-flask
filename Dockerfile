FROM python:3.9-slim
WORKDIR /app
ADD . .
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]