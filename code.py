print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.lock_status import LockStatus
from kmk.extensions.LED import LED

keyboard = KMKKeyboard()
leds = LED(led_pin=[board.GP6, board.GP5, board.GP7], brightness=0)

keyboard.col_pins = (board.GP28, board.GP27, board.GP26, board.GP22, board.GP21, board.GP20, board.GP19, board.GP18, board.GP17, board.GP16,)
keyboard.row_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9,  board.GP8,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.coord_mapping = [
59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 79, 77, 78,
41, 40, 49, 48, 47, 46, 45, 44, 43, 42, 63, 60, 76,
39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 67, 64, 75,
21, 20, 29, 28, 27, 26, 25, 24, 23, 22, 65, 68, 73,
9,  8,  7,  6,  5,  4,  3,  2,  1,  0,  66, 69, 74,
11, 10, 19, 18, 17, 16, 15, 14, 13, 12, 70, 71, 72,
]

class LEDLockStatus(LockStatus):
    def set_lock_leds(self):
        if self.get_num_lock():
            leds.set_brightness(100, leds=[0])
        else:
            leds.set_brightness(0, leds=[0])

        if self.get_caps_lock():
            leds.set_brightness(100, leds=[1])
        else:
            leds.set_brightness(0, leds=[1])

        if self.get_scroll_lock():
            leds.set_brightness(100, leds=[2])
        else:
            leds.set_brightness(0, leds=[2])

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)  # Critically important. Do not forget
        if self.report_updated:
            self.set_lock_leds()


keyboard.modules.append(Layers())
keyboard.extensions.append(leds)
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(LEDLockStatus())

keyboard.keymap = [[
    KC.ESC,  KC.F1,    KC.F2,   KC.F3,   KC.F4,  KC.F5, KC.F6,  KC.F7, KC.PSCR, KC.INS, KC.DEL,  KC.BSLS, KC.BSPC,
    KC.GRV,  KC.N1,    KC.N2,   KC.N3,   KC.N4,  KC.N5, KC.N6,  KC.N7, KC.N8,   KC.N9,  KC.N0,   KC.MINS, KC.EQL,
    KC.TAB,  KC.Q,     KC.W,    KC.E,    KC.R,   KC.T,  KC.Y,   KC.U,  KC.I,    KC.O,   KC.P,    KC.LBRC, KC.RBRC,
    KC.CAPS, KC.A,     KC.S,    KC.D,    KC.F,   KC.G,  KC.H,   KC.J,  KC.K,    KC.L,   KC.SCLN, KC.QUOT, KC.ENT,
    KC.LSFT, KC.Z,     KC.X,    KC.C,    KC.V,   KC.B,  KC.N,   KC.M,  KC.COMM, KC.DOT, KC.SLSH, KC.UP,   KC.RSFT,
    KC.LCTL, KC.MO(1), KC.LGUI, KC.LALT, KC.SPC, KC.NO, KC.SPC, KC.NO, KC.HOME, KC.END, KC.LEFT, KC.DOWN, KC.RGHT,
],[
	KC.ESC,  KC.MUTE, KC.VOLD, KC.VOLU, KC.BRID, KC.BRIU, KC.F6,  KC.F7, KC.PSCR, KC.SLCK, KC.DEL,  KC.BSLS, KC.BSPC,
    KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.F8,  KC.F9, KC.F10,  KC.F11,  KC.F12,  KC.MINS, KC.EQL,
    KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,   KC.U,  KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC,
    KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,   KC.J,  KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,
    KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,   KC.M,  KC.COMM, KC.DOT,  KC.SLSH, KC.PGUP, KC.RSFT,
    KC.LCTL, KC.TRNS, KC.LGUI, KC.LALT, KC.SPC,  KC.NO,   KC.SPC, KC.NO, KC.HOME, KC.END,  KC.LEFT, KC.PGDN, KC.RGHT,
]]

if __name__ == '__main__':
    keyboard.go()
