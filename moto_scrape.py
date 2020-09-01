from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://suchen.mobile.de/fahrzeuge/search.html?damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&makeModelVariant1.makeId=18100&makeModelVariant1.modelDescription=v7&minFirstRegistrationDate=2015&scopeId=MB&sfmr=false&sortOption.sortBy=searchNetGrossPrice&sortOption.sortOrder=ASCENDING"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())
