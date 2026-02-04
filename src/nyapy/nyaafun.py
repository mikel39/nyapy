from .enums import NyaaSite
from .nyaa import Nyaa
from .types.nyaa import NyaaFunCategories


class NyaaFun(Nyaa[NyaaFunCategories]):
    def __init__(self) -> None:
        super().__init__(NyaaSite.FUN)
