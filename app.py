from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, MODEL_VERSION, model
from schema.prediction_response import PredictionResponse
import warnings
warnings.filterwarnings("ignore")

app = FastAPI()

@app.get("/")
def home():
    return {'message':'Vehicle Insurance prediction API'}

@app.get("/health")
def health_check():
    return {
        'status': 'OK',
        'version' : MODEL_VERSION,
        'model_loaded' : model is not None
    }
    

@app.post("/predict", response_model=PredictionResponse)
def predict(data: UserInput):
    input_df = {    
        'Gender' : data.gender,
        'Age' : data.age,
        'Driving_License': data.driving_license,
        'Region_Code' : data.region_code,
        'Previously_Insured':data.previously_insured,
        'Vehicle_Damage':data.vehicle_damage,
        'Annual_Premium':data.annual_premium,
        'Vehicle_Age_lt_1_year':data.Vehicle_Age_lt_1_Year,
        'Vehicle_Age_gt_1_year':data.Vehicle_Age_gt_1_Year,
    }
    
    try:
        prediction = predict_output(input_df)   
        return JSONResponse(status_code=200, content={"response":prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))