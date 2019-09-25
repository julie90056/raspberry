from lcd_display import lcd

List= [Raspberry Pi, Hello, Julie]


my_lcd = lcd()

for i in range(3):
    print("", List[i])
    my_lcd.display_string(" ", List[i])

