import argparse
from instance_generation import generate_instances, DISTRIBUTIONS
from instance_writing import write_instance
import re

DEFAULT_PREFIX = 'gen'
DEFAULT_INSTANCES_PER_SIZE = 5
DEFAULT_JOB_COUNTS = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
DEFAULT_MACHINE_COUNTS = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
DEFAULT_DURATION_DISTRIBUTIONS = list(DISTRIBUTIONS.keys())


def main():
    parser = argparse.ArgumentParser(
        description='Generate random instances')
    parser.add_argument('--seed', help='randomness seed',
                        type=int, default=42)
    parser.add_argument('--output', help='output directory',
                        required=True, type=str)
    parser.add_argument('--prefix', help='instance name prefix',
                        type=str, default=DEFAULT_PREFIX)
    parser.add_argument('--instances-per-size', help='number of instances to generate for each size',
                        type=int, default=DEFAULT_INSTANCES_PER_SIZE)
    parser.add_argument('--duration-distributions', help='probability distributions for operation durations',
                        nargs='+', type=str, default=DEFAULT_DURATION_DISTRIBUTIONS, choices=DEFAULT_DURATION_DISTRIBUTIONS)
    parser.add_argument('--job-counts', help='list of number of jobs',
                        nargs='+', type=int, default=DEFAULT_JOB_COUNTS)
    parser.add_argument('--machine-counts', help='list of number of machines',
                        nargs='+', type=int, default=DEFAULT_MACHINE_COUNTS)
    args = parser.parse_args()

    print('Generating instances...')
    for inst in generate_instances(prefix=args.prefix, seed=args.seed, instances_per_size=args.instances_per_size, job_counts=args.job_counts, machine_counts=args.machine_counts, duration_distributions=args.duration_distributions):
        print(f'Generated {inst.name}')
        write_instance(args.output, inst)

    print(f'Done!')


if __name__ == '__main__':
    main()
