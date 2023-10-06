from pydub import AudioSegment
import numpy as np
import speech_recognition as sr

# Đường dẫn đến tệp ghi âm
audio_file_path = r"E:\HHP\Tacotron2\KMYLCSD.wav"

# Độ lớn của đoạn ngắt nghỉ (miligiây)
silence_threshold = -20

# Đọc tệp ghi âm
audio = AudioSegment.from_wav(audio_file_path)

# Chuyển đổi âm thanh thành mảng numpy để dễ xử lý
samples = np.array(audio.get_array_of_samples())

# Tìm vị trí các điểm ngắt nghỉ
silence_indices = np.where(samples < silence_threshold)[0]

# Chia đoạn âm thanh dựa trên ngắt nghỉ
segments = []
start = 0
for idx in silence_indices:
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

# for i in range(len(audio) // segment_length):
#     segment_path = f"{output_folder}segment_{i}.wav"
#     if os.path.exists(segment_path):
#         os.remove(segment_path)