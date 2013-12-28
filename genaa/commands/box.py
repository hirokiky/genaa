import sys

from genaa.box import Box, style_mapping


def apply_arguments(parser):
    parser.add_argument('-t', '--text', dest='text',
                        help='Passing text by argument into box')
    parser.add_argument('-W', '--width', dest='width', type=int)
    parser.add_argument('-H', '--height', dest='height', type=int)
    parser.add_argument('-s', '--style', dest='style',
                        default='ascii', choices=style_mapping.keys())
    parser.add_argument('-a', '--align', choices=('left', 'center', 'right'),
                        default='left', dest='align')
    parser.add_argument('-l', '--list', default=False, action='store_true',
                        help='Displaying examples for each styles')
    parser.set_defaults(func=run)
    return parser


def generate_style_list(styles=style_mapping):
    example_text = """\
Hello.
How about this style?\
"""
    examples = []
    for style in sorted(styles):
        example_box = Box(style_mapping[style],
                          align='left', text=example_text).render()
        examples.append(style + ':\n' + example_box)
    return '\n\n'.join(examples)


def run(opt):
    if opt.list:
        return generate_style_list()

    if getattr(opt, 'text'):
        text = opt.text
    else:
        text = sys.stdin.read()

    box = Box(style_mapping[opt.style],
              width=opt.width, height=opt.height,
              align=opt.align, text=text)

    return box.render()
