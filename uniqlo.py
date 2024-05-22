from store import BaseStore 
from overrides import overrides
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import sqlite3


class Uniqlo(BaseStore):
    """
    A class representing the Uniqlo store.

    Attributes:
        base_url (str): The base URL of the Uniqlo website.

    Methods:
        scrape_product(product_url): Scrapes the product details from the given product URL and stores them in the database.
        check_for_sale(product_url): Checks if the product is on sale by visiting the product URL.
    """
    def __init__(self):
        super().__init__(base_url="https://www.uniqlo.com")
    
    @overrides
    def scrape_product(self, product_url):
        """
        Scrapes the product details from the given product URL and stores them in the database.

        Args:
            product_url (str): The URL of the product page.

        Returns:
            None
        """
        driver = webdriver.Chrome()
        driver.get(product_url)

        #get the product name
        product_name = driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/section/div[2]/div[2]/div[1]/div/ul/li[1]/h1').text
        #get the product price
        product_price = driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/section/div[2]/div[2]/div[4]/div[2]/div[1]/div/div/p').text
        #close open resources 
        product_image = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/section/div[2]/div[1]/div[1]/div/div/div[1]/div[1]/div/div[1]/img').get_attribute('src')
        #grab product availability
        product_availability = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/section/div[2]/div[2]/div[5]/div[1]/p').text
        #product sale
        product_sale = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/section/div[2]/div[2]/ul/li/p').text

        #check to see if the product is on sale 

        #close open resources
        driver.implicitly_wait(2)
        driver.quit()

        #open database connection

        try:
            conn = sqlite3.connect('project_db.db')
            c = conn.cursor()
            
            query = 'INSERT INTO products (name, price, store, image, URL, availability, sale) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            c.execute(query, product_name, product_price, "Uniqlo", product_image, product_url, product_availability, product_sale)
        except sqlite3.Error as e:
            return str(e)

        c.close()
        conn.close()
    
    @overrides
    def update_information(self, product_url):
        """
        Checks if the product is on sale by visiting the product URL.

        Args:
            product_url (str): The URL of the product page.

        Returns:
            None
        """

        driver = webdriver.Chrome()
        driver.get(product_url)

        #get the product details
        product_price = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/section/div[2]/div[2]/div[4]/div[2]/div[1]/div/div/p').text
        product_availability = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/section/div[2]/div[2]/div[5]/div[1]/p').text

        try:
            if not (driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/section/div[2]/div[2]/ul/li/p') == None):
                sale = True
        except NoSuchElementException:
                sale = False

        driver.implicitly_wait(2)
        driver.quit()
        driver.close()

        #open database connection
        conn = sqlite3.connect('project_db.db')
        c = conn.cursor()

        c.execute('UPDATE products SET price = %s, availability = %s, sale = %s WHERE URL = %s', product_price, product_availability, sale, product_url)

if __name__ == "__main__":
    uniqlo = Uniqlo()
    uniqlo.scrape_product("https://www.uniqlo.com/us/en/products/E467145-000/00?colorDisplayCode=67&sizeDisplayCode=003")