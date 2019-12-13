import sys
from escpos.printer import Usb, File
from escpos.constants import ESC, GS, NUL, QR_ECLEVEL_L, QR_ECLEVEL_M, QR_ECLEVEL_H, QR_ECLEVEL_Q

def usage():
    """
    Usage: mybarcode.py <content> <dest_file>

    Arguments:
      <dest_file>   a file name or - for stdout
                    ex: /dev/usb/lp0
    """
    print(usage.__doc__.strip())


if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    content = sys.argv[1]
    dest    = sys.argv[2]
        
    if dest == '-':
        dest = '/dev/stdout'

    p = File(dest, profile='BRIGHTEK-H-U05')
    print(p.profile, file=sys.stderr)
    print("content length: %d" % len(content), file=sys.stderr)
    print("content: '%s'" % content, file=sys.stderr)

    # Some software barcodes (code128 is able to print 128 ascii character)
    p.text('\n')
    p.soft_barcode('code128', content)
    p.text('\n')
    p.text('\n')

