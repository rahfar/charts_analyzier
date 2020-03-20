## Build instruction
* git clone https://github.com/rahfar/Wartsila
* cd Wartsila
* download charts_prj_data.zip (from dropbox) to charts_analyzier/data/ and unarchive it (with same name and structure)
* docker-compose build
* docker-compose up -d
* docker-compose exec app python upload_data.py
    * it takes about 15 minutes

## Usage
* __task 1.b.i__ Zones crossed by the vessel
    * http://172.16.238.11:8000/vessel/
    * Example Vessel id: 9183984  
* __task 1.b.ii__ Vessels passing through the zone 
    * http://172.16.238.11:8000/zone/
    * Example Zone id: zone_1