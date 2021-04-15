

### Example Usage

#### Curl<br />
``` bash
curl -X POST -H "Content-type: application/json" -d '{
    "first_name": "Chipper",
    "last_name": "Jones",
    "born": "1972-04-24",
    "positions": ["Third Baseman", "Leftfielder"],
    "bats": "Switch",
    "throws": "Right",
    "height": 193,
    "weight": 95,
    "retired": true
}' 'http://localhost:8000/players/'
```