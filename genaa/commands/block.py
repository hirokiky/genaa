import sys

from genaa.block import render_block, style_mapping


def apply_arguments(parser):
    parser.add_argument('-t', '--text', dest='text',
                        help='Passing text by argument into block')
    parser.add_argument('-s', '--style', dest='style',
                        default='ascii', choices=style_mapping.keys())
    parser.add_argument('-l', '--list', default=False, action='store_true',
                        help='Displaying examples for each styles')
    parser.set_defaults(func=run)
    return parser


def generate_style_list(styles=style_mapping):
    example_text = """\
 *
  *  * *    *  *    *
***   **  * *   **   *
      *    **  **  ***\
""".split('\n')
    examples = []
    for style in sorted(styles):
        example_block = render_block(example_text, style_mapping[style])
        examples.append(style + ':\n' + example_block)
    return '\n\n'.join(examples)


def run(opt):
    if opt.list:
        return generate_style_list()

    if getattr(opt, 'text'):
        text = opt.text
    else:
        text = sys.stdin.read()

    return render_block(text.split('\n'), style_mapping[opt.style])
