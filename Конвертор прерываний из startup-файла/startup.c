Функции:

void WWDG_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void PVD_IRQHandler                (void) __attribute__ ((weak, alias("Default_Handler")));
void TAMP_STAMP_IRQHandler         (void) __attribute__ ((weak, alias("Default_Handler")));
void RTC_WKUP_IRQHandler           (void) __attribute__ ((weak, alias("Default_Handler")));
void FLASH_IRQHandler              (void) __attribute__ ((weak, alias("Default_Handler")));
void RCC_IRQHandler                (void) __attribute__ ((weak, alias("Default_Handler")));
void EXTI0_IRQHandler              (void) __attribute__ ((weak, alias("Default_Handler")));
void EXTI1_IRQHandler              (void) __attribute__ ((weak, alias("Default_Handler")));
void EXTI2_IRQHandler              (void) __attribute__ ((weak, alias("Default_Handler")));
void EXTI3_IRQHandler              (void) __attribute__ ((weak, alias("Default_Handler")));
void EXTI4_IRQHandler              (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA1_Stream0_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA1_Stream1_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA1_Stream2_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA1_Stream3_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA1_Stream4_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA1_Stream5_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA1_Stream6_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void ADC_IRQHandler                (void) __attribute__ ((weak, alias("Default_Handler")));
void CAN1_TX_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void CAN1_RX0_IRQHandler           (void) __attribute__ ((weak, alias("Default_Handler")));
void CAN1_RX1_IRQHandler           (void) __attribute__ ((weak, alias("Default_Handler")));
void CAN1_SCE_IRQHandler           (void) __attribute__ ((weak, alias("Default_Handler")));
void EXTI9_5_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM1_BRK_TIM9_IRQHandler      (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM1_UP_TIM10_IRQHandler      (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM1_TRG_COM_TIM11_IRQHandler (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM1_CC_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM2_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM3_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM4_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void I2C1_EV_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void I2C1_ER_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void I2C2_EV_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void I2C2_ER_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void SPI1_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void SPI2_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void USART1_IRQHandler             (void) __attribute__ ((weak, alias("Default_Handler")));
void USART2_IRQHandler             (void) __attribute__ ((weak, alias("Default_Handler")));
void USART3_IRQHandler             (void) __attribute__ ((weak, alias("Default_Handler")));
void EXTI15_10_IRQHandler          (void) __attribute__ ((weak, alias("Default_Handler")));
void RTC_Alarm_IRQHandler          (void) __attribute__ ((weak, alias("Default_Handler")));
void OTG_FS_WKUP_IRQHandler        (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM8_BRK_TIM12_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM8_UP_TIM13_IRQHandler      (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM8_TRG_COM_TIM14_IRQHandler (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM8_CC_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA1_Stream7_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void FMC_IRQHandler                (void) __attribute__ ((weak, alias("Default_Handler")));
void SDMMC1_IRQHandler             (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM5_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void SPI3_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void UART4_IRQHandler              (void) __attribute__ ((weak, alias("Default_Handler")));
void UART5_IRQHandler              (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM6_DAC_IRQHandler           (void) __attribute__ ((weak, alias("Default_Handler")));
void TIM7_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA2_Stream0_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA2_Stream1_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA2_Stream2_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA2_Stream3_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA2_Stream4_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void ETH_IRQHandler                (void) __attribute__ ((weak, alias("Default_Handler")));
void ETH_WKUP_IRQHandler           (void) __attribute__ ((weak, alias("Default_Handler")));
void CAN2_TX_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void CAN2_RX0_IRQHandler           (void) __attribute__ ((weak, alias("Default_Handler")));
void CAN2_RX1_IRQHandler           (void) __attribute__ ((weak, alias("Default_Handler")));
void CAN2_SCE_IRQHandler           (void) __attribute__ ((weak, alias("Default_Handler")));
void OTG_FS_IRQHandler             (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA2_Stream5_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA2_Stream6_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA2_Stream7_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void USART6_IRQHandler             (void) __attribute__ ((weak, alias("Default_Handler")));
void I2C3_EV_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void I2C3_ER_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void OTG_HS_EP1_OUT_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
void OTG_HS_EP1_IN_IRQHandler      (void) __attribute__ ((weak, alias("Default_Handler")));
void OTG_HS_WKUP_IRQHandler        (void) __attribute__ ((weak, alias("Default_Handler")));
void OTG_HS_IRQHandler             (void) __attribute__ ((weak, alias("Default_Handler")));
void DCMI_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void RNG_IRQHandler                (void) __attribute__ ((weak, alias("Default_Handler")));
void FPU_IRQHandler                (void) __attribute__ ((weak, alias("Default_Handler")));
void UART7_IRQHandler              (void) __attribute__ ((weak, alias("Default_Handler")));
void UART8_IRQHandler              (void) __attribute__ ((weak, alias("Default_Handler")));
void SPI4_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void SPI5_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void SPI6_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void SAI1_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void DMA2D_IRQHandler              (void) __attribute__ ((weak, alias("Default_Handler")));
void SAI2_IRQHandler               (void) __attribute__ ((weak, alias("Default_Handler")));
void QUADSPI_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void LPTIM1_IRQHandler             (void) __attribute__ ((weak, alias("Default_Handler")));
void CEC_IRQHandler                (void) __attribute__ ((weak, alias("Default_Handler")));
void I2C4_EV_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void I2C4_ER_IRQHandler            (void) __attribute__ ((weak, alias("Default_Handler")));
void SPDIF_RX_IRQHandler           (void) __attribute__ ((weak, alias("Default_Handler")));


Массив:

WWDG_IRQHandler,               /* Window WatchDog */
PVD_IRQHandler,                /* PVD through EXTI Line detection */
TAMP_STAMP_IRQHandler,         /* Tamper and TimeStamps through the EXTI line */
RTC_WKUP_IRQHandler,           /* RTC Wakeup through the EXTI line */
FLASH_IRQHandler,              /* FLASH */
RCC_IRQHandler,                /* RCC */
EXTI0_IRQHandler,              /* EXTI Line0 */
EXTI1_IRQHandler,              /* EXTI Line1 */
EXTI2_IRQHandler,              /* EXTI Line2 */
EXTI3_IRQHandler,              /* EXTI Line3 */
EXTI4_IRQHandler,              /* EXTI Line4 */
DMA1_Stream0_IRQHandler,       /* DMA1 Stream 0 */
DMA1_Stream1_IRQHandler,       /* DMA1 Stream 1 */
DMA1_Stream2_IRQHandler,       /* DMA1 Stream 2 */
DMA1_Stream3_IRQHandler,       /* DMA1 Stream 3 */
DMA1_Stream4_IRQHandler,       /* DMA1 Stream 4 */
DMA1_Stream5_IRQHandler,       /* DMA1 Stream 5 */
DMA1_Stream6_IRQHandler,       /* DMA1 Stream 6 */
ADC_IRQHandler,                /* ADC1, ADC2 and ADC3s */
CAN1_TX_IRQHandler,            /* CAN1 TX */
CAN1_RX0_IRQHandler,           /* CAN1 RX0 */
CAN1_RX1_IRQHandler,           /* CAN1 RX1 */
CAN1_SCE_IRQHandler,           /* CAN1 SCE */
EXTI9_5_IRQHandler,            /* External Line[9:5]s */
TIM1_BRK_TIM9_IRQHandler,      /* TIM1 Break and TIM9 */
TIM1_UP_TIM10_IRQHandler,      /* TIM1 Update and TIM10 */
TIM1_TRG_COM_TIM11_IRQHandler, /* TIM1 Trigger and Commutation and TIM11 */
TIM1_CC_IRQHandler,            /* TIM1 Capture Compare */
TIM2_IRQHandler,               /* TIM2 */
TIM3_IRQHandler,               /* TIM3 */
TIM4_IRQHandler,               /* TIM4 */
I2C1_EV_IRQHandler,            /* I2C1 Event */
I2C1_ER_IRQHandler,            /* I2C1 Error */
I2C2_EV_IRQHandler,            /* I2C2 Event */
I2C2_ER_IRQHandler,            /* I2C2 Error */
SPI1_IRQHandler,               /* SPI1 */
SPI2_IRQHandler,               /* SPI2 */
USART1_IRQHandler,             /* USART1 */
USART2_IRQHandler,             /* USART2 */
USART3_IRQHandler,             /* USART3 */
EXTI15_10_IRQHandler,          /* External Line[15:10]s */
RTC_Alarm_IRQHandler,          /* RTC Alarm (A and B) through EXTI Line */
OTG_FS_WKUP_IRQHandler,        /* USB OTG FS Wakeup through EXTI line */
TIM8_BRK_TIM12_IRQHandler,     /* TIM8 Break and TIM12 */
TIM8_UP_TIM13_IRQHandler,      /* TIM8 Update and TIM13 */
TIM8_TRG_COM_TIM14_IRQHandler, /* TIM8 Trigger and Commutation and TIM14 */
TIM8_CC_IRQHandler,            /* TIM8 Capture Compare */
DMA1_Stream7_IRQHandler,       /* DMA1 Stream7 */
FMC_IRQHandler,                /* FMC */
SDMMC1_IRQHandler,             /* SDMMC1 */
TIM5_IRQHandler,               /* TIM5 */
SPI3_IRQHandler,               /* SPI3 */
UART4_IRQHandler,              /* UART4 */
UART5_IRQHandler,              /* UART5 */
TIM6_DAC_IRQHandler,           /* TIM6 and DAC1&2 underrun errors */
TIM7_IRQHandler,               /* TIM7 */
DMA2_Stream0_IRQHandler,       /* DMA2 Stream 0 */
DMA2_Stream1_IRQHandler,       /* DMA2 Stream 1 */
DMA2_Stream2_IRQHandler,       /* DMA2 Stream 2 */
DMA2_Stream3_IRQHandler,       /* DMA2 Stream 3 */
DMA2_Stream4_IRQHandler,       /* DMA2 Stream 4 */
ETH_IRQHandler,                /* Ethernet */
ETH_WKUP_IRQHandler,           /* Ethernet Wakeup through EXTI line */
CAN2_TX_IRQHandler,            /* CAN2 TX */
CAN2_RX0_IRQHandler,           /* CAN2 RX0 */
CAN2_RX1_IRQHandler,           /* CAN2 RX1 */
CAN2_SCE_IRQHandler,           /* CAN2 SCE */
OTG_FS_IRQHandler,             /* USB OTG FS */
DMA2_Stream5_IRQHandler,       /* DMA2 Stream 5 */
DMA2_Stream6_IRQHandler,       /* DMA2 Stream 6 */
DMA2_Stream7_IRQHandler,       /* DMA2 Stream 7 */
USART6_IRQHandler,             /* USART6 */
I2C3_EV_IRQHandler,            /* I2C3 event */
I2C3_ER_IRQHandler,            /* I2C3 error */
OTG_HS_EP1_OUT_IRQHandler,     /* USB OTG HS End Point 1 Out */
OTG_HS_EP1_IN_IRQHandler,      /* USB OTG HS End Point 1 In */
OTG_HS_WKUP_IRQHandler,        /* USB OTG HS Wakeup through EXTI */
OTG_HS_IRQHandler,             /* USB OTG HS */
DCMI_IRQHandler,               /* DCMI */
0,                             /* Reserved */
RNG_IRQHandler,                /* Rng */
FPU_IRQHandler,                /* FPU */
UART7_IRQHandler,              /* UART7 */
UART8_IRQHandler,              /* UART8 */
SPI4_IRQHandler,               /* SPI4 */
SPI5_IRQHandler,               /* SPI5 */
SPI6_IRQHandler,               /* SPI6 */
SAI1_IRQHandler,               /* SAI1 */
0,                             /* Reserved */
0,                             /* Reserved */
DMA2D_IRQHandler,              /* DMA2D */
SAI2_IRQHandler,               /* SAI2 */
QUADSPI_IRQHandler,            /* QUADSPI */
LPTIM1_IRQHandler,             /* LPTIM1 */
CEC_IRQHandler,                /* HDMI_CEC */
I2C4_EV_IRQHandler,            /* I2C4 Event */
I2C4_ER_IRQHandler,            /* I2C4 Error */
SPDIF_RX_IRQHandler,           /* SPDIF_RX */

