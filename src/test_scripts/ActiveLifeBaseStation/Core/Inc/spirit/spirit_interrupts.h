/*
 * spirit_interrupts.h
 *
 *  Created on: Dec 3, 2021
 *      Author: steelph0enix
 */

#ifndef INC_SPIRIT_SPIRIT_INTERRUPTS_H_
#define INC_SPIRIT_SPIRIT_INTERRUPTS_H_
#include "s2lp.h"

void spirit_irq_rx_data_ready(S2LP_Handle* spirit);
void spirit_irq_rx_data_discarded(S2LP_Handle* spirit);
void spirit_irq_tx_data_sent(S2LP_Handle* spirit);
void spirit_irq_max_retransmissions_reached(S2LP_Handle* spirit);
void spirit_irq_crc_error(S2LP_Handle* spirit);
void spirit_irq_tx_fifo_error(S2LP_Handle* spirit);
void spirit_irq_rx_fifo_error(S2LP_Handle* spirit);
void spirit_irq_tx_fifo_almost_full(S2LP_Handle* spirit);
void spirit_irq_tx_fifo_almost_empty(S2LP_Handle* spirit);
void spirit_irq_rx_fifo_almost_full(S2LP_Handle* spirit);
void spirit_irq_rx_fifo_almost_empty(S2LP_Handle* spirit);
void spirit_irq_max_back_off(S2LP_Handle* spirit);
void spirit_irq_preamble_detected(S2LP_Handle* spirit);
void spirit_irq_sync_word_detected(S2LP_Handle* spirit);
void spirit_irq_rssi_above_threshold(S2LP_Handle* spirit);
void spirit_irq_wakeup_timeout_ldcr(S2LP_Handle* spirit);
void spirit_irq_ready(S2LP_Handle* spirit);
void spirit_irq_standby_switch_in_progress(S2LP_Handle* spirit);
void spirit_irq_low_battery(S2LP_Handle* spirit);
void spirit_irq_power_on_reset(S2LP_Handle* spirit);
void spirit_irq_rx_timer_timeout(S2LP_Handle* spirit);
void spirit_irq_sniff_timer_timeout(S2LP_Handle* spirit);

void spirit_process_irq();

#endif /* INC_SPIRIT_SPIRIT_INTERRUPTS_H_ */
