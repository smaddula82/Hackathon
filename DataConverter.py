import pandas as pd
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from HousePricePredict.AppConfig import AppConfig

init_object=AppConfig()
class Data_Converter:
    def __init__(self,listdata):
        self.listdata=listdata

    def convert_data(self):
        df = pd.DataFrame(self.listdata)
        df = df.T
        df.columns=['MSSubClass','MSZoning','LotFrontage','LotArea','Street','LotShape','LandContour','Utilities','LotConfig','LandSlope','Neighborhood','Condition1','Condition2','BldgType','HouseStyle','OverallQual','OverallCond','YearBuilt','YearRemodAdd','RoofStyle','RoofMatl','Exterior1st','Exterior2nd','MasVnrType','MasVnrArea','ExterQual','ExterCond','Foundation','BsmtQual','BsmtCond','BsmtExposure','BsmtFinType1','BsmtFinSF1','BsmtFinType2','BsmtFinSF2','BsmtUnfSF','TotalBsmtSF','Heating','HeatingQC','CentralAir','Electrical','1stFlrSF','2ndFlrSF','LowQualFinSF','GrLivArea','BsmtFullBath','BsmtHalfBath','FullBath','HalfBath','BedroomAbvGr','KitchenAbvGr','KitchenQual','TotRmsAbvGrd','Functional','Fireplaces','FireplaceQu','GarageType','GarageYrBlt','GarageFinish','GarageCars','GarageArea','GarageQual','GarageCond','PavedDrive','WoodDeckSF','OpenPorchSF','EnclosedPorch','3SsnPorch','ScreenPorch','PoolArea','MiscVal','MoSold','YrSold','SaleType','SaleCondition']
        numerical_features = ['MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond',
                              'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
                              'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
                              'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
                              'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces',
                              'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF',
                              'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
                              'MoSold', 'YrSold']
        categorical_features = ['MSZoning', 'Street', 'LotShape', 'LandContour', 'Utilities',
                                'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2',
                                'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st',
                                'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation',
                                'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
                                'Heating', 'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual',
                                'Functional', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual',
                                'GarageCond', 'PavedDrive', 'SaleType', 'SaleCondition']
        df[numerical_features]=df[numerical_features].astype('float64')
        print("printing dataframe: ",df)
        print("printing categorical: ",df[categorical_features])


        csv_file_name = init_object.data_path + init_object.test_file

        test = pd.read_csv(csv_file_name, encoding="UTF-8")

        test.drop(['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'Id'], axis=1, inplace=True)
        print("Shape of test before append: ",test.shape)
        print("Last row before append: ",test.tail(1))
        test=test.append(df,ignore_index=True)
        print("Shape of test after append: ", test.shape)
        print("Last row after append: ",test.tail(1))
        for c in categorical_features:
            lbl = LabelEncoder()
            lbl.fit(list(test[c].values))
            test[c] = lbl.transform(list(test[c].values))
        integer_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())])

        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent'))
        ])

        preprocessor = ColumnTransformer(
            transformers=[
                ('ints', integer_transformer, numerical_features),
                ('cat', categorical_transformer, categorical_features)])
        X = preprocessor.fit_transform(test)
        print("Shape of test after preprocessor: ", X.shape)
        print(" After preprocessor: ",X)
        print("Last row: ",X[-1,:])

        return X[-1,:]

