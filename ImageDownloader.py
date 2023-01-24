import requests
import os
from bs4 import BeautifulSoup

url = "https://www.google.com"
savePath = r"C:\Users\%USERPROFILE%\Desktop"
directory = "New folder"

def imageDownload(url, savePath, directory): 
  # Creating and Changing Path for image stored location
  try:
    path = os.path.join(savePath, directory)
    if not (os.path.exists(path)):
      os.mkdir(path)
  except:
    print("Error for creating folder path")

  os.chdir(path)

  # Getting response from URL and retrieve image url by finding corresponding element
  response = requests.get(url)

  if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')

    images = soup.findAll('img')
    # For specified class name
    # images = soup.findAll('img', {"class":"value"})

    for image in images:
      name = image.img['alt']
      link = image['src']

      with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as file:
        response = requests.get(link)
        file.write(response.content)
        print(f"Writing file {name} in {path}")
  print("Finished in download all files")


if __name__ == "__main__":
  imageDownload(url, savePath, directory)