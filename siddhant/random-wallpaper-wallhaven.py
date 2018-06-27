import requests, bs4, os, random
url = 'https://alpha.wallhaven.cc/toplist'
dir_name = 'wallpapers-wallhaven-toplist'
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
print('Downloading Page %s......' % url)
res = requests.get(url, verify=False)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
top_images_list = soup.select('section ul li figure a[class="preview"]')
if top_images_list == []:
    print('Could not find images!')
else:
    random_image_url = 'https:' + '//wallpapers.wallhaven.cc/wallpapers/full/wallhaven-' + top_images_list[random.randint(1, len(top_images_list))].get('href')[38:] + '.jpg'
    print('Downloading image.... %s' % random_image_url)
    random_image_res = requests.get(random_image_url, verify=False)
    imageFile = open(os.path.join('wallpapers-wallhaven-toplist', os.path.basename(random_image_url)), 'wb')
    for chunk in random_image_res.iter_content(10000):
        imageFile.write(chunk)
    imageFile.close()
    os.system('gsettings set org.gnome.desktop.background picture-uri %s' % os.path.join(dir_name, os.path.basename(random_image_url)))
    print('Done!')
