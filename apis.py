from HousePricePredict import *
from flask import jsonify, Response, session
import uuid
import datetime
from marshmallow import Schema, fields
from flask_restful import Resource, Api
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
import json
import enum



class HouseDataRequest(Schema):
    MSSubClass = fields.Int(default="60")
    MSZoning = fields.Str(default="RL")
    LotFrontage = fields.Int(default="85")
    LotArea = fields.Int(default="10000")
    Street = fields.Str(default="Pave")
    LotShape = fields.Str(default="IR1")
    LandContour = fields.Str(default="Lvl")
    Utilities = fields.Str(default="AllPub")
    LotConfig = fields.Str(default="Corner")
    LandSlope = fields.Str(default="Gtl")
    Neighborhood = fields.Str(default="Somerst")
    Condition1 = fields.Str(default="Norm")
    Condition2 = fields.Str(default="Artery")
    BldgType = fields.Str(default="1Fam")
    HouseStyle = fields.Str(default="2Story")
    OverallQual = fields.Int(default="7")
    OverallCond = fields.Int(default="7")
    YearBuilt = fields.Int(default="2004")
    YearRemodAdd = fields.Int(default="2007")
    RoofStyle = fields.Str(default="Gable")
    RoofMatl = fields.Str(default="CompShg")
    Exterior1st = fields.Str(default="VinylSd")
    Exterior2nd = fields.Str(default="Wd Shng")
    MasVnrType = fields.Str(default="None")
    MasVnrArea = fields.Int(default="200")
    ExterQual = fields.Str(default="TA")
    ExterCond = fields.Str(default="TA")
    Foundation = fields.Str(default="BrkTil")
    BsmtQual = fields.Str(default="TA")
    BsmtCond = fields.Str(default="Gd")
    BsmtExposure = fields.Str(default="No")
    BsmtFinType1 = fields.Str(default="GLQ")
    BsmtFinSF1 = fields.Int(default="1000")
    BsmtFinType2 = fields.Str(default="Unf")
    BsmtFinSF2 = fields.Int(default="40")
    BsmtUnfSF = fields.Int(default="300")
    TotalBsmtSF = fields.Int(default="1000")
    Heating = fields.Str(default="GasA")
    HeatingQC = fields.Str(default="Ex")
    CentralAir = fields.Str(default="Y")
    Electrical = fields.Str(default="SBrkr")
    FstFlrSF = fields.Int(default="1200")
    SndFlrSF = fields.Int(default="0")
    LowQualFinSF = fields.Int(default="50")
    GrLivArea = fields.Int(default="1500")
    BsmtFullBath = fields.Int(default="2")
    BsmtHalfBath = fields.Int(default="0")
    FullBath = fields.Int(default="1")
    HalfBath = fields.Int(default="0")
    BedroomAbvGr = fields.Int(default="4")
    KitchenAbvGr = fields.Int(default="2")
    KitchenQual = fields.Str(default="TA")
    TotRmsAbvGrd = fields.Int(default="8")
    Functional = fields.Str(default="Typ")
    Fireplaces = fields.Int(default="2")
    FireplaceQu = fields.Str(default="Gd")
    GarageType = fields.Str(default="Attchd")
    GarageYrBlt = fields.Int(default="2004")
    GarageFinish = fields.Str(default="RFn")
    GarageCars = fields.Int(default="3")
    GarageArea = fields.Int(default="600")
    GarageQual = fields.Str(default="Gd")
    GarageCond = fields.Str(default="Gd")
    PavedDrive = fields.Str(default="Y")
    WoodDeckSF = fields.Int(default="200")
    OpenPorchSF = fields.Int(default="100")
    EnclosedPorch = fields.Int(default="120")
    TSsnPorch = fields.Int(default="0")
    ScreenPorch = fields.Int(default="100")
    PoolArea = fields.Int(default="500")
    MiscVal = fields.Int(default="500")
    MoSold = fields.Int(default="5")
    YrSold = fields.Int(default="2010")
    SaleType = fields.Str(default="WD")
    SaleCondition = fields.Str(default="Normal")

class APIResponse(Schema):
    message = fields.Str(default="success")

class HouseDataAPI(MethodResource, Resource):
    @doc(description='HouseData API', tags=['HouseData API'])
    @use_kwargs(HouseDataRequest, location=('json'))
    @marshal_with(APIResponse)
    def post(self, **kwargs):
        try:
            print(kwargs)
            return APIResponse().dump(dict(message='Successfully Received House Data')), 200
        except Exception as e:
            return APIResponse().dump(dict(message=f'Not able to receive House Data:{str(e)}')), 400


api.add_resource(HouseDataAPI, '/HouseData')
docs.register(HouseDataAPI)

