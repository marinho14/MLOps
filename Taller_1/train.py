# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # 1. Dependencies import

import numpy as np
import joblib
import pandas as pd
from sklearn.metrics import f1_score, accuracy_score, precision_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# # 2. Parameters

TARGET = "specie"
COLUMNS_RENAME_DICT = {"Culmen Length (mm)": "culmenLen",
                       "Culmen Depth (mm)": "culmenDepth",
                       "Flipper Length (mm)": "flipperLen",
                       "Body Mass (g)": "bodyMass",
                       "Sex": "sex",
                       "Delta 15 N (o/oo)": "delta15N",
                       "Delta 13 C (o/oo)": "delta13C",
                       "Species": "specie"
}
FEATURES_DICT = {
    "culmenLen": ("float", [0.0075, 0.9975], "median"),
    "culmenDepth": ("float", [0.0075, 0.9975], "median"),
    "flipperLen": ("float", [0.0075, 0.9975], "median"),
    "bodyMass": ("float", [0.0075, 0.9975], "median"),
    "sex": ("category", "na", "mode"),
    "delta15N": ("float", [0.0075, 0.9975], "median"),
    "delta13C": ("float", [0.0075, 0.9975], "median")
}
FEATURES_CATEGORICAL = ["sex"]
FEATURES = list(FEATURES_DICT.keys())


# # 3. Helper Functions

def drop_outliers(data, features_dict):

    """
    Drop outliers from the given DataFrame based on specified quantile bounds for each feature.

    Parameters:
    - data (pd.DataFrame): The input DataFrame containing the data.
    - features_dict (dict): A dictionary where keys are feature names, and values are tuples.

    Returns:
    - pd.DataFrame: A new DataFrame with outliers removed based on the specified quantile bounds.

    """
    
    subset = data.copy()
    init_len = len(data)

    for feature in features_dict.keys():
        if features_dict[feature][0] == "float":
            lower_bound, upper_bound = features_dict[feature][1]
            subset = subset.loc[((subset[feature] > data[feature].quantile(lower_bound)) & (subset[feature] < data[feature].quantile(upper_bound)))].copy()
            dropped = len(subset) - init_len
            dropped_percent = 100 * dropped/init_len
            print(f"{feature} dropped rows: {dropped}, percent rows: {dropped_percent:.2f}%")
        elif features_dict[feature][0] == "category":
            pass
        else:
            pass
    return subset


def impute_values(data, features_dict):

    """
    Impute missing values in the DataFrame based on specified imputation methods.

    Parameters:
    - data (pd.DataFrame): The input DataFrame containing the data.
    - features_dict (dict): A dictionary where keys are feature names, and values are tuples
      representing the imputation method for each feature. Supported methods: 'median'.

    Returns:
    - pd.DataFrame: A new DataFrame with missing values imputed based on the specified methods.

    """

    subset = data.copy()

    for feature in features_dict.keys():
        if features_dict[feature][0] == "float":
            subset[feature].fillna(subset[feature].median(), inplace = True)
        elif features_dict[feature][0] == "category":
            subset[feature].fillna(subset[feature].mode().iloc[0], inplace = True)
        else:
            pass

    return subset


# # 4. Data Gathering & Processing 

df = pd.read_csv("data/penguins_lter.csv")
df.rename(columns=COLUMNS_RENAME_DICT, inplace=True)

# TODO: 1) Function to drop invalid values; 2) Function to cast every column according a dtype
df = df.loc[df["sex"].isin(["MALE","FEMALE"])].copy()
df["sex"] = df["sex"].astype("string")

df = df[FEATURES + [TARGET]].copy()

df.describe().T

100 * df.isna().sum()/len(df)

# Drop outliers
df = drop_outliers(df, FEATURES_DICT)

# Impute features
df = impute_values(df, FEATURES_DICT)


# Drop nan
df = df.dropna()

sex_label_encoder = LabelEncoder()
df["sex"] = sex_label_encoder.fit_transform(df["sex"])

target_encoder = LabelEncoder()
df[TARGET] = target_encoder.fit_transform(df[TARGET])

df.describe().T

df.head(10)

X = df[FEATURES]
y = df[TARGET]

# # 5. Constructing models

#Models
tree = DecisionTreeClassifier(random_state=0)
random_tree = RandomForestClassifier(random_state=0)

X

tree.fit(X, y)
random_tree.fit(X, y)

# # 6. Put model in prod

joblib.dump(tree, 'models/tree.pkl')
joblib.dump(random_tree, 'models/random_tree.pkl')

# # 7. Put label encoder for sex in prod
joblib.dump(sex_label_encoder, 'encoders/sex_label_encoder.pkl')
