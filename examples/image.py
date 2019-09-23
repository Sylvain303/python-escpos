import sys

from escpos.printer import Usb, File

def usage():
    print("usage: image.py <image_file>")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    content = sys.argv[1]

    # Adapt to your needs
    #p = Usb(0x0416, 0x5011, profile="POS-5890")
    p = File("output")
    p.image(content,  invert_byte=True)
