import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical

iris_df = pd.read_excel(r'/Users/praneethkumarpalepu/Documents/machine_learning/night_warrior/iris.xlsx')

y = iris_df['Flower_Class']
x = iris_df.drop(['Flower_Class'], axis=1).to_numpy()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0)
encoder = LabelEncoder()

y_train = encoder.fit_transform(y_train)
y_test = encoder.transform(y_test)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print(y_train)



