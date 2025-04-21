'''
The location for the Flask app interface for the project.
'''
import csv
from flask import Flask
from ProductionCode.most_banned import (
    most_banned_districts,
    most_banned_authors,
    most_banned_states,
    most_banned_titles)

app = Flask(__name__)

@app.route('/')
def home_page():
    '''
    The home page of the Flask app
    '''
    return(
        "<h1>The Forbidden Library</h1>"
        "<p>Use the following endpoints:</p>"
        "<ul>"
        "<li>/most-banned/districts</li>"
        "<li>/most-banned/authors</li>"
        "<li>/most-banned/states</li>"
        "<li>/most-banned/titles</li>"
        "</ul>"
    )
    
@app.route('/most-banned/states', strict_slashes=False)
def states():
    '''
    The endpoint for the most banned states
    '''
    search_results = most_banned_states(5)
    for result in search_results:
        return search_results

@app.route('/most-banned/districts', strict_slashes=False)
def districts():
    '''
    The endpoint for the most banned districts
    '''
    search_results = most_banned_districts(5)
    for result in search_results:
        return search_results
    
@app.route('/most-banned/authors', strict_slashes=False)
def authors():
    '''
    The endpoint for the most banned authors
    '''
    search_results = most_banned_authors(5)
    for result in search_results:
        return search_results
    
@app.route('/most-banned/titles', strict_slashes=False)
def titles():
    '''
    The endpoint for the most banned titles
    '''
    search_results = most_banned_titles(5)
    for result in search_results:
        return search_results
        
if __name__ == '__main__':
    app.run()
    