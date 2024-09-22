from flask import Flask, request

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.feature_selection import RFECV, SequentialFeatureSelector, SelectFromModel
from sklearn.inspection import permutation_importance
from sklearn.metrics import classification_report
#from sklearn.model_selection import train_test_split, StratifiedKFold
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.svm import SVC
import json

#import analysis.methods.personas_validation_methods as pvm


app = Flask(__name__)

stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


@app.get("/store")
def get_stores():
    # Sample data
    data = {'values': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
    df = pd.DataFrame(data)

    # Calculate the moving average with a window size of 3
    df['average'] = df['values'].mean()
    return {"stores": stores, "panda": df['average'].tolist()}

@app.get("/pca")
def get_pca():
    # Sample data
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    weights = np.array([1, 2, 1, 1])  # Weights for each sample

    transformed, pca_model = weighted_pca(data, weights)

    # Prepare results for JSON output
    results = {
        "transformed_data": transformed.tolist(),
        "explained_variance_ratio": pca_model.explained_variance_ratio_.tolist()
    }

    # Convert to JSON
    json_output = json.dumps(results, indent=4)

    return json_output, 200


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404


import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def weighted_pca(X, weights, n_components=2):
    # Normalize weights
    weights = weights / np.sum(weights)

    # Center the data
    X_centered = X - np.average(X, axis=0, weights=weights)

    # Compute the covariance matrix, weighted
    cov_matrix = np.cov(X_centered, rowvar=False, aweights=weights)

    # Perform PCA on the weighted covariance matrix
    pca = PCA(n_components=n_components)
    pca.fit(cov_matrix)

    # Transform the data
    transformed_data = pca.transform(X_centered)

    return transformed_data, pca




