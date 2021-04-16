

## Example Usage

### Obtaining Token

``` bash
TOKEN=$(curl -s -X POST -H 'Content-Type: application/json' -d '{"username":"admin","password":"password"}' 'http://localhost:8000/api-token-auth/' | jq -r '.token')
```

### Add Team example
``` bash
curl -X POST -H "Content-type: application/json" -H "Authorization: Token ${TOKEN}" -d '{
    "name": "Atlanta Braves",
    "location": "Atlanta, Georgia"
}' 'http://localhost:8000/teams/'

```

### Add Player example<br />
``` bash
curl -X POST -H "Content-type: application/json" -H "Authorization: Token ${TOKEN}" -d '{
    "first_name": "Chipper",
    "last_name": "Jones",
    "born": "1972-04-24",
    "positions": ["Third Baseman", "Leftfielder"],
    "bats": "Switch",
    "throws": "Right",
    "height": 193,
    "weight": 95,
    "retired": true,
    "teams": [1] # IDs returned from Teams
}' 'http://localhost:8000/players/'
```

