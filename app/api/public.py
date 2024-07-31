from typing import Optional

import openai
from fastapi import APIRouter, HTTPException

from app.config import OPENAI_MODEL

public_router = APIRouter()


@public_router.get("/today-news")
def get_today_news():
    try:
        prompt = ""
        # openai request
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL, messages=[{"role": "user", "content": prompt}]
        )
        # openai response
        answer = response.choices[0].message["content"].strip()
        return {"today-news": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@public_router.get("/news-keywords")
def get_news_keywords(keywords: Optional[str]):
    try:
        # openai request
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL, messages=[{"role": "user", "content": keywords}]
        )
        # openai response
        answer = response.choices[0].message["content"].strip()
        return {"resurt": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@public_router.get("/news-title")
def get_news_title(title: Optional[str]):
    try:
        # openai request
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL, messages=[{"role": "user", "content": title}]
        )
        # openai response
        answer = response.choices[0].message["content"].strip()
        return {"resurt": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
