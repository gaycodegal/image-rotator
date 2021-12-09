# Image Rotator (imrot10)

Its like rot13 but for images.

Calling the algorithm imrot10 for im = image, rot = rotation, 10 = default magnitude.

Unfortunately it is not symmetric like rot13 but i'm not wasting my time to develop fully symmetric so you have to use the -u parameter to undo it.

```
python3 image-rotator.py -h
usage: image-rotator.py [-h] [-i INPUT] [-o OUTPUT] [-u [UNDO]]
                        [--magnitude MAGNITUDE]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        source image filename
  -o OUTPUT, --output OUTPUT
                        destination filename
  -u [UNDO], --undo [UNDO]
                        undo the transformation [y/n]
  --magnitude MAGNITUDE
                        amount to rotate, warning, advanced
```

## installation

May require you to install PIL.

Do that with `pip3 install pillow` or `python3 -m pip install pillow`.

May require you to install pip via `sudo apt install python3-pip`.