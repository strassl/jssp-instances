from typing import NamedTuple, List

class Op(NamedTuple):
    machine: int
    duration: int


class Instance(NamedTuple):
    name: str
    n_jobs: int
    n_machines: int
    data: List[List[Op]]
