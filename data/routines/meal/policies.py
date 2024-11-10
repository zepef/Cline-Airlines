# Meal selection and modification policy
MEAL_POLICY = """
1. Verify the flight details for the meal request.
2. Check current meal selection status:
2a) If no meal is currently selected, proceed to step 3.
2b) If a meal is already selected, confirm if customer wants to change or remove it.
3. For new selection or changes:
3a) Present available meal options (Standard, Vegetarian, Vegan, Kosher, Halal).
3b) Call select_meal function with chosen option.
4. For removal:
4a) Call remove_meal function.
5. Confirm the changes with the customer.
6. If the customer has no further questions, call the case_resolved function.
"""
