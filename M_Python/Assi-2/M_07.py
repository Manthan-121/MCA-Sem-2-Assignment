states_and_capitals = {
    "Gujarat": "Gandhinagar",
    "Andhra Pradesh": "Hyderabad",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "West Bengal": "Kolkata"
}


while True:
    state = input("Enter the name of a state (type 'exit' to quit): ").strip()

    if state.lower() == 'exit':
        print("Exiting the program.")
        break

    # Check if the entered state exists in the dictionary
    if state in states_and_capitals:
        capital = input(f"What is the capital of {state}? ").strip()

        # Compare the entered capital with the correct capital from the dictionary
        if capital == states_and_capitals[state]:
            print("Correct!")
        else:
            print(f"Sorry, the correct capital of {state} is {states_and_capitals[state]}.")
    else:
        print("State not found in the dictionary. Please try again.")
