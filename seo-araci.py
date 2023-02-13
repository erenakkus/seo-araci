# Eren Antares Akkuş
import requests
a=input("Web Sitenizin adresini giriniz: ")
url = a
response = requests.get(url)
html_content = response.content
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_content, "html.parser")

# Meta etiketlerini arama
meta_tags = soup.find_all("meta")

# H1 etiketlerini arama
h1_tags = soup.find_all("h1")
# Meta açıklamasında anahtar kelime bulunup bulunmadığını kontrol etme
keyword = input("Anahtar Kelimenizi Giriniz: ")
keyword_found = False
for meta_tag in meta_tags:
    if "name" in meta_tag.attrs and meta_tag.attrs["name"] == "description":
        description = meta_tag.attrs["content"]
        if keyword in description:
            keyword_found = True

# H1 etiket sayısı kontrol etme
if len(h1_tags) == 1:
    h1_count = "Başarılı"
else:
    h1_count = "Başarısız"

# Sonuçları ekrana yazdırma
if keyword_found and h1_count == "Başarılı":
    print("Başarılı")
else:
    print("Başarısız")
