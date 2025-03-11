Start the server:
```
    # To set up the database
    docker compose up -d

    # To set up the application image
    docker build -t lovelost/parser .

    # To start the application
    docker run -p 23930:8080 lovelost/parser
```