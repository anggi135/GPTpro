import feedparser
import feedparser
import openai
import os
#ambil title, deskripsi dan deskripsi
rss_url = "https://example.com/feed"
feed = feedparser.parse(rss_url)
for entry in feed.entries:
    title = entry.title
    link = entry.link
    description = entry.description
    # melakukan ekstraksi informasi yang diperlukan dari setiap posting
#gambar
rss_url = "https://example.com/feed"
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    title = entry.title
    link = entry.link
    description = entry.description
    image_url = entry.media_content[0]['url']
    category = entry.category
    # melakukan ekstraksi informasi yang diperlukan dari setiap posting
#rewriet pake gpt
openai.api_key = os.environ["OPENAI_API_KEY"]
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()
    
#login ggle+keblogspot+posting 
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from bs4 import BeautifulSoup
import requests

# Path ke file credential dari akun google
SERVICE_ACCOUNT_FILE = 'credential.json'

# Inisialisasi credential
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=['https://www.googleapis.com/auth/blogger'])

# Inisialisasi API Blogspot
blogger = build('blogger', 'v3', credentials=creds)
# Definisikan fungsi untuk memposting artikel ke blogspot
def create_post(blog_id, title, content):
    try:
        # Membuat request untuk mengambil informasi blog
        blog_request = blogger.blogs().get(blogId=blog_id)
        blog = blog_request.execute()

        # Mengambil URL dari blog
        blog_url = blog['url']

        # Mengubah HTML ke teks biasa
        soup = BeautifulSoup(content, 'html.parser')
        plain_text = soup.get_text()

        # Membuat post request
        post_request = blogger.posts().insert(
                blogId=blog_id,
                body={
                    'title': title,
                    'content': content,
                    'labels': ['generated'],
                    'url': blog_url + '/post-title-' + str(title),
                    'isDraft': False
                })
        post_request.execute()
        print(f"Artikel '{title}' berhasil diposting ke blogspot")
    except HttpError as error:
        print(f'An error occurred: {error}')
        post = None

# Memanggil fungsi create_post dengan parameter yang sesuai
blog_id = '123456789' # ID blogspot
title = 'Judul Artikel'
content = 'Konten artikel'

create_post(blog_id, title, content)

