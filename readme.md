This Program is a Simple Circuitpython script, which lets you play Ping Pong on a Matrix.

The components you will need: 
        4 | Buttons / other devices to make inputs
        1 | 8x8 LED Matrix using a max7219 chip
        4 | 1K-Ohm Resistors
      16 | Jumper wires or more, depending on how organized you want to build it up
        1 | Interrupt button, to stop the program

Wire Setup with the defined pins in my script:
      GP2   Interrupt button - Plus Pin
      GP3   Interrupt button - Signal Pin
      GND  Interrupt button - Minus Pin
      VSYS LED Matrix - VCC Pin
      GP9   LED Matrix - CS Pin
      GP10 LED Matrix - CLK Pin
      GP11 LED Matrix - DIN Pin
      GND   LED Matrix - GND Pin
      3V3(OUT) ALL Buttons - Plus side for button paired with a resistor each
      GP18 Left Player Up Button - Diagonal to the Plus paired pin
      GP19 Left Player Down Button - Diagonal to the Plus paired pin 
      GP20 Right Player Up Button - Diagonal to the Plus paired pin 
      GP21 Right Player Down Button - Diagonal to the Plus paired pin 

      The Game operates with 1 tick per second.