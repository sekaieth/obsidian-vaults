# Authentication Methods
## Basic Authentication
- Basic auth is one of the most common, but it's least secure.  Credentials are in plaintext, so using HTTPs/TLS is imperative.
- Use Postman's [Echo API](https://learning.postman.com/docs/developer/echo-api/) to test different APIs out


In the video example, he sent a basic auth request from Postman to the Postman ECHO api.  The headers include the `authorization` key, which has a value of `Basic` plus a b64 string of the credentials (key:value pair of `postman:password`)
 
## Token Authentication
Allows us to create a custom token to only enter a U/P one time and then generate and store a token for authentication.

### Benefits
- Access can expire after amount of time
- Limit access for a certain amount of time
- Can revoke access

In the video, they are trying to create a new repo in GitHub.  The initial request gets `401 Unauthorized` because he does not hae a token.  They then provide in an auth token that was generated in GitHub.  They are authenticated, but they get a `400 bad request` because they sent a POST but did not send any actions.  They then send the token + an action to create a new repo, and they get `201 Created` response

**Python Example**
```python
import requests
response = requests.get('https://github.com/user/repos', headers={'Authorization': 'Bearer <TOKEN>})
print(response)
```


## API Key Authentication
Primarily used for overall projects rather than user level, and typically read-only

In the example, they use the [OpenWeather API](https://openweathermap.org/api).  Initially, they hit the API without any API key, and they receive `401 unauthorized` and the body of the HTTP code says invalid API key and where to go to troubleshoot.

**Python Example**
```python
import requests
params = {"appid":"<APIKEY>"}
response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=<LATITUDE>&lon=<LONGITUDE>', params = params) 
```
