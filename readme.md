This Program is a Simple Circuitpython script, which <br />
lets you play Ping Pong on a Matrix.<br />
<br />
The components you will need: <br />
        4 | Buttons / other devices to make inputs<br />
        1 | 8x8 LED Matrix using a max7219 chip<br />
        4 | 1K-Ohm Resistors<br />
      16 | Jumper wires or more, depending on how <br />organized you want to build it up<br />
        1 | Interrupt button, to stop the program<br />

Wire Setup with the defined pins in my script:<br />
      GP2   Interrupt button - Plus Pin<br />
      GP3   Interrupt button - Signal Pin<br />
      GND  Interrupt button - Minus Pin<br />
      VSYS LED Matrix - VCC Pin<br />
      GP9   LED Matrix - CS Pin<br />
      GP10 LED Matrix - CLK Pin<br />
      GP11 LED Matrix - DIN Pin<br />
      GND   LED Matrix - GND Pin<br />
      3V3(OUT) ALL Buttons - Plus side for button paired with a resistor each<br />
      GP18 Left Player Up Button - Diagonal to the Plus paired pin<br />
      GP19 Left Player Down Button - Diagonal to the Plus paired pin <br />
      GP20 Right Player Up Button - Diagonal to the Plus paired pin <br />
      GP21 Right Player Down Button - Diagonal to the Plus paired pin <br />
<br />
      The Game operates with 1 tick per second.