# Remote Procedural Call (RPC)
## Constrast REST and RPC
### REST
- Performs CRUD operations using HTTP verbs like GET, PUT, POST, PATCH, DELETE
- Resource-oriented

### RPC
- Uses GET and POST 
- Action Oriented
- A way to send user requests to server for action
- Interacts in a remote manner
- Considered more of a legacy method
- REST APIs have taken over popularity
- Request-response model
- Similar to calling a function
- Can use various formats (JSON or XML for example)

During an RPC call from a client to a server, any further requests from the client are blocked while the server is taking action.  This is to prevent things like DDOS or resource exhaustion.  Once the request is complete, the response is sent to the client.


# Syncronous vs Asyncronous
## Syncronous
- Real-time communication/interaction where things are scheduled
- E.G. voice/video calls
- Client must wait for a response from the API before continuiing
- RPCs are a common example of syncronous APIs

## Async
- Communication not in real time
- E.g. email communication
- Client can function normally while the request is processed

## REST APIs
- Rest APIs are not exclusively sync or async.
- Simple database may use syncronous API
- Remote service integration may use asyncronous API
	- Think of a travel booking website that books hotels, cars, airplanes, etc.. The API can work on each service independently and whether one piece works or not.
