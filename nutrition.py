import pandas as pd

# Read data from Excel file into a DataFrame
try:
    df = pd.read_excel("C:\\Users\\91986\\Documents\\indian food.xlsx")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()

# Convert column names to lowercase for case-insensitive matching
df.columns = df.columns.str.lower()

# Check if the correct column name exists in the DataFrame
if 'food item' not in df.columns:
    print("Error: 'Food Item' column not found in the Excel file.")
    exit()

# Convert DataFrame to dictionary for easy access
indian_food = df.set_index('food item').to_dict(orient='index')

def get_food_info(food_item):
    if food_item in indian_food:
        info = indian_food[food_item]
        print(f"Food Item: {food_item}")
        print(f"Ingredients: {info['ingredients']}")
        print(f"Calories: {info['calories']} kcal")
        print(f"Protein: {info['protein (g)']} g")
        print(f"Fat: {info['fat (g)']} g")
        print(f"Carbohydrates: {info['carbohydrates (g)']} g")
        print(f"Vitamins: {info['vitamins ']}")
        print(f"Minerals: {info['minerals ']}")
    else:
        print("Food item not found.")

# Example usage
food_item = input("Enter the food item: ")
get_food_info(food_item)