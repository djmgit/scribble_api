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


