/*
 * spirit_interrupts.c
 *
 *  Created on: Dec 3, 2021
 *      Author: steelph0enix
 */

#include "spirit/spirit_interrupts.h"
#include "spirit/spirit_manager.h"
#include "bsp.h"

extern S2LP_Handle spirit;

void spirit_irq_rx_data_ready(S2LP_Handle* spirit) {
	BSP_LEDToggle();
	uint8_t bytes_in_fifo = S2LP_RX_GetFIFOCount(spirit);
	spirit_data_received_handler(spirit, bytes_in_fifo);
}

void spirit_irq_rx_data_discarded(S2LP_Handle* spirit) {
}

void spirit_irq_tx_data_sent(S2LP_Handle* spirit) {
	BSP_LEDToggle();
    spirit_begin_receive();
}

void spirit_irq_max_retransmissions_reached(S2LP_Handle* spirit) {
}

void spirit_irq_crc_error(S2LP_Handle* spirit) {
}

void spirit_irq_tx_fifo_error(S2LP_Handle* spirit) {
	S2LP_SendCommand(spirit, S2LP_CMD_FLUSHTXFIFO);
}

void spirit_irq_rx_fifo_error(S2LP_Handle* spirit) {
	S2LP_SendCommand(spirit, S2LP_CMD_FLUSHRXFIFO);
}

void spirit_irq_tx_fifo_almost_full(S2LP_Handle* spirit) {
}

void spirit_irq_tx_fifo_almost_empty(S2LP_Handle* spirit) {
}

void spirit_irq_rx_fifo_almost_full(S2LP_Handle* spirit) {
}

void spirit_irq_rx_fifo_almost_empty(S2LP_Handle* spirit) {
}

void spirit_irq_max_back_off(S2LP_Handle* spirit) {
}

void spirit_irq_preamble_detected(S2LP_Handle* spirit) {
}

void spirit_irq_sync_word_detected(S2LP_Handle* spirit) {
}

void spirit_irq_rssi_above_threshold(S2LP_Handle* spirit) {
}

void spirit_irq_wakeup_timeout_ldcr(S2LP_Handle* spirit) {
}

void spirit_irq_ready(S2LP_Handle* spirit) {
}

void spirit_irq_standby_switch_in_progress(S2LP_Handle* spirit) {
}

void spirit_irq_low_battery(S2LP_Handle* spirit) {
}

void spirit_irq_power_on_reset(S2LP_Handle* spirit) {
}

void spirit_irq_rx_timer_timeout(S2LP_Handle* spirit) {
}

void spirit_irq_sniff_timer_timeout(S2LP_Handle* spirit) {
}

void spirit_process_irq() {
	uint32_t irqFlags = S2LP_GetInterrupts(&spirit);

	if (GETBIT(irqFlags, S2LP_INT_RX_DATA_READY)) {
		spirit_irq_rx_data_ready(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_RX_DATA_DISCARDED)) {
		spirit_irq_rx_data_discarded(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_TX_DATA_SENT)) {
		spirit_irq_tx_data_sent(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_MAX_RE_TX_REACHED)) {
		spirit_irq_max_retransmissions_reached(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_CRC_ERROR)) {
		spirit_irq_crc_error(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_TX_FIFO_ERROR)) {
		spirit_irq_tx_fifo_error(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_RX_FIFO_ERROR)) {
		spirit_irq_rx_fifo_error(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_TX_FIFO_ALMOST_FULL)) {
		spirit_irq_tx_fifo_almost_full(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_TX_FIFO_ALMOST_EMPTY)) {
		spirit_irq_tx_fifo_almost_empty(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_RX_FIFO_ALMOST_FULL)) {
		spirit_irq_rx_fifo_almost_full(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_RX_FIFO_ALMOST_EMPTY)) {
		spirit_irq_rx_fifo_almost_empty(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_MAX_BACK_OFF_CCA)) {
		spirit_irq_max_back_off(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_VALID_PREAMBLE_DETECTED)) {
		spirit_irq_preamble_detected(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_SYNC_WORD_DETECTED)) {
		spirit_irq_sync_word_detected(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_RSSI_ABOVE_THRESHOLD)) {
		spirit_irq_rssi_above_threshold(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_WAKEUP_TIMEOUT_LDCR)) {
		spirit_irq_wakeup_timeout_ldcr(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_READY)) {
		spirit_irq_ready(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_STANDBY_STATE_SWITCHING)) {
		spirit_irq_standby_switch_in_progress(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_LOW_BATTERY)) {
		spirit_irq_low_battery(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_POWER_ON_RESET)) {
		spirit_irq_power_on_reset(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_RX_TIMER_TIMEOUT)) {
		spirit_irq_rx_timer_timeout(&spirit);
	}
	if (GETBIT(irqFlags, S2LP_INT_SNIFF_TIMER_TIMEOUT)) {
		spirit_irq_sniff_timer_timeout(&spirit);
	}
}

