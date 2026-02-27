List Bot (Discord Slash Command Queue Bot)
==========================================

A Discord slash-command bot that manages a structured list using a queue data structure.
Each entry stores:

- Title (text content)
- User who added it
- Date added

The bot persists data locally using JSON storage and runs in a single development server.

---------------------------------------------------------------------

Overview
--------

List Bot allows Discord users to maintain a shared queue of items.
Each queued item is stored as a structured object containing:

{
  "title": "<item text>",
  "user": "<nickname>",
  "time": "<YYYY-MM-DD>"
}

The bot uses slash commands (discord.app_commands) and synchronizes
commands to a development guild.

Queue data is persisted locally in a data.json file.

---------------------------------------------------------------------

Features
--------

- /queue <item>        → Add a new item to the queue
- /list [n]            → View the first n items (or all if omitted)
- /size                → View total number of items
- /next                → View the next item in queue
- /pick                → Randomly select an item
- /shuffle             → Shuffle queue order
- /remove <item>       → Remove item by title
- /ping                → Health check

---------------------------------------------------------------------

Technical Details
-----------------

Language: Python  
Libraries:
- discord.py (app_commands / slash commands)
- python-dotenv
- JSON (local persistence)

Architecture:

- Custom Queue class (myQueue.py)
- In-memory list-based queue
- JSON file used for persistence across restarts
- Slash command registration scoped to a development guild
- Bot syncs commands on startup

---------------------------------------------------------------------

Queue Implementation
--------------------

The Queue class provides:

- enqueue()
- dequeue()
- size()
- isEmpty()
- displayQueue(n)
- get(index)
- remove(title)
- shuffle()
- load_json()
- save_json()

Data is stored internally as a list of dictionaries.
Shuffling uses Python's built-in random.shuffle().

---------------------------------------------------------------------

Persistence Model
-----------------

Queue state is stored in data.json.

- On startup: load_json() attempts to load previous state.
- On mutation (queue, shuffle, remove): save_json() writes updated state.
- If no file exists, bot initializes with empty queue.

No external database is used.

---------------------------------------------------------------------

Environment Variables
---------------------

Required in .env file:

DISCORD_TOKEN=<your_bot_token>
DEV_SERVER=<development_guild_id>

---------------------------------------------------------------------

Limitations
-----------

- Local JSON storage only (no production database)
- Guild-scoped slash commands (not global)
- No permission roles implemented
- Title-based removal may remove first matching entry only

---------------------------------------------------------------------

Future Improvements
-------------------

- Add unique IDs for each queue entry
- Implement role-based permissions
- Improve date formatting
- Add pagination for long lists
- Add per-channel queues
- Deploy to cloud hosting (Docker / VPS)
- Replace JSON with SQLite for stronger persistence

---------------------------------------------------------------------

Purpose
-------

This project demonstrates:

- Slash command integration with Discord API
- Custom data structure implementation
- Local persistence using JSON
- Object-based state modeling
- Event-driven bot development
- Environment-based configuration handling
