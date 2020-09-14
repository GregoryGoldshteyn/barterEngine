MONGO_CONNECTION_STRING="mongodb://localhost:27017"
DEFAULT_DATABASE_NAME="BarterDB"
COLLECTIONS = [
    "ITEMS",
    "TRADES",
    "STORIES",
    "HUBS"
]

DEFAULT_ITEM = {
    "ID" : 0,
    "NAME" : "ITEM_NAME",
    "LONG_DESC" : "Long description for item. Can be several lines long",
    "SHORT_DESC" : "Tooltip description",
    "IMAGE_LINKS" : {
        "ICON" : "someIconPath",
        "SMALL" : "someSmallPath",
        "LARGE" : "someLargePath"
    },
    "VISIBILITY" : "NEVER"
}

DEFAULT_TRADE = {
    "ID" : 0,
    "ITEMS_IN" : {
        "ITEM_ID": "QUANTITY"
    },
    "ITEMS_OUT": {
        "ITEM_ID" : "QUANTITY"
    },
    "VISIBILITY" : "NEVER"
}

DEFAULT_STORY = {
    "ID" : 0,
    "TITLE" : "Story title",
    "LONG_DESC" : "Long description for story. Can be several lines long",
    "SHORT_DESC" : "Tooltip description",
    "VISIBILITY" : "NEVER",
    "TRADES" : {
        "TRADE_ID": "NEXT_STORY_ID"
    }
}

DEFAULT_HUB = {
    "ID" : 0,
    "TITLE" : "Story title",
    "LONG_DESC" : "Long description for story. Can be several lines long",
    "SHORT_DESC" : "Tooltip description",
    "VISIBILITY" : "NEVER",
    "STORIES" : [],
    "HUBS" : {
        "HUB_ID": "TIME_REQUIRED"
    }
}