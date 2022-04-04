/*
 * spirit_setup.c
 *
 *  Created on: Dec 3, 2021
 *      Author: steelph0enix
 */
#include "spirit/spirit_setup.h"
#include "s2lp.h"
#include "spi.h"
#include "main.h"

extern S2LP_Handle spirit;

void spirit_setup_handle() {
	spirit.spi = &hspi1;

	spirit.gpio_csn_port = S2LP_CSN_GPIO_Port;
	spirit.gpio_csn_pin = S2LP_CSN_Pin;

#ifndef S2LP_SOFTWARE_RESET
	spirit.gpio_sdn_port = S2LP_SDN_GPIO_Port;
	spirit.gpio_sdn_pin = S2LP_SDN_Pin;
#endif

	spirit.gpio_port[0] = S2LP_GPIO0_AMP_CSD_GPIO_Port;
	spirit.gpio_pin[0] = S2LP_GPIO0_AMP_CSD_Pin;

	spirit.gpio_port[1] = S2LP_GPIO1_AMP_CPS_GPIO_Port;
	spirit.gpio_pin[1] = S2LP_GPIO1_AMP_CPS_Pin;

	spirit.gpio_port[2] = S2LP_GPIO2_AMP_CTX_GPIO_Port;
	spirit.gpio_pin[2] = S2LP_GPIO2_AMP_CTX_Pin;

	spirit.gpio_port[3] = S2LP_GPIO3_IRQ_GPIO_Port;
	spirit.gpio_pin[3] = S2LP_GPIO3_IRQ_Pin;
}

void spirit_setup_config() {
	// setup the common config for every s2lp in the system

	// RF settings
	// Base frequency: 868MHz
	// Channel spacing: 10
	// Channel: 0
	// Modulation: 2-GFSK
	// Datarate: 50kbps
	// Frequency deviation: 100kHz
	// Charge pump current: 240uA

	S2LP_RF_SetSynthBand(&spirit, S2LP_SYNTH_BAND_HIGH);
	S2LP_RF_SetBaseFrequency(&spirit, 868000000);
	S2LP_RF_SetChannelSpacing(&spirit, 10);
	S2LP_RF_SetChannelNumber(&spirit, 0);
	S2LP_RF_SetModulationType(&spirit, S2LP_MODULATION_2GFSK);
	S2LP_RF_SetDataRate(&spirit, 300000);
	S2LP_RF_SetFrequencyDeviation(&spirit, 100000);
	S2LP_RF_SetChargePumpCurrent(&spirit, S2LP_CHARGE_PUMP_140UA);

	// Intermediate frequency settings for 50MHz xtal
	S2LP_WriteRegister(&spirit, S2LP_REG_IF_OFFSET_ANA, 0x2F);
	S2LP_WriteRegister(&spirit, S2LP_REG_IF_OFFSET_DIG, 0xC2);

	// RX settings:
	// Channel filter value: 300kHz
	// Data source: Normal

	S2LP_RX_SetChannelFilterValueRaw(&spirit, 7, 1);
	S2LP_RX_SetDataSource(&spirit, S2LP_RX_SOURCE_NORMAL);

	// TX settings:
	// Data source: Normal
	// Power ramping: disabled
	// Power level: minimum

	S2LP_TX_SetDataSource(&spirit, S2LP_TX_SOURCE_NORMAL);
//	S2LP_TX_SetStaticPowerLevel(&spirit, S2LP_DBM_TO_POWER_LEVEL_STEP(0));

	// Packet settings:
	// Format: Basic
	// Packet length: variable (set on TX)
	// CRC mode: 32-bit eth
	// Data coding: FEC
	// Whitening: enabled

	S2LP_PCKT_SetPacketFormat(&spirit, S2LP_PACKET_BASIC);
	S2LP_PCKT_SetCRCMode(&spirit, S2LP_CRC_POLY_04C011BB7);
	S2LP_PCKT_SetDataWhiteningState(&spirit, true);
	S2LP_PCKT_SetDataCoding(&spirit, S2LP_CODING_FEC);
	S2LP_PCKT_SetVariablePacketLengthState(&spirit, true);

	// Packet filtering
//	    S2LP_PCKT_SetCRCFilteringState(&spirit, true);
//	    S2LP_PCKT_SetAutoPacketFilteringState(&spirit, true);
//	    S2LP_PCKT_SetSourceAddress(&spirit, 0x69);
//	    S2LP_PCKT_SetDestinationAddress(&spirit, 0x42);
//	    S2LP_PCKT_SetDestinationAddressState(&spirit, true);
//	    S2LP_PCKT_SetDestinationAddressFilteringState(&spirit, true);

	// GPIO settings for external amp:
	// GPIO0 is connected to CSD (Shutdown)
	// GPIO1 is connected to CPS (RX path select)
	// GPIO2 is connected to CTX (TX enable)
	// Bypass: CSD = 1, CPS = 0, CTX = 0
	// RX: CSD = 1, CPS = 1, CTX = 0
	// TX: CSD = 1, CPS = 0, CTX x 1

	// Callibrate RCO
//	S2LP_CallibrateRCO(&spirit);
}

void spirit_setup_irq() {
	// we start with all IRQs disabled, and enable
	// the ones that we want to &spirit
	uint32_t irq_mask = 0;

	// enable the IRQs like that:
	// SETBIT(irq_mask, S2LP_INT_SOME_INTERRUPT);
	SETBIT(irq_mask, S2LP_INT_RX_DATA_READY);
	SETBIT(irq_mask, S2LP_INT_RX_DATA_DISCARDED);
	SETBIT(irq_mask, S2LP_INT_TX_DATA_SENT);
	SETBIT(irq_mask, S2LP_INT_MAX_RE_TX_REACHED);
	SETBIT(irq_mask, S2LP_INT_CRC_ERROR);
	SETBIT(irq_mask, S2LP_INT_TX_FIFO_ERROR);
	SETBIT(irq_mask, S2LP_INT_RX_FIFO_ERROR);
	SETBIT(irq_mask, S2LP_INT_TX_FIFO_ALMOST_FULL);
	SETBIT(irq_mask, S2LP_INT_TX_FIFO_ALMOST_EMPTY);
	SETBIT(irq_mask, S2LP_INT_RX_FIFO_ALMOST_FULL);
	SETBIT(irq_mask, S2LP_INT_RX_FIFO_ALMOST_EMPTY);
//	SETBIT(irq_mask, S2LP_INT_MAX_BACK_OFF_CCA);
//	SETBIT(irq_mask, S2LP_INT_VALID_PREAMBLE_DETECTED);
//	SETBIT(irq_mask, S2LP_INT_SYNC_WORD_DETECTED);
//	SETBIT(irq_mask, S2LP_INT_RSSI_ABOVE_THRESHOLD);
//	SETBIT(irq_mask, S2LP_INT_WAKEUP_TIMEOUT_LDCR);
	SETBIT(irq_mask, S2LP_INT_READY);
//	SETBIT(irq_mask, S2LP_INT_STANDBY_STATE_SWITCHING);
//	SETBIT(irq_mask, S2LP_INT_LOW_BATTERY);
	SETBIT(irq_mask, S2LP_INT_POWER_ON_RESET);
//	SETBIT(irq_mask, S2LP_INT_RX_TIMER_TIMEOUT);
//	SETBIT(irq_mask, S2LP_INT_SNIFF_TIMER_TIMEOUT);

	S2LP_GPIO_SetPinOutput(&spirit, S2LP_PIN_GPIO_3, S2LP_GPIO_OUT_NIRQ);
	S2LP_SetInterruptMasks(&spirit, irq_mask);
}
