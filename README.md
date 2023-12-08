# social_media_backend-backend
social_media_backend Backend

## Local Deployment

1. make virtual env   `mkvirtualenv social_media_backend-backend`
2. Install required python packages
   `pip install -r ../requirements.txt`

   (might have to comment out psycopg2==2.9.3 on mac and use pip install psycopg-binary)

3. Make a database in postgres
   `sudo -u postgres -i` for server side and then `psql`

   Run following commands in `psql` terminal

```
CREATE DATABASE social_media_backend;
CREATE USER social_media_backend_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE social_media_backend TO social_media_backend_user;
create extension hstore;
```

4. `cd app`
5. `touch social_media_backend/local_settings.py`
6. `python manage.py migrate`
7. `python manage.py createsuperuser`
8. `python manage.py collectstatic`
9. `python manage.py runserver`
10. To run https server use `python manage.py runsslserver 0:8000`



