def validate_data(data):

    validated = {}

    for key, value in data.items():

        # Skip None values
        if value is None:
            continue

        # -------------------------
        # Numeric Fields
        # -------------------------

        if key in ["num_plants"]:
            try:
                validated[key] = int(value)
            except:
                raise ValueError(f"{key} must be a number.")

        elif key in ["soil_ph"]:
            try:
                validated[key] = float(value)
            except:
                raise ValueError("soil_ph must be a number.")

        elif key in ["shade_percent"]:
            try:
                validated[key] = int(value)
            except:
                raise ValueError("shade_percent must be a number.")

        # -------------------------
        # String Fields
        # -------------------------

        else:
            if isinstance(value, str):
                validated[key] = value.lower().strip()
            else:
                validated[key] = value

    return validated