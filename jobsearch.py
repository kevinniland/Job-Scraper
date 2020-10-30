import urllib
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import os

def search_jobs_indeed(job_title, location):
    # https://ie.indeed.com/jobs?q=junior+software&l=ireland
    parameters = {'q': job_title, 'l': location, 'fromage' : 'last', 'sort': 'date'}
    url = ('https://ie.indeed.com/jobs?' + urllib.parse.urlencode(parameters))
    page = requests.get(url)
    beautifuloup = BeautifulSoup(page.content, 'html.parser')
    job_soup = beautifuloup.find(id = 'resultsCol')

    return job_soup

def extract_title_indeed():
    return 0

def extract_company_indeed():
    return 0

def extract_link_indeed():
    return 0

def extract_date_indeed():
    return 0
