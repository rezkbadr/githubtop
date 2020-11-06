# Github Top Trending Languages #

## Description ##
A REST microservice that lists the languages used by the 100 trending public repos on GitHub.
It works by fetching trending repositories by getting the most starred repos created in the last 30 days.
It consumes Github's public API:
https://api.github.com/search/repositories?q=created:>{date}&sort=stars&order=desc

## Requirements ##
* python3.7
* Django Rest Framework

## Installation ##
`` pip install -r requirements.txt ``

## Run ##
`` python manage.py runserver ``

## Run Tests ##
`` python manage.py test ``