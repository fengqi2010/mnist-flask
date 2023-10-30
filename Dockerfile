FROM python:3.9-slim
WORKDIR /app
ADD . .
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN apt update && apt install net-tools -y
EXPOSE 7777
CMD ["python3", "app.py"]