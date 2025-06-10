# page perpage restaurants sort index, sortOrder
#
#
"""
restaurants = [
     #name, start, rank,  cuisine

    ["A", "1", "1", "Korean"],
    ["B", "2", "2", "American"],
    ["C", "3", "3", "Ramen"],
    ["D", "4", "4", "Korean"],
    ["E", "5", "5", "American"],
    ["F", "6", "5", "Latin American"],

]



1. Sort the restaurants based on rank 
2. paginate the restaurants based on perPage
3. return the restaurants of the given page


"""


from collections import defaultdict
def paginate_restaurant(restaurants, perPage):
    cuisineMap = defaultdict(set)
    res = []

    for restaurant in restaurants:
        n = len(cuisineMap)

        for i in range(n + 1):
            if i not in cuisineMap:
                cuisineMap[i].add(restaurant[3])

                if i not in res:
                    res.append([])

                res[i].append(restaurant[0])








restaurants = [
     #name, start, rank,  cuisine

    ["A", "1", "1", "Korean"],
    ["B", "2", "2", "American"],

    ["C", "3", "3", "Korean"],
    ["D", "4", "4", "Ramen"],
    ["E", "5", "5", "American"],

    ["F", "6", "6", "Ramen"],

]

print("res:", paginate_restaurant(restaurants, 3))

# if the restaurant cuisine same move to the next page
