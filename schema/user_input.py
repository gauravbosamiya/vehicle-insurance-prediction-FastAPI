from pydantic import BaseModel, Field
from typing import Literal, Annotated

class UserInput(BaseModel):
    gender: Annotated[Literal["Male", "Female"], Field(..., description="Gender of the person")]
    age: Annotated[int, Field(..., gt=0, lt=100, description="Age of the person")]
    driving_license: Annotated[int, Field(..., description="Is person have a license or not ?")]
    region_code: Annotated[int, Field(..., description="Region code of the vehicle")]
    previously_insured: Annotated[int, Field(..., description="Is vehicle previously insured or not ?")]
    vehicle_damage: Annotated[Literal["Yes","No"], Field(..., description="Is vehicle damaged or not ?")]
    annual_premium: Annotated[float, Field(..., description="annual premium of the vehicle insurance")]
    Vehicle_Age_lt_1_Year:Annotated[Literal[0, 1], Field(..., description="is Vehicle_Age_lt_1_Year")]
    Vehicle_Age_gt_1_Year:Annotated[Literal[0,1], Field(..., description="is Vehicle_Age_gt_1_Year")]
    
    # @field_validator('gender')
    # @classmethod
    # def normalize_gender(cls, v: str) -> str:
    #     return v.strip().title()

    # @field_validator('vehicle_damage')
    # @classmethod
    # def normalize_vehicle_damage(cls, v:str) -> str:
    #     v = v.strip().title()
    #     return v  