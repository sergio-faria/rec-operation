from rec_op_lem_prices.custom_types.btm_storage_types import BtmStorage
from typing import TypedDict, Dict, List
try:
    from typing_extensions import TypeAlias
except ImportError:
    TypeAlias = object


# -- INPUTS ------------------------------------------------------------------------------------------------------------
class BackpackS1Dict(TypedDict):
    btm_storage: BtmStorage
    delta_t: float
    e_c: List[float]
    e_g: List[float]
    horizon: int
    id: str
    l_buy: List[float]
    l_extra: float
    l_market_buy: List[float]
    l_market_sell: List[float]
    l_sell: List[float]
    max_p: float


# -- OUTPUTS -----------------------------------------------------------------------------------------------------------
BtmStorageOutputsDict: TypeAlias = Dict[str, List[float]]


class OutputsS1Dict(TypedDict):
    c_ind: float
    c_ind_without_deg: float
    c_ind_without_deg_and_p_extra: float
    c_ind_without_p_extra: float
    deg_cost: float
    delta_bc: BtmStorageOutputsDict
    delta_sup: List[float]
    e_bat: BtmStorageOutputsDict
    e_bc: BtmStorageOutputsDict
    e_bd: BtmStorageOutputsDict
    e_cmet: List[float]
    e_sup_market: List[float]
    e_sup_retail: List[float]
    e_sur_market: List[float]
    e_sur_retail: List[float]
    meter_id: str
    milp_status: str
    obj_value: float
    p_extra: List[float]
    p_extra_cost: float
    soc_bat: BtmStorageOutputsDict
