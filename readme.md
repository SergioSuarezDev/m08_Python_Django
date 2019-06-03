# WordPlease

Python-Django Module - Keepcoding 2019



## Installation

### Clone this repo:

`git clone https://github.com/SergioSuarezDev/m08_Python_Django.git`

### Setup enviroment

`virtualenv env`

`source env/bin/activate`

### Install requirements:
`pip install -r requirements.txt`

### Create data base
`python manage.py migrate`

### Create super user
`python manage.py createsuperuser`

### Run Dev server
`python manage.py runserver`


### WordPlease API REST

### Users

| Method | Result | URL |
| ------ | ------ | --- |
| GET |  list | `/api/v1.0/users/` |
| POST | create  | `/api/v1.0/users/`
| GET |  detail | `/api/v1.0/users/<int:pk>` |
| PUT |  update | `/api/v1.0/users/<int:pk>` |
| DELETE |  delete | `/api/v1.0/users/<int:pk>` |

### Blog & Posts
| Method | Result | URL |
| ------ | ------ | --- |
| GET | blogs list | `/api/v1.0/blogs/` | 
| GET |  blog detail  | `/api/v1.0/blogs/<str:username>` |
| GET |  post list | `/api/v1.0/posts/` |
| POST | new post | `/api/v1.0/posts/` |
| GET | post detail | `/api/v1.0/posts/<int:pk>` |
| PUT | post update | `/api/v1.0/posts/<int:pk>` |
| DELETE | post delete | `/api/v1.0/posts/<int:pk>` |

