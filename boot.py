import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid

pin1 = digitalio.DigitalInOut(board.GP4)
pin2 = digitalio.DigitalInOut(board.GP3)
pin1.switch_to_output(value=True)
pin2.switch_to_input(pull=digitalio.Pull.DOWN)

if not pin2.value:
    storage.disable_usb_drive()
    # Equivalent to usb_cdc.enable(console=False, data=False)
    usb_cdc.disable()
    usb_hid.enable(boot_device=1)

pin1.deinit()
pin2.deinit()
