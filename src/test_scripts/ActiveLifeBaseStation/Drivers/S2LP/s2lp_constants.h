/*
 * s2lp_constants.h
 *
 *  Created on: Jul 14, 2021
 *      Author: phoen
 */

#ifndef S2LP_S2LP_CONSTANTS_H_
#define S2LP_S2LP_CONSTANTS_H_

// Datarate helper constants
#define S2LP_DATARATE_EXPONENT_MIN 0
#define S2LP_DATARATE_EXPONENT_MAX 15
#define S2LP_DATARATE_EXPONENT_INVALID 0xFF
#define S2LP_DATARATE_MANTISSA_MIN 0
#define S2LP_DATARATE_MANTISSA_MAX 65535
#define S2LP_DATARATE_MIN 100
#define S2LP_DATARATE_MAX 500000

// Frequency deviation helper constants
#define S2LP_FDEV_EXPONENT_MIN 0
#define S2LP_FDEV_EXPONENT_MAX 15
#define S2LP_FDEV_EXPONENT_INVALID 0xFF
#define S2LP_FDEV_MANTISSA_MIN 0
#define S2LP_FDEV_MANTISSA_MAX 255

typedef enum S2LP_Pins_t {
	S2LP_PIN_GPIO_0, S2LP_PIN_GPIO_1, S2LP_PIN_GPIO_2, S2LP_PIN_GPIO_3, S2LP_PIN_SDN, S2LP_PIN_CSN,
} S2LP_Pin;

typedef enum S2LP_PinMode_t {
	S2LP_PINMODE_ANALOG = 0b00, S2LP_PINMODE_INPUT = 0b01, S2LP_PINMODE_OUTPUT_LP = 0b10, S2LP_PINMODE_OUTPUT_HP = 0b11
} S2LP_PinMode;

typedef enum S2LP_State_t {
	S2LP_STATE_SHUTDOWN = 0xFF,
	S2LP_STATE_STANDBY = 0x02,
	S2LP_STATE_SLEEP_A = 0x01,
	S2LP_STATE_SLEEP_B = 0x03,
	S2LP_STATE_READY = 0x00,
	S2LP_STATE_LOCK = 0x0C,
	S2LP_STATE_RX = 0x30,
	S2LP_STATE_TX = 0x5C,
	S2LP_STATE_SYNTH_SETUP = 0x50
} S2LP_State;

typedef enum S2LP_ClockFrequency_t {
	S2LP_CLOCK_FREQ_INVALID,
	S2LP_CLOCK_FREQ_24MHZ,
	S2LP_CLOCK_FREQ_25MHZ,
	S2LP_CLOCK_FREQ_26MHZ,
	S2LP_CLOCK_FREQ_48MHZ,
	S2LP_CLOCK_FREQ_50MHZ,
	S2LP_CLOCK_FREQ_52MHZ
} S2LP_ClockFrequency;

typedef enum S2LP_SMPS_Voltage_t {
	S2LP_SMPS_1_2V = 0b001,
	S2LP_SMPS_1_3V = 0b010,
	S2LP_SMPS_1_4V = 0b011,
	S2LP_SMPS_1_5V = 0b100,
	S2LP_SMPS_1_6V = 0b101,
	S2LP_SMPS_1_7V = 0b110,
	S2LP_SMPS_1_8V = 0b111
} S2LP_SMPS_Voltage;

typedef enum S2LP_SMPS_Level_Mode_t {
	S2LP_SMPS_LEVEL_RX_TX = 0, S2LP_SMPS_LEVEL_TX = 1
} S2LP_SMPS_Level_Mode;

typedef enum S2LP_Sleep_Mode_t {
	S2LP_SLEEP_A = 0, S2LP_SLEEP_B = 1
} S2LP_Sleep_Mode;

typedef enum S2LP_ChargePumpCurrent_t {
	S2LP_CHARGE_PUMP_120UA,
	S2LP_CHARGE_PUMP_200UA,
	S2LP_CHARGE_PUMP_140UA,
	S2LP_CHARGE_PUMP_240UA,
	S2LP_CHARGE_PUMP_INVALID
} S2LP_ChargePumpCurrent;

typedef enum S2LP_SynthesizerBand_t {
	S2LP_SYNTH_BAND_HIGH = 0, S2LP_SYNTH_BAND_MID = 1
} S2LP_SynthesizerBand;

typedef enum S2LP_Modulation_t {
	S2LP_MODULATION_2FSK = 0,
	S2LP_MODULATION_4FSK = 1,
	S2LP_MODULATION_2GFSK = 2,
	S2LP_MODULATION_4GFSK = 3,
	S2LP_MODULATION_ASK_OOK = 5,
	S2LP_MODULATION_DIRECT = 6,
	S2LP_MODULATION_NONE = 7,
	S2LP_MODULATION_2GFSK_UNSHAPED = 10,
	S2LP_MODULATION_4GFSK_UNSHAPED = 12
} S2LP_Modulation;

typedef enum S2LP_CS_Mode_t {
	S2LP_CS_STATIC = 0, S2LP_CS_DYNAMIC_6DB = 1, S2LP_CS_DYNAMIC_12DB = 2, S2LP_CS_DYNAMIC_18DB = 3
} S2LP_CS_Mode;

typedef enum S2LP_AFC_Mode_t {
	S2LP_AFC_SLICER_CORRECTION = 0, S2LP_AFC_2ND_IF_CORRECTION = 1
} S2LP_AFC_Mode;

typedef enum S2LP_AGC_Low_Threshold_t {
	S2LP_AGC_LOW_THRESHOLD_0 = 0, S2LP_AGC_LOW_THRESHOLD_1 = 1
} S2LP_AGC_Low_Threshold;

typedef enum S2LP_Command_t {
	S2LP_CMD_TX = 0x60,
	S2LP_CMD_RX = 0x61,
	S2LP_CMD_READY = 0x62,
	S2LP_CMD_STANDBY = 0x63,
	S2LP_CMD_SLEEP = 0x64,
	S2LP_CMD_LOCKRX = 0x65,
	S2LP_CMD_LOCKTX = 0x66,
	S2LP_CMD_SABORT = 0x67,
	S2LP_CMD_LDC_RELOAD = 0x68,
	S2LP_CMD_SRES = 0x70,
	S2LP_CMD_FLUSHRXFIFO = 0x71,
	S2LP_CMD_FLUSHTXFIFO = 0x72,
	S2LP_CMD_SEQUENCE_UPDATE = 0x73
} S2LP_Command;

typedef enum S2LP_Preamble_t {
	S2LP_PREAMBLE_0 = 0, S2LP_PREAMBLE_1 = 1, S2LP_PREAMBLE_2 = 2, S2LP_PREAMBLE_3 = 3
} S2LP_Preamble;

typedef enum S2LP_Packet_Format_t {
	S2LP_PACKET_BASIC = 0, S2LP_PACKET_802_15_4G = 1, S2LP_PACKET_UART = 2, S2LP_PACKET_STACK = 3
} S2LP_Packet_Format;

typedef enum S2LP_Length_Field_Size_t {
	S2LP_PAYLOAD_LENGTH_1B = 1, S2LP_PAYLOAD_LENGTH_2B = 2
} S2LP_Length_Field_Size;

typedef enum S2LP_BLD_Threshold_t {
	S2LP_BLD_THRESH_2_7V = 0b00, S2LP_BLD_THRESH_2_5V = 0b01, S2LP_BLD_THRESH_2_3V = 0b10, S2LP_BLD_THRESH_2_1V = 0b11
} S2LP_BLD_Threshold;

typedef enum S2LP_TX_Source_t {
	S2LP_TX_SOURCE_NORMAL = 0, S2LP_TX_SOURCE_DIRECT_FIFO = 1, S2LP_TX_SOURCE_DIRECT_GPIO = 2, S2LP_TX_SOURCE_PN9 = 3,
} S2LP_TX_Source;

typedef enum S2LP_RX_Source_t {
	S2LP_RX_SOURCE_NORMAL = 0, S2LP_RX_SOURCE_DIRECT_FIFO = 1, S2LP_RX_SOURCE_DIRECT_GPIO = 2
} S2LP_RX_Source;

typedef enum S2LP_CRC_Mode_t {
	S2LP_CRC_NO_CRC = 0,
	S2LP_CRC_POLY_07 = 1,
	S2LP_CRC_POLY_8005 = 2,
	S2LP_CRC_POLY_1021 = 3,
	S2LP_CRC_POLY_864CFB = 4,
	S2LP_CRC_POLY_04C011BB7 = 5
} S2LP_CRC_Mode;

typedef enum S2LP_Data_Coding_t {
	S2LP_CODING_NONE, S2LP_CODING_FEC, S2LP_CODING_MANCHESTER, S2LP_CODING_3_OUT_OF_6,
} S2LP_Data_Coding;

typedef enum S2LP_Interrupt_t {
	S2LP_INT_RX_DATA_READY = 0,
	S2LP_INT_RX_DATA_DISCARDED = 1,
	S2LP_INT_TX_DATA_SENT = 2,
	S2LP_INT_MAX_RE_TX_REACHED = 3,
	S2LP_INT_CRC_ERROR = 4,
	S2LP_INT_TX_FIFO_ERROR = 5,
	S2LP_INT_RX_FIFO_ERROR = 6,
	S2LP_INT_TX_FIFO_ALMOST_FULL = 7,
	S2LP_INT_TX_FIFO_ALMOST_EMPTY = 8,
	S2LP_INT_RX_FIFO_ALMOST_FULL = 9,
	S2LP_INT_RX_FIFO_ALMOST_EMPTY = 10,
	S2LP_INT_MAX_BACK_OFF_CCA = 11,
	S2LP_INT_VALID_PREAMBLE_DETECTED = 12,
	S2LP_INT_SYNC_WORD_DETECTED = 13,
	S2LP_INT_RSSI_ABOVE_THRESHOLD = 14,
	S2LP_INT_WAKEUP_TIMEOUT_LDCR = 15,
	S2LP_INT_READY = 16,
	S2LP_INT_STANDBY_STATE_SWITCHING = 17,
	S2LP_INT_LOW_BATTERY = 18,
	S2LP_INT_POWER_ON_RESET = 19,
	S2LP_INT_RX_TIMER_TIMEOUT = 28,
	S2LP_INT_SNIFF_TIMER_TIMEOUT = 29
} S2LP_Interrupt;

typedef enum S2LP_FIFOSelect_t {
	S2LP_FIFO_RX = 0, S2LP_FIFO_TX = 1
} S2LP_FIFOSelect;

typedef enum S2LP_GPIO_Output_Mode_t {
	S2LP_GPIO_OUT_NIRQ = 0,
	S2LP_GPIO_OUT_POR_INVERTED = 1,
	S2LP_GPIO_OUT_WAKE_UP_EXPIRATION = 2,
	S2LP_GPIO_OUT_LOW_BATTERY_DETECTION = 3,
	S2LP_GPIO_OUT_TX_DATA_CLOCK_OUT = 4,
	S2LP_GPIO_OUT_TX_STATE_OUT = 5,
	S2LP_GPIO_OUT_FIFO_ALMOST_EMPTY = 6,
	S2LP_GPIO_OUT_FIFO_ALMOST_FULL = 7,
	S2LP_GPIO_OUT_RX_DATA_OUT = 8,
	S2LP_GPIO_OUT_RX_CLOCK_OUT = 9,
	S2LP_GPIO_OUT_RX_STATE_INDICATION = 10,
	S2LP_GPIO_OUT_NOT_IN_SLEEP_STANDBY = 11,
	S2LP_GPIO_OUT_IN_STANDBY = 12,
	S2LP_GPIO_OUT_ANTENNA_SWITCH = 13,
	S2LP_GPIO_OUT_PREAMBLE_DETECTED = 14,
	S2LP_GPIO_OUT_SYNC_WORD_DETECTED = 15,
	S2LP_GPIO_OUT_RSSI_ABOVE_THRESHOLD = 16,
	S2LP_GPIO_OUT_TX_RX_MODE_INDICATOR = 18,
	S2LP_GPIO_OUT_VDD = 19,
	S2LP_GPIO_OUT_GND = 20,
	S2LP_GPIO_OUT_EXTERNAL_SMPS_EN = 21,
	S2LP_GPIO_OUT_IN_SLEEP = 22,
	S2LP_GPIO_OUT_IN_READY = 23,
	S2LP_GPIO_OUT_IN_LOCK = 24,
	S2LP_GPIO_OUT_WAITING_FOR_LOCK_DETECTOR_OUT = 25,
	S2LP_GPIO_OUT_TX_DATA_OOK = 26,
	S2LP_GPIO_OUT_WAITING_FOR_READY2 = 27,
	S2LP_GPIO_OUT_WAITING_FOR_TIME_EXPIR = 28,
	S2LP_GPIO_OUT_WAITING_FOR_VCO_CALLIB = 29,
	S2LP_GPIO_OUT_SYNTH_CIRCUIT_ENABLED = 30,
	S2LP_GPIO_OUT_INVALID = 0xFF,
} S2LP_GPIO_Output_Mode;

typedef enum S2LP_GPIO_Input_Mode_t {
	S2LP_GPIO_IN_TX_CMD = 0,
	S2LP_GPIO_IN_RX_CMD = 1,
	S2LP_GPIO_IN_TX_IN = 2,
	S2LP_GPIO_IN_WAKEUP = 3,
	S2LP_GPIO_IN_EXT_CLOCK = 4,
	S2LP_GPIO_IN_INVALID = 0xFF,
} S2LP_GPIO_Input_Mode;

typedef enum S2LP_Register_t {
	S2LP_REG_GPIO0_CONF = 0x00,
	S2LP_REG_GPIO1_CONF = 0x01,
	S2LP_REG_GPIO2_CONF = 0x02,
	S2LP_REG_GPIO3_CONF = 0x03,
	S2LP_REG_SYNT3 = 0x05,
	S2LP_REG_SYNT2 = 0x06,
	S2LP_REG_SYNT1 = 0x07,
	S2LP_REG_SYNT0 = 0x08,
	S2LP_REG_IF_OFFSET_ANA = 0x09,
	S2LP_REG_IF_OFFSET_DIG = 0x0A,
	S2LP_REG_CHSPACE = 0x0C,
	S2LP_REG_CHNUM = 0x0D,
	S2LP_REG_MOD4 = 0x0E,
	S2LP_REG_MOD3 = 0x0F,
	S2LP_REG_MOD2 = 0x10,
	S2LP_REG_MOD1 = 0x11,
	S2LP_REG_MOD0 = 0x12,
	S2LP_REG_CHFLT = 0x13,
	S2LP_REG_AFC2 = 0x14,
	S2LP_REG_AFC1 = 0x15,
	S2LP_REG_AFC0 = 0x16,
	S2LP_REG_RSSI_FLT = 0x17,
	S2LP_REG_RSSI_TH = 0x18,
	S2LP_REG_AGCCTRL4 = 0x1A,
	S2LP_REG_AGCCTRL3 = 0x1B,
	S2LP_REG_AGCCTRL2 = 0x1C,
	S2LP_REG_AGCCTRL1 = 0x1D,
	S2LP_REG_AGCCTRL0 = 0x1E,
	S2LP_REG_ANT_SELECT_CONF = 0x1F,
	S2LP_REG_CLOCKREC2 = 0x20,
	S2LP_REG_CLOCKREC1 = 0x21,
	S2LP_REG_PCKTCTRL6 = 0x2B,
	S2LP_REG_PCKTCTRL5 = 0x2C,
	S2LP_REG_PCKTCTRL4 = 0x2D,
	S2LP_REG_PCKTCTRL3 = 0x2E,
	S2LP_REG_PCKTCTRL2 = 0x2F,
	S2LP_REG_PCKTCTRL1 = 0x30,
	S2LP_REG_PCKTLEN1 = 0x31,
	S2LP_REG_PCKTLEN0 = 0x32,
	S2LP_REG_SYNC3 = 0x33,
	S2LP_REG_SYNC2 = 0x34,
	S2LP_REG_SYNC1 = 0x35,
	S2LP_REG_SYNC0 = 0x36,
	S2LP_REG_QI = 0x37,
	S2LP_REG_PCKT_PSTMBL = 0x38,
	S2LP_REG_PROTOCOL2 = 0x39,
	S2LP_REG_PROTOCOL1 = 0x3A,
	S2LP_REG_PROTOCOL0 = 0x3B,
	S2LP_REG_FIFO_CONFIG3 = 0x3C,
	S2LP_REG_FIFO_CONFIG2 = 0x3D,
	S2LP_REG_FIFO_CONFIG1 = 0x3E,
	S2LP_REG_FIFO_CONFIG0 = 0x3F,
	S2LP_REG_PCKT_FLT_OPTIONS = 0x40,
	S2LP_REG_PCKT_FLT_GOALS4 = 0x41,
	S2LP_REG_PCKT_FLT_GOALS3 = 0x42,
	S2LP_REG_PCKT_FLT_GOALS2 = 0x43,
	S2LP_REG_PCKT_FLT_GOALS1 = 0x44,
	S2LP_REG_PCKT_FLT_GOALS0 = 0x45,
	S2LP_REG_TIMERS5 = 0x46,
	S2LP_REG_TIMERS4 = 0x47,
	S2LP_REG_TIMERS3 = 0x48,
	S2LP_REG_TIMERS2 = 0x49,
	S2LP_REG_TIMERS1 = 0x4A,
	S2LP_REG_TIMERS0 = 0x4B,
	S2LP_REG_CSMA_CONF3 = 0x4C,
	S2LP_REG_CSMA_CONF2 = 0x4D,
	S2LP_REG_CSMA_CONF1 = 0x4E,
	S2LP_REG_CSMA_CONF0 = 0x4F,
	S2LP_REG_IRQ_MASK3 = 0x50,
	S2LP_REG_IRQ_MASK2 = 0x51,
	S2LP_REG_IRQ_MASK1 = 0x52,
	S2LP_REG_IRQ_MASK0 = 0x53,
	S2LP_REG_FAST_RX_TIMER = 0x54,
	S2LP_REG_PA_POWER8 = 0x5A,
	S2LP_REG_PA_POWER7 = 0x5B,
	S2LP_REG_PA_POWER6 = 0x5C,
	S2LP_REG_PA_POWER5 = 0x5D,
	S2LP_REG_PA_POWER4 = 0x5E,
	S2LP_REG_PA_POWER3 = 0x5F,
	S2LP_REG_PA_POWER2 = 0x60,
	S2LP_REG_PA_POWER1 = 0x61,
	S2LP_REG_PA_POWER0 = 0x62,
	S2LP_REG_PA_CONFIG1 = 0x63,
	S2LP_REG_PA_CONFIG0 = 0x64,
	S2LP_REG_SYNTH_CONFIG2 = 0x65,
	S2LP_REG_VCO_CONFIG = 0x68,
	S2LP_REG_VCO_CALIBR_IN2 = 0x69,
	S2LP_REG_VCO_CALIBR_IN1 = 0x6A,
	S2LP_REG_VCO_CALIBR_IN0 = 0x6B,
	S2LP_REG_XO_RCO_CONF1 = 0x6C,
	S2LP_REG_XO_RCO_CONF0 = 0x6D,
	S2LP_REG_RCO_CALIBR_CONF3 = 0x6E,
	S2LP_REG_RCO_CALIBR_CONF2 = 0x6F,
	S2LP_REG_PM_CONF4 = 0x75,
	S2LP_REG_PM_CONF3 = 0x76,
	S2LP_REG_PM_CONF2 = 0x77,
	S2LP_REG_PM_CONF1 = 0x78,
	S2LP_REG_PM_CONF0 = 0x79,
	S2LP_REG_MC_STATE1 = 0x8D,
	S2LP_REG_MC_STATE0 = 0x8E,
	S2LP_REG_TX_FIFO_STATUS = 0x8F,
	S2LP_REG_RX_FIFO_STATUS = 0x90,
	S2LP_REG_RCO_CALIBR_OUT4 = 0x94,
	S2LP_REG_RCO_CALIBR_OUT3 = 0x95,
	S2LP_REG_RCO_CALIBR_OUT1 = 0x99,
	S2LP_REG_VCO_CALIBROUT0 = 0x9A,
	S2LP_REG_TX_PCKT_INFO = 0x9C,
	S2LP_REG_RX_PCKT_INFO = 0x9D,
	S2LP_REG_AFC_CORR = 0x9E,
	S2LP_REG_LINK_QUALIF2 = 0x9F,
	S2LP_REG_LINK_QUALIF1 = 0xA0,
	S2LP_REG_RSSI_LEVEL = 0xA2,
	S2LP_REG_RX_PCKT_LEN1 = 0xA4,
	S2LP_REG_RX_PCKT_LEN0 = 0xA5,
	S2LP_REG_CRC_FIELD3 = 0xA6,
	S2LP_REG_CRC_FIELD2 = 0xA7,
	S2LP_REG_CRC_FIELD1 = 0xA8,
	S2LP_REG_CRC_FIELD0 = 0xA9,
	S2LP_REG_RX_ADDRE_FIELD1 = 0xAA,
	S2LP_REG_RX_ADDRE_FIELD0 = 0xAB,
	S2LP_REG_RSSI_LEVEL_RUN = 0xEF,
	S2LP_REG_DEVICE_INFO1 = 0xF0,
	S2LP_REG_DEVICE_INFO0 = 0xF1,
	S2LP_REG_IRQ_STATUS3 = 0xFA,
	S2LP_REG_IRQ_STATUS2 = 0xFB,
	S2LP_REG_IRQ_STATUS1 = 0xFC,
	S2LP_REG_IRQ_STATUS0 = 0xFD,
	S2LP_ADDR_FIFO = 0xFF,
} S2LP_Register;

typedef enum S2LP_Register_DefaultValue_t {
	S2LP_REG_DEFAULT_GPIO0_CONF = 0x0A,
	S2LP_REG_DEFAULT_GPIO1_CONF = 0xA2,
	S2LP_REG_DEFAULT_GPIO2_CONF = 0xA2,
	S2LP_REG_DEFAULT_GPIO3_CONF = 0xA2,
	S2LP_REG_DEFAULT_SYNT3 = 0x42,
	S2LP_REG_DEFAULT_SYNT2 = 0x16,
	S2LP_REG_DEFAULT_SYNT1 = 0x27,
	S2LP_REG_DEFAULT_SYNT0 = 0x62,
	S2LP_REG_DEFAULT_IF_OFFSET_ANA = 0x2A,
	S2LP_REG_DEFAULT_IF_OFFSET_DIG = 0xB8,
	S2LP_REG_DEFAULT_CHSPACE = 0x3F,
	S2LP_REG_DEFAULT_CHNUM = 0x00,
	S2LP_REG_DEFAULT_MOD4 = 0x83,
	S2LP_REG_DEFAULT_MOD3 = 0x2B,
	S2LP_REG_DEFAULT_MOD2 = 0x77,
	S2LP_REG_DEFAULT_MOD1 = 0x03,
	S2LP_REG_DEFAULT_MOD0 = 0x93,
	S2LP_REG_DEFAULT_CHFLT = 0x23,
	S2LP_REG_DEFAULT_AFC2 = 0xC8,
	S2LP_REG_DEFAULT_AFC1 = 0x18,
	S2LP_REG_DEFAULT_AFC0 = 0x25,
	S2LP_REG_DEFAULT_RSSI_FLT = 0xE3,
	S2LP_REG_DEFAULT_RSSI_TH = 0x28,
	S2LP_REG_DEFAULT_AGCCTRL4 = 0x54,
	S2LP_REG_DEFAULT_AGCCTRL3 = 0x10,
	S2LP_REG_DEFAULT_AGCCTRL2 = 0x22,
	S2LP_REG_DEFAULT_AGCCTRL1 = 0x59,
	S2LP_REG_DEFAULT_AGCCTRL0 = 0x8C,
	S2LP_REG_DEFAULT_ANT_SELECT_CONF = 0x45,
	S2LP_REG_DEFAULT_CLOCKREC2 = 0xC0,
	S2LP_REG_DEFAULT_CLOCKREC1 = 0x58,
	S2LP_REG_DEFAULT_PCKTCTRL6 = 0x80,
	S2LP_REG_DEFAULT_PCKTCTRL5 = 0x10,
	S2LP_REG_DEFAULT_PCKTCTRL4 = 0x00,
	S2LP_REG_DEFAULT_PCKTCTRL3 = 0x20,
	S2LP_REG_DEFAULT_PCKTCTRL2 = 0x00,
	S2LP_REG_DEFAULT_PCKTCTRL1 = 0x2C,
	S2LP_REG_DEFAULT_PCKTLEN1 = 0x00,
	S2LP_REG_DEFAULT_PCKTLEN0 = 0x14,
	S2LP_REG_DEFAULT_SYNC3 = 0x88,
	S2LP_REG_DEFAULT_SYNC2 = 0x88,
	S2LP_REG_DEFAULT_SYNC1 = 0x88,
	S2LP_REG_DEFAULT_SYNC0 = 0x88,
	S2LP_REG_DEFAULT_QI = 0x01,
	S2LP_REG_DEFAULT_PCKT_PSTMBL = 0x00,
	S2LP_REG_DEFAULT_PROTOCOL2 = 0x40,
	S2LP_REG_DEFAULT_PROTOCOL1 = 0x00,
	S2LP_REG_DEFAULT_PROTOCOL0 = 0x08,
	S2LP_REG_DEFAULT_FIFO_CONFIG3 = 0x30,
	S2LP_REG_DEFAULT_FIFO_CONFIG2 = 0x30,
	S2LP_REG_DEFAULT_FIFO_CONFIG1 = 0x30,
	S2LP_REG_DEFAULT_FIFO_CONFIG0 = 0x30,
	S2LP_REG_DEFAULT_PCKT_FLT_OPTIONS = 0x40,
	S2LP_REG_DEFAULT_PCKT_FLT_GOALS4 = 0x00,
	S2LP_REG_DEFAULT_PCKT_FLT_GOALS3 = 0x00,
	S2LP_REG_DEFAULT_PCKT_FLT_GOALS2 = 0x00,
	S2LP_REG_DEFAULT_PCKT_FLT_GOALS1 = 0x00,
	S2LP_REG_DEFAULT_PCKT_FLT_GOALS0 = 0x00,
	S2LP_REG_DEFAULT_TIMERS5 = 0x01,
	S2LP_REG_DEFAULT_TIMERS4 = 0x00,
	S2LP_REG_DEFAULT_TIMERS3 = 0x01,
	S2LP_REG_DEFAULT_TIMERS2 = 0x00,
	S2LP_REG_DEFAULT_TIMERS1 = 0x01,
	S2LP_REG_DEFAULT_TIMERS0 = 0x00,
	S2LP_REG_DEFAULT_CSMA_CONF3 = 0x4C,
	S2LP_REG_DEFAULT_CSMA_CONF2 = 0x00,
	S2LP_REG_DEFAULT_CSMA_CONF1 = 0x04,
	S2LP_REG_DEFAULT_CSMA_CONF0 = 0x00,
	S2LP_REG_DEFAULT_IRQ_MASK3 = 0x00,
	S2LP_REG_DEFAULT_IRQ_MASK2 = 0x00,
	S2LP_REG_DEFAULT_IRQ_MASK1 = 0x00,
	S2LP_REG_DEFAULT_IRQ_MASK0 = 0x00,
	S2LP_REG_DEFAULT_FAST_RX_TIMER = 0x28,
	S2LP_REG_DEFAULT_PA_POWER8 = 0x01,
	S2LP_REG_DEFAULT_PA_POWER7 = 0x0C,
	S2LP_REG_DEFAULT_PA_POWER6 = 0x18,
	S2LP_REG_DEFAULT_PA_POWER5 = 0x24,
	S2LP_REG_DEFAULT_PA_POWER4 = 0x30,
	S2LP_REG_DEFAULT_PA_POWER3 = 0x48,
	S2LP_REG_DEFAULT_PA_POWER2 = 0x60,
	S2LP_REG_DEFAULT_PA_POWER1 = 0x00,
	S2LP_REG_DEFAULT_PA_POWER0 = 0x47,
	S2LP_REG_DEFAULT_PA_CONFIG1 = 0x03,
	S2LP_REG_DEFAULT_PA_CONFIG0 = 0x8A,
	S2LP_REG_DEFAULT_SYNTH_CONFIG2 = 0xD0,
	S2LP_REG_DEFAULT_VCO_CONFIG = 0x03,
	S2LP_REG_DEFAULT_VCO_CALIBR_IN2 = 0x88,
	S2LP_REG_DEFAULT_VCO_CALIBR_IN1 = 0x40,
	S2LP_REG_DEFAULT_VCO_CALIBR_IN0 = 0x40,
	S2LP_REG_DEFAULT_XO_RCO_CONF1 = 0x45,
	S2LP_REG_DEFAULT_XO_RCO_CONF0 = 0x30,
	S2LP_REG_DEFAULT_RCO_CALIBR_CONF3 = 0x70,
	S2LP_REG_DEFAULT_RCO_CALIBR_CONF2 = 0x4D,
	S2LP_REG_DEFAULT_PM_CONF4 = 0x17,
	S2LP_REG_DEFAULT_PM_CONF3 = 0x20,
	S2LP_REG_DEFAULT_PM_CONF2 = 0x00,
	S2LP_REG_DEFAULT_PM_CONF1 = 0x39,
	S2LP_REG_DEFAULT_PM_CONF0 = 0x42,
	S2LP_REG_DEFAULT_MC_STATE1 = 0x52,
	S2LP_REG_DEFAULT_MC_STATE0 = 0x07,
	S2LP_REG_DEFAULT_TX_FIFO_STATUS = 0x00,
	S2LP_REG_DEFAULT_RX_FIFO_STATUS = 0x00,
	S2LP_REG_DEFAULT_RCO_CALIBR_OUT4 = 0x70,
	S2LP_REG_DEFAULT_RCO_CALIBR_OUT3 = 0x00,
	S2LP_REG_DEFAULT_RCO_CALIBR_OUT1 = 0x00,
	S2LP_REG_DEFAULT_VCO_CALIBROUT0 = 0x00,
	S2LP_REG_DEFAULT_TX_PCKT_INFO = 0x00,
	S2LP_REG_DEFAULT_RX_PCKT_INFO = 0x00,
	S2LP_REG_DEFAULT_AFC_CORR = 0x00,
	S2LP_REG_DEFAULT_LINK_QUALIF2 = 0x00,
	S2LP_REG_DEFAULT_LINK_QUALIF1 = 0x00,
	S2LP_REG_DEFAULT_RSSI_LEVEL = 0x00,
	S2LP_REG_DEFAULT_RX_PCKT_LEN1 = 0x00,
	S2LP_REG_DEFAULT_RX_PCKT_LEN0 = 0x00,
	S2LP_REG_DEFAULT_CRC_FIELD3 = 0x00,
	S2LP_REG_DEFAULT_CRC_FIELD2 = 0x00,
	S2LP_REG_DEFAULT_CRC_FIELD1 = 0x00,
	S2LP_REG_DEFAULT_CRC_FIELD0 = 0x00,
	S2LP_REG_DEFAULT_RX_ADDRE_FIELD1 = 0x00,
	S2LP_REG_DEFAULT_RX_ADDRE_FIELD0 = 0x00,
	S2LP_REG_DEFAULT_RSSI_LEVEL_RUN = 0x00,
	S2LP_REG_DEFAULT_DEVICE_INFO1 = 0x03,
	S2LP_REG_DEFAULT_DEVICE_INFO0 = 0xC1,
	S2LP_REG_DEFAULT_IRQ_STATUS3 = 0x00,
	S2LP_REG_DEFAULT_IRQ_STATUS2 = 0x09,
	S2LP_REG_DEFAULT_IRQ_STATUS1 = 0x05,
	S2LP_REG_DEFAULT_IRQ_STATUS0 = 0x00,
} S2LP_Register_DefaultValue;

#endif /* S2LP_S2LP_CONSTANTS_H_ */
