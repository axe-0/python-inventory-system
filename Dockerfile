From python:3.11
WORKDIR /app
COPY . /app
CMD ["python", "inventory.py"]
