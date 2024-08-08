# feature_selection.py

from sklearn.feature_selection import SelectKBest, f_classif

#Select k number of features
def select_features(X, y, k=10):
    selector = SelectKBest(f_classif, k=k)
    return selector.fit_transform(X, y), selector
