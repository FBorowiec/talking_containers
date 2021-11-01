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

    parser.add_argument(
        "-a",
        "--add",
        help="just a random shit",
        required=False,
    )

    return parser.parse_args()
