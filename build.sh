sudo apt-get install default-libmysqlclient-dev build-essential


pip install -r requirements.txt
python3.9 manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py collectstatic
