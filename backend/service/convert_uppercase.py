def convert_uppercase(param):
    """Convert values of a dictionary into uppercase."""
    if isinstance(param, dict):
        for key, value in param.items():
            if isinstance(value, str):
                param[key] = value.upper()
        return param
    if isinstance(param, str):
        param = param.upper()
        return param
