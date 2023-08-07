from telegram.ext import Updater, MessageHandler, CallbackContext, filters
from telegram import Update

TOKEN = "6545013009:AAEs67tClClVppeQGIFmCSqAa3ImTl-yFEc"

# Definimos una clase llamada TextMessageFilter que hereda de filters.
# Esta clase se utilizará para filtrar mensajes de texto que no son comandos.
class TextMessageFilter(filters):
    # Implementamos el método filter para determinar si el mensaje debe ser aceptado o no.
    def filter(self, message):
        # Verificamos si el mensaje es de texto y no comienza con '/'
        return message.text and not message.text.startswith('/')

# Definimos la función de manejo para responder a los mensajes.
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    # Imprimimos el ID del chat desde el que se recibió el mensaje.
    print(update.message.chat.id)
    # Respondemos al mensaje con el mismo texto que recibimos.
    update.message.reply_text(update.message.text)

def main() -> None:
    """Inicia el bot."""
    # Creamos una instancia de Updater y pasamos el token del bot.
    updater = Updater(TOKEN)
    # Obtenemos el objeto dispatcher para registrar los manejadores de eventos.
    dispatcher = updater.dispatcher

    # Creamos una instancia de TextMessageFilter.
    text_filter = TextMessageFilter()
    # Agregamos un manejador de mensajes que utiliza el filtro de mensajes de texto personalizado.
    # Cuando el filtro aprueba un mensaje, se activa la función de manejo "echo".
    dispatcher.add_handler(MessageHandler(text_filter, echo))

    # Iniciamos la recepción de actualizaciones del bot.
    updater.start_polling()
    # Mantenemos el proceso en ejecución hasta que se detenga manualmente.
    updater.idle()

if __name__ == '__main__':
    main()
