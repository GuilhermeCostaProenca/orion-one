import pyttsx3

def falar(texto):
    print(f"🗣️ ORION dizendo: {texto}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)  # Velocidade da fala
    engine.setProperty('volume', 1.0)  # Volume
    engine.say(texto)
    engine.runAndWait()

# Teste
if __name__ == "__main__":
    falar("Comando salvo com sucesso, Guilherme.")
