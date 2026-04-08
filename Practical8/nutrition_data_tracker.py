#Create a new Python class named "food_item"
class food_item(object):
    """
    Class to represent a food item and its nutritional information
    Attributes:
    name (str): The name of the food item
    calories (float): The number of calories in the food item
    protein (float): The amount of protein in the food item
    carbohydrates (float): The amount of carbohydrates in the food item
    fat (float): The amount of fat in the food item
    """

    #Define the __init__ method to initialize the attributes of the class
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat

#Define a function to calculate the total nutritional information for a list of food items
def nutrition_summary(food_list):
    """
    Calculate the total nutritional information for a list of food items
    Print the total nutritional information and report any warnings if the total exceeds recommended daily limits
    Input: A list of food_item objects
    Return: A dictionary containing the total calories, protein, carbohydrates, and fat for the list of food items
    """
    #Initialize variables to store the total nutritional information
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0

    #Iterate through the list of food items and add their nutritional information to the total
    for food_item in food_list:
        total_calories += food_item.calories
        total_protein += food_item.protein
        total_carbohydrates += food_item.carbohydrates
        total_fat += food_item.fat

    #Report the total nutritional information
    print("24h Nutritional Information:")
    print(f"Total Calories: {total_calories}")
    print(f"Total Protein: {total_protein} g")
    print(f"Total Carbohydrates: {total_carbohydrates} g")
    print(f"Total Fat: {total_fat} g")

    #Report warnings if the total nutritional information exceeds recommended daily limits
    if total_calories > 2500:
        print("Warning: Total calories exceed the recommended daily limit of 2500 calories!")
    if total_fat > 90:
        print("Warning: Total fat exceeds the recommended daily limit of 90 grams!")

    #Output the total nutritional information as a dictionary
    return {
        "total_calories": total_calories,
        "total_protein": total_protein,
        "total_carbohydrates": total_carbohydrates,
        "total_fat": total_fat
    }


#The main function to test the food_item class and nutrition_summary function
if __name__ == "__main__":
    #Create some sample food items
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    rice = food_item("Rice", 130, 2.7, 28, 0.2)
    beef = food_item("Beef", 250, 26, 0, 15)
    coke = food_item("Coke", 210, 0, 52, 0)

    #Put the food items in a list
    food_list = [apple, rice, beef, coke]

    #Calculate the total nutritional information for the list of food items (using the nutrition_summary function)
    #Report the outcomes and warnings
    nutrition_summary(food_list)
