# Digital Control Room - Django Test

Thank you for taking the time to complete this exercise.

## Introduction

This Django project contains:
 * Models to store simple Country and Region data
 * A JSON API view to retrieve statistics about this data
 * A Django managment command to import this data
 * sqlite database pre-populated with required data

Please clone (don't fork) this repository, complete the exercises below and then upload to a public repository on github and send us the link.

Please don't spend more than 2 hours on this task (not including initial download and setup). If you reach 2 hours, please commit your code as-is to your repository.

## Project Setup

The instructions below are for use with venv, but of course you can setup the project however is most comfortable for you (virtualenv, pipenv, etc.). You will need python3.5+ to run this code.

```bash
git clone https://github.com/DigitalControlRoom/dcr-django-test.git
python3 -m venv dcr-django-test-env
source dcr-django-test-env/bin/activate

cd dcr-django-test
git remote remove origin
git remote add origin <Your Repository>
pip install -r requirements.txt

cd testsite
python manage.py runserver
```

## Exercises

### Exercise 1 - Complete Stats View

http://localhost:8000/countries/stats/ currently returns an empty JSON response, this should be updated to provide a list of regions. 

Each region object should contain:
 * The region's name
 * The number of countries in that region (a simple count)
 * The total population of the region (the sum of the population of each country)

The output format should be:
```json
{
    "regions": [
        {
        "name": "Africa",
        "number_countries": xxx,
        "total_population": xxx
        },
        {
        "name": "Americas",
        "number_countries": xxx,
        "total_population": xxx
        },
        ...
    ]
}
```

### Exercise 2 - Integrate with API

The management command:
```bash
python manage.py update_country_listing
```
currently updates the models from a local JSON file. Please update this management command to obtain the JSON input data from this url:  
https://storage.googleapis.com/dcr-django-test/countries.json

### Exercise 3 - Store additional Data

The management command:
```bash
python manage.py update_country_listing
```
currently extracts and stores the data:
 * name
 * alpha2Code
 * alpha3Code
 * population
 * region

Please update the models and management command to also import:
 * topLevelDomain
 * capital
