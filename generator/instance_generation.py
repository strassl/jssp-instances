from typing import List, Generator
import random
import numpy as np
import scipy.stats as stats
from common import Instance, Op

DISTRIBUTIONS = {
    'const-1': stats.randint(1, 1+1),
    'uniform-1-99': stats.randint(1, 99+1),
    'uniform-1-200': stats.randint(1, 200+1),
    'binom-0.5-1-99': stats.binom(98, 0.5, loc=1),
    'nbinom-0.5-1': stats.nbinom(1, 0.5, loc=1),
}

def generate_instances(prefix: str, seed: int, instances_per_size: int, job_counts: List[int], machine_counts: List[int], duration_distributions: List[str]) -> Generator[Instance, None, None]:
    count = instances_per_size * len(job_counts) * len(machine_counts) * len(duration_distributions)
    num_len = len(str(count+1))
    num = 0
    for duration_distribution in duration_distributions:
        for jobs in job_counts:
            for machines in machine_counts:
                for _ in range(0, instances_per_size):
                    num += 1
                    name = f'{prefix}{num:0{num_len}d}_s{seed}_j{jobs}_m{machines}_d{duration_distribution}'
                    data = generate_instance(seed=seed+num, n_jobs=jobs, n_machines=machines,
                                             duration_distribution=DISTRIBUTIONS[duration_distribution])
                    yield Instance(name=name, n_jobs=jobs, n_machines=machines, data=data)


def generate_instance(seed: int, n_jobs: int, n_machines: int, duration_distribution) -> List[List[Op]]:
    r = random.Random(seed)
    order_seed = r.randint(0, 9999)
    duration_seed = r.randint(0, 9999)

    r_order = random.Random(order_seed)
    durations = duration_distribution.rvs(
        [n_jobs, n_machines], random_state=duration_seed)

    data = []
    for job in range(0, n_jobs):
        ops = []
        for machine in range(0, n_machines):
            duration = durations[job, machine]
            op = Op(machine=machine, duration=duration)
            ops += [op]
        random.shuffle(ops, random=lambda: r_order.uniform(0, 1))
        data += [ops]

    return data
