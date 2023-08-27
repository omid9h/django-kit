## Get Started
pre-commit
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
poetry install --dev
# get pre-commit hooked
pre-commit install
# intial run (just for test)
pre-commit run -a
# you're good to go
```

## TODO
- dockerizing
- postgresql
- elastic stack
