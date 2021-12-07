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

`https://pti-final-project-be.herokuapp.com` method="GET"

GET ALL FILM SORTED BY YEAR ASCENDING

`https://pti-final-project-be.herokuapp.com?sort=year_ascending` method="GET"

GET ALL FILM SORTED BY YEAR DESCENDING

`https://pti-final-project-be.herokuapp.com?sort=year_descending` method="GET"

GET FILM BY TITLE

`https://pti-final-project-be.herokuapp.com/search/?search=<title>` method="GET"

POST FILM

`https://pti-final-project-be.herokuapp.com/` method="POST"

ADD LIKE

`https://pti-final-project-be.herokuapp.com/id/like` method="PUT"

ADD DISLIKE

`https://pti-final-project-be.herokuapp.com/id/dislike` method="PUT"

DELETE FILM

`https://pti-final-project-be.herokuapp.com/id` method="DELETE"
