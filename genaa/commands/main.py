import argparse

from genaa.commands import box


subcommand_mapping = {
    'box': box
}


def build_parser():
    parser = argparse.ArgumentParser(description='genaa AA generator.')
    subparsers = parser.add_subparsers()

    for name, subcommand in subcommand_mapping.items():
        subcommand_parser = subparsers.add_parser(name)
        subcommand.apply_arguments(subcommand_parser)
    return parser


def run():
    parser = build_parser()
    opt = parser.parse_args()

    if hasattr(opt, 'func'):
        print(opt.func(opt))
    else:
        parser.print_help()
