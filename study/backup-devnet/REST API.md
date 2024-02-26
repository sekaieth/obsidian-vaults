# Fundamentals of REST API
- API (Application Programming Interface)
- E.g. third-party website login with existing accounts
- Communicate with other network components

## REST APIs
- Architectual standard for using web services
- REST = Representational state transfer
- HTTP verbs used to obtain and manipulate data 

## HTTP Verbs
CRUD Functions
- Create, Read, Update, Delete
- API Requests used to ask a server to perform something

## REST API - Basic Auth
- Simplest and most common method
- Passes creds in unencrypted plain text
- Typically leverage SSL or TLS with basic auth

## API Key Authentication
- Pre-shared keys known by client and server
- Key transmission is susceptible to interception
- Typically only used where limited to READ function only

## OATH - Open Auth
- Using generated tokens from an auth server
- Tokens can be checked at any time to prove validation
- Ability to limit scope and authorization time span

- No specific standards to constructing and API request
- Requests will vary depending on software
- API documentation is crucial

## REST API Structures
- URL (or URI)
- Method
- Header
- Body

### Method
- Comes from standard HTTP methods
- POST, GET, PUT, UPDATE, PATCH, DELETE

### Header
- Standard HTTP headers
- Formatted in name:value pairs and comma separated
	- Keep-alive:timeout=1, max=50

### Body
- Contains the body of the message
- Optional, depending on the type of HTTP method
- Reading data doesn't require a body, but updating should contain a body of data to update the endpoint with


# Webhooks
Also referred to as Reverse APIs
- HTTP POST messages triggered by an event
- Provide event notifications
- Most modern applications support web hooks
- Lightweight APIs driven by events
- Require application to be registered with URL
- Application with webhook must always be running
- Preferred for monitoring frequently updated data
- Provide real-time updates about the data

# REST Constraints
- Uniform interface
	- Method of interaction with data
	- Key differentiator of RESTful APIs
	- Uniform way to interact with a server
	- Identification of Resources
	- Manipulation of Resources
	- Self-descriptive messages
	- Hypermedia as the Engine of Application State (HATEOAS)
		- Client should be able to interact with API entirely on the responses provided by the server
- Stateless
	- Server does not store information about the last action from the client
	- Every request will be treated as a new request
- Cacheable or Non-cacheable label
	- Cached data used for repeated actions to save time
	- prevents work being repeated
- Independent Clients and Servers
	- Leverages SoC principle
	- Provides more scalable architecture
- Layered System
	- E.G. proxy servers or load balancers
	- Layers should be transparent to the client'
	- Can optimize traffic flow or provide security
- Code-On-Demand
	- Client Downloads code from server for execution


# REST API With Python
Tools:
- Fake Store API
	- https://fakestoreapi.com