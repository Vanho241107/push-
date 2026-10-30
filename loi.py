import time
import os

FILE_MAY = "tin_hieu_may_smt.txt"

def doi_trang_thai(trang_thai):
    with open(FILE_MAY, "w", encoding="utf-8") as f:
        f.write(trang_thai)
    print(f"👉 Đã giả lập trạng thái: {trang_thai}")

if __name__ == "__main__":
    print("=== CHƯƠNG TRÌNH GIẢ LẬP LỖI MÁY SMT ===")
    print("Hệ thống sẽ tự động đổi trạng thái máy sau mỗi 10 giây để bạn test code.")
    print("--------------------------------------------------")
    
    try:
        # 1. Ban đầu máy chạy bình thường
        doi_trang_thai("BINH_THUONG")
        time.sleep(10)
        
        # 2. Giả lập lỗi hết linh kiện linh kiện SMT
        doi_trang_thai("HẾT CUỘN TRỞ 10K - LINE 2 DỪNG")
        time.sleep(15) # Đợi bạn bấm tắt popup cảnh báo
        
        # 3. Kỹ thuật nạp lại liệu, máy chạy lại bình thường
        doi_trang_thai("BINH_THUONG")
        time.sleep(10)
        
        # 4. Giả lập lỗi kẹt mạch (PCB Jam)
        doi_trang_thai("KẸT MẠCH TẠI BĂNG TẢI ĐẦU VÀO")
        time.sleep(15)
        
        # 5. Máy hoạt động bình thường trở lại
        doi_trang_thai("BINH_THUONG")
        print("\n Thử nghiệm kết thúc!")
        
    except KeyboardInterrupt:
        print("\n🛑 Dừng giả lập.")
