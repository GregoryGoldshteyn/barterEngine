# BarterEngine
A simple game engine based on trading things for other things. Based in part on the quest and item system in "Sunless Sea"

Requires
- Python 3
- Flask
- FlaskAPI

## Included

- Server
  The game engine itself. Player actions are sent as requests to the server, which takes actions based on the current state of the game.
- Tools
  A few tools to help develop games for this engine. Includes tools to add and view game objects.
- LocalDB
  Example save files for testing the tools and game engine.

## Design

There are four basic objects that the player interacts with to play games created with this engine

- Items
  Items tepresent physical things, abstract concepts, or anywhere in between. Come with a description and images
- Trades
  Trades are the exchange of some collection of items for another collection of items. May progress a story, or be repeatable (like a shop interaction)
- Stories
  Stories offer trades in exchange for more story. As trades are made, stories progress. Can be repeatable, or have a conclusion
- Hubs
  Hubs represent real world places in which stories can be found. There may be a cost (trade) associated with entering a hub

The main gameplay loop of a game created by this engine would most likely be as follows:
1. The player has some set of resources
2. The player trades for other resources
3. New stories and trades become available
4. Repeat at 1