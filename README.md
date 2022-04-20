# REQUIREMENT: Zemoga Portfolio web (test project)

## Overview

Build a simple portfolio web app that displays the profile image, name, some text with
the experience, and the last five tweets list of the user's Twitter timeline.
The second part should be a straightforward API with two endpoints of the profile
content.


## Part 1

Build a simple portfolio page with the user info, image, title, text description, and a list of
5 tweets of the user timeline. Feel free to choose any design or layout for this site. The
focus of the test should be the back-end side of things.

## Part 2

Create a REST API with two endpoints that allow the consumer to get and modify the
profile information. Make sure it complies with the REST specification. Pull out all the
profile information from the database detailed below in the resources section.
In the same API, create a separate endpoint for pulling the tweets. We suggest using the
Twitter API:
https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-use
r_timeline+







# SOLUTION

Observation:

 - I have used modularization for API and website
 - The aws database was not disponible for to use on this project. I use the simple SQLITE
    (the database name was not)

Note: The solution dont have:
 - twitter timeLine

## 01.Requiremnets

    python 3.7
    flask

## 02.Setttings

By terminal execute the next command: (here we are going to set the  enviroment variables)

    mv app/.env.dist app/.env

(optional) This is default variables if you need change for example the port you can do it:

    FLASK_ENV=development
    SERVER_NAME=localhost:5000
    DEBUG=True
    API_URL=http://localhost:5000/api

## 03.Installation With Docker

Create image & container

    docker-compose build
    docker-compose up

(optional)Deploy in docker container

    docker start <container-name>
    docker stop <container-name>

(optional) Access to container:

    docker exec -it <container-name> /bin/sh
    docker logs -f <container-name-or-id> # tracking server

## 04.Acces to the Projects:

Website:

    http://localhost:5000


API REST: 

    http://localhost:5000/api/users/1

