<div align="center">
  <img src="https://raw.githubusercontent.com/David-Che/Resources-Git/main/bots/notificaciones-de-pago/logo.png" alt="Project Logo" width="150">
  <h1 align="center">🤖 Bot de Notificaciones de Pago para Telegram</h1>
  <p align="center">
    Un bot de Telegram eficiente y automatizado que te recordará las fechas de pago importantes, asegurando que nunca más te olvides de una transacción.
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
    <img src="https://img.shields.io/github/last-commit/David-Che/bot_telegram_fecha?style=for-the-badge" alt="Last Commit">
  </p>
</div>

---

## 🌟 Descripción

Este bot de Telegram, desarrollado en Python, está diseñado para enviar notificaciones automáticas en fechas de pago clave. Su lógica se centra en dos momentos importantes del mes: el día 15 y el último día.

- **Día 14**: Envía un recordatorio de que el pago es mañana (día 15).
- **Día 15**: Envía una notificación de que el pago es HOY.
- **Penúltimo día del mes**: Envía un recordatorio de que el pago es mañana (último día).
- **Último día del mes**: Envía una notificación de que el pago es HOY.

## ✨ Características Principales

- 📅 **Detección Automática de Fechas**: Identifica automáticamente los días 14, 15, penúltimo y último de cada mes.
- 🗓️ **Cálculo Dinámico**: Maneja sin problemas meses con 28, 29, 30 o 31 días.
- 💬 **Mensajes Personalizados**: Envía mensajes diferentes para recordatorios y días de pago.
- 💼 **Soporte para Múltiples Wallets**: Configurado para mostrar direcciones de TRC20 y ERC20.
- 🧪 **Modo de Pruebas Integrado**: Permite probar cada tipo de notificación de forma manual.
- 📈 **Logging de Actividad**: Registra todas las acciones para un seguimiento sencillo.
- ⏰ **Ejecución Programada**: Se ejecuta automáticamente todos los días a una hora configurable.

## 🚀 Puesta en Marcha

Sigue estos pasos para tener tu bot funcionando en minutos.

### Prerrequisitos

- Python 3.7 o superior.
- Una cuenta de Telegram.

### 1. Clonar el Repositorio

```bash
git clone https://github.com/David-Che/bot_telegram_fecha.git
cd bot_telegram_fecha
```

### 2. Configurar el Entorno Virtual

Es una buena práctica usar un entorno virtual para aislar las dependencias del proyecto.

```bash
# Crear el entorno
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate
```

### 3. Instalar Dependencias

Instala todas las librerías necesarias con un solo comando:

```bash
pip install -r requirements.txt
```

### 4. Configurar tus Credenciales

Antes de ejecutar el bot, necesitas configurarlo con tus propios datos.

#### a. Crear un Bot en Telegram
1.  Abre Telegram y busca a **@BotFather**.
2.  Envía el comando `/newbot` y sigue sus instrucciones.
3.  Al finalizar, **guarda el token** que te proporcionará.

#### b. Obtener tu Chat ID
1.  Busca el bot que acabas de crear en Telegram y envíale un mensaje.
2.  Abre tu navegador y visita la siguiente URL (reemplaza `<TU_TOKEN>` con tu token):
    ```
    https://api.telegram.org/bot<TU_TOKEN>/getUpdates
    ```
3.  En la respuesta, busca el `id` dentro del objeto `chat`. Ese es tu `CHAT_ID`.

#### c. Actualizar el Script
Abre el archivo `bot_fecha.py` y modifica las siguientes variables con tus datos:

```python
# CONFIGURACIÓN - TUS DATOS
BOT_TOKEN = "7873505067:AAG7aeM7BKHI8cnH_7ztSddCE3N07dm9In8" # ⬅️ Pega tu token aquí
CHAT_ID = "-1002712341833" # ⬅️ Pega tu Chat ID aquí

DAVID_TRON_TRC20 = "TSVgxtNpWpdKww68NHZPR4AHx8r2nDvKA6" # ⬅️ Tu wallet TRC20
DAVID_ETHEREUM_ERC20 = "0xd8d1ca8b1d7236b338fc370ad677ff2e7131759b" # ⬅️ Tu wallet ERC20
```

## ▶️ Cómo Usar el Bot

Puedes ejecutar el bot de dos maneras: en modo de prueba o en modo de producción.

### Modo de Prueba (Interactivo)

Este modo es ideal para verificar que todo funciona correctamente.

```bash
python bot_fecha.py
```

Verás un menú interactivo que te permitirá probar cada tipo de notificación:

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

### Modo de Producción (Automático)

Para que el bot se ejecute de forma continua y envíe las notificaciones automáticamente, elige la **opción 6**.

```
🤖 Bot de Notificación de Pago iniciado...
Notificará los días: 14, 15, penúltimo y último de cada mes
Presiona Ctrl+C para detener el bot
```
El bot revisará la fecha todos los días a las **08:00 AM**.

## ⚙️ Personalización

### Cambiar la Hora de Envío

Puedes cambiar la hora a la que se envía la notificación modificando esta línea en `bot_fecha.py`:

```python
# Programar revisión diaria a las 8:00 AM
schedule.every().day.at("08:00").do(job)  # Cambia "08:00" a la hora que prefieras (formato 24h)
```

### Modificar el Mensaje

El contenido de los mensajes se puede editar directamente en las funciones `enviar_notificacion` y `test_forzado`. Por ejemplo, para cambiar el monto:

```python
💰 **MONTO** ➡️ 400 USDT  # Cambia 400 por el nuevo monto
```

## ☁️ Despliegue en un Servidor

Para que el bot funcione 24/7, necesitas desplegarlo en un servidor.

### Usando `screen` en un VPS

`screen` es una herramienta que te permite mantener procesos corriendo en segundo plano.

1.  Conéctate a tu servidor.
2.  Inicia una nueva sesión de `screen`:
    ```bash
    screen -S bot-telegram
    ```
3.  Navega a la carpeta del proyecto, activa el entorno virtual y ejecuta el bot:
    ```bash
    cd bot_telegram_fecha
    source venv/bin/activate
    python bot_fecha.py
    # Elige la opción 6
    ```
4.  Para salir de la sesión sin detener el bot, presiona `Ctrl+A` y luego `D`.

Para volver a la sesión más tarde, usa `screen -r bot-telegram`.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el bot, por favor sigue estos pasos:

1.  Haz un **Fork** de este repositorio.
2.  Crea una nueva rama (`git checkout -b feature/MejoraIncreible`).
3.  Realiza tus cambios y haz **Commit** (`git commit -m 'Añadir MejoraIncreible'`).
4.  Haz **Push** a tu rama (`git push origin feature/MejoraIncreible`).
5.  Abre un **Pull Request**.