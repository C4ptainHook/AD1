import json
import pandas as pd
import numpy as np
import os


def cut_csv(params_json):
    params = json.loads(params_json)
    csv_file_path = params["csv_file_path"]
    separator = params["separator"]
    columns = params["columns"]
    df = pd.read_csv(csv_file_path, sep=separator, encoding="utf-8")
    missing_columns = set(df.columns) - set(columns)
    for col in missing_columns:
        df.drop(col, axis=1, inplace=True)
    df = df.fillna("null")
    file_name = os.path.basename(csv_file_path)
    df.to_csv(f"./Datasets/Processed/{file_name}", index=False)
    print(file_name)


# play_time_by_gamers = json.dumps(
#     {
#         "csv_file_path": "./Datasets/Selected/metacritic.csv",
#         "columns": ["metascore", "name", "console"],
#         "separator": ",",
#     }
# )

# cut_csv(play_time_by_gamers)

# play_time_by_gamers = json.dumps(
#     {
#         "csv_file_path": "./Datasets/Selected/requirements.csv",
#         "columns": [
#             "steam_appid",
#             "pc_requirements",
#             "mac_requirements",
#             "linux_requirements",
#             "minimum",
#         ],
#         "separator": ";",
#     }
# )

# cut_csv(play_time_by_gamers)

# play_time_by_gamers = json.dumps(
#     {
#         "csv_file_path": "./Datasets/Selected/all_steam.csv",
#         "columns": [
#             "game",
#             "link",
#             "release",
#             "rating",
#             "publisher",
#             "developer",
#             "detected_technologies",
#             "all_time_peak",
#             "all_time_peak_date",
#         ],
#         "separator": ",",
#     }
# )

# cut_csv(play_time_by_gamers)

# play_time_by_gamers = json.dumps(
#     {
#         "csv_file_path": "./Datasets/Selected/regions.csv",
#         "columns": [
#             "Name",
#             "Platform",
#             "Year_of_Release",
#             "Genre",
#             "Publisher",
#             "NA_players",
#             "EU_players",
#             "JP_players",
#             "Other_players",
#             "Global_players",
#             "Developer",
#             "Rating",
#         ],
#         "separator": ",",
#     }
# )

# cut_csv(play_time_by_gamers)

# play_time_by_gamers = json.dumps(
#     {
#         "csv_file_path": "./Datasets/Selected/time_to_beat.csv",
#         "columns": [
#             "achievements",
#             "description",
#             "developers",
#             "gfq_difficulty",
#             "gfq_rating",
#             "grnk_score",
#             "hltb_complete",
#             "hltb_single",
#             "igdb_score",
#             "igdb_single",
#             "igdb_uscore",
#             "languages",
#             "name",
#             "platforms",
#             "published_hltb",
#             "publishers",
#             "tags",
#             "voiceovers"
#         ],
#         "separator": ",",
#     }
# )

# cut_csv(play_time_by_gamers)
