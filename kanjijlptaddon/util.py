import json

kanji_data = {}

def get_kanji_data(kanji: str):
    global kanji_data
    if len(kanji) != 1:
        print("'%s' is not a kanji" % kanji)
        return {}
    if len(kanji_data) == 0:
        # If kanji_data hasn't been loaded yet
        reload_kanji_data()
    if kanji in kanji_data:
        return kanji_data[kanji]
    # Return default value
    return {"jlpt": 5, "grade": 1}

def kanji_to_jlpt(kanji: str) -> int:
    """

    :param kanji:
    :return:
    """

    # Get jlpt level of each kanji in string
    jlpt_levels = [get_kanji_data(k) for k in kanji_data]
    
    # The hardest kanji determines the result of this function
    return min(jlpt_levels)

def reload_kanji_data():
    global kanji_data
    with open("./kanji_data.json", "r") as f:
        kanji_data = json.load(f)
        f.close()