import sys
from datetime import date, datetime
import sounddevice as sd
import speech_recognition as sr
import pyttsx3

# Đảm bảo in tiếng Việt không lỗi trên Terminal Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Khởi tạo giọng nói và não robot
robot_mouth = pyttsx3.init()
robot_brain = ""
you = ""  # Khởi tạo mặc định rỗng

while True:
    # Cấu hình thu âm
    samplerate = 16000
    duration = 4  # Số giây lắng nghe

    print("Robot: I'm listening... (Hãy nói gì đó vào micro)")

    # 1. PHẦN NGHE: Thu âm từ micro
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype="int16")
    sd.wait()

    print("Robot: Đang nhận dạng giọng nói...")

    robot_ear = sr.Recognizer()
    audio = sr.AudioData(audio_data.tobytes(), samplerate, 2)

    try:
        # Nhận diện giọng nói
        you = robot_ear.recognize_google(audio, language="vi-VN")
        print(f"You: {you}")
    except sr.UnknownValueError:
        you = ""
        print("Robot: Không nhận dạng được âm thanh.")
    except sr.RequestError as e:
        you = ""
        print(f"Robot: Lỗi mạng Google Speech ({e})")


    # 2. PHẦN HIỂU: Xử lý nội dung bạn vừa nói
    you_lower = you.lower()  # Chuyển về chữ thường để so sánh linh hoạt

    if "hello" in you_lower or "chào" in you_lower:
        robot_brain = "chào bạn"
    elif "văn hồ" in you_lower:
        robot_brain = "rất vui được gặp bạn"
    elif "giờ" in you_lower or "time" in you_lower:
        now = datetime.now()
        robot_brain = now.strftime("bây giờ là %H giờ %M phút %S giây")
    elif "today" in you_lower or "hôm nay" in you_lower or "ngày" in you_lower:
        now = datetime.now()
        robot_brain = now.strftime("hôm nay là ngày %d tháng %m năm %Y")
    elif you == "":
        robot_brain = "bạn có gì muốn hỏi tôi không"
    elif "tạm biệt" in you_lower or "bye" in you_lower:
        robot_brain = "tạm biệt bạn, hẹn gặp lại"
        break  # Thoát vòng lặp nếu bạn nói tạm biệt
    else:
        robot_brain = "tôi không hiểu bạn nói gì"


    # 3. PHẦN NÓI: Robot phản hồi
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()

