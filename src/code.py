import board
import displayio
import terminalio
import time
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import adafruit_scd4x

delay_sec = 0.5
oled_width = 128
oled_height = 64
border = 1

i2c = board.I2C()

displayio.release_displays()
oled_bus = displayio.I2CDisplay(i2c, device_address=0x3D)
oled = adafruit_displayio_ssd1306.SSD1306(
    oled_bus, width=oled_width, height=oled_height
)
scd4x = adafruit_scd4x.SCD4X(i2c)

print("initializing sensors...")
scd4x.start_periodic_measurement()

splash = displayio.Group()
oled.show(splash)

color_bitmap = displayio.Bitmap(oled_width, oled_height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(oled_width - border * 2, oled_height - border * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=border, y=border
)
splash.append(inner_sprite)

# Draw a label
text = "initializing..."
text_area = label.Label(
    terminalio.FONT, text=text, color=0xFFFFFF, x=4, y=oled_height // 2 - 1
)
splash.append(text_area)

while True:
    if scd4x.data_ready:
        # plot the data point(s)
        splash.pop()
        temp_f = scd4x.temperature * 1.8 + 32
        text = f"Temp: %0.1f *F\nRel. Humid.: %0.1f %%\nCO2: %d ppm" % (
            temp_f,
            scd4x.relative_humidity,
            scd4x.CO2,
        )
        text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=4, y=14)
        splash.append(text_area)
        print((scd4x.CO2, scd4x.temperature, scd4x.relative_humidity))
    time.sleep(delay_sec)
