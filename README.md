# Personal Website Version-2 - The Backend
A new version of my personal website/data analytics blog that I started working on late January 2023. 

This is written using Flask & SQLAlchemy to server data from a Postgres database. As of this writing on February 25, 2023, I am still developing the website and nothing is live. Currently the database only lives on my machine and API calls are to localhost. My target is to have a live version of this website by the end of March with the backend hosted in a cloud provider that I am still deciding upon.

## /controllers
Handle all the user requests and general logic for API calls.

## /models
SQLAlchemy models that represent the db tables.

## /test
Unit tests using pytest. I am currently a little light on the TDD - hoping to have a more complete test suite before this goes live.