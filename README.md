# TigerAPI

A Django REST API developed as a backend service for a Roblox game, providing persistent player progression, statistics tracking, and integration with Roblox group roles.

TigerAPI stores player data in PostgreSQL and exposes HTTP endpoints that allow game servers to create users, retrieve statistics, update XP, and record weapon performance. Player progression can also trigger automatic Roblox group-role updates.

## Features

* Persistent player data backed by PostgreSQL
* REST API built with Django REST Framework
* Player XP and progression tracking
* Per-game-mode statistics
* Per-weapon kill tracking
* Medal and achievement data
* Automatic initialisation of statistics for new players
* Roblox group-role integration based on XP thresholds
* Django ORM for database access and relationships

## Technologies

* Python
* Django
* Django REST Framework
* Django ORM
* PostgreSQL
* Requests
* Roblox Web APIs

## Data Model

TigerAPI stores progression across several related models.

### GameUser

Represents the core player record and stores:

* Roblox user ID
* First join date
* XP
* Events attended
* Events hosted
* Heals given

### UserStats

Stores statistics for individual game modes, including:

* Wins
* Kills
* Top-frag finishes

### UserWeaponStats

Tracks the number of kills recorded with each weapon.

### UserMedals

Stores player medals and their associated tier.

## API

The API is exposed under `/v1/`.

### Register Player

```http
POST /v1/user_joined/<user_id>
```

Creates a player record if one does not already exist.

When a new player is created, TigerAPI automatically creates the associated game-mode statistics, weapon statistics, and initial medal data.

### Retrieve Player Statistics

```http
GET /v1/user_stats/<user_id>
```

Returns the player's statistics across supported game modes alongside their weapon kill counts.

Example response:

```json
{
  "tdm": {
    "wins": 12,
    "total_kills": 184,
    "topfrags": 4
  },
  "weapon_kills": {
    "AR-11": 80,
    "ARX-5": 51,
    "SR-03": 34,
    "MP-22": 19
  }
}
```

### Retrieve XP

```http
GET /v1/user_xp/<user_id>
```

Returns the player's current XP and configured progression thresholds.

### Add XP

```http
PATCH /v1/user_xp/<user_id>/add_xp/<amount>
```

Adds XP to a player's account.

Updating a player's XP can automatically trigger a corresponding Roblox group-role change based on configured XP thresholds.

### Add Weapon Kills

```http
PATCH /v1/user_stats/<user_id>/add_weapon_kills/<weapon_name>/<amount>
```

Adds kills to the player's statistics for the specified weapon.

## Progression Integration

TigerAPI uses Django model signals to react to changes in player data.

When a new player is created, the backend automatically generates statistics records for each supported game mode and weapon.

When an existing player's XP changes, their current XP is compared against configured progression thresholds. The backend can then communicate with the Roblox Groups API to update the player's group role automatically.

This creates a flow similar to:

```text
Roblox Game
    |
    v
TigerAPI REST Endpoint
    |
    v
Django ORM
    |
    v
PostgreSQL
    |
    v
Progression Check
    |
    v
Roblox Group API
```

## Project Structure

```text
TigerAPI/
├── app/
│   ├── api/
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── signals.py
│   │   ├── tasks.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── app/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── roblox/
│   │   └── client.py
│   │
│   ├── constants.py
│   └── manage.py
│
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd TigerAPI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database and configure the Django database settings.

Sensitive configuration such as database passwords, Django secret keys, and Roblox authentication credentials should be provided through environment variables rather than committed to source control.

### 5. Apply migrations

```bash
cd app
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

The API will then be available from the Django development server under:

```text
/v1/
```

## Security

Do not commit:

* PostgreSQL credentials
* Django `SECRET_KEY` values
* Roblox `.ROBLOSECURITY` cookies
* production environment configuration

Use environment variables or another secret-management solution when deploying the project.

The Roblox integration should only be used with accounts and groups you are authorised to administer.

## Status

This is a legacy project and is no longer actively maintained.

It is preserved as an example of my earlier backend development work involving Django, REST APIs, relational databases, ORM-based data modelling, event-driven model signals, and external API integration.

## License

Licensed under the Apache License 2.0.
