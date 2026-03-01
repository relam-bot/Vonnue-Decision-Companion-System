ALLOWED_FIELDS = {
    "module",
    "num_plants",
    "water_availability",
    "budget",
    "rainfall_level",
    "soil_drainage",
    "terrain",
    "climate_temperature",
    "growth_stage",
    "labour_availability",
    "water_source",
    "climate_humidity",
    "soil_ph",
    "nitrogen_level",
    "phosphorus_level",
    "potassium_level",
    "organic_matter",
    "leaf_symptom",
    "pest_query",
    "season",
    "disease_pressure",
    "shade_percent",
    "altitude",
    "market_priority"
}


def validate_data(data):

    validated = {}

    for key, value in data.items():

        if key not in ALLOWED_FIELDS:
            continue

        if value is None:
            continue

        try:
            if key == "num_plants":
                validated[key] = int(value)

            elif key == "soil_ph":
                validated[key] = float(value)

            elif key == "shade_percent":
                validated[key] = int(value)

            else:
                validated[key] = value.lower().strip() if isinstance(value, str) else value

        except:
            continue

    return validated
