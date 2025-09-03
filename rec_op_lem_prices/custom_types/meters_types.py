from rec_op_lem_prices.custom_types.btm_storage_types import BtmStorage
from typing import TypedDict, Union, List, Dict
try:
    from typing_extensions import TypeAlias
except ImportError:
    TypeAlias = object


class SinglePostMeter(TypedDict):
    e_c: List[float]
    e_g: List[float]
    l_buy: List[float]
    l_sell: List[float]
    max_p: float


class SinglePreMeter(SinglePostMeter):
    btm_storage: Union[BtmStorage, None]


class SingleMeter(SinglePreMeter):
    c_ind: float


SinglePostMeters: TypeAlias = Dict[str, SinglePostMeter]
SinglePreMeters: TypeAlias = Dict[str, SinglePreMeter]
Meters: TypeAlias = Dict[str, SingleMeter]
