import pandas as pd

def capitalcities(user_input):   
    # Read the table from the Wikipedia page
    caps = pd.read_html('https://en.wikipedia.org/wiki/List_of_national_capitals')
    capital = caps[1]
    
    # Drop the 'Notes' column and unnecessary rows
    capital = capital.drop(columns=['Notes']). drop([0, 62])
    
    # Rename the columns for better readability
    capital.columns = ['Capital', 'Country']
    
    # Function to replace country names
    def replace_country_names(old_name, new_name):
        capital['Country'] = capital['Country'].str.replace(old_name, new_name)
    
    # Replace specific country names
    replacements = {
        'Israel': 'Israel',
        'Palestine': 'Palestine',
        'Western Sahara': 'Western Sahara',
        'Kosovo': 'Kosovo',
        'Cocos (Keeling) Islands': 'Cocos Islands',
        'Guinea-Bissau': 'Guinea Bissau'
    }
    
    for old_name, new_name in replacements.items():
        replace_country_names(old_name, new_name)
    
    # Convert country names to lowercase
    capital['Country'] = capital['Country'].str.lower()
    
    # Create lists of countries and their capitals
    countries = capital['Country'].tolist()
    capitals = capital['Capital'].tolist()
    
    # Convert user input to lowercase
    user_input = user_input.lower()
    
    # Find and return the capital city if the country is in the list
    if user_input in countries:
        index = countries.index(user_input)
        return capitals[index]
    else:
        return 'Call the function with the country name to get the capital'
