/*
 * spirit_manager.h
 *
 *  Created on: Dec 3, 2021
 *      Author: steelph0enix
 */

#ifndef INC_SPIRIT_SPIRIT_MANAGER_H_
#define INC_SPIRIT_SPIRIT_MANAGER_H_
#include <stdbool.h>
#include <stdint.h>

#include "s2lp.h"

typedef enum ExtAmpMode_t {
	EXT_AMP_SHUTDOWN, EXT_AMP_BYPASS, EXT_AMP_TX, EXT_AMP_RX
} ExtAmpMode;

void spirit_initialize();
void spirit_startup();
bool is_spirit_detected();

// This function transmits the raw text data over S2-LP
void spirit_send_data(uint8_t const* data, size_t length);
void spirit_send_text(char const* data);
void spirit_begin_receive();
void spirit_data_received_handler(S2LP_Handle* handle, size_t dataLength);
void spirit_data_received_callback(uint8_t const* data, size_t dataLength);
void spirit_setup_ext_amp(ExtAmpMode mode);

void spirit_irq_handler();

#endif /* INC_SPIRIT_SPIRIT_MANAGER_H_ */
