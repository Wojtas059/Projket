/*
 * bsp.h
 *
 *  Created on: Feb 12, 2022
 *      Author: phoen
 */

#ifndef INC_BSP_H_
#define INC_BSP_H_

void BSP_LEDOn();
void BSP_LEDOff();
void BSP_LEDToggle();
void BSP_LEDBlink(unsigned off_time, unsigned on_time);

void BSP_OnButtonClicked();

#endif /* INC_BSP_H_ */
