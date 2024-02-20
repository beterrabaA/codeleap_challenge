# Codeleap Challenge

API to manage users data

## Run locally

```bash
python3 -m venv env
source env/bin/activate
pip install djangorestframework

cd api_codeleap
python .\manage.py runserver
```

## Endpoints

#### List all users

```http
GET http://localhost:8000/user/
```

```json
[
  {
    "id": 1,
    "username": "leomaneiro",
    "created_datetime": "2024-02-20T22:42:44.703253Z",
    "title": "charmer",
    "content": "content"
  },
  {
    "id": 2,
    "username": "leomaneiro2",
    "created_datetime": "2024-02-20T22:56:57.057420Z",
    "title": "unic",
    "content": "content"
  }
]
```

#### Create a new user

```http
POST http://localhost:8000/user/
```

Input

```json
  {
    "username": "leomaneiro3",
    "title": "runner",
    "content": "content"
  },
```

Output

```json
  {
    "id": 3,
    "username": "leomaneiro3",
    "created_datetime": "2024-02-20T22:56:57.057420Z",
    "title": "runner",
    "content": "content"
  },
```

#### Update user

```http
PATCH http://localhost:8000/user/${id}
```

| Parâmetro | Tipo     | Descrição                                   |
| :-------- | :------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

Input

```json
  {
    "title": "suspicious",
    "content": "another content"
  },
```

Output

```json
  {
    "id": 3,
    "username": "leomaneiro3",
    "created_datetime": "2024-02-20T22:56:57.057420Z",
    "title": "suspicious",
    "content": "another content"
  },
```

#### Delete user

```http
DELETE http://localhost:8000/user/${id}
```

| Parâmetro | Tipo     | Descrição                                   |
| :-------- | :------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

Output

```json
{}
```
