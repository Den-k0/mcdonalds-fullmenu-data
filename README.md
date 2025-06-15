# McDonald's Full Menu Data

## Description
This project collects data about the full menu of McDonald's using web scraping and provides an API to access this data.

## Requirements
- `Python 3.12` or later
- `Poetry` installed for dependency management

## Installation
1. Clone the repository:
```
git clone https://github.com/Den-k0/mcdonalds-fullmenu-data.git
cd mcdonalds-fullmenu-data
```
   
2. Activate the virtual environment and nstall required dependencies:
```
poetry install --no-root
```

## Running Locally
Start the FastAPI server:
```bash
poetry run uvicorn app.main:app --reload
```

The API docs will be available at:
```
http://127.0.0.1:8000/docs
```
