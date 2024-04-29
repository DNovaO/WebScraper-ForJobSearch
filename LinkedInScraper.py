from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time 

linkedinUrl = "https://www.linkedin.com/jobs"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

request = Request(linkedinUrl, headers=headers)

page = urlopen(request)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')

# Extraer el texto dentro de la etiqueta <strong> dentro de cada job-card-container
job_titles = []
for job_container in soup.find_all('strong'):
    job_link = job_container
    if job_link:
        job_titles.append(job_link.get_text())
        time.sleep(10)
            

# Guardar los títulos de los trabajos en un archivo
with open('archivo.txt', 'w', encoding='utf-8') as archivo:
    archivo.write("TÍTULOS DE TRABAJOS:\n")
    archivo.write("-----------------------------\n")
    for title in job_titles:
        archivo.write(title + "\n")
    archivo.write("-----------------------------\n")

print("Datos guardados en archivo.txt")
