from enum import IntEnum, StrEnum


class SukebeiCategories(StrEnum):
    art = '1_0'
    art_anime = '1_1'
    art_doujinshi = '1_2'
    art_games = '1_3'
    art_manga = '1_4'
    art_pictures = '1_5'
    real_life = '2_0'
    real_life_pictures = '2_1'
    real_life_videos = '2_2'


class NyaaFunCategories(StrEnum):
    anime = '1_0'
    anime_amv = '1_1'
    anime_english = '1_2'
    anime_non_english = '1_3'
    anime_raw = '1_4'
    audio = '2_0'
    audio_lossless = '2_1'
    audio_lossy = '2_2'
    literature = '3_0'
    literature_english = '3_1'
    literature_non_english = '3_2'
    literature_raw = '3_3'
    live_action = '4_0'
    live_action_english = '4_1'
    live_action_idol_pv = '4_2'
    live_action_non_english = '4_3'
    live_action_raw = '4_4'
    pictures = '5_0'
    pictures_graphics = '5_1'
    pictures_photos = '5_2'
    software = '6_0'
    software_apps = '6_1'
    software_games = '6_2'


class Filter(IntEnum):
    no_remakes = 1
    trusted_only = 2


class NyaaSite(StrEnum):
    FUN = 'https://nyaa.si/'
    FAP = 'https://sukebei.nyaa.si/'
