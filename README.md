# MCP23017 Library
Easy to use library for the MCP23017 connected to a Raspberry Pi.

### Installation

i2c is required to be enabled in order to communicate with the chip. Also install these packages:

```sh
$ sudo apt-get install python-smbus i2c-tools
```

### Usage

This library aims at being very similar to the RPi.GPIO library. At the moment it provides the following functions:

`start(address)`: Starts the library on the specified chip address.
`setup(pin, mode, pullupEnable)`: Writes direction (IN, OUT) to the specified pin. `pullupEnable` enables the internal 100k pullup resistor. Optional, and only works when setting a pin as an input. Valid values are PUHIGH and PULOW.

`output(pin, dir)`: Writes state (HIGH, LOW) to the specified pin.
`input(pin)`: Reads and returns pin state (True, False)

`puRead(bank)`: Reads and returns the pullup registers from both GPIO banks.
   * Valid parameter values: **PU_A**, **PU_B**, **ALL** or leave blank for a default graphic diagram of both banks.

`dirRead(bank)`: Reads and returns the direction registers from both GPIO banks.
   * Valid parameter values: **BANK_A**, **BANK_B**, **ALL** or leave blank for a default graphic diagram of both banks.

`latRead(bank)`: Reads and returns the latch registers from both GPIO banks.
   * Valid parameter values: **LAT_A**, **LAT_B**, **ALL** or leave blank for a default graphic diagram of both banks.

Please refer to the image below for the pin mapping.

### Constant list

 * MCP.OUT = 1
 * MCP.IN = 0
 * MCP.BANK_A = 0
 * MCP.BANK_B = 1
 * MCP.ALL = 2
 * MCP.LAT_A = 3
 * MCP.LAT_B = 4
 * MCP.PU_A = 5
 * MCP.PU_B = 6
 * MCP.HIGH = 1
 * MCP.LOW = 0
 * MCP.PUHIGH = 1
 * MCP.PULOW = 0

### Pinout

Pins are mapped according to this diagram:

![Diagram](pinmap.png)

### Code example

This example will set pin #2 as an input, with the pullup resistor enabled and #1 as an output.
When the input goes `high`, pin #1 will also go high.

```py
import mcp23017_lib as MCP

MCP.start(0x26)

MCP.setup(2, MCP.IN, MCP.PUHIGH)
MCP.setup(1, MCP.OUT)

while 1:
   if(MCP.read(2)):
      MCP.write(1, MCP.HIGH)
   else:
      MCP.write(1, MCP.LOW)
```

### TODO list

 - [x] ~~Do not use hardcoded i2c address~~
 - [x] ~~Add pullup function~~
 - [ ] Add raw write function
 - [x] ~~Finish function documentation~~

### Contributors

Development:
 *  [@ResonantWave](https://github.com/ResonantWave)

### Contributing

* The code is licensed under the [GPL V3](LICENSE)
* Feel free to contribute to the code
