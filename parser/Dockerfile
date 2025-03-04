FROM python:3.12
WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./src
EXPOSE 8080

RUN useradd app
USER app

CMD ["uvicorn", "main:app", "--reload", "--timeout-keep-alive", "90", "--host", "0.0.0.0.", "--port", "8080"]