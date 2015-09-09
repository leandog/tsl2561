def readRaw8(device, handle):
    """Read an 8-bit value on the bus (without register)."""
    result = device.i2c_read_byte(handle) & 0xFF
    return result

def readU8(device, handle, register):
    """Read an unsigned byte from the specified register."""
    result = device.i2c_read_byte_data(handle, register) & 0xFF
    return result

def readS8(device, handle, register):
    """Read a signed byte from the specified register."""
    result = readU8(device, handle, register)
    if result > 127:
        result -= 256
    return result

def readU16(device, handle, register, little_endian=True):
    """Read an unsigned 16-bit value from the specified register, with the
    specified endianness (default little endian, or least significant byte
    first)."""
    result = device.i2c_read_word_data(handle, register) & 0xFFFF
    # Swap bytes if using big endian because read_word_data assumes little
    # endian on ARM (little endian) systems.
    if not little_endian:
        result = ((result << 8) & 0xFF00) + (result >> 8)
    return result

def readS16(device, handle, register, little_endian=True):
    """Read a signed 16-bit value from the specified register, with the
    specified endianness (default little endian, or least significant byte
    first)."""
    result = readU16(device, handle, register, little_endian)
    if result > 32767:
        result -= 65536
    return result

def readU16LE(device, handle, register):
    """Read an unsigned 16-bit value from the specified register, in little
    endian byte order."""
    return readU16(device, handle, register, little_endian=True)

def readU16BE(device, handle, register):
    """Read an unsigned 16-bit value from the specified register, in big
    endian byte order."""
    return readU16(device, handle, register, little_endian=False)

def readS16LE(device, handle, register):
    """Read a signed 16-bit value from the specified register, in little
    endian byte order."""
    return readS16(device, handle, register, little_endian=True)

def readS16BE(device, handle, register):
    """Read a signed 16-bit value from the specified register, in big
    endian byte order."""
    return readS16(device, handle, register, little_endian=False)

def writeRaw8(device, handle, value):
    """Write an 8-bit value on the bus (without register)."""
    value = value & 0xFF
    device.i2c_write_byte(handle, value)

def write8(device, handle, register, value):
    """Write an 8-bit value to the specified register."""
    value = value & 0xFF
    device.i2c_write_byte_data(handle, register, value)

def write16(device, handle, register, value):
    """Write a 16-bit value to the specified register."""
    value = value & 0xFFFF
    device.i2c_write_word_data(handle, register, value)

def writeList(device, handle, register, data):
    """Write bytes to the specified register."""
    device.i2c_write_block_data(handle, register, data)

def readList(device, handle, register, length):
    """Read a length number of bytes from the specified register.  Results
    will be returned as a bytearray."""
    results = device.i2c_read_block_data(handle, register, length)
    return results

