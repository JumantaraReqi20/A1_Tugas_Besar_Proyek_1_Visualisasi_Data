from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

url = r"https://www.tokopedia.com/search?navsource=&srp_component_id=04.06.00.00&srp_page_id=&srp_page_title=&st=&q=ADVAN%20Laptop%20Workplus%20AMD%20RYZEN%205"
# url = r"https://www.tokopedia.com/search?q=axioo+pongo+725&source=universe&st=product&navsource=home&srp_component_id=02.02.02.02"
opsi = webdriver.ChromeOptions()
opsi.add_argument("--start-maximized")
servis = webdriver.chrome.service.Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)
# opsi = webdriver.EdgeOptions()
# opsi.add_argument("--start-maximized")
# servis = EdgeService('msedgedriver.exe')
# driver = webdriver.Edge(service=servis, options=opsi)

driver.get(url)

try:
    list_nama, list_rating, list_harga, list_link, list_terjual, list_lokasi = [], [], [], [], [], []
    for i in range(14):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "css-llwpbs")))
        for i in range(1, 10):
            akhir = 1000 * i
            driver.execute_script(f"window.scrollTo(0, {akhir})")
            print(f"loading ke-{i}")
            time.sleep(1)

        time.sleep(7)  # Tunggu hingga semua elemen ter-load

        content = driver.page_source
        data = BeautifulSoup(content, 'html.parser')

        for index, area in enumerate(data.find_all('div', class_="css-llwpbs"), start=1):

            product_link = area.find('a')['href'] if area.find('a') else 'N/A'

            nama = area.find('div', class_="prd_link-product-name css-3um8ox").get_text(strip=True) if area.find('div', class_="prd_link-product-name css-3um8ox") else None

            # Memproses data harga produk
            harga = area.find('div', class_="prd_link-product-price css-h66vau").get_text(strip=True) if area.find('div', class_="prd_link-product-price css-h66vau") else None
            harga = harga.replace('Rp', '').replace('.', '') if harga else None
            harga = int(harga) if harga else None

            # Memproses data jumlah produk yang terjual
            terjual = area.find('span', class_="prd_label-integrity css-1sgek4h").get_text() if area.find('span', class_="prd_label-integrity css-1sgek4h") else '0'
            terjual = terjual.replace(' terjual', '').replace('rb', '000').replace('+', '')
            terjual = int(terjual)

            # Memproses data rating produk
            rating = area.find('span', class_="prd_rating-average-text css-t70v7i").get_text() if area.find('span', class_="prd_rating-average-text css-t70v7i") else None
            rating = float(rating) if rating else None

            lokasi = area.find('span', class_="prd_link-shop-loc css-1kdc32b flip").get_text(strip=True) if area.find('span', class_="prd_link-shop-loc css-1kdc32b flip") else None

            # # Navigasi ke halaman produk
            # if product_link != 'N/A':
            #     driver.get(product_link)
            #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.css-1asz3by")))

            #     # Cari elemen yang berisi informasi stok
            #     stok_element = driver.find_element_by_css_selector("p.css-1yy88m3-unf-heading.e1qvo2ff8 > b")
            #     stok = stok_element.text if stok_element else 'N/A'
            # else:
            #     stok = 'N/A'

            list_nama.append(nama)
            list_rating.append(rating)
            list_harga.append(harga)
            list_link.append(product_link)
            list_terjual.append(terjual)
            list_lokasi.append(lokasi)

        # Tunggu hingga tombol "Next" muncul (maksimal 10 detik)
        pagination = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "nav.css-txlndr-unf-pagination"))
        )

        # Cari tombol "Next" dalam pagination
        next_button = pagination.find_element(By.CSS_SELECTOR, "button[aria-label='Laman berikutnya']")

        # Klik tombol "Next"
        next_button.click()

    df = pd.DataFrame({
        'Nama': list_nama,
        'Rating': list_rating,
        'Harga': list_harga,
        'Link': list_link,
        'Terjual': list_terjual,
        'Lokasi': list_lokasi
    })

    df.to_json('data_advan_workplus.json', orient='records', indent=2)

finally:
    driver.quit()