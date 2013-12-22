from genaa.box import Box, style_mapping


def apply_arguments(parser):
    parser.add_argument('--width', dest='width', type=int, default=3)
    parser.add_argument('--height', dest='height', type=int, default=3)
    parser.add_argument('--style', dest='style', default='simple')
    parser.set_defaults(func=run)
    return parser


def run(opt, text):
    box = Box(opt.width, opt.height, style_mapping[opt.style], text=text)

    return box.render()
