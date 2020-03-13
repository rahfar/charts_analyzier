## Build instruction
* git clone https://github.com/rahfar/Wartsila
* cd Wartsila
* docker-compose build
* docker-compose up -d
* docker-compose exec app python manage.py migrate

### For initial upload test data:
* download charts_prj_data.zip (from dropbox) to charts_analyzier/data/ and unarchive it (with same name and structure)
* docker-compose exec app python upload_data.py
