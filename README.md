# Django Todo HTMX

Just trying out [htmx](https://htmx.org/) with Django.

Also used [django-tailwind](https://github.com/timonweb/django-tailwind) for styling.

## Requirements
- python 3.9 (but can work with any python 3.8+)
- node.js (for building tailwind)


## Running

### Poetry

```
$ poetry install
$ poetry shell
$ python manage.py runserver
```

### Pip
   Activate your venv first.

```
$ pip install -r requirements.txt
$ python manage.py runserver
```

### Building CSS

```
$ python manage.py tailwind start
```
