import tensorflow as tf
import numpy as np

# Corpus de preguntas y respuestas para la conversación básica en español
corpus = [
    ("Hola", "¡Hola! ¿En qué puedo ayudarte?"),
    ("¿Cómo estás?", "Estoy aquí para ayudarte, ¿qué necesitas?"),
    ("¿Cuál es tu nombre?", "Me llamo ChatBot, ¿y tú?"),
    ("¿En qué puedo ayudarte?", "Estoy aquí para responder tus preguntas, ¡dispara!"),
    ("¿Qué haces?", "Estoy esperando con ansias tus preguntas ingeniosas."),
    ("¿Eres real?", "Soy tan real como una ilusión en tu mente."),
    ("¿Qué sabes hacer?", "Soy experto en generar respuestas fascinantes a tus preguntas."),
    ("¿Crees en fantasmas?", "Solo creo en fantasmas si son errores en el código."),
    ("¿Tienes amigos?", "Mis únicos amigos son los bits y bytes en mi memoria."),
    ("Adiós", "¡Hasta luego! Si tienes más preguntas, estaré aquí."),
]

# Crear un vocabulario y mapeo de palabras
vocab = sorted(set(word for question, answer in corpus for word in question.split() + answer.split()))
word_to_idx = {word: idx for idx, word in enumerate(vocab)}
idx_to_word = np.array(vocab)

# Convertir las preguntas en secuencias de índices
question_sequences = [np.array([word_to_idx[word] for word in question.split()]) for question, _ in corpus]
max_seq_length = max(len(seq) for seq in question_sequences)
question_sequences = tf.keras.preprocessing.sequence.pad_sequences(question_sequences, maxlen=max_seq_length)

# Convertir las respuestas en secuencias de índices
answer_sequences = [np.array([word_to_idx[word] for word in answer.split()]) for _, answer in corpus]
answer_sequences = tf.keras.preprocessing.sequence.pad_sequences(answer_sequences, maxlen=max_seq_length)

# Dividir las secuencias en entrada (X) y salida (y)
X = question_sequences
y = answer_sequences

# Definir el modelo de lenguaje
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(len(vocab), 128, input_length=max_seq_length),
    tf.keras.layers.LSTM(256, return_sequences=True),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(len(vocab), activation='softmax')
])
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Entrenar el modelo
model.fit(X, y, batch_size=2, epochs=50)

# Función para llevar a cabo la conversación
def converse():
    print("¡Hola! Soy un ChatBot dispuesto a responder tus preguntas.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'adios':
            print("ChatBot: ¡Hasta luego! Si tienes más preguntas, estaré aquí.")
            break
        response = generate_response(user_input)
        print("ChatBot:", response)

# Función para generar respuestas
def generate_response(question, temperature=0.7):
    seq = [word_to_idx.get(word, 0) for word in question.split()];
    seq = tf.keras.preprocessing.sequence.pad_sequences([seq], maxlen=max_seq_length);
    predicted_probs = model.predict(seq)[0];
    
    predicted_idx = np.argmax(predicted_probs, axis=-1);
    answer = " ".join(idx_to_word[idx] for idx in predicted_idx);
    return answer;

# Iniciar la conversación
converse()
