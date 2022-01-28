#!/usr/bin/env python3

import sys


RESET_ESCAPE = '\x1b[m'
GAMMA = 3


def gamma_blend(frac):
    f_from = (1 - frac) ** (1 / GAMMA)
    f_to = frac ** (1 / GAMMA)
    return f_from, f_to


def rainbow_color(frac):
    assert 0 <= frac <= 1
    if frac < 1 / 6:
        frac *= 3
        frac += 1 / 2
        f_from, f_to = gamma_blend(frac)
        rgb = (f_to, 0, f_from)
    elif frac < 3 / 6:
        frac -= 1 / 6
        frac *= 3
        f_from, f_to = gamma_blend(frac)
        rgb = (f_from, f_to, 0)
    elif frac < 5 / 6:
        frac -= 3 / 6
        frac *= 3
        f_from, f_to = gamma_blend(frac)
        rgb = (0, f_from, f_to)
    else:
        frac -= 5 / 6
        frac *= 3
        f_from, f_to = gamma_blend(frac)
        rgb = (f_to, 0, f_from)
    return tuple(round(c * 255) for c in rgb)


def rainbow_color_escape(frac, foreground):
    r, g, b = rainbow_color(frac)
    code = 38 if foreground else 48
    # ESC[ 38;2;⟨r⟩;⟨g⟩;⟨b⟩ m
    return f'\x1b[{code};2;{r};{g};{b}m'


def rainbowify(text):
    total_len = len(text)
    if total_len == 0:
        return ''
    if total_len == 1:
        if text == '\n':
            return text
        return rainbow_color_escape(0, False) + rainbow_color_escape(0.5, True) + text + RESET_ESCAPE
    return ''.join(rainbow_color_escape(i / (total_len - 1), False) + rainbow_color_escape((i / (total_len - 1) + 0.5) % 1, True) + c for (i, c) in enumerate(text)) + RESET_ESCAPE


def init_gay():
    old_write = sys.stdout.write
    sys.stdout.write = lambda text: old_write(rainbowify(text))


def perhaps_init_gay():
    # Sneaky magic flag to disable auto init, if you want to call init_gay() yourself.
    import os
    try:
        do_auto_init = not os.environ.SKIP_GAY_AUTO_INIT
    except AttributeError:
        do_auto_init = True
    if do_auto_init:
        init_gay()


if __name__ == '__main__':
    init_gay()
    print('RAAAAINBOWS!')
    print('(Also try "import gay"!)')
else:
    perhaps_init_gay()
