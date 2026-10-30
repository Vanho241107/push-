import sys
import os
import time
import winsound
import ctypes
from datetime import datetime

# Đảm bảo in tiếng Việt chuẩn trong Terminal Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# BƯỚC 1: CẤU HÌNH THÔNG SỐ CÁC MÁY
TEN_MAY   = "MÁY DÁN SMT 01"
IP_MAY    = "192.168.1.50"
FILE_LOG  = os.path.join(os.path.expanduser("~"), "Desktop", "nhat_ky_may_smt.txt")
FILE_MAY  = "tin_hieu_may_smt.txt"

TEN_MAY   = "MÁY DÁN SMT 02"  # Tên máy SMT trong xưởng
IP_MAY    = "192.168.1.52"   # Địa chỉ IP của máy SMT trong xưởng
FILE_LOG  = os.path.join(os.path.expanduser("~"), "Desktop", "nhat_ky_may_smt.txt")
FILE_MAY  = "tin_hieu_may_smt.txt"  # Nơi nhận tín hiệu lỗi từ máy SMT


# ==============================================================
# BƯỚC 2: HÀM BÁO ĐỘNG KHI MÁY DỪNG HOẶC HẾT LIỆU
# ==============================================================
def bao_dong(loi):
    gio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # 1. Ghi lại vào file nhật ký trên Desktop
    with open(FILE_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{gio}] , 🚨 DỪNG MÁY , {TEN_MAY} , Lỗi: {loi}\n")

    print(f"\n🚨 [{gio}] PHÁT HIỆN LỖI: {TEN_MAY} - {loi}")

    # 2. Hú còi 3 tiếng qua loa laptop
    for _ in range(3):
        winsound.Beep(2000, 200)

    # 3. Tự động bật mở file Notepad lên màn hình
    try:
        os.startfile(FILE_LOG)
    except Exception:
        pass

    # 4. Bật hộp thoại cảnh báo đè lên màn hình
    noi_dung = (
        f"🚨 {TEN_MAY} ĐÃ DỪNG ĐỘT NGỘT!\   n\n"
        f"⚠️ Nguyên nhân : {loi}\n"
        f"⏰ Thời gian   : {gio}\n\n"
        f"👉 File nhật ký đã mở. Đội kỹ thuật hãy xử lý gấp!"
    )
    ctypes.windll.user32.MessageBoxW(0, noi_dung, "⚠️ CẢNH BÁO SỰ CỐ NHÀ MÁY", 0x10 | 0x40000)


# ==============================================================
# BƯỚC 3: VÒNG LẶP TỰ ĐỘNG GIÁM SÁT 24/7
# ==============================================================
def chay_giam_sat():
    print("=" * 55)
    print(f"🤖 ĐANG TỰ ĐỘNG GIÁM SÁT: {TEN_MAY}")
    print(f"📡 Địa chỉ IP xưởng : {IP_MAY}")
    print(f"📂 File nhật ký     : nhat_ky_su_co.txt (trên Desktop)")
    print("💡 Mẹo: Nhấn [Ctrl + C] bất cứ lúc nào để dừng.")
    print("=" * 55 + "\n")

    trang_thai_cu = "BINH_THUONG"

    while True:
        # Tự động kiểm tra tín hiệu từ máy SMT
        if os.path.exists(FILE_MAY):
            with open(FILE_MAY, "r", encoding="utf-8") as f:
                trang_thai_moi = f.read().strip()

            # Khi phát hiện máy có lỗi mới -> Kích hoạt báo động ngay
            if trang_thai_moi != trang_thai_cu:
                if trang_thai_moi != "BINH_THUONG" and trang_thai_moi != "":
                    bao_dong(trang_thai_moi)
                else:
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] 🟢 Máy SMT đã hoạt động bình thường trở lại.")
                
                trang_thai_cu = trang_thai_moi

        time.sleep(1)


if __name__ == "__main__":
    try:
          chay_giam_sat()
    except KeyboardInterrupt:
        print("\n🛑 Đã tắt hệ thống giám sát!")