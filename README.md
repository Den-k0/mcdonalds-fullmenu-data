# McDonald's Full Menu Data

## Description
This project collects data about the full menu of McDonald's using web scraping and provides an API to access this data.

## Requirements
- `Python 3.12` or later
- `Poetry` installed for dependency management

## Installation
1. Clone the repository:
```
git clone https://github.com/your-username/mcdonalds-fullmenu-data.git
cd mcdonalds-fullmenu-data
```
   
2. Activate the virtual environment:
```
poetry install
poetry shell
```
3. Install required dependencies:
```
poetry install
```

## Running Locally
Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at:
```
http://127.0.0.1:8000
```