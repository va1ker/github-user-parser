## Requirements 
- Python ^3.11
- [Poetry](https://python-poetry.org/)

## Run project
Install dependencies
```bash
poetry install
```

Copy .env.example to .env
```bash
cp .env.example .env
```

Add your token to .env

Create database
```bash
python3 create_database.py
```

Run parser script
```bash
python3 manager.py
```