def get_height_category(gender, height ):
    result = ""
    if gender == "male":
        if height > 70:
            result = "above average"
        else:
            result = "below average"
    elif gender == "female":
        if height > 64:
            result = "above average"
        else:
            result = "below average"
    else:
        result = "unknown average"
    return(result)
