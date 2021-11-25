### FastApi and Docker example
Clone this repo:
```
git clone git@github.com:kazak600/fastapi-app-example.git && cd fastapi-app-example  
```
Create new environment:

```
virtualenv --python=python3.9 venv
```

Activate environment:

```
. venv/bin/activate
```

Install backend package:

```
pip install -e .
```

Copy or create config file `.env`:

```
cp .env.example .env
```

Run project:

```
uvicorn main:app --reload
```

Run tests:

```
export IS_TEST=True && pytest tests
```

Run docker app container

```
docker-compose up
```