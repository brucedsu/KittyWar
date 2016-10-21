# Sprint 1 Plan

* Product name: Kitty War
* Team name: Dog & Koala Bear
* Sprint completion date: Oct 19, 2016
* Revision number: 1.2
* Revision date: Oct 19, 2016

## Goal

* Enable user account registration via both a website and iPhone app.
* Create working server that establishes communication to iPhone client and SQL database.

## User Stories

### As a back-end developer, I need a database to store user information and card data

* (5) Research Django and MySQL
* (2) Configure SQL server
* (2) Configure Django server to process these requests
* Total Story Points: 9

### As a player, I want to register an account via a website

* (3) Build basic website to handle registration
* (2) Store data into a database to track who has registered
* Total Story Points: 5

### As a player, I want to register an account via an iPhone app

* (8) Build front end of iPhone app to accept registration
* (5) Configure django web server to accept registration requests and forward to database
* (2) Ensure protocol is working between django server and iPhone client 
* Total Story Points: 15

### As a player, I want to log into a website and view my cards

* (5) Build webpage to display all of this data
* (2) Enable authentication and appropriate setting on Django server
* (3) Build SQL model for card data
* Total Story Points: 10

### As a player, I want to log into an iPhone app and view my cards

* (5) Build UI centered around signing in and displaying personal saved information
* (5) Ensure custom python server routes login data to database and authenticates the user
* Total Story Points: 10

### As a player, I am matched against an opponent and put into a lobby

* (5) Improve custom server to wait for connections using TCP and place connecting players into a lobby
* (5) Establish connection to the server from iPhone app
* (5) Ensure data is properly sent between client and server
* Total Story Points: 15

#### Grand Total Story Points: 64

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

