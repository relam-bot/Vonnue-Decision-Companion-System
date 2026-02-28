import json
from google import genai

API_KEY = "AIzaSyDnWLtSKIl4xSXvRwXy2RGFpUfIJT6e-j0"

client = genai.Client(api_key=API_KEY)


def normalize_output(data):

    # -------------------------
    # If Gemini returns list instead of dict
    # -------------------------
    if isinstance(data, list) and len(data) > 0:
        data = data[0]

    if not isinstance(data, dict):
        return {}

    # -------------------------
    # Convert soil_ph to float
    # -------------------------
    if "soil_ph" in data:
        try:
            data["soil_ph"] = float(data["soil_ph"])
        except:
            del data["soil_ph"]

    # -------------------------
    # Fix shade_percent
    # -------------------------
    if "shade_percent" in data:
        value = data["shade_percent"]
        if isinstance(value, str):
            value = value.replace("%", "")
            if value.isdigit():
                data["shade_percent"] = int(value)

    # -------------------------
    # Normalize leaf symptom
    # -------------------------
    if "leaf_symptom" in data:
        symptom = data["leaf_symptom"].lower()
        if "yellow" in symptom:
            data["leaf_symptom"] = "yellow"
        elif "purple" in symptom:
            data["leaf_symptom"] = "purple"
        elif "brown" in symptom:
            data["leaf_symptom"] = "brown edges"

    # -------------------------
    # Fix monsoon mapping
    # -------------------------
    if data.get("season") == "monsoon":
        data["rainfall_level"] = "high"
        data["climate_humidity"] = "high"

    # -------------------------
    # Ensure module exists
    # -------------------------
    if "module" not in data:
        if "num_plants" in data:
            data["module"] = "irrigation"
        elif "soil_ph" in data or "nitrogen_level" in data:
            data["module"] = "fertilizer"
        elif "pest_query" in data:
            data["module"] = "pesticide"
        elif "shade_percent" in data:
            data["module"] = "shade"
        elif "rainfall_level" in data and "disease_pressure" in data:
            data["module"] = "variety"

    return data


def extract_intent_and_entities(user_input: str):

    prompt = f"""
Return only valid JSON object.
Do not explain.
Do not return list.
Extract agricultural decision fields from:

\"\"\"{user_input}\"\"\"

Possible fields:
module
num_plants
water_availability
budget
rainfall_level
soil_drainage
terrain
climate_temperature
growth_stage
labour_availability
water_source
climate_humidity
soil_ph
nitrogen_level
phosphorus_level
potassium_level
organic_matter
leaf_symptom
pest_query
season
disease_pressure
shade_percent
altitude
market_priority
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "temperature": 0
            }
        )

        raw_data = json.loads(response.text)

        return normalize_output(raw_data)

    except Exception as e:
        print("Gemini extraction error:", e)
        return {}