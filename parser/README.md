Start the server:
```
    # To start the services (to test region restriction and IPv4 network organization)
    docker compose -f ./docker-compose.ipv4.yml up

    # To start the services (to test region restriction and IPv6 network organization)
    docker compose -f ./docker-compose.ipv6.yml up

    # To forward the IP (Enter your own $NGROK_AUTHTOKEN)
    docker run --net=host -it -e NGROK_AUTHTOKEN=authtoken ngrok/ngrok http 80
```