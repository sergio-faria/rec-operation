from rec_op_lem_prices.custom_types.individual_cost_types import OutputsIndCostDict
from rec_op_lem_prices.custom_types.stage_one_milp_types import OutputsS1Dict
from rec_op_lem_prices.custom_types.meters_types import (
    SinglePostMeters,
    SinglePreMeters,
    Meters
)
from typing import TypedDict, List, Dict, Tuple
try:
    from typing_extensions import TypeAlias
except ImportError:
    TypeAlias = object


# -- INPUTS ------------------------------------------------------------------------------------------------------------
LGridBilateral: TypeAlias = Dict[str, Dict[str, List[float]]]


class BaseBackpackS2BilateralDict(TypedDict):
    delta_t: float
    horizon: int
    l_extra: float
    l_grid: LGridBilateral
    l_market_buy: List[float]
    l_market_sell: List[float]
    strict_pos_coeffs: bool
    total_share_coeffs: bool


class LoopPreBackpackS2BilateralDict(BaseBackpackS2BilateralDict):
    meters: SinglePreMeters


class SinglePreBackpackS2BilateralDict(LoopPreBackpackS2BilateralDict):
    l_lem: List[float]


CollectivePreBackpackS2BilateralDict: TypeAlias = SinglePreBackpackS2BilateralDict


class LoopPostBackpackS2BilateralDict(BaseBackpackS2BilateralDict):
    meters: SinglePostMeters


class SinglePostBackpackS2BilateralDict(LoopPostBackpackS2BilateralDict):
    l_lem: List[float]


CollectivePostBackpackS2BilateralDict: TypeAlias = SinglePostBackpackS2BilateralDict


class BackpackS2BilateralDict(BaseBackpackS2BilateralDict):
    l_lem: List[float]
    meters: Meters
    second_stage: bool


# -- OUTPUTS -----------------------------------------------------------------------------------------------------------
ValuePerId: TypeAlias = Dict[str, float]
ListPerId: TypeAlias = Dict[str, List[float]]
ListPerIdPerId: TypeAlias = Dict[str, ListPerId]


class SinglePostOutputsS2BilateralDict(TypedDict):
    c_ind2bilateral: ValuePerId
    c_ind2bilateral_without_p_extra: ValuePerId
    delta_alc: ListPerId
    delta_cmet: ListPerId
    delta_coeff: ListPerId
    delta_slc: ListPerId
    delta_sup: ListPerId
    e_alc: ListPerId
    e_cmet: ListPerId
    e_consumed: ListPerId
    e_pur_bilateral: ListPerIdPerId
    e_sale_bilateral: ListPerIdPerId
    e_slc_bilateral: ListPerIdPerId
    e_sup_market: ListPerId
    e_sup_retail: ListPerId
    e_sur_market: ListPerId
    e_sur_retail: ListPerId
    milp_status: str
    obj_value: float
    p_extra: ListPerId
    p_extra_cost2bilateral: ValuePerId


CollectivePostOutputsS2BilateralDict: TypeAlias = Tuple[
    SinglePostOutputsS2BilateralDict,
    List[OutputsIndCostDict]
]


class OutputsS2BilateralDict(SinglePostOutputsS2BilateralDict):
    c_ind2bilateral_without_deg: ValuePerId
    c_ind2bilateral_without_deg_and_p_extra: ValuePerId
    deg_cost2bilateral: ValuePerId
    delta_bc: ListPerIdPerId
    e_bat: ListPerIdPerId
    e_bc: ListPerIdPerId
    e_bd: ListPerIdPerId
    soc_bat: ListPerIdPerId


SinglePreOutputsS2BilateralDict: TypeAlias = OutputsS2BilateralDict

CollectivePreOutputsS2BilateralDict: TypeAlias = Tuple[
    OutputsS2BilateralDict,
    List[OutputsS1Dict]
]
