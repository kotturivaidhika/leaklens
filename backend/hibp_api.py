import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def check_email(email):
    demo_mode = st.session_state.get("demo_mode", True)

    if demo_mode:
        return {
            "email": email,
            "mode": "DEMO — SYNTHETIC DATA",
            "breaches": [
                {
                    "name": "SampleForum",
                    "date": "2023-08-14",
                    "data_classes": [
                        "Email addresses",
                        "Passwords",
                        "Usernames"
                    ]
                },
                {
                    "name": "ExampleShop",
                    "date": "2024-02-03",
                    "data_classes": [
                        "Email addresses",
                        "Phone numbers"
                    ]
                }
            ]
        }

    api_key = os.getenv("HIBP_API_KEY", "").strip()

    if not api_key:
        raise RuntimeError(
            "HIBP API key missing. Add it to .env."
        )

    url = (
        "https://haveibeenpwned.com/api/v3/"
        "breachedaccount/"
        + requests.utils.quote(email, safe="")
    )

    headers = {
        "hibp-api-key": api_key,
        "user-agent": "LeakLens-Hackathon"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params={"truncateResponse": "false"},
            timeout=20
        )
    except requests.RequestException as e:
        raise RuntimeError(
            "Network error. Please try again."
        ) from e

    if response.status_code == 404:
        return {
            "email": email,
            "mode": "LIVE",
            "breaches": []
        }

    if response.status_code in (401, 403):
        raise RuntimeError(
            "API key invalid or access not permitted."
        )

    if response.status_code == 429:
        raise RuntimeError(
            "Rate limit reached. Try again later."
        )

    response.raise_for_status()

    breaches = []

    for item in response.json():
        breaches.append({
            "name": item.get("Name", "Unknown"),
            "date": item.get("BreachDate", "Unknown"),
            "data_classes": item.get(
                "DataClasses", []
            )
        })

    return {
        "email": email,
        "mode": "LIVE",
        "breaches": breaches
    }