from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def scrape_job_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }

    request = Request(url, headers=headers)

    try:
        page = urlopen(request)
    except Exception as e:
        print(f"Error al abrir la página: {e}")
        return []

    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')

    job_info = []

    # Buscar todas las etiquetas <a> con la clase "base-card__full-link"
    for job_link in soup.find_all('a', class_='base-card__full-link'):
        # Buscar la etiqueta <span> dentro de la etiqueta <a>
        job_title_tag = job_link.find('span', class_='sr-only')
        # Obtener el texto del título de trabajo si se encuentra la etiqueta <span>
        if job_title_tag:
            job_title = job_title_tag.get_text(strip=True)
            # Buscar la etiqueta <h4> con la clase "base-search-card__subtitle"
            company_info = job_link.find_next('h4', class_='base-search-card__subtitle')
            # Obtener el texto de la empresa si se encuentra la etiqueta <h4>
            company_name = company_info.get_text(strip=True) if company_info else "Información no disponible"
            # Obtener el enlace del trabajo
            job_link = job_link.get('href')
            # Agregar el título, la empresa y el enlace a la lista job_info
            job_info.append({'title': job_title, 'company': company_name, 'link': job_link})

    return job_info

def main():
    linkedinUrl = "https://www.linkedin.com/jobs/search?keywords=becario&location=%C3%81rea%20metropolitana%20de%20Quer%C3%A9taro&geoId=90010050&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    
    job_info = scrape_job_info(linkedinUrl)
    
    if job_info:
        with open('job_info.txt', 'w', encoding='utf-8') as archivo:
            archivo.write("INFORMACIÓN DE TRABAJO:\n")
            archivo.write("-----------------------------\n")
            for i, job in enumerate(job_info, start=1):
                archivo.write(f"{i}. Título del trabajo: {job['title']}\n")
                archivo.write(f"   Empresa: {job['company']}\n")
                archivo.write(f"   Enlace: {job['link']}\n\n")
            archivo.write("-----------------------------\n")
        
        print("Datos guardados en job_info.txt")
    else:
        print("No se encontró información de trabajo.")

if __name__ == "__main__":
    main()
