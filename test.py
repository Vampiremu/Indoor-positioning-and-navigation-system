import serial
from com import Comd

# ser = serial.Serial("COM10", 115200)
# flag = b'\x7e'
#
# if ser.is_open:
#     print(1)
# com = [0xbb, 0x00, 0x03, 0x00, 0x01, 0x00, 0x04, 0x7e]
# for st in com:
#     sts = str(hex(st))
#     sts = sts[2]+sts[3]
#     print(sts)
#     data = bytes.fromhex(sts)
#     ser.write(data)
# ser.write(b'\xbb\x00\x27\x00\x03\x22\x00\x05\x51\x7e')
# while True:
#     recv = ser.read(1)
#     print(recv)
#     if recv == flag:
#         break

com = Comd()

tt = 0x7e

tr = com.Character_conversion(tt)
print(tr)
