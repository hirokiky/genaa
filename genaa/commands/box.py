from genaa.box import Box, SimpleBorder


def run(opt, text):
    box = Box(opt.width, opt.height, SimpleBorder, text=text)

    return box.render()
