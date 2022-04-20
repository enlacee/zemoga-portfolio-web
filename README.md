# Zemoga Portfolio web (test project)

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



## Installation With Docker

Fisrt Time (to create image & container)

    docker-compose build
    docker-compose up

Second Time (deploy in development)

    docker start <container-name>
    docker stop <container-name>

Access to container:

docker exec -it <container-name> /bin/sh
docker logs -f <container-name> # tracking server

## Application

Website:

    http://localhost:5000


API REST: 

    http://localhost:5000/api/users/1

