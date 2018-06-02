## Scribble API

This repository hosts the backend API for Sribbble. This API has been used to build [Scribble CLI](https://github.com/djmgit/scribble) and [Scribble chrome extension](https://github.com/djmgit/scribble_web_extension).

## What is Scribble

Scribble is primarily a terminal based note taking application for devs. It allow us to create notes, view existing notes,
search existing notes, delete notes from the terminal itself. We can take note while working on terminal without switching to
any other web based or desktop based application.

## How it works

Scribble mainly consists of a backend API (this repository) which is deployed on [hasura](https://hasura.io/) cloud platform.
Scribble uses Hasura data and auth APIs to authenticate users and store user information and the notes created by them. Notes
and other data are stored on a Hasura cloud instance of the popular Postgresql dabase. The entire API is deployed as a
microservice on hasura platform.
The CLI application (which is built using python) interacts with this backend API via http requests. So the basic workflow is
some what as follows :
- User interacts with Scribble CLI via the desired command.
- The CLI sends HTTP calls to the backend API (microservice)
- The backend microservice interects with Hasura auth service for authenticating user and fetches data from Hausra Postgresql
  database.
- The microservice then returns the required data to the CLI tool.
- The CLI application displays data on terminal

Apart from this the Scribble package also provides a [chrome extension](https://github.com/djmgit/scribble_web_extension)

## The Scribble microservice

As mentioned earlier the entire backend API is deployed as a microservice on the Hasura platform. The code for the microservice
can be found at /microservices/app/src.

### Stack used to build the microservice

- Python
- Flask
- Python requests
- Hasura data service
- Hasura auth service
- Docker for deployment

The micoservice can be deployed as a separate web application. Instructions for locally running the microservice can be found
[here](https://github.com/djmgit/scribble_api/tree/master/microservices/app)

### Endpoints

The backend API provides several endpoints so that the CLI tool can communicate smoothly with it. The endpoints are described below :

1) ```http://app.accidentally14.hasura-app.io/api/signup``` : This endpoint is used to register an user. It allows only POST 
   request. It accepts a json object of the following form :
   ```
   {
    "username" : <username of the user>,
    "password" : <password of the user>
   }
   ```
   If there is no error, it returns an **ok** status message and registers the user.
 
2) ```http://app.accidentally14.hasura-app.io/api/login``` : This endpoint is used to login a user. It allows only POST request.
   It accepts a json object of the following form:
   
   ```
   {
    "username" : <username of the user>,
    "password" : <password of the user>
   }
   ```
   If there is no error, it returns an **ok** status along with a token which has to be used make all further requtests.
   
3) ```http://app.accidentally14.hasura-app.io/api/add_note``` : This endpoint is used to save a new note. It allows only POST
   request. It accepts all the parameters related to the new note like its title, body etc as a json object of the
   following form. Also one has to send the auth token as a Authorization header.
   
   ```
   Authorization: Bearer <token>
   {
    "note_title" :  <title of the note>,
    "note_body" : <body of the note>,
    "keywords"  : <keywords associated with the note [optional]>,
    "category"  : <category of the note [option]>
   }
   ```
   If there is no error then, it returns a **ok** status message and saves the new note in database.
   
4) ```http://app.accidentally14.hasura-app.io/api/all_notes``` : This endpoint is used to view the id and tiitle of all the
   notes present for a particular logged in user. This endpoint allows only POST request. It takes no parameters. One has to
   send only the Authorization token.
   If there is no error, it returns a **ok** status message and also all the note titles and their respective IDs.
   
5) ```http://app.accidentally14.hasura-app.io/api/note_by_id``` : This is endpoint is used to view the details of a
   particular note of a given id. The endpoint only allows POST request. One has to provide the note_id in form of a json
   object and Authoriation token as header.
   
   ```
    Authorization: Bearer <token>
   {
    "note_id": <id of the note>
   }
   ```
   If there is no error then it returns a **ok** along with the details of the required note.
   
6) ```http://app.accidentally14.hasura-app.io/api/note_search``` : This endpoint is used to search existing notes for given
   word or phrase. It only allows POST request. The endpoint requires a json object containing the search phrase and a list
   of fields to be searched. If no search field is provided then all the fields are searched for a match. It also requires
   Authorization token as header.
   
   ```
    Authorization: Bearer <token>
   {
    "search" : <phrase or words to be searched>,
    "fields" : [a list of comma separated fields like: note_title, note_body, etc]
   }
   ```
   If there is no error, then it returns a **ok** status message along with a list of notes which has shown successfull
   match.
   
7) ```http://app.accidentally14.hasura-app.io/api/delete_note``` : This endpoint is used to delete an existing note
   identified by its note_id. This endpoint only allows POST request. It takes the note_id in a json object and also
   the Authorization token as header.
   
    ```
    Authorization: Bearer <token>
   {
    "note_id" : <id of the note to be deleted>
   }
   ```
   
   If there is no error, then it returns a **ok** status message and deletes the required note.
   
   
   
   
