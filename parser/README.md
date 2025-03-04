Start the server:
```
    # To set up the database
    docker compose up -d
    # To start the application
    uvicorn main:app --reload --timeout-keep-alive 90
```