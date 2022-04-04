/*
 * spirit_manager.c
 *
 *  Created on: Dec 3, 2021
 *      Author: steelph0enix
 */

#include <string.h>

#include "s2lp.h"
#include "spirit/spirit_manager.h"
#include "spirit/spirit_setup.h"
#include "spirit/spirit_interrupts.h"

#include "FreeRTOS.h"
#include "cmsis_os.h"
#include "task.h"

#include "main.h"

S2LP_Handle spirit;

void spirit_initialize_handle();
void spirit_task(void* taskData);

uint8_t spiritReceivedData[128] = { 0 };

static osThreadId_t spiritTaskHandle = NULL;
// @formatter:off
static const osThreadAttr_t spiritTaskAttributes = {
		.name = "spirit_task",
		.stack_size = 512 * 4,
		.priority =
		(osPriority_t) osPriorityBelowNormal,
};
// @formatter:on

void spirit_startup() {
	spirit_initialize();
	spiritTaskHandle = osThreadNew(spirit_task, NULL, &spiritTaskAttributes);
}

void spirit_initialize() {
	spirit_setup_handle();
	S2LP_Initialize(&spirit, S2LP_CLOCK_FREQ_50MHZ);
	spirit_setup_config();
	spirit_setup_irq();
	spirit_setup_ext_amp(EXT_AMP_BYPASS);
}

bool is_spirit_detected() {
	uint8_t const s2lp_pn = S2LP_GetDevicePartNumber(&spirit);
	// version may vary, unreliable
//	uint8_t const s2lp_version = S2LP_GetDeviceVersionNumber(&spirit);

	return (s2lp_pn == 0x03);
}

void spirit_send_text(char const* data) {
	size_t const textLength = strlen(data);

	spirit_send_data((uint8_t const*) data, textLength);
}

void spirit_send_data(uint8_t const* data, size_t length) {
	// Wait until the last transmission is complete
	while (S2LP_ReadStatus(&spirit).state == S2LP_STATE_TX) {
		osDelay(1);
	}

	// Switch from listening state to idle
	if (S2LP_ReadStatus(&spirit).state == S2LP_STATE_RX) {
		S2LP_SendCommand(&spirit, S2LP_CMD_SABORT);
	}

	// Send the data to spirit
	S2LP_PCKT_SetPacketLength(&spirit, length);
	S2LP_WriteFIFO(&spirit, length, (uint8_t*) data);

	// Start transmission
	spirit_setup_ext_amp(EXT_AMP_TX);
	S2LP_SendCommand(&spirit, S2LP_CMD_TX);
}

void spirit_begin_receive() {
	spirit_setup_ext_amp(EXT_AMP_RX);
	S2LP_SendCommand(&spirit, S2LP_CMD_RX);
}

void spirit_data_received_handler(S2LP_Handle* spirit, size_t dataLength) {
	S2LP_ReadFIFO(spirit, dataLength, spiritReceivedData);
	spirit_begin_receive();
	spirit_data_received_callback(spiritReceivedData, dataLength);
}

void spirit_task(void* taskData) {
	UNUSED(taskData);

	uint32_t notificationValue = 0;
	TickType_t const notificationWaitingTime = 2;

	spirit_process_irq();

	for (;;) {
		// Notification indicates whether an interrupt happened and should be handled, or not
		notificationValue = ulTaskNotifyTake(pdTRUE, notificationWaitingTime);
		if (notificationValue != 0) {
			spirit_process_irq();
		}
	}
}

void spirit_irq_handler() {
	if (spiritTaskHandle != NULL) {
		BaseType_t xHigherPriorityTaskWoken = pdFALSE;
		vTaskNotifyGiveFromISR(spiritTaskHandle, &xHigherPriorityTaskWoken);
		// Yielding from ISR is disabled for now, as it's not necessary and can cause issues.
		// RTOS will eventually jump to spirit task anyway.
//		portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
	} else {
		// whoops, nothing to do here
	}
}
void spirit_setup_ext_amp(ExtAmpMode mode) {
	// GPIO settings for external amp:
	// GPIO0 is connected to CSD (Shutdown)
	// GPIO1 is connected to CPS (RX path select)
	// GPIO2 is connected to CTX (TX enable)
	// Bypass: CSD = 1, CPS = 0, CTX = 0
	// RX: CSD = 1, CPS = 1, CTX = 0
	// TX: CSD = 1, CPS = 0, CTX x 1

	switch (mode) {
		case EXT_AMP_SHUTDOWN:
			HAL_GPIO_WritePin(S2LP_GPIO0_AMP_CSD_GPIO_Port, S2LP_GPIO0_AMP_CSD_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(S2LP_GPIO1_AMP_CPS_GPIO_Port, S2LP_GPIO1_AMP_CPS_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(S2LP_GPIO2_AMP_CTX_GPIO_Port, S2LP_GPIO2_AMP_CTX_Pin, GPIO_PIN_RESET);
			break;
		case EXT_AMP_BYPASS:
			HAL_GPIO_WritePin(S2LP_GPIO0_AMP_CSD_GPIO_Port, S2LP_GPIO0_AMP_CSD_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(S2LP_GPIO1_AMP_CPS_GPIO_Port, S2LP_GPIO1_AMP_CPS_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(S2LP_GPIO2_AMP_CTX_GPIO_Port, S2LP_GPIO2_AMP_CTX_Pin, GPIO_PIN_RESET);
			break;
		case EXT_AMP_TX:
			HAL_GPIO_WritePin(S2LP_GPIO0_AMP_CSD_GPIO_Port, S2LP_GPIO0_AMP_CSD_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(S2LP_GPIO1_AMP_CPS_GPIO_Port, S2LP_GPIO1_AMP_CPS_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(S2LP_GPIO2_AMP_CTX_GPIO_Port, S2LP_GPIO2_AMP_CTX_Pin, GPIO_PIN_SET);
			break;
		case EXT_AMP_RX:
			HAL_GPIO_WritePin(S2LP_GPIO0_AMP_CSD_GPIO_Port, S2LP_GPIO0_AMP_CSD_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(S2LP_GPIO1_AMP_CPS_GPIO_Port, S2LP_GPIO1_AMP_CPS_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(S2LP_GPIO2_AMP_CTX_GPIO_Port, S2LP_GPIO2_AMP_CTX_Pin, GPIO_PIN_RESET);
			break;
	}
}

