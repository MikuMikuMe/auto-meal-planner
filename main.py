Creating an auto-meal-planner in Python involves various components, including user input processing, generating meal plans based on dietary preferences and budgets, and managing a shopping list. Below is a basic implementation of the auto-meal-planner with key features, comments, and error handling.

```python
import random

class MealPlanner:
    def __init__(self, dietary_preferences, budget):
        self.dietary_preferences = dietary_preferences  # List of user dietary preferences
        self.budget = budget  # User budget for meals
        self.meal_database = self.load_meal_database()  # Placeholder for meal database
    
    def load_meal_database(self):
        # Placeholder meal database that should be replaced by a comprehensive list or API call
        meal_database = [
            {'name': 'Grilled Chicken Salad', 'diet': 'protein', 'cost': 10},
            {'name': 'Vegan Buddha Bowl', 'diet': 'vegan', 'cost': 8},
            {'name': 'Pasta Primavera', 'diet': 'vegetarian', 'cost': 7},
            {'name': 'Beef Stir Fry', 'diet': 'protein', 'cost': 12},
            {'name': 'Quinoa Salad', 'diet': 'vegan', 'cost': 9},
            {'name': 'Tuna Sandwich', 'diet': 'protein', 'cost': 6},
        ]
        return meal_database

    def generate_meal_plan(self):
        # Generate a weekly meal plan with the input dietary preferences and within the budget
        try:
            meal_plan = []
            remaining_budget = self.budget
            for day in range(7):  # Generate meals for 7 days
                potential_meals = [meal for meal in self.meal_database 
                                   if meal['diet'] in self.dietary_preferences 
                                   and meal['cost'] <= remaining_budget]
                if not potential_meals:
                    raise ValueError("Budget too low or dietary preference too restrictive. Could not find suitable meals.")
                
                chosen_meal = random.choice(potential_meals)
                meal_plan.append(chosen_meal)
                remaining_budget -= chosen_meal['cost']
            return meal_plan
        except Exception as e:
            print(f"Error generating meal plan: {e}")
            return None
    
    def generate_shopping_list(self, meal_plan):
        try:
            if meal_plan is None:
                raise ValueError("Invalid meal plan, cannot generate shopping list.")
            
            ingredients_needed = {
                'Grilled Chicken Salad': ['chicken', 'lettuce', 'tomatoes', 'olive oil'],
                'Vegan Buddha Bowl': ['quinoa', 'chickpeas', 'broccoli'],
                'Pasta Primavera': ['pasta', 'bell peppers', 'zucchini', 'olive oil'],
                'Beef Stir Fry': ['beef', 'soy sauce', 'broccoli', 'bell peppers'],
                'Quinoa Salad': ['quinoa', 'cucumber', 'tomatoes', 'mint'],
                'Tuna Sandwich': ['tuna', 'bread', 'mayonnaise', 'lettuce']
            }
            
            shopping_list = []
            for meal in meal_plan:
                shopping_list.extend(ingredients_needed.get(meal['name'], []))
            # Remove duplicates
            shopping_list = list(set(shopping_list))
            return shopping_list
        except Exception as e:
            print(f"Error generating shopping list: {e}")
            return None

def main():
    try:
        dietary_preferences = input("Enter your dietary preferences separated by commas (e.g., vegan, protein): ").split(',')
        dietary_preferences = [preference.strip().lower() for preference in dietary_preferences]  # Convert inputs to lowercase and remove whitespace
        budget = float(input("Enter your weekly meal budget: "))
        
        planner = MealPlanner(dietary_preferences, budget)
        meal_plan = planner.generate_meal_plan()
        
        if meal_plan is not None:
            print("\nGenerated Meal Plan:")
            for day, meal in enumerate(meal_plan):
                print(f"Day {day + 1}: {meal['name']} - Cost: ${meal['cost']}")
                
            shopping_list = planner.generate_shopping_list(meal_plan)
            if shopping_list is not None:
                print("\nShopping List:")
                for item in shopping_list:
                    print(item)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Explanation:
- **MealPlanner Class:** Handles the creation of meal plans and shopping lists based on user preferences and budget.
- **Error Handling:** Includes try-except blocks for handling potential errors, such as invalid user inputs and issues when no suitable meals are found.
- **Input Processing:** Allows users to input dietary preferences and budget.
- **Random Meal Selection:** Randomly selects meals that conform to dietary preferences and budget constraints.
- **Shopping List Generation:** Aggregates required ingredients for the selected meal plan, removing duplicates.

### Note:
This is a simplified example and real-world applications might involve more complex requirements such as a larger meal database, nutritional information handling, user authentication, data persistence, and integration with external APIs.