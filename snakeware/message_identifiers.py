from enum import Enum


class MessageIdentifier(int, Enum):
    UNKNOWN = -1
    NOTIFICATION = 7
    BURNIN_FW = 8
    START_SESSION = 257
    STOP_SESSION = 258
    RESET_VF = 259
    STOP_VF = 260
    SET_CLNT_INFO = 261
    RECORD_START = 513
    RECORD_STOP = 514
    MEDIA_INFO = 1026
    LS = 1282
    CD = 1283
    GET_FILE = 1285
    PUT_FILE = 1286
    CANCEL_FILE_XFER = 1287
    WIFI_RESET = 1537
    SET_WIFI_SETTING = 1538
    GET_WIFI_SETTING = 1539
    SET_STATUS = 2049
    GET_STATUS = 2050
    ALIVE_TICK = 2051
    APP_CONNECT = 2052
    APP_DISCONNECT = 2053
    APP_SWITCH_TO_MAIN = 2054
    APP_SWITCH_TO_SUB = 2055
    WIFI_RESTART = 2056
    MAKE_THUMBNAIL = 2057
    APP_SWITCH_TO_THUMB = 2058
    DB_LOCK = 2059
    DB_UNLOCK = 2060
    GET_DRIVING_DATA_LIST = 2061
    AP_INFO = 2070
    AP_CONNECT = 2071
    SCAN_INFO = 2072
    SCAN_CONNECT = 2073
