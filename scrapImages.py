import re

import requests
import os
from bs4 import BeautifulSoup
import shutil
import csv
import json

url = "https://imgflip.com/?page="

try:
    os.mkdir("images")
except FileExistsError:
    shutil.rmtree("images")
    os.mkdir("images")

file_json = open("meme.json", "w", encoding="utf8")
file_json.write("[\n")  # to open the object in jason لوضع البيانات التي سيتم قراءتها داخله

file_csv = open("meme.csv", "w", encoding="utf8")
csv_columns = ["author", "title", "img"]
csv_writer = csv.DictWriter(file_csv, fieldnames=csv_columns)
csv_writer.writeheader()

for pageNum in range(2, 4):
    r = requests.get(url + str(pageNum))
    print(r.url)
    soup = BeautifulSoup(r.content, "html.parser")
    divs = soup.findAll("div", class_="base-unit clearfix")

    for div in divs:
        try:
            title = div.find("h2", class_="base-unit-title").find("a").get_text()
        except:
            title = "Not Available"

        try:
            author = div.find("a", class_="u-username").get_text()
        except:
            author = "Not Available"

        try:
            img = div.find("img", class_="base-img")['src']
        except:
            try:
                img = div.find("video", class_="base-img ctx-gif")['src']
            except:
                img = "Not Available"

        # to Save the Image in file
        if img != "Not Available":
            # clean the title and author values , Remove Special Characters From the them لتجنب الأخطاء في التسمية
            title = re.sub(r"[^a-zA-Z0-9]", "", title)
            author = re.sub(r"[^a-zA-Z0-9]", "", author)

            if img.endswith(".jpg"):
                output = open("images/" + title + str(pageNum) + author + ".jpg", "wb")
            else:
                output = open("images/" + title + str(pageNum) + author + ".gif", "wb")

            resource = requests.get("http:" + img)
            output.write(resource.content)  # الموقع الذي يحتوي على الصورة, نأخذ محتواه ونخزنه
            output.close()

            # write data in csv file
            csv_writer.writerow({"author": author, "title": title, "img": img})

            # write data into json file
            data = {}
            data['img'] = img
            data['title'] = title
            data['author'] = author
            json_data = json.dumps(data, ensure_ascii=False)
            file_json.write(json_data)
            file_json.write(",\n")  # new line to create new Array of data in jason

file_json.write("\n]")  # to close the object in jason
file_json.close()
file_csv.close()

print(len(os.listdir('images')), " images are extracted")
