from typing import TypedDict, List, Dict
try:
    from typing_extensions import TypeAlias
except ImportError:
    TypeAlias = object


# pricing_helpers.py
EMet: TypeAlias = List[float]
LBuy: TypeAlias = List[float]
LSell: TypeAlias = List[float]


class SingleMeterDict(TypedDict):
    e_met: EMet
    l_buy: LBuy
    l_sell: LSell


MetersDict: TypeAlias = Dict[str, SingleMeterDict]
