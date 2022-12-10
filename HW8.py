import matplotlib.pyplot as plt
import os
import sqlite3
import unittest

def get_restaurant_data(db_filename):
    """
    This function accepts the file name of a database as a parameter and returns a list of
    dictionaries. The key:value pairs should be the name, category, building, and rating
    of each restaurant in the database.
    """
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_filename)
    cur = conn.cursor()
    cur.execute("SELECT restaurants.name, categories.category, buildings.building, restaurants.rating FROM restaurants JOIN categories, buildings ON restaurants.building_id = buildings.id AND restaurants.category_id = categories.id")
    count = cur.fetchall()
    conn.commit()

    list_of_restaurants = []
    for i in count:
        restaurant_info = {}
        restaurant_info["name"] = i[0]
        restaurant_info["category"] = i[1]
        restaurant_info["building"] = i[2]
        restaurant_info["rating"] = i[3]

        list_of_restaurants.append(restaurant_info)
    return list_of_restaurants


def barchart_restaurant_categories(db_filename):
    """
    This function accepts a file name of a database as a parameter and returns a dictionary. The keys should be the
    restaurant categories and the values should be the number of restaurants in each category. The function should
    also create a bar chart with restaurant categories and the counts of each category.
    """

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_filename)
    cur = conn.cursor()
    cur.execute("SELECT categories.category, COUNT(*) FROM restaurants JOIN categories ON restaurants.category_id = categories.id GROUP BY Category")
    count2 = cur.fetchall()
    conn.commit()
    

    restaurant_categories = {}
    for i in count2:
        restaurant_categories[i[0]] = i[1]
        
        x = list(restaurant_categories.keys())
        y = list(restaurant_categories.values())
    
    
    plt.barh(x,y)
    plt.xlabel("Number of Restaurants")
    plt.ylabel('Category of Restaurants')
    plt.title("Types of Restaurants on South University Ave")
    plt.show()
    return restaurant_categories


#EXTRA CREDIT
def highest_rated_category(db_filename):#Do this through DB as well
    """
    This function finds the average restaurant rating for each category and returns a tuple containing the
    category name of the highest rated restaurants and the average rating of the restaurants
    in that category. This function should also create a bar chart that displays the categories along the y-axis
    and their ratings along the x-axis in descending order (by rating).
    """
    pass

#Try calling your functions here
def main():
    get_restaurant_data("South_U_Restaurants.db")
    barchart_restaurant_categories("South_U_Restaurants.db")

class TestHW8(unittest.TestCase):
    def setUp(self):
        self.rest_dict = {
            'name': 'M-36 Coffee Roasters Cafe',
            'category': 'Cafe',
            'building': 1101,
            'rating': 3.8
        }
        self.cat_dict = {
            'Asian Cuisine ': 2,
            'Bar': 4,
            'Bubble Tea Shop': 2,
            'Cafe': 3,
            'Cookie Shop': 1,
            'Deli': 1,
            'Japanese Restaurant': 1,
            'Juice Shop': 1,
            'Korean Restaurant': 2,
            'Mediterranean Restaurant': 1,
            'Mexican Restaurant': 2,
            'Pizzeria': 2,
            'Sandwich Shop': 2,
            'Thai Restaurant': 1
        }
        self.best_category = ('Deli', 4.6)

    def test_get_restaurant_data(self):
        rest_data = get_restaurant_data('South_U_Restaurants.db')
        self.assertIsInstance(rest_data, list)
        self.assertEqual(rest_data[0], self.rest_dict)
        self.assertEqual(len(rest_data), 25)

    def test_barchart_restaurant_categories(self):
        cat_data = barchart_restaurant_categories('South_U_Restaurants.db')
        self.assertIsInstance(cat_data, dict)
        self.assertEqual(cat_data, self.cat_dict)
        self.assertEqual(len(cat_data), 14)

    # def test_highest_rated_category(self):
    #     best_category = highest_rated_category('South_U_Restaurants.db')
    #     self.assertIsInstance(best_category, tuple)
    #     self.assertEqual(best_category, self.best_category)

if __name__ == '__main__':
    main()
    unittest.main(verbosity=2)
