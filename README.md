# 🤖 Bot de Telegram - Notificaciones de Pago Automáticas

Bot de Telegram desarrollado en Python que envía notificaciones automáticas de recordatorios y fechas de pago cada 15 días (día 15 y último día de cada mes).

## 📋 Descripción

Este bot está diseñado para automatizar las notificaciones de pago con la siguiente lógica:

- **Día 14**: Recordatorio de que mañana (día 15) toca pagar
- **Día 15**: Notificación de que HOY toca pagar
- **Penúltimo día del mes**: Recordatorio de que mañana (último día) toca pagar
- **Último día del mes**: Notificación de que HOY toca pagar

## 🚀 Características

- ✅ **Detección automática** de fechas de pago (día 15 y último día del mes)
- ✅ **Cálculo dinámico** del último día de cada mes (maneja 28, 29, 30 y 31 días)
- ✅ **Mensajes diferenciados** para recordatorios vs. días de pago
- ✅ **Múltiples wallets** (TRC20 y ERC20)
- ✅ **Sistema de pruebas** integrado
- ✅ **Logging** completo de actividades
- ✅ **Ejecución automática** diaria

## 📦 Instalación

### Prerrequisitos

- Python 3.7 o superior
- Una cuenta de Telegram
- Acceso para crear bots de Telegram

### 1. Clonar el proyecto

```bash
git clone <url-del-repositorio>
cd bot_telegram_fecha
```

### 2. Crear entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install python-telegram-bot schedule
```

### 4. Configuración del Bot de Telegram

#### Crear el Bot:
1. Busca **@BotFather** en Telegram
2. Envía `/newbot`
3. Sigue las instrucciones para crear tu bot
4. Guarda el **token** que te proporciona

#### Obtener tu Chat ID:
1. Envía cualquier mensaje a tu bot
2. Visita: `https://api.telegram.org/bot<TU_TOKEN>/getUpdates`
3. Busca tu Chat ID en la respuesta JSON

### 5. Configurar el archivo

Edita las siguientes variables en `bot_fecha.py`:

```python
BOT_TOKEN = "tu_token_aqui"
CHAT_ID = "tu_chat_id_aqui"
DAVID_TRON_TRC20 = "tu_wallet_trc20"
DAVID_ETHEREUM_ERC20 = "tu_wallet_erc20"
```

## 🎯 Uso

### Modo de Prueba

```bash
python bot_fecha.py
```

Aparecerá un menú con las siguientes opciones:

```
🧪 MODO DE PRUEBA
Selecciona una opción:
1. Prueba automática (según fecha actual)
2. Probar recordatorio día 15
3. Probar pago día 15
4. Probar recordatorio último día
5. Probar pago último día
6. Ejecutar bot en modo normal
```

### Modo Automático

Selecciona la **opción 6** para que el bot se ejecute automáticamente y envíe notificaciones todos los días a las 8:00 AM (solo en las fechas correspondientes).

## 📱 Tipos de Mensajes

### Recordatorio (Día 14)
```
⚠️ RECORDATORIO DE PAGO

👤 David A. Chentes

🚨 MAÑANA (15) TOCA PAGAR 🚨

💰 MONTO ➡️ 400 USDT

🌐 RED ➡️ TRC20
💎 WALLET ➡️ TSVgxtNpWpdKww68NHZPR4AHx8r2nDvKA6

🌐 RED ➡️ ERC20
💎 WALLET ➡️ 0xd8d1ca8b1d7236b338fc370ad677ff2e7131759b

📅 FECHA LÍMITE DE PAGO ➡️ 15/08/2025
```

### Día de Pago (Día 15)
```
🔥 ¡PAGO HOY!

👤 David A. Chentes

🚨 HOY TOCA PAGAR 🚨

💰 MONTO ➡️ 400 USDT

🌐 RED ➡️ TRC20
💎 WALLET ➡️ TSVgxtNpWpdKww68NHZPR4AHx8r2nDvKA6

🌐 RED ➡️ ERC20
💎 WALLET ➡️ 0xd8d1ca8b1d7236b338fc370ad677ff2e7131759b

📅 FECHA LÍMITE DE PAGO ➡️ 15/08/2025
```

## ⚙️ Configuración Avanzada

### Cambiar Hora de Envío

Modifica la línea 188 en `bot_fecha.py`:

```python
schedule.every().day.at("08:00").do(job)  # Cambiar "08:00" por la hora deseada
```

### Cambiar Monto

Modifica la línea correspondiente en las funciones de mensaje:

```python
💰 **MONTO** ➡️ 400 USDT  # Cambiar 400 por el monto deseado
```

### Agregar Más Wallets

Puedes agregar más direcciones de wallet editando las variables al inicio del archivo.

## 📁 Estructura del Proyecto

```
bot_telegram_fecha/
│
├── bot_fecha.py          # Archivo principal del bot
├── README.md            # Este archivo
└── requirements.txt     # Dependencias (opcional)
```

## 🚀 Despliegue en Servidor

### Opción 1: VPS/Servidor Propio

1. Sube el archivo a tu servidor
2. Instala Python y las dependencias
3. Ejecuta el bot en modo normal (opción 6)
4. Usa `screen` o `tmux` para mantenerlo ejecutándose:

```bash
screen -S bot_telegram
python bot_fecha.py
# Seleccionar opción 6
# Ctrl+A, D para desconectar sin cerrar
```

### Opción 2: Servicios en la Nube

#### Heroku
1. Crea un `Procfile`: `worker: python bot_fecha.py`
2. Sube a tu repositorio de Heroku
3. Configura las variables de entorno

#### Railway/Render
Similar proceso con sus respectivas configuraciones.

## 🔧 Troubleshooting

### Error de Token
```
❌ Error: Unauthorized
```
**Solución**: Verifica que el token del bot sea correcto.

### Error de Chat ID
```
❌ Error: Chat not found
```
**Solución**: Asegúrate de haber enviado al menos un mensaje al bot antes de obtener el Chat ID.

### Bot no envía mensajes
1. Verifica la fecha actual con las opciones de prueba
2. Revisa los logs en consola
3. Confirma que el bot esté ejecutándose en modo normal (opción 6)

## 📝 Logs

El bot genera logs informativos que te ayudan a monitorear su funcionamiento:

```
2025-08-03 08:00:01 - __main__ - INFO - Notificación enviada: recordatorio_15
2025-08-03 08:00:01 - __main__ - INFO - Bot funcionando correctamente
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Si tienes problemas o preguntas:

1. Revisa la sección de Troubleshooting
2. Verifica que todas las dependencias estén instaladas
3. Asegúrate de que la configuración sea correcta

## 🔄 Changelog

### v1.0.0
- ✅ Implementación inicial
- ✅ Sistema de notificaciones automáticas
- ✅ Soporte para múltiples wallets
- ✅ Sistema de pruebas integrado
- ✅ Detección automática de fechas

---