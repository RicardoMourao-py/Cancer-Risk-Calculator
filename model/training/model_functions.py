import pandas as pd
import numpy as np

from sklearn.model_selection import StratifiedShuffleSplit, KFold, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import roc_auc_score

## Converte valores float para int variaveis categoricas
def convert_float_to_int(df, float_to_int_columns):
    nan_values = df[float_to_int_columns].where(df[float_to_int_columns].isna(), np.nan)
    df[float_to_int_columns] = df[float_to_int_columns].apply(pd.to_numeric, errors='coerce').astype('Int64')
    df[float_to_int_columns] = df[float_to_int_columns].mask(df[float_to_int_columns].isna(), nan_values)
    return df
## Pipeline de pre-processamento
def preprocess_data(numerical_features, categorical_features):
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(sparse_output=False, handle_unknown='ignore', drop='first'))
    ])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)
        ], remainder='drop')
    
    return preprocessor

## Avaliando modelos por Curva ROC
def evaluate_models_roc(X, y, models, preprocessor, n_splits=10, test_size=0.2, random_state=42):
    results = {}
    for name, model in models.items():
        pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', model),
        ])

        sss = StratifiedShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=random_state)

        model_results = []
        for train_index, test_index in sss.split(X, y):
            X_train = X.iloc[train_index]
            y_train = y.iloc[train_index]
            X_test = X.iloc[test_index]
            y_test = y.iloc[test_index]
            
            pipeline.fit(X_train, y_train)
            y_pred = pipeline.predict_proba(X_test)
            y_pred = y_pred[:, -1]
            
            auc = roc_auc_score(y_test, y_pred)
            model_results.append(auc)

        results[name] = model_results
    return results
## Avaliando modelos por acurácia
def evaluate_models_accuracy(X, y, models, preprocessor, n_splits=10, test_size=0.2, random_state=42):
    results = {}
    for name, model in models.items():
        pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', model),
        ])

        sss = StratifiedShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=random_state)

        model_results = []
        for train_index, test_index in sss.split(X, y):
            X_train = X.iloc[train_index]
            y_train = y.iloc[train_index]
            X_test = X.iloc[test_index]
            y_test = y.iloc[test_index]
            
            pipeline.fit(X_train, y_train)
            y_pred = pipeline.predict(X_test)
            
            accuracy = accuracy_score(y_test, y_pred)
            model_results.append(accuracy)

        results[name] = model_results
    return results
## Estimando melhores hiperparâmetros
def find_best_model_params(X_train, y_train,param_grid,model):
    kfold = KFold(n_splits=10)
    # Criando um objeto GridSearchCV
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=kfold, n_jobs=-1)
    grid_search.fit(X_train, y_train)
    return grid_search.best_params_
