import sys
from PIL import Image
import argparse

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v == '':
        return True
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="source image filename")
parser.add_argument("-o", "--output", help="destination filename")
parser.add_argument("-u", "--undo", type=str2bool, nargs='?', help="undo the transformation [y/n]", default=False)

parser.add_argument("--magnitude", type=int, help="amount to rotate, warning, advanced", default=10)

args = parser.parse_args()

print("opening" , args.input)
im = Image.open(args.input)
pixels = im.load()


def shiftX(data, width, height, shift):
    for x in range(width):
        for y in range(height):
            dest = (y + shift * x) % height
            temp = data[x,y]
            data[x,y] = data[x,dest]
            data[x,dest] = temp

def unshiftX(data, width, height, shift):
    for x in reversed(range(width)):
        for y in reversed(range(height)):
            dest = (y + shift * x) % height
            temp = data[x,y]
            data[x,y] = data[x,dest]
            data[x,dest] = temp

            
def shiftY(data, width, height, shift):
    for y in range(height):
        for x in range(width):
            dest = (x + shift * y) % width
            temp = data[x,y]
            data[x,y] = data[dest,y]
            data[dest,y] = temp

def unshiftY(data, width, height, shift):
    for y in reversed(range(height)):
        for x in reversed(range(width)):
            dest = (x + shift * y) % width
            temp = data[x,y]
            data[x,y] = data[dest,y]
            data[dest,y] = temp

# use --undo or -u instead of negative numberse
mag = abs(args.magnitude)

if (args.undo):
    unshiftY(pixels, im.width, im.height, mag)
    unshiftX(pixels, im.width, im.height, mag)
else:
    shiftX(pixels, im.width, im.height, mag)
    shiftY(pixels, im.width, im.height, mag)

im.save(args.output)
print("wrote", args.output)
