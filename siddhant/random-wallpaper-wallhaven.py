import requests, bs4, os, random
#import subprocess
url = "https://alpha.wallhaven.cc/toplist"
dir_name = 'wallpapers-wallhaven-toplist'
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
print("Downloading Page %s......" % url)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
top_images_list = soup.select('section ul li figure a')
if top_images_list == []:
    print('Could not find images!')
else:
    random_image_url = top_images_list[random.randint(1, len(top_images_list))].get('href')
    res = requests.get(random_image_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    image = soup.select('main section div img')
    image_url = 'https:' + image[0].get('src')
    print('Downloading image.... %s' % image_url)
    res = requests.get(image_url)
    res.raise_for_status()
    imageFile = open(os.path.join('wallpapers-wallhaven-toplist', os.path.basename(image_url)), 'wb')
    for chunk in res.iter_content(10000):
        imageFile.write(chunk)
    imageFile.close()
    #subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri %s" % os.path.join('wallpapers-wallhaven-toplist', os.path.basename(image_url)))
    os.system("gsettings set org.gnome.desktop.background picture-uri %s" % os.path.join(dir_name, os.path.basename(image_url)))
    print("Done!")

