import requests
import json
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
postURL = input("Enter Instagram Post Link: ")
postURL = postURL + "?__a=1"

response = requests.get(postURL, headers=headers).json()

file_name = response['graphql']['shortcode_media']['edge_media_preview_comment']['edges'][0]['node']['owner']['username'] + '_' + response['graphql']['shortcode_media']['id'] + '.mp4'

r = requests.get(response['graphql']['shortcode_media']['video_url'], allow_redirects=True, headers=headers)

open(file_name, 'wb').write(r.content)
print("Downloaded: " + file_name)
print("Thanks for using out CLI tool!!!")