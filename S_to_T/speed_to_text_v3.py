from pydub import AudioSegment
import numpy as np
import speech_recognition as sr

# Đường dẫn đến tệp ghi âm
audio_file_path = r"E:\HHP\Tacotron2\KMYLCSD.wav"

# Ngưỡng cường độ âm để xác định các khoảng
amplitude_threshold = 1000

# Đọc tệp ghi âm
audio = AudioSegment.from_wav(audio_file_path)

# Chuyển đổi âm thanh thành mảng numpy để dễ xử lý
samples = np.array(audio.get_array_of_samples())

# Tìm vị trí các điểm chuyển đổi giữa các phần dựa trên cường độ âm
change_points = np.where(samples > amplitude_threshold)[0]

# Chia đoạn âm thanh dựa trên các điểm chuyển đổi cường độ âm
segments = []
start = 0
for idx in change_points:
    segment = audio[start:idx]
    if len(segment) > 0:
        segments.append(segment)
    start = idx

# Sử dụng recognizer để chuyển đổi từng đoạn thành văn bản
recognizer = sr.Recognizer()
for i, segment in enumerate(segments):
    with sr.AudioFile(segment.export(format="wav")) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="vi-VN")
            print(f"Đoạn {i}: {text}")
        except sr.UnknownValueError:
            print(f"Không thể nhận dạng giọng nói cho đoạn {i}")
        except sr.RequestError as e:
            print(f"Lỗi kết nối tới API cho đoạn {i}: {e}")
