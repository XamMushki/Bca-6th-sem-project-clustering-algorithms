import random
import csv


def saveToCsv(name, list_of_lists):
    with open(name, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(list_of_lists)
        print('Saved')


def generateDataset(n=10, filename='test.csv'):
    product_name_list = []
    product_price_list = []
    customer_rating_list = []
    for i in range(n):
        name = 'Product ' + str(i)
        product_name_list.append(name)
        price = random.randint(100, 50000)
        product_price_list.append(price)
        rating = random.randint(1, 10)
        customer_rating_list.append(rating)

    lol_product_ratings = [['ProductID', 'Product Name', 'Product Price', 'Customer Rating']]

    for i in range(n):
        l = [i + 1, product_name_list[i], product_price_list[i], customer_rating_list[i]]
        lol_product_ratings.append(l)

    saveToCsv(filename, lol_product_ratings)


# Method call final
generateDataset(200, 'product_ratings.csv')
