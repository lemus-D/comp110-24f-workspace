__author__ = "730736088"


def invert(Dict: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}
    iv_key_values = []
    for keys in Dict:
        for key_values in iv_key_values:
            if Dict[keys] == key_values:
                raise KeyError("wouldve been a key error")
        iv_key_values.append(Dict[keys])
        inverted_dict[Dict[keys]] = keys
    return inverted_dict


def favorite_color(Dict: dict[str, str]) -> str:
    if len(Dict) == 0:
        return ""
    value_list = []
    count = 0
    mcount = 0
    for key in Dict:
        value = Dict[key]
        value_list.append(value)
    mcolor = value_list[0]
    for i in value_list:
        for j in value_list:
            if i == j:
                count += 1
        if count > mcount:
            mcolor = i
            mcount = count
        count = 0
    return mcolor


def count(List: list[str]) -> dict[str, int]:
    Dict: dict[str, int] = {}
    for i in List:
        if i in Dict:
            Dict[i] += 1
        else:
            Dict[i] = 1
    return Dict


def alphabetizer(List: list[str]) -> dict[str, list[str]]:
    Dict: dict[str, list[str]] = {}
    for i in List:
        if i[0].lower() in Dict:
            Dict[i[0]].append(i)
        else:
            Dict[i[0].lower()] = [i]
    return Dict


def update_attendance(Dict: dict[str, list[str]], day: str, student: str) -> None:
    count = 0
    if day in Dict:
        for i in Dict[day]:
            if i == student:
                count += 1
        if count == 0:
            Dict[day].append(student)
        count = 0
    else:
        Dict[day] = [student]
    print(Dict)
