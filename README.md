# Demo

- step 1: `cd api` 
- step 2: `python app.py` 
- step 3: click http://127.0.0.1:8080/ 

# API
**URL: /short_url**

**Type: GET**

**Description**

Input raw url, output short url.

**Parameters**

| Field         | Type   | Description                              |
| ------------- | ------ | ---------------------------------------- |
| url | string | raw url |

**Sample Input**

```
http://127.0.0.1:8080/short_url?url=https://teaches.cc/
```

**Output Data**
- status code: 200

| Field           | Type    | Description     |
| --------------- | ------- | --------------- |
| short_url     | string  | short url        |

- status code: 400 or 500

| Field           | Type    | Description     |
| --------------- | ------- | --------------- |
| msg     | string  | error msg        |

**Sample Output**
- status code: 200
```
{
    short_url: "http://127.0.0.1:8080/short2raw/TFBjk"
}
```
- status code: 400 or 500
```
{
    msg: "Invalid url"
}
```
# Testing
```
pytest --cov-report term-missing --cov=api
```
