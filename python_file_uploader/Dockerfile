FROM python:3.7.5-slim
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "./file_uploader.py"]
