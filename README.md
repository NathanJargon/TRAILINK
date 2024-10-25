# TRAILINK

This project is a full-stack application with a React frontend (client) and a Django backend (server).

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Starting the Client](#starting-the-client)
- [Starting the Server](#starting-the-server)
- [Running the Application](#running-the-application)

## Project Structure
TRAILINK/
├── client/                  # React Frontend
│   ├── public/              
│   ├── src/
│   │   ├── components/      # Reusable components
│   │   ├── screens/         # Page-specific components
│   │   ├── styles/          # Styling files
│   │   ├── App.js           # Main React component
│   │   ├── App.css          # Global styles
│   │   └── index.js         # React entry point
│   ├── package.json         # Client dependencies
│   └── README.md
└── server/                  # Django Backend
    ├── myproject/
    │   ├── api/             # Django app for API
    │   │   ├── migrations/  # Database migrations
    │   │   ├── __init__.py  # API init file
    │   │   ├── admin.py     # Django admin setup
    │   │   ├── apps.py      # API app configuration
    │   │   ├── models.py    # API models
    │   │   ├── serializers.py # API serializers
    │   │   ├── tests.py     # API tests
    │   │   ├── views.py     # API views
    │   │   └── urls.py      # API routes
    │   ├── myproject/
    │   │   ├── __init__.py  
    │   │   ├── settings.py  # Django settings
    │   │   ├── urls.py      # Global routes
    │   │   ├── wsgi.py      # WSGI config for server
    └── manage.py            # Django's command-line utility


## Getting Started

### Prerequisites

- **Node.js** (for React client) - [Download](https://nodejs.org/)
- **Python 3.x** (for Django server) - [Download](https://www.python.org/downloads/)
- **Django** and **Django REST Framework** for the backend
- **npm** or **yarn** for managing dependencies in React

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/trailink.git
   cd trailink
   ```

2. Navigate to the client directory and install dependencies:
    ```
    cd client/app
    npm install
    # or if you're using yarn
    yarn install
    ```

3. Navigate to the server directory and run server
    ```
    cd server/myproject
    python manage.py runserver
    ```

### Running the Application

Once both the client and server are running, you can access the full application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api
