# HTTP Response Codes
## 5 main categories:
- 1XX Codes - informations
- 2XX Codes - Success
- 3XX Codes - Redirection
- 4XX Codes - Client Side Error
- 5XX Codes - Server side error
Under each of these categories there are many codes.

## 1XX Code Range
- *101 Continue*
- Interim response to a request
- Final response is later seen after request is completed

## 2XX Range
- *200 OK*
- Request was successful and completed

## 3XX Range
- *301 Moved Permanently*
- *302 Found* - Resource temporarily relocated 
- *304 Not Modified* 

## 4XX Range
- *400 Bad Request*
- *401 Unauthorized*
- *403 Forbidden*
- *404 Not Found*
- *408 Request Timed Out*

## 5XX Range-
- *500 Internal Server Error*
- *502 Bad Gateway*
- *503 Service Unavailable*

Many more codes from IANA

# Troubleshooting HTTP Requests
## Response Codes
- Every request will have an HTTP status code response
- Most commonly errors are in the 4XX or 5XX codes

## Response Body
- Body information can detail issues
- Server often returns code along with a detailed body
- ALWAYS CHECK API DOCUMENTATION

## Troubleshooting Steps
- Check for correct URL/URI
- Ensure valid API key is in place
- Request parameters must be valid
- Check user permissions for proper access
