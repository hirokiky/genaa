from genaa.box import Box, SimpleBorder


def run(opt):
    box = Box(opt.width, opt.height, SimpleBorder)

    return box.render()
