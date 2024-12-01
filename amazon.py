from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import os
import requests
import zipfile
import io

def download_chromedriver():
    # Download ChromeDriver version 131
    version = "131.0.6778.86"  # Match your Chrome version
    print(f"Downloading ChromeDriver version {version}...")
    
    # Use the newer chromedriver storage URL
    url = f"https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{version}/win64/chromedriver-win64.zip"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Extract the zip file
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall("chromedriver")
        
        # The path is different in the newer versions
        return os.path.abspath("chromedriver/chromedriver-win64/chromedriver.exe")
    else:
        raise Exception(f"Failed to download ChromeDriver. Status code: {response.status_code}")

def scrape_amazon(keyword, max_pages=20):
    # Setup Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    # Initialize Chrome driver with downloaded ChromeDriver
    chromedriver_path = download_chromedriver()
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    
    worst_product = None
    lowest_rating = float('inf')
    
    try:
        urls = [
            f"https://www.amazon.com/s?k={keyword}+1+star+reviews&rh=p_72%3A1248882011",
            f"https://www.amazon.com/s?k={keyword}&rh=p_72%3A1248882011%2Cp_72%3A1-2&s=review-rank",
            f"https://www.amazon.com/s?k={keyword}+worst+rated&rh=p_72%3A1248882011",
            f"https://www.amazon.com/s?k={keyword}+bad+reviews&rh=p_72%3A1248882011",
        ]
        
        for url in urls:
            print(f"\nTrying search method: {url.split('?k=')[1].split('&')[0]}")
            driver.get(url)
            
            # Add cookie to show all reviews
            driver.add_cookie({
                "name": "show-all-reviews",
                "value": "true"
            })
            
            driver.refresh()
            time.sleep(3)
            
            for page in range(1, max_pages + 1):
                print(f"\nScanning page {page}...")
                
                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-component-type='s-search-result']"))
                    )
                    
                    products = driver.find_elements(By.CSS_SELECTOR, "[data-component-type='s-search-result']")
                    
                    if not products:
                        print("No products found, trying next search method...")
                        break
                        
                    print(f"Found {len(products)} products")
                    
                    for product in products:
                        try:
                            review_count = product.find_elements(By.CSS_SELECTOR, "span.a-size-base.s-underline-text")
                            if not review_count:
                                continue
                                
                            title = product.find_element(By.CSS_SELECTOR, "h2").text.strip()
                            rating_element = product.find_elements(By.CSS_SELECTOR, "span.a-icon-alt")
                            
                            if rating_element:
                                rating_text = rating_element[0].get_attribute("innerHTML")
                                if "out of 5" in rating_text:
                                    rating = float(rating_text.split()[0])
                                    
                                    # Only process ratings with significant number of reviews
                                    review_text = review_count[0].text.replace(',', '')
                                    num_reviews = int(''.join(filter(str.isdigit, review_text)))
                                    
                                    if num_reviews >= 10:  # Minimum review threshold
                                        link = product.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")
                                        
                                        if rating < lowest_rating:
                                            lowest_rating = rating
                                            worst_product = {
                                                "title": title,
                                                "rating": rating,
                                                "reviews": num_reviews,
                                                "link": link
                                            }
                                            print(f"New worst rating found: {rating} stars ({num_reviews} reviews)")
                                            
                        except Exception as e:
                            continue
                    
                    try:
                        next_button = driver.find_element(By.CSS_SELECTOR, "a.s-pagination-next")
                        if "disabled" in next_button.get_attribute("class"):
                            break
                        next_button.click()
                        time.sleep(random.uniform(3, 5))
                    except:
                        break
                        
                except Exception as e:
                    print(f"Error on page: {str(e)}")
                    break
                    
    finally:
        driver.quit()
        if os.path.exists("chromedriver"):
            import shutil
            shutil.rmtree("chromedriver")
    
    return worst_product

if __name__ == "__main__":
    keyword = input("Enter a product keyword to search (e.g., headphones): ")
    print(f"\nSearching for the worst-rated {keyword}...")
    worst_product = scrape_amazon(keyword)
    
    if worst_product:
        print("\nWorst Rated Product Found:")
        print(f"Title: {worst_product['title']}")
        print(f"Rating: {worst_product['rating']} stars")
        print(f"Number of Reviews: {worst_product['reviews']}")
        print(f"Link: {worst_product['link']}")
    else:
        print("No products found.")
