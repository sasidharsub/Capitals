def capitalcities(user_input):   
    import pandas as pd
    caps = pd.read_html('https://en.wikipedia.org/wiki/List_of_national_capitals')
    capital = caps[1]
    capital.drop('Notes', axis = 1, inplace = True)
    capital.columns = ['Capital', 'Country']
    capital[capital['Country'] == 'Sri Lanka']
    capital.drop([0,62], inplace=True)
    def remove_extra(x):
        for i in capital.Country:
            if x in i:
                capital.Country.replace({ i : x}, inplace = True)
    remove_extra('Israel')
    remove_extra('Palestine')
    remove_extra('Western Sahara')
    remove_extra('Kosovo')
    capital.Country.replace({ 'Cocos (Keeling) Islands' : 'Cocos Islands', 'Guinea-Bissau':'Guinea Bissau'}, inplace = True)
    for i in capital.Country:
        capital.Country.replace({i : i.lower()}, inplace = True)
    Country = capital.Country.tolist()
    Capital = capital.Capital.tolist()
    while True:
        user_input = user_input.lower()
        if user_input in Country:
            index = Country.index(user_input)
            return f'{Capital[index]}'
            break
        else:
            return 'Call the function with the country name to get the capital'
