import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_next_day():

    df = pd.read_csv("data/icu_history.csv")

    X = df[["Day"]]
    y = df["OccupiedBeds"]

    model = LinearRegression()
    model.fit(X, y)

    next_day = [[16]]

    prediction = model.predict(next_day)

    return round(prediction[0])
