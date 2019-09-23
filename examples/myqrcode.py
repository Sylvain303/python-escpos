import sys

from escpos.printer import Usb, File


def usage():
    print("usage: myqrcode.py <content>")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    content = sys.argv[1]

    # Adapt to your needs
    p = File("output")
    p.qr(content, size=10, center=True)
