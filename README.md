# CutIt
CutIt is a platform to shorten your URLs. 

# Installation Guide
Pre Requirements-
- Python >= 2.7
- git
- MySql 5.5 or above
- virtualenv

Get the source code from git-
```
git clone https://github.com/pingrs/CutIt.git
```
Create virtual environment and install dependencies-
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
Create local settings file-
```
cd CutIt
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
