# CutIt
Cutit (<http://cutit.tk/>) is a URL shortening platform. It is a free service. No need to login or register. Just paste your url in box and get the shorten URL to share on internet.

# Installation Guide
Pre Requirements-
- Python 3.x
- git
- MySql 5.7 or above
- virtualenv

Get the source code from git-
```
git clone https://github.com/pingrs/CutIt.git cutIt
```
Create virtual environment and install dependencies-
```
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```
Create local settings file-
```
cd cutIt
cp cutit/dev_settings_sample.py cutit/dev_settings.py
```
Change the MySql credentials in cutit/dev_settings.py

Migrate Database-
```
python manage.py makemigrations
python manage.py migrate --settings=cutit.dev_settings
```
Now you are all done. You can run server using-
```
python manage.py runserver --settings=cutit.dev_settings
```
Open <http://127.0.0.1:8000> in browser and enjoy!!!


### Future Plans

* Add admin dashboard

* Add expiry and other features

* Add analytics system

* Add logger
