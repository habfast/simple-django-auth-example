This is a super simple demo of authentication in Django.  More detail here: http://b.wj.io/2012/10/simple-django-authentication.html

To start every service:
`docker-compose up -d`

You'll need to create a `sentry` named database in the db container:
`docker exec -ti <db_container_name> psql -U postgres` 
and then:
`create database sentry`

To run django migrations:
`docker-compose run --rm web python manage.py migrate`

To start a sentry background worker:
`docker-compose run -d -e C_FORCE_ROOT=True sentry celery worker -B`

If you want to promote a user to superuser:
```
docker-compose run --rm web python manage.py shell
from django.contrib.auth.models import User
user = User.objects.get(id=1)
user.is_staff = True
user.is_superuser = True
user.save()
```
