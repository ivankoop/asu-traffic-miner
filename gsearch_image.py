import requests
from bs4 import BeautifulSoup
import datetime
import uuid

def imgFind(html):

    soup = BeautifulSoup(html, "html.parser")

    img_data = soup.findAll('img')[0]['src']
    img_src = "https://www.google.com.py" + img_data
    img_data = requests.get(img_src).content
    img_tmp_name = uuid.uuid4().hex[:6].upper() + ".jpg"


    with open('traffic_images/' + img_tmp_name, 'wb') as handler:
        handler.write(img_data)

response = requests.get('https://www.google.com.py/search?q=asuncion+traffic+report&oq=asuncion+traffic+report+&aqs=chrome..69i57j69i60l2.3784j0j7&sourceid=chrome&ie=UTF-8')

imgFind(response.text)
