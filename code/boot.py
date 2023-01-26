import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid

#GP3与GP4连接到电子锁的1,7号引脚，当插入键盘且1,7号引脚导通时，键盘将不禁用USB储存器和串口（可编程模式）
#理论上，GP3和GP4可以换成键盘上按键所对应的引脚以实现按住某按键插入键盘进入可编程模式的效果
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
