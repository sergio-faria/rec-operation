from typing import TypedDict, Dict
try:
    from typing_extensions import TypeAlias
except ImportError:
    # fallback se typing_extensions não estiver instalado
    TypeAlias = object


class SingleBtmStorage(TypedDict):
    degradation_cost: float
    e_bn: float
    eff_bc: float
    eff_bd: float
    init_e: float
    p_max: float
    soc_max: float
    soc_min: float


BtmStorage: TypeAlias = Dict[str, SingleBtmStorage]
