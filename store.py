from abc import ABC, abstractmethod
from typing import Any

from abc import ABC, abstractmethod

class BaseStore(ABC):
    """
    Abstract base class for a store.

    Attributes:
        base_url (str): The base URL of the store's website.

    Methods:
        __init__(): Initializes the BaseStore object.
        scrape_product(product_url): Scrapes the product details from the given URL.
        check_for_sale(product_url): Checks if the product is on sale at the given URL.
    """

    @abstractmethod
    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def scrape_product(self, product_url):
        """
        Scrapes the product details from the given URL. Needs to be overriden since 
        the implementation will be different for each site.

        Args:
            product_url (str): The URL of the product page.

        Returns:
            None. Inserts the products directly into the database instead of returning them.
        """
        pass

    @abstractmethod
    def update_information(self, product_url):
        """
        Checks if the product is on sale at the given URL.

        Args:
            product_url (str): The URL of the product page.

        Returns:
            bool: True if the product is on sale, False otherwise.
        """
        pass
