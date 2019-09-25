#!/usr/bin/env python3
import sys
import qrcode
from escpos.printer import Usb, File
from escpos.constants import ESC, GS, NUL, QR_ECLEVEL_L, QR_ECLEVEL_M, QR_ECLEVEL_H, QR_ECLEVEL_Q

def usage():
    """
    Usage: myqrcode.py [-r] <content> <dest_file>

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

    #max_width = int(p.profile.profile_data['media']['width']['pixels'])

    qr_code = qrcode.QRCode(version=5, box_size=6, border=4, error_correction=QR_ECLEVEL_L)
    qr_code.add_data(content)
    qr_img = qr_code.make_image()
    im = qr_img._img.convert("RGB")

    width_pixels = im.size[0]
    print("qr_code_width: %d" % width_pixels, file=sys.stderr)

    p.text('\n')
    p.image(im, center=True, invert_byte=reverse)
    p.text('\n')
    p.text('\n')
    
    #p.qr(content, size=10, center=True)
