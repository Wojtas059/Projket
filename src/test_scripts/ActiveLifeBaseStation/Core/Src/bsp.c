/*
 * bsp.c
 *
 *  Created on: Feb 12, 2022
 *      Author: phoen
 */

#include "main.h"
#include "cmsis_os.h"

void BSP_LEDOn() {
	HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
}

void BSP_LEDOff() {
	HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
}

void BSP_LEDToggle() {
	HAL_GPIO_TogglePin(LD2_GPIO_Port, LD2_Pin);
}

void BSP_LEDBlink(unsigned on_time, unsigned off_time) {
	BSP_LEDOn();
	osDelay(on_time);
	BSP_LEDOff();
	osDelay(off_time);
}

__attribute__((weak)) void BSP_OnButtonClicked() {}
