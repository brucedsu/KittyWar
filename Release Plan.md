# Release Plan

## Basic Information

* Product name: Kitty War
* Team name: Dog & Koala Bear
* Team members:
	1. Hejia Su (Bruce) (Product Owner)
	2. Yueqiao Zhang (Janet)
	3. Juan Gonzalez
	4. Eric Martinez

## High Level Goals

* Users are able to register their accounts via both the website and the iPhone app.
* The server matches two players with closing level of skill into one game. 
* During the game, two players choose their representing cat cards and battle against each other by following the Kitty War Game Rule.
### Kitty War Game Rule1. Each player should select one kind of cat card to represent.And each player has 10 chips (represent as favorability) at the beginning.2. Each round, every player has to choose 2 cards to show at the same time based on the card combinations. One card is the function card, and the other one is the target you choose3. Victory condition: if all opponents lose their chips,the one who survived is the winner; if someone gets 20 chips at first, he/she wins.
## User Stories
### Sprint 1
* [web]website for registration
* [server]databases including user database, game database and etc
* [iPhone]iPhone app interface and partial animations
### Sprint 2
* [server]algorithms including game rules, match matching algorithms and etc* [server]server APIs for iPhone client
* [iPhone]use server APIs to send and receive data  
* [iPhone]polish animations and app structure
### Sprint 3
make the game playable and keep polishing the client app
## Architecture

* Web application for registration
* iPhone App for playing games
* Server for storing data and doing algorithms
## Challenges/Risks
* Animation effects* Server compatibility* Fault tolerance
## Technologies
* Web application: HTML/CSS/Javascript
* Server: PHP or Python, MySQL
* iPhone App: Swift Xcode