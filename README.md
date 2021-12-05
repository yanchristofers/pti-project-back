# pti-project-back

## TODO :

1. Implement get movie by title
2. Implement update like field
3. Implement get all data sorted by like amount
4. Implement get all data sorted by released year (descending and ascending)

## Clone this repository

`git clone`

`git checkout -b "<branch_name>"`


Install modules

`pip install -r requirements.txt`

Run server

`python manage.py runserver`

## Contributing


`git pull origin main`


`git add .`

`git commit -m "<message>"`

`git push origin <branch name>`

## API Docs 
GET ALL FILM

`https://localhost:8000/showcase` method="GET"

GET ALL FILM SORTED BY YEAR ASCENDING

`https://localhost:8000/showcase/year_ascending` method="GET"

GET ALL FILM SORTED BY YEAR DESCENDING

`https://localhost:8000/showcase/year_descending` method="GET"

POST FILM

`https://localhost:8000/showcase` method="POST"

ADD LIKE

`https://localhost:8000/showcase/id/like` method="PUT"

ADD DISLIKE

`https://localhost:8000/showcase/id/dislike` method="PUT"

DELETE FILM

`https://localhost:8000/showcase/id` method="DELETE"
