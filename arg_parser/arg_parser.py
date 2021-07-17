import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Argument parser for talking_containers"
    )
    parser.add_argument(
        "-t",
        "--type",
        help="Choose how the container should be used: server | client",
        required=True,
    )

    return parser.parse_args()
