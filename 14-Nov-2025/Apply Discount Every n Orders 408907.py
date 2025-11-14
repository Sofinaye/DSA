# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.customer_count = 0
        
        self.price_map = {}
        for i in range(len(products)):
            self.price_map[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        
        subtotal = 0
        for i in range(len(product)):
            product_id = product[i]
            product_amount = amount[i]
            subtotal += product_amount * self.price_map[product_id]
        
        if self.customer_count % self.n == 0:
            return subtotal * (100 - self.discount) / 100
        else:
            return subtotal


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)