## Get Started
init the project
```bash
# clone the repo
git clone https://github.com/omid9h/django-kit.git
# check into the directory (linux)
cd django-kit
# creating a virtual env manually (not by poetry)
python -m venv .venv
# activating venv (linux)
source .venv/bin/activate
# you need poetry: https://python-poetry.org/
poetry install
# get pre-commit hooked
pre-commit install
# intial run (just for test)
pre-commit run -a
# you're good to go
```
populating blog data and test its endpoint
```
python manage.py generate_fake_blog_data
```
and then after runserver this is post_list endpoint:

```<ip>:<port>/blog/?limit=10&offset=0&title=<term>&content=<term>```

## TODO
- postgresql - done using connection string to a running dockerized postgres (for now)
- dockerizing
- elastic stack
