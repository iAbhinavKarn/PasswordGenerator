import random

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class GeneratePasswordInput(BaseModel):
    site: str
    username: str
    email: str
    maxLength: int


class PasswordOutput(object):
    username: str
    site: str
    password: str


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z']

upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
             'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
             'Z']

symbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
          '*', '(', ')', '<']


@app.get("/")
def root():
    return {"Its live"}


@app.post("/generateNewPassword")
def say_hello(userInput: GeneratePasswordInput):
    combineList = numbers + upperCase + lowerCase + symbol
    password = random.choice(numbers) + random.choice(lowerCase) + random.choice(upperCase) + random.choice(symbol)
    for i in range(userInput.maxLength - 4):
        password = password + random.choice(combineList)
    response = PasswordOutput()
    response.password = password
    response.username = userInput.username
    response.site = userInput.site
    return response
