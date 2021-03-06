# Cinewise - Movie Recommendation Using Graph Theory

<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/Presto-Chango"> <img alt="PyPI - Django Version" src="https://camo.githubusercontent.com/f5c59809fc4f0316f011de93c19a513853bec99b/68747470733a2f2f696d672e736869656c64732e696f2f707970692f646a76657273696f6e732f6472662d796173672d65646765"> <img alt="PyPI - License" src="https://img.shields.io/pypi/l/Presto-Chango">


Recommend movies based on user's preferred movies, genres, actors, directors and storywriters. **[Click here](http://cinewise.yashrajkakkad.me/) to see it in action.**

![Preview](https://github.com/yashrajkakkad/movie-recommendation/blob/master/preview.png?raw=true)

This project implements the first two algorithms [from a research paper](https://ieeexplore.ieee.org/document/6621363) published in IEEE Xplore:
- Union Colors - a combination of multisource 'breadth first search' (BFS) and union-find data structure.
- Energy Spread - a variation of multisource breadth first search.

The explanation for these algorithms can be found in the paper. Credits for the same go to the respective authors.

We have created a Django application around the algorithm for a smooth experience. Bootstrap is used for creating a simple yet elegant frontpage.

## The Graph
The graph has movie titles, genres and the assoicated directors, actors and story writers as the vertices. These vertices are mutually connected for every movie.

## OMDB API
We used [OMDB API](http://www.omdbapi.com/) to obtain movie information and create a graph around it. The data is stored using serialization. (movies.pickle, node.pickle and graph.pickle)

## Configuration
You need to manually add the movie attributes in the database for autocompletion. Rest of the steps are the same as any other Django project.

- Clone this repository
```sh
git clone https://github.com/yashrajkakkad/movie-recommendation.git
cd movie-recommendation
```
- Install the required packages. Using a virtual environment is recommended.
```sh
pip install -r requirements.txt
```
- Create a file to store your environment variables for python-decouple to give them at the right places.
```sh
nano .env
```
```
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
APIKEY=''
SECRET_KEY=''
DEBUG=''
```
- If you're not going to use a PostgreSQL database, change the DATABASES variable in mysite/settings.py accordingly. Refer [Django documentation](https://docs.djangoproject.com/en/3.0/ref/databases/) for that. 

- If you're going to play with movie related information, you can obtain your API key from OMDB website [here](https://www.omdbapi.com/apikey.aspx). Otherwise keep it blank.

- `DEBUG=True` for development and `False` for production.

- Make the initial migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

**Here's the 'different' part:**
- Open the Django shell:
```sh
python manage.py shell
```
- Add the vertices:
```py
from utils.Movies import *
from cinewise.models import Node
nodes = load_nodes()
for node in nodes:
    Node(name=node).save()
```

