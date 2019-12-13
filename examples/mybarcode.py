import sys
from escpos.printer import File
from escpos.constants import ESC, GS, NUL, QR_ECLEVEL_L, QR_ECLEVEL_M, QR_ECLEVEL_H, QR_ECLEVEL_Q
import barcode
from barcode.writer import ImageWriter
import os

def usage():
    """
    Usage: mybarcode.py <content> <dest_file>

    Options:
      -r    reverse bit order in bytes.

    Arguments:
      <dest_file>   a file name or - for stdout
                    ex: /dev/usb/lp0
    """
    print(usage.__doc__.strip())


if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    reverse = False
    if sys.argv[1] == "-r":
        reverse = True
        content = sys.argv[2]
        dest    = sys.argv[3]
    else:
        content = sys.argv[1]
        dest    = sys.argv[2]
    if dest == '-':
        dest = '/dev/stdout'

    p = File(dest, profile='BRIGHTEK-H-U05')
    print(p.profile, file=sys.stderr)
    print("content length: %d" % len(content), file=sys.stderr)
    print("content: '%s'" % content, file=sys.stderr)


    # Most of the code is copied from ~/Printer/python-escpos/src/escpos/escpos.py
    # soft_barcode()
    image_writer = ImageWriter()
    # Some software barcodes (code128 is able to print 128 ascii character)
    barcode_type = 'code128'
    barcode_class = barcode.get_barcode_class(barcode_type)
    my_code = barcode_class(content, writer=image_writer)

    module_height=7
    module_width=0.3
    text_distance=1
    with open(os.devnull, "wb") as nullfile:
        my_code.write(nullfile, {
            'module_height': module_height,
            'module_width': module_width,
            'text_distance': text_distance
        })

    # Retrieve the Pillow image
    im = my_code.writer._image

    p.text('\n')
    p.image(im, center=True, invert_byte=reverse, impl='bitImageRaster')
    p.text('\n')
    p.text('\n')

