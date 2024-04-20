def calculate_discount(prices, discount):
    """
    Calculate discounted prices based on the given discount.
    Args:
        prices (list): List of original prices.
        discount (float): Discount percentage.
    Returns:
        list: List of discounted prices.
    """
    result = []
    for price in prices:
        discounted_price = price * (1 - discount)  # Corrected the calculation of discounted price
        result.append(discounted_price)
    return result

prices = [100, 200, 300]
discount = 0.2  # Corrected variable name from discounts to discount
final_prices = calculate_discount(prices, discount)  # Corrected function call
print(final_prices)



- Variable Name Error: The variable discounts is used instead of discount when defining the discount percentage, which leads to incorrect variable references.
- Logical Error: In the calculate_discount function, the calculation of discounted prices is incorrect. The line result.append(price (price * discount)) incorrectly tries to apply the discount by multiplying the price by the discount squared, leading to incorrect results.
