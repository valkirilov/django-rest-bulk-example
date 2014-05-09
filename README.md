django-rest-bulk-example
========================

Not working example from bulk POST with django-rest

How to run it
========================

* Create file `local_settings.py` under the `giftycards/giftycards/` and setup your db.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'table-name',
        'USER': 'root',
        'PASSWORD': 'your-password',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
```
* Create the db tables with `./giftycards/manage.py syncdb`
* Then run it from with `./giftycards/manage.py runserver`
* Go to `/api/teachers/` and try to POST something like this:
```
[{
    "name": "Some test name", 
    "degree": "-", 
    "short": "-", 
    "email": "gosho@mail.com", 
    "department": "-"
},
{
    "name": "Trugvai..", 
    "degree": "-", 
    "short": "-", 
    "email": "pesho@mail.com", 
    "department": "-"
}]
```
