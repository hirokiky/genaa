from genaa.box import Box, style_mapping


def apply_arguments(parser):
    parser.add_argument('-w', '--width', dest='width', type=int)
    parser.add_argument('-h,--height', dest='height', type=int)
    parser.add_argument('-s,--style', dest='style', default='simple', choices=style_mapping.keys())
    parser.set_defaults(func=run)
    return parser


def run(opt, text):
    box = Box(style_mapping[opt.style],
              width=opt.width, height=opt.height,
              text=text)

    return box.render()
