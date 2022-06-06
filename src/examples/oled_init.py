import board
import displayio
import adafruit_displayio_ssd1306

i2c = board.I2C()
# dir(i2c): ['__class__', '__enter__', '__exit__', 'deinit', 'readfrom_into', 'scan', 'try_lock', 'unlock', 'writeto', 'writeto_then_readfrom']

displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
# dir(displayio): ['__class__', '__name__', 'Bitmap', 'ColorConverter', 'Colorspace', 'Display', 'EPaperDisplay', 'FourWire', 'Group', 'I2CDisplay', 'OnDiskBitmap', 'Palette', 'ParallelBus', 'Shape', 'TileGrid', 'release_displays']
# dir(display_bus): ['__class__', 'send', 'reset']

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
# dir(display): ['__class__', '__init__', '__module__', '__qualname__', '__dict__', 'auto_brightness', 'auto_refresh', 'brightness', 'bus', 'fill_row', 'height', 'refresh', 'root_group', 'rotation', 'show', 'sleep', 'width', 'is_awake', 'wake', '_is_awake']

print("Hello world")
