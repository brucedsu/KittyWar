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

* As a player, I am able to register an account via both the website and the iPhone app. 
* As a player, I should be able to choose the cat character and draw two effect or ability cards locally.
* As a game player, I am able to get matched with another player with the same level of skills to play the game.
* As a back-end developer, I need to build a user database to store all the user information and a card database to store card data.
* As a back-end developer, I need to create APIs on the server side for the front-end app.
* As a designer, I need to design cat cards (characters), ability cards and effect cards.
### Sprint 2

* As a back-end developer, I need to build the match matching system which match two players with the same level of skills. 
* As a back-end developer, I need to implement the game logic (picking characters, drawing cards, using cars against the target) at the server side. 
* As a front-end developer, I need to use APIs provided by the server to send requests and receive responds. Then I make the front-end app update UI and internal data structures according to the returned data from the server.
### Sprint 3

* As a game player, the game now is playable. Game logics are correct. The animation of the front-end app is clear and intuitive.
* As a front-end developer, I need to keep polishing the app, including transitions between views and card animations.* As a back-end developer, I need to keep improving all the algorithms to make the whole system more stable.
## Architecture

* Web application for registration
* iPhone App for playing games
* Server for storing data and doing algorithms
## Challenges/Risks
* Animation effects* Server compatibility* Fault tolerance
## Technologies
* Web application: HTML/CSS/Javascript
* Server: Django, Python, MySQL
* iPhone App: Swift, Xcode