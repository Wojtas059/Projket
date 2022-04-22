/* USER CODE BEGIN Header */
/**
 ******************************************************************************
 * File Name          : freertos.c
 * Description        : Code for freertos applications
 ******************************************************************************
 * @attention
 *
 * Copyright (c) 2022 STMicroelectronics.
 * All rights reserved.
 *
 * This software is licensed under terms that can be found in the LICENSE file
 * in the root directory of this software component.
 * If no LICENSE file comes with this software, it is provided AS-IS.
 *
 ******************************************************************************
 */
/* USER CODE END Header */

/* Includes ------------------------------------------------------------------*/
#include "FreeRTOS.h"
#include "task.h"
#include "main.h"
#include "cmsis_os.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "usart.h"
#include "bsp.h"
#include "spirit/spirit_manager.h"
#include <stdbool.h>
#include <string.h>
#include "printf.h"
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
#define SPIRIT_DATA_BUFFER_SIZE 128
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
/* USER CODE BEGIN Variables */
uint8_t spiritData[SPIRIT_DATA_BUFFER_SIZE] = { 0 };
bool sendSampleData = false;
char const *sampleData = "Hello, this is a test message!\r\n";

uint8_t *userDataBuffer = spiritData;
size_t userDataLength = 0;
bool isDataFromUserReceived = false;

uint8_t const *spiritDataBuffer = NULL;
size_t spiritDataLength = 0;
bool isDataFromSpiritReceived = false;
/* USER CODE END Variables */
/* Definitions for defaultTask */
osThreadId_t defaultTaskHandle;
const osThreadAttr_t defaultTask_attributes = { .name = "defaultTask", .stack_size = 512 * 4, .priority =
		(osPriority_t) osPriorityNormal, };

/* Private function prototypes -----------------------------------------------*/
/* USER CODE BEGIN FunctionPrototypes */
void notify_main_task();
void start_uart_rx(uint8_t* buffer, size_t capacity);
void uart_transmit(uint8_t* buffer, size_t length);

void transmit_data_from_spirit_to_user(uint8_t const* data, size_t length);
void transmit_data_from_user_to_spirit(uint8_t const* data, size_t length);

void print_buffer_to_itm(uint8_t const* data, size_t length);
/* USER CODE END FunctionPrototypes */

void StartDefaultTask(void* argument);

void MX_FREERTOS_Init(void); /* (MISRA C 2004 rule 8.1) */

/**
 * @brief  FreeRTOS initialization
 * @param  None
 * @retval None
 */
void MX_FREERTOS_Init(void) {
	/* USER CODE BEGIN Init */

	/* USER CODE END Init */

	/* USER CODE BEGIN RTOS_MUTEX */
	/* add mutexes, ... */
	/* USER CODE END RTOS_MUTEX */

	/* USER CODE BEGIN RTOS_SEMAPHORES */
	/* add semaphores, ... */
	/* USER CODE END RTOS_SEMAPHORES */

	/* USER CODE BEGIN RTOS_TIMERS */
	/* start timers, add new ones, ... */
	/* USER CODE END RTOS_TIMERS */

	/* USER CODE BEGIN RTOS_QUEUES */
	/* add queues, ... */
	/* USER CODE END RTOS_QUEUES */

	/* Create the thread(s) */
	/* creation of defaultTask */
	defaultTaskHandle = osThreadNew(StartDefaultTask, NULL, &defaultTask_attributes);

	/* USER CODE BEGIN RTOS_THREADS */
	/* add threads, ... */
	/* USER CODE END RTOS_THREADS */

	/* USER CODE BEGIN RTOS_EVENTS */
	/* add events, ... */
	/* USER CODE END RTOS_EVENTS */

}

/* USER CODE BEGIN Header_StartDefaultTask */
/**
 * @brief  Function implementing the defaultTask thread.
 * @param  argument: Not used
 * @retval None
 */
/* USER CODE END Header_StartDefaultTask */
void StartDefaultTask(void* argument) {
	/* USER CODE BEGIN StartDefaultTask */
	UNUSED(argument);

	uint32_t notificationValue = 0;
	TickType_t const notificationWaitingTime = 2;

	spirit_startup();
	if (!is_spirit_detected()) {
		for (;;) {
			BSP_LEDBlink(200, 200);
			printf("SPIRIT DEAD!\r\n");
		}
	}

	spirit_begin_receive();
	start_uart_rx(spiritData, SPIRIT_DATA_BUFFER_SIZE);

	printf("  Ready to go!\r\n");

	/* Infinite loop */
	for (;;) {
		notificationValue = ulTaskNotifyTake(pdTRUE, notificationWaitingTime);
		if (notificationValue != 0) {
			if (isDataFromUserReceived) {
//				printf("USER -> SPIRIT (%u bytes): ", userDataLength);
//				print_buffer_to_itm(userDataBuffer, userDataLength);
//				printf("\r\n");
				transmit_data_from_user_to_spirit(userDataBuffer, userDataLength);
				isDataFromUserReceived = false;
				BSP_LEDToggle();
			}
			if (isDataFromSpiritReceived) {
//				printf("SPIRIT -> USER (%u bytes): ", spiritDataLength);
//				print_buffer_to_itm(spiritDataBuffer, spiritDataLength);
//				printf("\r\n");
				transmit_data_from_spirit_to_user(spiritDataBuffer, spiritDataLength);
				isDataFromSpiritReceived = false;
				BSP_LEDToggle();
			}
			if (sendSampleData) {
				transmit_data_from_user_to_spirit((uint8_t const*) sampleData, strlen(sampleData));
				sendSampleData = false;
			}
		}
	}
	/* USER CODE END StartDefaultTask */
}

/* Private application code --------------------------------------------------*/
/* USER CODE BEGIN Application */
void transmit_data_from_spirit_to_user(uint8_t const* data, size_t length) {
	uart_transmit((uint8_t*) data, length);
	start_uart_rx(spiritData, SPIRIT_DATA_BUFFER_SIZE);
}

void transmit_data_from_user_to_spirit(uint8_t const* data, size_t length) {
	spirit_send_data(data, length);
	start_uart_rx(spiritData, SPIRIT_DATA_BUFFER_SIZE);
}

void spirit_data_received_callback(uint8_t const* data, size_t dataLength) {
	// spirit data received - transmit it to user via UART
	spiritDataLength = dataLength;
	spiritDataBuffer = data;
	isDataFromSpiritReceived = true;
	notify_main_task();
}

void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef* huart, uint16_t Size) {
	// user data received - transmit it to board via spirit
	userDataLength = Size;
	isDataFromUserReceived = true;
	notify_main_task();
}

void start_uart_rx(uint8_t* buffer, size_t capacity) {
	HAL_UART_StateTypeDef uart_state = HAL_UART_GetState(&huart2);
	if (uart_state == HAL_UART_STATE_BUSY_RX) {
		return;
	}

	while ((uart_state = HAL_UART_GetState(&huart2)) != HAL_UART_STATE_READY) {
		osDelay(2);
	}
	HAL_UARTEx_ReceiveToIdle_DMA(&huart2, buffer, capacity);
}

void uart_transmit(uint8_t* buffer, size_t length) {
	HAL_UART_AbortReceive(&huart2);
	HAL_UART_Transmit_DMA(&huart2, buffer, length);
}

void notify_main_task() {
	static BaseType_t xHigherPriorTaskWoken = pdFALSE;
	vTaskNotifyGiveFromISR(defaultTaskHandle, &xHigherPriorTaskWoken);
}

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin) {
	if (GPIO_Pin == S2LP_GPIO3_IRQ_Pin) {
		spirit_irq_handler();
	} else if (GPIO_Pin == B1_Pin) {
		BSP_OnButtonClicked();
	}
}

void BSP_OnButtonClicked() {
	sendSampleData = true;
	notify_main_task();
}

void print_buffer_to_itm(uint8_t const* data, size_t length) {
	for (uint8_t const *b = data; b != (data + length); b++) {
		printf("0x%02X ", *b);
	}
}

void _putchar(char character) {
//	ITM_SendChar(character);
}
/* USER CODE END Application */

