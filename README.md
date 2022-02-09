
## Utility to find CRC32 checksum tables or entries in a binary read from a SPI/I2C NOR flash 

When we dump a flash memory in an embedded device we would like to check whether the binary has stored an CRC32 checksum with it. The checksum can be either in a table or an entry after each block/sector/page. 

### How it works:

1. The utility will read the given binary contents in block/sector/pages.
2. The utility will bruteforce/search for a CRC32 checksum value in each block/sector/pages and returns "-1" or "0" when a match crc32 value is found.

For example, the tool here was written for a GD25VE16C SPI NOR flash(16Mb/2MB). The datasheeet of the flash memory mentions the memory organization and how the Block/Sector/Page size is defined.

The memory organization for the above example is,

* Each Device has - 2M bytes
* Each Block has - 64K/32K bytes
* Each Sector has - 4K bytes
* Each Page has - 256 bytes

So the value defined in the script(Line 11-13) is, 

* page_size = 0xFF  #256 bytes
* sector_size = 0xFFF  #4095 bytes
* block_size = 0xFFFF  #65535 bytes

### How to use:

1. Add the binary name to be checked in the crc32_check.py - Line 7. 
2. Verify/Change the memory organization as per the target memory you want to check the crc entries - Line 11-13. 
3. Install the python library requirements.
4. Run the tool. 
``` 
python3 crc32_check.py
```
### Demo

![](crc32_check.gif)


