# OneShotAPI
The Development of OneShot -The Contest Platform's API. This is a contest platform that connects 3 types or groups of users. It is intended to act as a creative hub for contest sponsors (individuals and corporates) that seek to crowd-source solutions to creativity problems. 


## Requirements

- Python >= 3.6 


## Install:

```yaml
Clone Repo:
  https://github.com/ibrahimshittu/OneShotAPI.git
  
  cd OneShotAPI
  
Create venv:
  virtualenv env
  
Activate Venv:
  env\Scripts\activate.bat
  
  pip install requirements.txt
 
 Run:
  Uvicorn OneShot.main:app --reload 
  
```

## Swagger Documentation

## Install:

```yaml
Swagger Documentation:
  http://127.0.0.1:8000/docs
 
 Redoc Documentation:
  http://127.0.0.1:8000/redoc
  
```

# API

The REST API to OneShot - The \Contest Platform is described below.

## Get All contests

### Request

`GET /thing/`

    curl -i -H 'Accept: application/json' http://localhost:7000/contests/

### Response

    HTTP/1.1 202 OK
    Date: Fri,01 Oct 2021 14:16:50 GMT
    Content-Type: application/json
    Content-Length: 470
    Server: uvicorn 

    [
    {
      "contest_name": "string2",
      "contest_description": "string",
      "contest_prize": "string",
      "contest_category": "Essay Contest",
      "start_date": "2021-08-30",
      "end_date": "2021-08-30",
      "published": true,
      "owner": {
        "name": "string",
        "email": "ibshittu01@gmail.com"
      }
    },
    {
      "contest_name": "string",
      "contest_description": "string",
      "contest_prize": "string",
      "contest_category": "Essay Contest",
      "start_date": "2021-08-12",
      "end_date": "2021-09-12",
      "published": true,
      "owner": {
        "name": "string",
        "email": "string"
      }
    }
    ]

