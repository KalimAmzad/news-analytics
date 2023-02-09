from requests_html import HTMLSession
import pandas as pd

# Create a session object
session = HTMLSession()

# Use the object above to connect to needed webpage
r = session.get('https://www.sharenews24.com/index.php?page=allnews&catid=3&start=1')

# Run JavaScript code on webpage
# r.html.render()

# Create empty lists to store data in
titles = []
links = []
dates = []
descriptions = []

# Extract information from the webpage and store in the created lists
# for i in r.html.find('div.news-list'):
#     for j in i.find('div.news-list-item'):
#         titles.append(j.find('h3', first=True).text)
#         links.append(j.find('a', first=True).attrs['href'])
#         dates.append(j.find('span', first=True).text)
#         descriptions.append(j.find('p', first=True).text)

# # Create a dataframe and export to csv
# df = pd.DataFrame({'Title': titles, 'Link': links, 'Date': dates, 'Description': descriptions})
# df.to_csv('data/news.csv', index=False)

rr = session.get('https://www.sharenews24.com/article/58662/index.html')
print(rr.html.find('div.news-content>div>p'))
print(rr.html.find('div.news-content>div>p')[0].text)

