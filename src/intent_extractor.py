import re


def extract_intent_and_entities(user_input: str):

    user_input = user_input.lower()
    data = {}

    # =========================================================
    # IRRIGATION INTENT
    # =========================================================

    if any(phrase in user_input for phrase in [
        "irrigation",
        "watering",
        "water plan",
        "irrigation system",
        "water system"
    ]):
        data["intent_irrigation"] = True

    # =========================================================
    # LABOUR INTENT
    # =========================================================

    if any(phrase in user_input for phrase in [
        "labour",
        "labours",
        "worker",
        "workers",
        "manpower",
        "how many labour",
        "how many workers",
        "labour required",
        "workers required",
        "manpower required"
    ]):
        data["intent_labour"] = True

    # =========================================================
    # FERTILIZER INTENT
    # =========================================================

    if any(phrase in user_input for phrase in [
        "fertilizer",
        "fertiliser",
        "nutrient",
        "deficiency",
        "yellow leaves",
        "leaf problem"
    ]):
        data["intent_fertilizer"] = True

    # =========================================================
    # PESTICIDE INTENT
    # =========================================================

    if any(phrase in user_input for phrase in [
        "pest",
        "borer",
        "capsule borer",
        "insect",
        "disease control",
        "control pest"
    ]):
        data["intent_pesticide"] = True
        data["pest_query"] = user_input

    # =========================================================
    # SOIL INTENT
    # =========================================================

    if any(phrase in user_input for phrase in [
        "soil",
        "soil ph",
        "drainage",
        "soil condition"
    ]):
        data["intent_soil"] = True

    # =========================================================
    # SHADE INTENT
    # =========================================================

    if "shade" in user_input:
        data["intent_shade"] = True

    # =========================================================
    # VARIETY INTENT
    # =========================================================

    if any(phrase in user_input for phrase in [
        "variety",
        "which type",
        "best type",
        "cardamom type"
    ]):
        data["intent_variety"] = True

    # =========================================================
    # NUMERIC EXTRACTION
    # =========================================================

    # Plant count
    plant_match = re.search(r'(\d+)\s*plants?', user_input)
    if plant_match:
        data["num_plants"] = int(plant_match.group(1))

    # Shade percentage
    shade_match = re.search(r'(\d+)\s*%', user_input)
    if shade_match:
        data["shade_percent"] = int(shade_match.group(1))

    # Soil pH
    ph_match = re.search(r'ph\s*(\d+(\.\d+)?)', user_input)
    if ph_match:
        try:
            data["soil_ph"] = float(ph_match.group(1))
        except:
            pass

    # =========================================================
    # WATER LEVEL
    # =========================================================

    if "low water" in user_input:
        data["water_availability"] = "low"
    elif "medium water" in user_input:
        data["water_availability"] = "medium"
    elif "high water" in user_input:
        data["water_availability"] = "high"

    # =========================================================
    # BUDGET
    # =========================================================

    if "low budget" in user_input:
        data["budget"] = "low"
    elif "medium budget" in user_input:
        data["budget"] = "medium"
    elif "high budget" in user_input:
        data["budget"] = "high"

    # =========================================================
    # DRAINAGE
    # =========================================================

    if "poor drainage" in user_input:
        data["soil_drainage"] = "poor"
    elif "good drainage" in user_input:
        data["soil_drainage"] = "good"

    # =========================================================
    # RAINFALL
    # =========================================================

    if "high rainfall" in user_input:
        data["rainfall_level"] = "high"
    elif "low rainfall" in user_input:
        data["rainfall_level"] = "low"

    # =========================================================
    # LEAF SYMPTOMS
    # =========================================================

    if "yellow" in user_input:
        data["leaf_symptom"] = "yellow"
    elif "brown" in user_input:
        data["leaf_symptom"] = "brown"
    elif "curl" in user_input:
        data["leaf_symptom"] = "curling"

    return data
