# world population server

## installation
- install node
- `npm install`
- `npm start`
- for great justice, set it to automatically run when your server boots - this kinda sucks though

## access from Python
```python
import requests
r = requests.get('http://localhost:3000') # or wherever the server is
r.status_code # 200, or something else if shit broke
r.text # '7,671,361,936' or equivalent, as long as no shit broke
```
