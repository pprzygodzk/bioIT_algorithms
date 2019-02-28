import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

dt = pd.read_csv("titanic.csv") # czytanie z pliku csv

dt["Sex_cleaned"] = np.where(dt["Sex"] == 'male', 0, 1)
dt.loc[dt["Embarked"] == 'S', "Embarked_cleaned"] = 0
dt.loc[dt["Embarked"] == 'C', "Embarked_cleaned"] = 1
dt.loc[dt["Embarked"] == 'Q', "Embarked_cleaned"] = 2
dt = dt.drop(dt.columns[[4, 11]], axis = 1)

correct_dt = dt[["Survived",
                 "Pclass",
                 "Name",
                 "Age",
                 "SibSp",
                 "Parch", 
                 "Fare",
                 "Sex_cleaned",
                 "Embarked_cleaned"]].dropna(axis = 0, how = 'any')

survivors = correct_dt.loc[correct_dt["Survived"] == 1]
dead = correct_dt.loc[correct_dt["Survived"] == 0]

pl.figure(figsize = (8, 8))
pl.hist(correct_dt["Age"], color = 'b', label = "wszyscy")
pl.hist([survivors["Age"], dead["Age"]], rwidth = 0.75, color = ['g', 'r'], label = ["przeżyli", "nie żyją"])
# alpha = 0.75 (ustawia przezroczystosc na 75%)
pl.xlabel("WIEK")
pl.ylabel("LICZBA OSÓB")
pl.legend()

pl.figure(figsize = (8, 8))
pl.hist(correct_dt["Fare"], color = 'k', label = "wszyscy")
pl.hist([survivors["Fare"], dead["Fare"]], rwidth = 0.75, color = ['r', 'm'], label = ["przeżyli", "nie żyją"])
pl.xlabel("CENA BILETU")
pl.ylabel("LICZBA OSÓB")
pl.legend()
pl.show()
