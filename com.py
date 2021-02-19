
class Comd:
    def __init__(self):
        super(Comd, self).__init__()

        self.CMD_HELLO = 0x01
        self.CMD_HEART_BEAT = 0x02
        self.CMD_GET_MODULE_INFO = 0x03
        self.CMD_SINGLE_ID = 0x22
        self.CMD_MULTI_ID = 0x27
        self.CMD_STOP_MULTI = 0x28
        self.CMD_READ_DATA = 0x39
        self.CMD_WRITE_DATA = 0x49
        self.CMD_LOCK_UNLOCK = 0x82
        self.CMD_KILL = 0x65
        self.CMD_SET_REGION = 0x07
        self.CMD_INSERT_FHSS_CHANNEL = 0xA9
        self.CMD_GET_RF_CHANNEL = 0xbb
        self.CMD_SET_RF_CHANNEL = 0xAB
        self.CMD_SET_CHN2_CHANNEL = 0xAF
        self.CMD_SET_US_CHANNEL = 0xAC
        self.CMD_OPEN_PA = 0xAE
        self.CMD_SET_FHSS = 0xAD
        self.CMD_SET_POWER = 0xB6
        self.CMD_GET_POWER = 0xB7
        self.CMD_GET_SELECT_PARA = 0x0B
        self.CMD_SET_SELECT_PARA = 0x0C
        self.CMD_GET_QUERY_PARA = 0x0D
        self.CMD_SET_QUERY_PARA = 0x0E
        self.CMD_SET_CW = 0xB0
        self.CMD_SET_BLF = 0xBF
        self.CMD_FAIL = 0xFF
        self.CMD_SUCCESS = 0x00
        self.CMD_SET_SFR = 0xFE
        self.CMD_READ_SFR = 0xFD
        self.CMD_INIT_SFR = 0xEC
        self.CMD_CAL_MX = 0xEA
        self.CMD_CAL_LPF = 0xED
        self.CMD_READ_MEM = 0xFB
        self.CMD_SET_INV_MODE = 0x12
        self.CMD_SET_UART_BAUDRATE = 0x11
        self.CMD_SCAN_JAMMER = 0xF2
        self.CMD_SCAN_RSSI = 0xF3
        self.CMD_AUTO_ADJUST_CH = 0xF4
        self.CMD_SET_MODEM_PARA = 0xF0
        self.CMD_READ_MODEM_PARA = 0xF1
        self.CMD_SET_ENV_MODE = 0xF5
        self.CMD_TEST_RESET = 0x55
        self.CMD_POWERDOWN_MODE = 0x17
        self.CMD_SET_SLEEP_TIME = 0x1D
        self.CMD_IO_CONTROL = 0x1A
        self.CMD_RESTART = 0x19
        self.CMD_LOAD_NV_CONFIG = 0x0A
        self.CMD_SAVE_NV_CONFIG = 0x09
        self.CMD_ENABLE_FW_ISP_UPDATE = 0x1F
        self.CMD_SET_READ_ADDR = 0x14

    def Character_conversion(self, bf_str):         #十六进制整形转换为bytes
        aft_str = hex(bf_str)
        if len(aft_str) == 3:
            aft_str = '0' + aft_str[2]
        elif len(aft_str) == 4:
            aft_str = aft_str[2] + aft_str[3]
        aft_str = bytes.fromhex(aft_str)
        return aft_str
