from pydantic import BaseModel

class SwapCreate(BaseModel):
    shift_id: int

class SwapApprove(BaseModel):
    match_id: int

