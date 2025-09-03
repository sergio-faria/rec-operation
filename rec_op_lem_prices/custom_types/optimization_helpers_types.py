# general_helpers.py
from typing import Dict, List, Union
try:
    from typing_extensions import TypeAlias
except ImportError:
    # fallback se typing_extensions não estiver instalado
    TypeAlias = object

ForecastsList = List[Dict]  # type: TypeAlias


class SinglePeerMeasuresDict(Dict):
    peer_id: str
    measure: float


class SingleUpacMeasuresDict(Dict):
    upac_id: str
    measure: float


class PeerMeasuresDict(Dict):
    peer_measures: List[SinglePeerMeasuresDict]


class UpacMeasuresDict(Dict):
    upac_measures: List[SingleUpacMeasuresDict]


InputDatadict = Union[PeerMeasuresDict, UpacMeasuresDict]  # type: TypeAlias

# milp_helpers.py
MetersDict = Dict[str, Dict[str, List[float]]]  # type: TypeAlias
MetersParamDict = Dict[str, List[float]]        # type: TypeAlias
