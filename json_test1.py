import json
from collections import OrderedDict

group_data = OrderedDict()
albums = OrderedDict()

group_data["name"] = "여자친구"
group_data["members"] = ["소원", "예린", "은하", "유주", "신비", "엄지"]

albums["EP 1집"] = "Season of Glass"
albums["EP 2집"] = "Flower Bud"
albums["EP 3집"] = "Snowflake"
albums["정규 1집"] = "LOL"
albums["EP 4집"] = "THE AWAKENING"

group_data["albums"] = albums

print(json.dumps(group_data, ensure_ascii=False, indent="\t"))
