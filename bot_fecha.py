import asyncio
import schedule
import time
from datetime import datetime, timedelta
from calendar import monthrange
from telegram import Bot
from telegram.error import TelegramError
import logging

# Configuración de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# CONFIGURACIÓN - TUS DATOS
BOT_TOKEN = "7873505067:AAG7aeM7BKHI8cnH_7ztSddCE3N07dm9In8"
CHAT_ID = "-1002712341833"

DAVID_TRON_TRC20 = "TSVgxtNpWpdKww68NHZPR4AHx8r2nDvKA6"
DAVID_ETHEREUM_ERC20 = "0xd8d1ca8b1d7236b338fc370ad677ff2e7131759b"

# Crear instancia del bot
bot = Bot(token=BOT_TOKEN)

def obtener_ultimo_dia_mes(año, mes):
    """Obtiene el último día del mes"""
    return monthrange(año, mes)[1]

def obtener_tipo_notificacion():
    """Determina qué tipo de notificación enviar según la fecha actual"""
    hoy = datetime.now()
    dia_actual = hoy.day
    mes_actual = hoy.month
    año_actual = hoy.year
    
    ultimo_dia = obtener_ultimo_dia_mes(año_actual, mes_actual)
    penultimo_dia = ultimo_dia - 1
    
    if dia_actual == 14:
        return "recordatorio_15"
    elif dia_actual == 15:
        return "pago_15"
    elif dia_actual == penultimo_dia:
        return "recordatorio_ultimo"
    elif dia_actual == ultimo_dia:
        return "pago_ultimo"
    else:
        return None

async def enviar_notificacion():
    """Función que envía la notificación según el tipo de día"""
    try:
        tipo_notificacion = obtener_tipo_notificacion()
        
        if tipo_notificacion is None:
            logger.info("Hoy no corresponde enviar notificación")
            return
            
        fecha_actual = datetime.now()
        dia = fecha_actual.day
        mes = fecha_actual.month
        año = fecha_actual.year
        
        # Determinar el mensaje según el tipo de notificación
        if tipo_notificacion == "recordatorio_15":
            emoji_urgencia = "⚠️"
            titulo = "RECORDATORIO DE PAGO"
            mensaje_urgencia = "🚨 **MAÑANA (15) TOCA PAGAR** 🚨"
            fecha_pago = f"{15:02d}/{mes:02d}/{año}"
            
        elif tipo_notificacion == "pago_15":
            emoji_urgencia = "🔥"
            titulo = "¡PAGO HOY!"
            mensaje_urgencia = "🚨 **HOY TOCA PAGAR** 🚨"
            fecha_pago = f"{dia:02d}/{mes:02d}/{año}"
            
        elif tipo_notificacion == "recordatorio_ultimo":
            emoji_urgencia = "⚠️"
            titulo = "RECORDATORIO DE PAGO"
            mensaje_urgencia = "🚨 **MAÑANA (ÚLTIMO DÍA) TOCA PAGAR** 🚨"
            ultimo_dia = obtener_ultimo_dia_mes(año, mes)
            fecha_pago = f"{ultimo_dia:02d}/{mes:02d}/{año}"
            
        elif tipo_notificacion == "pago_ultimo":
            emoji_urgencia = "🔥"
            titulo = "¡PAGO HOY!"
            mensaje_urgencia = "🚨 **HOY (ÚLTIMO DÍA) TOCA PAGAR** 🚨"
            fecha_pago = f"{dia:02d}/{mes:02d}/{año}"
        
        # Formatear mensaje
        mensaje = f"""{emoji_urgencia} **{titulo}**

👤 **David A. Chentes**

{mensaje_urgencia}

💰 **MONTO** ➡️ 400 USDT

🌐 **RED** ➡️ TRC20
💎 **WALLET** ➡️ {DAVID_TRON_TRC20}

🌐 **RED** ➡️ ERC20  
💎 **WALLET** ➡️ {DAVID_ETHEREUM_ERC20}

📅 **FECHA LÍMITE DE PAGO** ➡️ {fecha_pago}"""
        
        # Enviar mensaje
        await bot.send_message(chat_id=CHAT_ID, text=mensaje, parse_mode='Markdown')
        logger.info(f"Notificación enviada: {tipo_notificacion}")
        
    except TelegramError as e:
        logger.error(f"Error al enviar mensaje: {e}")
    except Exception as e:
        logger.error(f"Error inesperado: {e}")

async def test_forzado(tipo_test):
    """Función para probar un tipo específico de notificación"""
    try:
        fecha_actual = datetime.now()
        dia = fecha_actual.day
        mes = fecha_actual.month
        año = fecha_actual.year
        
        if tipo_test == "recordatorio_15":
            emoji_urgencia = "⚠️"
            titulo = "RECORDATORIO DE PAGO"
            mensaje_urgencia = "🚨 **MAÑANA (15) TOCA PAGAR** 🚨"
            fecha_pago = f"{15:02d}/{mes:02d}/{año}"
            
        elif tipo_test == "pago_15":
            emoji_urgencia = "🔥"
            titulo = "¡PAGO HOY!"
            mensaje_urgencia = "🚨 **HOY TOCA PAGAR** 🚨"
            fecha_pago = f"{15:02d}/{mes:02d}/{año}"
            
        elif tipo_test == "recordatorio_ultimo":
            emoji_urgencia = "⚠️"
            titulo = "RECORDATORIO DE PAGO"
            mensaje_urgencia = "🚨 **MAÑANA (ÚLTIMO DÍA) TOCA PAGAR** 🚨"
            ultimo_dia = obtener_ultimo_dia_mes(año, mes)
            fecha_pago = f"{ultimo_dia:02d}/{mes:02d}/{año}"
            
        elif tipo_test == "pago_ultimo":
            emoji_urgencia = "🔥"
            titulo = "¡PAGO HOY!"
            mensaje_urgencia = "🚨 **HOY (ÚLTIMO DÍA) TOCA PAGAR** 🚨"
            ultimo_dia = obtener_ultimo_dia_mes(año, mes)
            fecha_pago = f"{ultimo_dia:02d}/{mes:02d}/{año}"
        
        mensaje = f"""{emoji_urgencia} **{titulo}**

👤 **David A. Chentes**

{mensaje_urgencia}

💰 **MONTO** ➡️ 400 USDT

🌐 **RED** ➡️ TRC20
💎 **WALLET** ➡️ {DAVID_TRON_TRC20}

🌐 **RED** ➡️ ERC20  
💎 **WALLET** ➡️ {DAVID_ETHEREUM_ERC20}

📅 **FECHA LÍMITE DE PAGO** ➡️ {fecha_pago}"""
        
        await bot.send_message(chat_id=CHAT_ID, text=mensaje, parse_mode='Markdown')
        print(f"✅ Prueba de '{tipo_test}' enviada correctamente!")
        
    except Exception as e:
        print(f"❌ Error en la prueba: {e}")

def job():
    """Función wrapper para schedule"""
    asyncio.run(enviar_notificacion())

async def test_bot():
    """Función para probar que el bot funciona"""
    try:
        tipo = obtener_tipo_notificacion()
        if tipo:
            await enviar_notificacion()
            print(f"✅ Prueba exitosa! Notificación tipo '{tipo}' enviada correctamente.")
        else:
            print("ℹ️ Hoy no corresponde enviar notificación (no es día 14, 15, penúltimo o último del mes)")
    except Exception as e:
        print(f"❌ Error en la prueba: {e}")

def main():
    print("🤖 Bot de Notificación de Pago iniciado...")
    print("Notificará los días: 14, 15, penúltimo y último de cada mes")
    print("Presiona Ctrl+C para detener el bot")
    
    # Programar revisión diaria a las 8:00 AM
    schedule.every().day.at("08:00").do(job)
    
    # Bucle principal
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Revisar cada minuto
    except KeyboardInterrupt:
        print("\n🛑 Bot detenido por el usuario")

if __name__ == "__main__":
    print("🧪 MODO DE PRUEBA")
    print("Selecciona una opción:")
    print("1. Prueba automática (según fecha actual)")
    print("2. Probar recordatorio día 15")
    print("3. Probar pago día 15") 
    print("4. Probar recordatorio último día")
    print("5. Probar pago último día")
    print("6. Ejecutar bot en modo normal")
    
    try:
        opcion = input("\nIngresa el número de opción (1-6): ")
        
        if opcion == "1":
            asyncio.run(test_bot())
        elif opcion == "2":
            asyncio.run(test_forzado("recordatorio_15"))
        elif opcion == "3":
            asyncio.run(test_forzado("pago_15"))
        elif opcion == "4":
            asyncio.run(test_forzado("recordatorio_ultimo"))
        elif opcion == "5":
            asyncio.run(test_forzado("pago_ultimo"))
        elif opcion == "6":
            main()
        else:
            print("❌ Opción no válida")
            
    except KeyboardInterrupt:
        print("\n🛑 Programa terminado")