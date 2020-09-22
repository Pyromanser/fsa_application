# FSA application

Pre-requirements:
- [docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)
- [google api key](https://developers.google.com/maps/documentation/geocoding/get-api-key)

How to run this app:
1) Replace `DJANGO_SECRET_KEY` and `GOOGLE_API_KEY` in `config/.env` with your api and secret key
2) Run `docker-compose build`
3) Run `docker-compose up`
4) Open [fsa](http://localhost:3000/) in browser

API endpoints (check [swagger](http://localhost/api/swagger/)):

- `/api/geo/address-to-geocode/`
- `/api/geo/geocode-to-address/`
- `/api/geo/calc-distance/`

***

Extras:
- `docker-compose run web python manage.py test --debug-mode` - runs test
- [swagger](http://localhost/api/swagger/) - Use it to view and check endpoints.
- [openapi](http://localhost/api/swagger/?format=openapi)
- [mailhog](http://localhost:8025/)
- [pgadmin](http://localhost:5050/) - Use those credentials - `admin@example.com` / `admin`
- [silk](http://localhost/silk/)

List of containers:
- frontend
- web
- db
- nginx
- mailhog
- pgadmin
