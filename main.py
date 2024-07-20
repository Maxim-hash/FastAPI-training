from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI
import json
import sqlalchemy
import alembic
from pydantic import BaseModel, Field

per_page = 20

app = FastAPI(
    title="Training FastAPI"
)

class Vacancy(BaseModel):
    id: str
    requirement: str
    responsobility: Optional[str]
    prof_roles: str
    empoyment: str
    publishied_at: datetime
    name: str
    area_id: int = Field(ge=1)
    schedule: str
    exp: str
    employers_name: str
    salary: Optional[int]
    key_skills: Optional[List[str]] = []

with open ("fastAPI.json", "r", encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        jsonify_data = [{**{"id": key}, **json_data[key]} for key in json_data]

@app.get("/")
def show_stats():
    return {
        "pages" : len(jsonify_data) // per_page,
        "per_page" : per_page,
        "amount_vacancsies" : len(jsonify_data)
    }

@app.get("/vacancies", response_model=List[Vacancy])
def get_vacansies(limit: int = per_page, page: int = 0):
    return jsonify_data[page*limit:][:limit]

@app.get("/vacancies/{vacancy_id}", response_model=List[Vacancy])
def get_vacancy(vacancy_id: str):
    return [vacancy for vacancy in jsonify_data if vacancy.get("id") == vacancy_id]

@app.post("/vacancies/{vacancy_id}")
def change_vacancy_name(vacancy_id : str, new_vacancy_name : str):
    current_vacancy = list(filter(lambda vacancy: vacancy.get("id") == vacancy_id, jsonify_data))[0]
    current_vacancy["name"] = new_vacancy_name
    return {"status" : 200, "data" : current_vacancy}



@app.post("/vacancies")
def add_vacancies(vacancies: List[Vacancy]):
    jsonify_data.extend(vacancies)
    return {"status" : 200, "data" : jsonify_data}