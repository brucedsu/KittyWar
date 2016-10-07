# Sprint 1 Plan

* Product name: Kitty War
* Team name: Dog & Koala Bear
* Sprint completion date: Oct 19, 2016
* Revision number: 1.1
* Revision date: Oct 6, 2016

## Goal

* Enable user account registration via both a website and iPhone app.
* Create working server that establishes communication to iPhone client and SQL database.

## User Stories

### As a back-end developer, I need a user database to store user information and card a database to store card data

* (2) Configure SQL server
* (2) Configure Django server to process these requests
* (3) Develop working SQL model for this information
* Total Story Points: 7

### As a player, I want to be able to register an account via a website

* (3) Build basic website to handle registration
* (2) Store data into a database to track who has registered
* Total Story Points: 5

### As a player, I want to be able to register an account via an iPhone app

* (8) Build front end of iPhone app to accept registration
* (8) Configure custom python server to accept registration requests and forward to database
* (8) Build protocol between iPhone app and server
* Total Story Points: 24

### As a player, I should be able to log into the website and view what cards I have

* (5) Build webpage to display all of this data
* (2) Enable authentication and appropriate setting on Django server
* (2) Ensure SQL model accurately has user information plus what cards they have
* Total Story Points: 9

### As a player, I should to able to log into the iPhone app and view what cards I have

* (8) Build UI centered around signing in and display personal saved information
* (8) Ensure custom python server routes login data to database and authenticates the user
* Total Story Points: 16

### As a player, I am matched against an opponent and put into a lobby

* (8) Improve custom server to wait for connections using UDP and place connecting players into a lobby
* (5) Establish connection to the server from iPhone app
* (5) Ensure data is proper sent between client and server
* Total Story Points: 18

### As a back-end developer, I need to create APIs on the server side for the front-end app

* (8) Continue to improve API client/server for better communication
* Total Story Points: 8

#### Grand Total Story Points: 87

## Team roles

* :bowtie: Hejia Su (iPhone & Backend Developer)
* :blush: Yueqiao Zhang (iPhone Developer)
* :smirk: Juan Gonzalez (Backend Developer)
* :sleeping: Eric Martinez (Backend Developer)

## Initial Tasks

### Hejia Su
#### As a back-end developer, I need a user database to store user information and card a database to store card data

* Configure SQL server
* Develop working SQL model for this information
* Configure Django server to process these requests

### Yueqiao Zhang
#### As a player, I want to be able to register an account via an iPhone app

* Build front end of iPhone app to accept registration
* Build protocol between iPhone app and server

### Juan Gonzalez
#### As a player, I want to be able to register an account via an iPhone app

* Configure custom python server to accept registration requests and forward to database

### Eric Martinez
#### As a player, I want to be able to register an account via a website

* Build basic website to handle registration
* Store data into a database to track who has registered

## Initial Burnup Chart
![Alt text](https://docs.google.com/spreadsheets/d/1cR18Zlbq7eRBpJ_cUE_FLFMCvzjE2VScGuYUP0Wnkp8/pubchart?oid=1455941923&format=image "Burnup Chart")

## Scrum Times

* Tuesday, Thursday, Friday
* Times: 1:00 pm - 2:00pm

