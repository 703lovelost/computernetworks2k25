Start the server:
```
    # To set up the database
    docker compose up -d

    # To set up the application image
    docker build -t lovelost/parser .

    # To start the application
    docker compose up

    # To open the IP
    docker run --net=host -it -e NGROK_AUTHTOKEN=authtoken ngrok/ngrok http 80
```