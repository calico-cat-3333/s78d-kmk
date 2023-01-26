# 使用YD-RP2040和KMK固件改造S78D键盘

## 文件说明

`code/`：code.py和boot.py

`keycap/`：键帽夹纸设计

`s78d.jpg`：S78D键盘板电路接线图

`2023-01-16-225507_1920x1080_scrot.png`：上图出处的截图

`yd-rp2040.png`：YD-RP2040引脚图

## 有用的链接

KMK官网[http://kmkfw.io/](http://kmkfw.io/)

KMK Github储存库[https://github.com/KMKfw/kmk\_firmware](https://github.com/KMKfw/kmk_firmware)

CircuitPython官网[https://circuitpython.org/](https://circuitpython.org/)

## 有用的提示

参考[https://docs.circuitpython.org/en/latest/shared-bindings/microcontroller/index.html](https://docs.circuitpython.org/en/latest/shared-bindings/microcontroller/index.html)，可以通过进入REPL后执行以下代码重启到UF2模式以便更新CircuitPython

```
import microcontroller
microcontroller.on_next_reset(microcontroller.RunMode.UF2)
microcontroller.reset()
```
