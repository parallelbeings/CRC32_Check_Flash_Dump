
import binascii
import struct

filename = "sample.bin"

#Define Memory organization for Flash IC


page_size = 0xFF  # 256 bytes
sector_size = 0xFFF  # 4095 bytes
block_size = 0xFFFF  # 65535 bytes


# Check CRC32 for each block

def calculate_crc_block():
    for i in range(0, 0x1fffff, 0x10000):  # Block 0 starting at address 0 to 0xffff
        f = open(filename, "rb")

        offset = i

        # Set offset for every iteration
        f.seek(offset, 1)

        # Read from file at address offset
        output = f.read(block_size)

        # Calculate CRC for each block
        crc = binascii.crc32(output)

        hex_out = hex(crc)[2:]

        # Some time CRC32 output is less than 8 bytes, So do the check
        length = len(hex_out)

        if length == 6:
            hex_out = hex_out + '00'
        elif length == 7:
            hex_out = hex_out + '0'

        check = bytearray.fromhex(hex_out)

        # print(check)

        # Open the file again and check whether the Calculated CRC is found - return -1 if not found, else position

        f = open(filename, "rb")
        s = f.read()
        out = s.find(check)

        print("CRC32 for address range:", hex(offset), " - ", hex(offset + block_size), ":", "CRC checksum:", ":",
              hex_out,  ": Match Found:", out)


def calculate_crc_sector():
    for i in range(0, 0x1fffff, 0x1000):  # Block 0 starting at address 0 to 0xffff
        f = open(filename, "rb")
        offset = i

        # Set offset for every iteration
        f.seek(offset, 1)

        # Read from file at address offset
        output = f.read(sector_size)

        # Calculate CRC for each block
        crc = binascii.crc32(output)

        hex_out = hex(crc)[2:]

        # Some time CRC32 output is less than 8 bytes, So do the check
        length = len(hex_out)

        if length == 6:
            hex_out = hex_out + '00'
        elif length == 7:
            hex_out = hex_out + '0'

        check = bytes.fromhex(hex_out)

        # Open the file again and check whether the Calculated CRC is found - return -1 if not found, else position

        f = open(filename, "rb")
        s = f.read()
        out = s.find(check)

        # if out == -1:
        print("CRC32 for address range:", hex(offset), " - ", hex(offset + sector_size), ":", "CRC checksum:", ":",
              hex_out, ": Match Found:", out)


def calculate_crc_page():
    for i in range(0, 0x1fffff, 0x100):  # Block 0 starting at address 0 to 0xffff
        f = open(filename, "rb")
        offset = i

        # Set offset for every iteration
        f.seek(offset, 1)

        # Read from file at address offset
        output = f.read(page_size)

        # Calculate CRC for each block
        crc = binascii.crc32(output)

        hex_out = hex(crc)[2:]

        # Some time CRC32 output is less than 8 bytes, So do the check
        length = len(hex_out)

        if length == 6:
            hex_out = hex_out + '00'
        elif length == 7:
            hex_out = hex_out + '0'

        check = bytes.fromhex(hex_out.replace(' ', ''))
        # print(check)

        # Open the file again and check whether the Calculated CRC is found - return -1 if not found, else position

        f = open(filename, "rb")
        s = f.read()
        out = s.find(check)

        # if out == 0:
        print("CRC32 for address range:", hex(offset), " - ", hex(offset + page_size), ":", "CRC checksum:", ":", hex_out,
              ": Match Found:", out)


print("-------------------------------------------------------------------------------")
print("Calculate CRC for each Block and check whether the CRC is present inside the image")
print("-------------------------------------------------------------------------------")
calculate_crc_block()

print("-------------------------------------------------------------------------------")
print("Calculate CRC for each Sector and check whether the CRC is present inside the image ")
print("-------------------------------------------------------------------------------")
calculate_crc_sector()

print("-------------------------------------------------------------------------------")
print("Calculate CRC for each Page and check whether the CRC is present inside the image")
print("-------------------------------------------------------------------------------")
calculate_crc_page()