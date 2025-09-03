from typing import TypedDict
from typing import List


# -- INPUTS ------------------------------------------------------------------------------------------------------------
class BackpackIndCostDict(TypedDict):
	delta_t: float
	e_met: List[float]
	id: str
	l_buy: List[float]
	l_extra: float
	l_market_buy: List[float]
	l_market_sell: List[float]
	l_sell: List[float]
	max_p: float


# -- OUTPUTS -----------------------------------------------------------------------------------------------------------
class OutputsIndCostDict(TypedDict):
	c_ind: float
	meter_id: str
	e_sup_market: List[float]
	e_sup_retail: List[float]
	e_sur_market: List[float]
	e_sur_retail: List[float]
	p_extra: List[float]
