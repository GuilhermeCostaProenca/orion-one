import speech_recognition as sr
import requests

# URL da rota que recebe o comando
URL = "http://127.0.0.1:5000/enviar"

def ouvir_comando():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙️ ORION ouvindo... fale agora:")
        audio = recognizer.listen(source)

        try:
            texto = recognizer.recognize_google(audio, language="pt-BR")
            print(f"🧠 Você disse: {texto}")

            # Envia o comando como um formulário (mimetype: application/x-www-form-urlencoded)
            response = requests.post(URL, data={'mensagem': texto})

            if response.status_code in [200, 302]:
                print("✅ Comando enviado com sucesso.")
            else:
                print(f"❌ Erro {response.status_code}: {response.text}")

        except sr.UnknownValueError:
            print("😕 Não entendi o que foi dito.")
        except sr.RequestError:
            print("❌ Erro ao conectar com o serviço de reconhecimento.")

if __name__ == "__main__":
    ouvir_comando()
