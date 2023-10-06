import speech_recognition as sr
# Tạo đối tượng recognizer
recognizer = sr.Recognizer()

# Sử dụng microphone để lắng nghe âm thanh
with sr.Microphone() as source:
# with sr.AudioFile(r"E:\HHP\S_to_T\KMYLCSD.wav") as source:
    print("Hãy nói gì đó...")
    audio = recognizer.listen(source)

    try:
        print("Đang chuyển đổi...")
        # Sử dụng Google Web Speech API để chuyển đổi âm thanh thành văn bản
        text = recognizer.recognize_google(audio, language="vi-VN")
        print("Đoạn văn bản đã nhận dạng:", text)
    except sr.UnknownValueError:
        print("Không thể nhận dạng giọng nói.")
    except sr.RequestError as e:
        print("Lỗi trong quá trình kết nối đến Google Web Speech API; {0}".format(e))
# import speech_recognition as sr

# # Tạo một đối tượng recognizer
# recognizer = sr.Recognizer()

# # Đường dẫn đến tệp âm thanh MP3
# audio_file_path =r"E:\HHP\Tacotron2\KMYLCSD.wav"

# # Mở tệp âm thanh
# with sr.AudioFile(audio_file_path) as source:
#     # Đọc dữ liệu từ tệp âm thanh
#     audio_data = recognizer.record(source)

#     try:
#         # Sử dụng Google Web Speech API để chuyển đổi giọng nói thành văn bản
#         text = recognizer.recognize_google(audio_data, language="vi-VN")
#         print("Văn bản đã nhận dạng:", text)
#     except sr.UnknownValueError:
#         print("Không thể nhận dạng giọng nói")
#     except sr.RequestError as e:
#         print("Lỗi kết nối tới API:", e)
