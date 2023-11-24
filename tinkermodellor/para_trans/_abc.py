from abc import ABCMeta, abstractmethod
from typing import Any

class Base(metaclass=ABCMeta):
    
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
        
    def _transform_to_tinker(self, atom_type : str, trans_dict : dict) -> str:
        return trans_dict.items(atom_type)

