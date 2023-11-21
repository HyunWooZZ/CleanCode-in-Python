class PurchasesStats:
    """
    A class that calculates statistics for a list of purchases.
    """

    def __init__(self, purchases):
        """
        Initializes the PurchasesStats object.

        Args:
            purchases (list): A list of purchase values.
        """
        self.purchases = iter(purchases)
        self.min_price: float = None
        self.max_price: float = None
        self._total_purchases_price: float = 0.0
        self._total_purchases = 0
        self._initialize()

    def _initialize(self):
        """
        Initializes the minimum and maximum prices with the first value from the purchases list.
        Raises a ValueError if the purchases list is empty.
        """
        try:
            first_value = next(self.purchases)
        except StopIteration:
            raise ValueError("No more value in here")
        
        self.min_price = self.max_price = first_value
        self._update_avg(first_value)
        
    def process(self):
        """
        Processes the remaining purchases and updates the statistics.

        Returns:
            self: The updated PurchasesStats object.
        """
        for purchase_value in self.purchases:
            self._update_min(purchase_value)
            self._update_max(purchase_value)
            self._update_avg(purchase_value)
        return self
    
    def _update_min(self, new_value: float):
        """
        Updates the minimum price if the new value is smaller.

        Args:
            new_value (float): The new purchase value.
        """
        self.min_price = min(self.min_price, new_value)
    
    def _update_max(self, new_value: float):
        """
        Updates the maximum price if the new value is larger.

        Args:
            new_value (float): The new purchase value.
        """
        self.max_price = max(self.min_price, new_value)
    
    @property
    def avg_price(self):
        """
        Calculates and returns the average price of the purchases.

        Returns:
            float: The average price.
        """
        return self._total_purchases_price / self._total_purchases
    
    def _update_avg(self, new_value: float):
        """
        Updates the total purchases count and total purchases price.

        Args:
            new_value (float): The new purchase value.
        """
        self._total_purchases += 1
        self._total_purchases_price += new_value

    def __str__(self):
        """
        Returns a string representation of the PurchasesStats object.

        Returns:
            str: The string representation.
        """
        return (
            f"{self.__class__.__name__}({self.min_price}, {self.max_price}, {self.avg_price})"
        )

    
