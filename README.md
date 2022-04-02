# twice-data-scrape
#### Scraped using BeautifulSoup
Scraping album data from https://kprofiles.com/twice-discography/  
just made for educational purpose.  
site is a bit wacky so i'm missing a few albums  
ill maybe add database later idk


## How to run
```
pip install -r requirement.text
python app.py
```

### Struggles
getting the right elements from the website  
while also looping through all the albums, figured album format would be  a `<p>` element first with all the album info followed by a `<ol>` element with all the songs from the corresponding album.  
WRONG: example `Eyes Wide Open` had 2 `<p>` elements like ????    
