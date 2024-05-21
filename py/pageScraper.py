from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib.parse

# Fungsi untuk mendekode URL
def decode_url(encoded_url):
    # Mengganti escape karakter `\_` dengan spasi ` `
    encoded_url = encoded_url.replace("\\_", " ")

    # Mendekode URL menggunakan urllib.parse.unquote
    decoded_url = urllib.parse.unquote(encoded_url)

    # Mengekstrak URL tujuan dari parameter `r=`
    target_url_start = decoded_url.find("r=") + 2
    target_url_end = decoded_url.find("&", target_url_start)
    target_url = urllib.parse.unquote(decoded_url[target_url_start:target_url_end])

    return target_url


df = pd.read_json('data_axioo_pongo_with_stock.json', orient='records')
# print(df.head(5))

# df['Stok'] = None
# df[['rate_5', 'rate_4', 'rate_3', 'rate_2', 'rate_1']] = None
try:
    opsi = webdriver.ChromeOptions()
    opsi.add_argument("--start-maximized")
    servis = webdriver.chrome.service.Service('chromedriver.exe')
    driver = webdriver.Chrome(service=servis, options=opsi)
    for index, url in enumerate(df['Link'][345:]): # Looping setiap URL
        index += 345
        if 'www.tokopedia.com' not in url[:30]:
            url = decode_url(url)

        driver.get(url)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "css-17qnh40")))
        for i in range(1, 2):
            akhir = 1000 * i
            driver.execute_script(f"window.scrollTo(0, {akhir})")
            print(f"loading ke-{i}")
            time.sleep(1)
        time.sleep(2)  # Tunggu hingga semua elemen ter-load

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        stock = soup.find('div', class_='css-1waacjy').find('b').get_text(strip=True).replace('Sisa', '').strip().replace('.', '')
        df.loc[index, 'Stok'] = int(stock) if (stock != 'Tidak Dijual') else 0
        
        rate_count = [int(row.select_one('td p.css-jtcihq-unf-heading').get_text(strip=True).replace('.', '')) for row in soup.select('table.css-8atqhb tbody tr')]
        df.loc[index, ['rate_5', 'rate_4', 'rate_3', 'rate_2', 'rate_1']] = rate_count if rate_count else 0

        print("data ke-", index, ":", stock)
except Exception as e:
    print(e)
finally:
    df.to_json('data_axioo_pongo_with_stock.json', orient='records', indent=2)

driver.quit()

