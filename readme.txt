This project creates 2 container in local docker. One for database and one for flask project.
you can reach to flask container with curl or localhost:5000 from your browser. Also, curl command has ability to make post to filter data.


SETUP on your local:
Prerequest:
    You need docker and python installed in your local.
In this project there are 2 container :
    1. database container : postgresql
    2. project container
To create images in container:
    $ docker-compose build
To run containers:
    $ docker-compose up -d

    you can check  http://localhost:5000/ or  http://localhost:5000/get for to see container is working.

To create table in postgresql container:
    $ docker-compose exec web python manage.py create_db

To feed table with initial data:
    $ docker-compose exec web python manage.py seed_db

To check to table:
    $ docker-compose exec db psql --username=hello_flask --dbname=hello_flask_dev

    hello_flask_dev=# \c hello_flask_dev
    hello_flask_dev=# select * from campaign;

For windows curl command to run from CMD :
    curl -i localhost:5000/post -X POST -d "{\"filter\": { \"slot_id\": [123], \"device\": [\"mobile\", \"desktop\"] },\"start_time\": \"12/01/2020\", \"end_time\": \"12/02/2020\", \"group_by\": [\"slot_id\",\"device\"]}