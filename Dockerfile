FROM python:3.7

COPY image_comparsion /app/image_comparsion
COPY tests /app/tests
COPY README.md /app
COPY requirements.txt /app
COPY setup.py /app

WORKDIR /app

RUN "python3.7" "setup.py" "install"

CMD ["python3.7", "setup.py", "test"]