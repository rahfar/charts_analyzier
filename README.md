## Build instruction
* git clone https://github.com/rahfar/Wartsila
* cd Wartsila
* docker-compose build
* docker-compose up -d
* docker-compose exec app python manage.py migrate

### For initial upload test data:
* docker-compose exec app python upload_data.py
