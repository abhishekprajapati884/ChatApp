# Real-Time Chat Application

A real-time chat application built using FastAPI and WebSockets, enabling instant bidirectional communication between connected clients.

## Features

- Real-time messaging using WebSockets
- Asynchronous backend with FastAPI
- Persistent client-server connections
- Jinja2 template rendering
- Static asset management

## Tech Stack

- Python
- FastAPI
- WebSockets
- Jinja2
- HTML
- JavaScript

## Installation

```bash
git clone <repo-url>
cd chatapp

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

fastapi dev main.py
