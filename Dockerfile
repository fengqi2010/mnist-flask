FROM python:3.9-slim
WORKDIR /app
ADD . .
RUN apt update && apt install net-tools curl -y
RUN pip3 install -r requirements.txt
EXPOSE 7777
CMD ["python3", "app.py"]