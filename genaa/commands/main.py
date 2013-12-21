import argparse

from genaa.commands import box


subcommand_mapping = {
    'box': box.run
}


def build_parser():
    parser = argparse.ArgumentParser(description='genaa AA generator.')
    parser.add_argument('subcommand', choices=subcommand_mapping.keys())
    parser.add_argument('--width', dest='width', type=int, default=3)
    parser.add_argument('--height', dest='height', type=int, default=3)
    return parser


def run():
    parser = build_parser()
    opt = parser.parse_args()

    print(subcommand_mapping[opt.subcommand](opt))
