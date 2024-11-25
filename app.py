from fastapi import FastAPI
from pydantic import BaseModel
from calc24 import Game24  # 导入 Game24 类

app = FastAPI()

class Numbers(BaseModel):
    nums: str  # 这是输入的字符串

@app.post("/calc24/", summary="Solve 24 points problem", description="Given 4 numbers, solve the 24 points game.")
def solve_24(nums: Numbers):
    game = Game24()
    solutions = game.Calc24([nums.nums])  # 使用字符串列表
    return {"solutions": solutions}

@app.get("/calc24/", summary="Solve 24 points problem with query", description="Given 4 numbers as a query string, solve the 24 points game.")
def solve_24_get(nums: str):
    game = Game24()
    solutions = game.Calc24([nums])  # 使用字符串列表
    return {"solutions": solutions}

