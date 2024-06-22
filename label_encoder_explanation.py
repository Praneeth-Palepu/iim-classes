import pandas as pd
from sklearn.preprocessing import LabelEncoder

tr_cities = pd.DataFrame(['Bangalore', 'Bhopal', 'Chennai', 'Ahmedabad', 'Hyderabad', 'Pune', 'Mumbai', 'Delhi'], columns=['Cities'])
te_cities = pd.DataFrame(['Bhopal', 'Delhi', 'Hyderabad'], columns=['cities'])
print(tr_cities, "\n")
print(te_cities)

encoder = LabelEncoder()
tr_cities_encoded = encoder.fit_transform([tr_cities])

tr_cities['encoded_city_values'] = tr_cities_encoded

print(tr_cities)

te_cities_encoded = encoder.transform(te_cities)
print(te_cities_encoded)