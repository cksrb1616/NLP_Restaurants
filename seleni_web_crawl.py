from selenium import webdriver
import time
from bs4 import BeautifulSoup

location = ['amsterdam-1025', 'diemen-1112', 'amsterdam-1077', 'amsterdam-1077']
titles = []
ratings = []
key = {'100':5, '90':4.5, '80':4,' 70':3.5, '60':3, '50':2.5, '40':2, '30':1.5, '20':1, '10':0.5, '0':0}

for j in range(len(location)):
    browser = webdriver.Chrome("/Users/minjunchoi/Documents/GitHub/Web/selenium/chromedriver")
    browser.maximize_window()
    url = "https://www.thuisbezorgd.nl/en/order-takeaway-"
    browser.get(url+location[j])
    soup = BeautifulSoup(browser.page_source, "lxml")
    movies = soup.find_all("div", attrs={"class": "restaurant js-restaurant"})

    for i in range(len(movies)):
        title = movies[i].find("h2", attrs={"class": "restaurantname"}).get_text()[1:-1]
        titles.append(title)
        rating = movies[i].find("span", attrs={"class": "review-stars-range"})['style'][7:-2]
        ratings.append(rating)

    ratings[:]=[key.get(e,) for e in ratings]
    time.sleep(2)
    browser.quit()