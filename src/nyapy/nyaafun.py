from .enums import Filter, NyaaFunCategories, NyaaSite
from .nyaa import Nyaa
from .types.nyaa import Order, ResponseData, Sort


class NyaaFun(Nyaa):
    def __init__(self) -> None:
        super().__init__(NyaaSite.FUN)

    async def get_content(
        self,
        *,
        filter: Filter | None = None,
        category: NyaaFunCategories | None = None,
        query: str | None = None,
        page: int = 1,
        sort: Sort | None = None,
        order: Order = 'desc',
    ) -> ResponseData:
        return await super().get_content(
            filter=filter,
            category=category,
            query=query,
            sort=sort,
            page=page,
            order=order,
        )
