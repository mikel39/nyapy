from .enums import NyaaSite
from .nyaa import Nyaa
from .types.nyaa import SukebeiCategories


class Sukebei(Nyaa[SukebeiCategories]):
    def __init__(self) -> None:
        super().__init__(NyaaSite.FAP)
