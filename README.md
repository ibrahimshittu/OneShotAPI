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

Install requirements:
  pip install requirements.txt
 
Run:
  Uvicorn OneShot.main:app --reload 
  
```

## Online Documentation

```yaml
Swagger Documentation:
  http://127.0.0.1:8000/docs

Redoc Documentation:
  http://127.0.0.1:8000/redoc
  
```

# API

The REST API to OneShot - The Contest Platform is described below.

## Contests

## Get All contests

### Request

`GET /contests/`

    curl -i -H 'Accept: application/json' http://localhost:8000/contests/

### Response

    HTTP/1.1 202 OK
    Date: Fri,01 Oct 2021 14:16:50 GMT
    Content-Type: application/json
    Content-Length: 470
    Server: uvicorn 

    [
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
   
  ## Get Single Contest

  ### Request

  `GET /contests/{id}/`

      curl -i -H 'Accept: application/json' http://localhost:8000/contest/{id}/

  ### Response

      HTTP/1.1 202 OK
      Date: Fri,01 Oct 2021 14:16:50 GMT
      Content-Type: application/json
      Content-Length: 226
      Server: uvicorn 

      [
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
    
  ## Create Contest

  ### Request

  `POST /contests/{id}/`

      curl -X 'POST' \
      'http://127.0.0.1:8000/create_contest' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxx' \
      -H 'Content-Type: application/json' \
      -d '{
      "contest_name": "string34",
      "contest_description": "string",
      "contest_prize": "string",
      "contest_category": "Essay Contest",
      "start_date": "2021-10-01",
      "end_date": "2021-10-01",
      "published": true
    }'

  ### Response

      HTTP/1.1 201 Created
      access-control-allow-origin: http://127.0.0.1:8000 
      content-length: 251 
      content-type: application/json 
      date: Fri,01 Oct 2021 14:28:58 GMT 
      server: uvicorn 

      {
      "id": 4,
      "contest_description": "string",
      "contest_prize": "string",
      "start_date": "2021-10-01",
      "published": true,
      "owner_id": 2,
      "contest_name": "string3dd4",
      "contest_category": "Essay Contest",
      "end_date": "2021-10-01",
      "created_date": "2021-10-01T14:28:59.471642"
    }
    
    
  ## Update Contest

  ### Request

  `PUT /contests/{id}/`

      curl -X 'PUT' \
      'http://127.0.0.1:8000/update_contest/{1}/' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxx' \
      -H 'Content-Type: application/json' \
      -d '{
      "contest_name": "string34",
      "contest_description": "string",
      "contest_prize": "string",
      "contest_category": "Essay Contest",
      "start_date": "2021-10-01",
      "end_date": "2021-10-01",
      "published": true
    }'

  ### Response

      HTTP/1.1 201 Created
      access-control-allow-origin: http://127.0.0.1:8000 
      content-length: 251 
      content-type: application/json 
      date: Fri,01 Oct 2021 14:28:58 GMT 
      server: uvicorn 

      {
      "id": 4,
      "contest_description": "string",
      "contest_prize": "string",
      "start_date": "2021-10-01",
      "published": true,
      "owner_id": 2,
      "contest_name": "string3dd4",
      "contest_category": "Essay Contest",
      "end_date": "2021-10-01",
      "created_date": "2021-10-01T14:28:59.471642"
    }

  ## Delete Contest

  ### Request

    `DELETE /contests/{id}/`

     curl -X 'DELETE' \
    'http://127.0.0.1:8000/delete_contest/{id}' \
    -H 'accept: */*' \
    -H 'Authorization: Bearer xxxxxxx'

   ### Response
        
       access-control-allow-credentials: true 
       access-control-allow-origin: http://127.0.0.1:8000 
       content-length: 30 
       content-type: application/json 
       date: Fri,01 Oct 2021 14:37:10 GMT 
       server: uvicorn 



## Submission

## Get All Submission for a Contest

### Request

    `GET /contest/{id}/submissions/`

    curl -X 'GET' \
    'http://127.0.0.1:8000/contest/{id}/submissions/' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer xxxxxxxx'

### Response

    HTTP/1.1 202 OK
    Date: Fri,01 Oct 2021 14:16:50 GMT
    Content-Type: application/json
    Content-Length: 470
    Server: uvicorn 

    [
      {
        "created_date": "2021-08-12T17:07:00.211636",
        "body": "testing update",
        "image": "http://res.cloudinary.com/ibrahimshittu/image/upload/v1629611858/ib5uhylumixccwx1axwc.jpg",
        "contestant": {
          "name": "string",
          "email": "string"
        },
        "voter": [
          {
            "created_date": "2021-08-12T17:25:16.192145",
            "user": 1
          },
          {
            "created_date": "2021-08-21T17:40:15.105930",
            "user": 2
          }
        ]
    ]
   
  ## Get Single Submission for a Contest

  ### Request

  `GET /contest/{id}/submissions/{submission_id}/`

      curl -i -H 'Accept: application/json' http://localhost:8000/contest/{id}/submissions/{submission_id}/'

  ### Response

      HTTP/1.1 202 OK
      Date: Fri,01 Oct 2021 14:16:50 GMT
      Content-Type: application/json
      Content-Length: 226
      Server: uvicorn 

      {
        "image": "http://res.cloudinary.com/xxxxx/image/upload/v1629611858/ib5uhylumixccwx1axwc.jpg",
        "created_date": "2021-08-12T17:07:00.211636",
        "body": "testing update",
        "contestant": "string",
        "total votes": 2
      }
    
  ## Make Submission 

  ### Request

  `POST /contests/{id}/`

      curl -X 'POST' \
      'http://127.0.0.1:8000/create_contest' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxx' \
      -H 'Content-Type: application/json' \
      -d '{
      "contest_name": "string34",
      "contest_description": "string",
      "contest_prize": "string",
      "contest_category": "Essay Contest",
      "start_date": "2021-10-01",
      "end_date": "2021-10-01",
      "published": true
    }'

  ### Response

      HTTP/1.1 201 Created
      access-control-allow-origin: http://127.0.0.1:8000 
      content-length: 251 
      content-type: application/json 
      date: Fri,01 Oct 2021 14:28:58 GMT 
      server: uvicorn 

      {
      "id": 4,
      "contest_description": "string",
      "contest_prize": "string",
      "start_date": "2021-10-01",
      "published": true,
      "owner_id": 2,
      "contest_name": "string3dd4",
      "contest_category": "Essay Contest",
      "end_date": "2021-10-01",
      "created_date": "2021-10-01T14:28:59.471642"
    }
    
    
  ## Update Contest

  ### Request

  `PUT /contests/{id}/`

      curl -X 'PUT' \
      'http://127.0.0.1:8000/update_contest/{1}/' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxx' \
      -H 'Content-Type: application/json' \
      -d '{
      "contest_name": "string34",
      "contest_description": "string",
      "contest_prize": "string",
      "contest_category": "Essay Contest",
      "start_date": "2021-10-01",
      "end_date": "2021-10-01",
      "published": true
    }'

  ### Response

      HTTP/1.1 201 Created
      access-control-allow-origin: http://127.0.0.1:8000 
      content-length: 251 
      content-type: application/json 
      date: Fri,01 Oct 2021 14:28:58 GMT 
      server: uvicorn 

      {
      "id": 4,
      "contest_description": "string",
      "contest_prize": "string",
      "start_date": "2021-10-01",
      "published": true,
      "owner_id": 2,
      "contest_name": "string3dd4",
      "contest_category": "Essay Contest",
      "end_date": "2021-10-01",
      "created_date": "2021-10-01T14:28:59.471642"
    }

  ## Delete Submission

  ### Request

    `DELETE /contests/{id}/`

     curl -X 'DELETE' \
    'http://127.0.0.1:8000/delete_contest/{id}' \
    -H 'accept: */*' \
    -H 'Authorization: Bearer xxxxxxx'

   ### Response
        
       access-control-allow-credentials: true 
       access-control-allow-origin: http://127.0.0.1:8000 
       content-length: 30 
       content-type: application/json 
       date: Fri,01 Oct 2021 14:37:10 GMT 
       server: uvicorn 



