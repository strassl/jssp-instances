import os
from common import Instance


def write_instance(folder: str, instance: Instance):
    path = os.path.join(folder, f'{instance.name}.txt')

    with open(path, 'w') as f:
        write_data_to_file(
            f, instance.n_jobs, instance.n_machines, instance.data)


def write_data_to_file(f, n_jobs, n_machines, data):
    print(f'{n_jobs}\t{n_machines}', file=f)

    for job in data:
        line = '\t'.join([f'{op.machine} {op.duration}' for op in job])
        print(line, file=f)
