# import pandas as pd

# print(pd.__version__)
# print(pd.__name__)

# s1 = "Per"
# s2 = "fec"
# s3 = "fe"
# s4 = "ct"
# new_string = s1+s3+s4
# print(new_string)
# #Perfect


# products = {'Oranges (packaged)': 114.99, 'Candy (Rotfront)': 280.0, 'Boiled sausage': 199.99, 'Juice J7 (orange)': 119.99, 'Trout (Seven Seas)': 399.99}
# stocks = {'Boiled sausage': '33%', 'Juice J7 (orange)': '12%', 'Trout (Seven Seas)': '18%'}

# def apply_discounts(products, stocks):
#     result = {}
#     for product, price in products.items():
#         if product in stocks:
#             discount_str = stocks[product]
#             if discount_str.endswith('%'):
#                 discount = float(discount_str[:-1])
#                 discounted_price = round(price * (1 - discount / 100), 2)
#                 result[product] = discounted_price
#             else:
#                 result[product] = price
#         else:
#             result[product] = price
#     return result


# print(apply_discounts(products, stocks))




# {'Oranges (packaged)': 114.99, 'Candy (Rotfront)': 280.0, 'Boiled sausage': 133.99, 
# 'Juice J7 (orange)': 105.59, 'Trout (Seven Seas)': 327.99}
    

# import pandas as pd

 
# bronze_df = pd.read_csv('bronze_top.csv')
# silver_df = pd.read_csv('silver_top.csv')
# merged = pd.merge(bronze_df, silver_df, on='Country', suffixes=('_bronze', '_silver'))
# print(merged)



