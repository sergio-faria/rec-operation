from typing import TypedDict, List
try:
    from typing_extensions import TypeAlias
except ImportError:
    TypeAlias = object


class OfferDict(TypedDict):
    origin: str
    amount: float
    value: float


OffersList: TypeAlias = List[OfferDict]
PricesList: TypeAlias = List[float]
