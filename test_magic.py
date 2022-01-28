#!/usr/bin/env python3

import os
os.environ.SKIP_GAY_AUTO_INIT = True
import gay

if __name__ == '__main__':
    print('Yay, testing!')
    print(f'This is a {gay.rainbowify("wonderfully long test with many characters")} of {gay.rainbowify("a")} very {gay.rainbowify("gay")}.')
else:
    raise AssertionError()
