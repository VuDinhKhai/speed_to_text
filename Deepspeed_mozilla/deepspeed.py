import deepspeech
import wave
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
# Đường dẫn đến tệp âm thanh WAV
wav_file_path = r"E:\HHP\Deepspeed_mozilla\00006.wav"
# Đường dẫn đến mô hình đã được tải về
model_path = r"E:\HHP\Deepspeed_mozilla\deepspeech-0.9.3-models.pbmm"

# Tạo đối tượng DeepSpeech với mô hình đã tải về
ds = deepspeech.Model(model_path)

# Đọc file âm thanh hoặc sử dụng microphone để lắng nghe âm thanh
# audio_data là dữ liệu âm thanh đọc từ file hoặc microphone

# Chuyển đổi âm thanh thành văn bản
with wave.open(wav_file_path, 'rb') as wav_file:
    # Lấy thông tin về tần số lấy mẫu và độ phân giải
    sample_rate = wav_file.getframerate()
    print(sample_rate)
    sample_width = wav_file.getsampwidth()
    print(sample_width)
    # Đọc dữ liệu âm thanh
    audio_data = wav_file.readframes(wav_file.getnframes())
# print(audio_data)
audio_data_bytes = bytearray(audio_data)
# print(audio_data_bytes)
text = ds.stt(audio_data_bytes)
print("Đoạn văn bản đã nhận dạng:", text)
