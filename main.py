import requests
import tkinter as tk
from tkinter import messagebox

# GitHub에서 파일을 불러오기
url = 'https://raw.githubusercontent.com/wwwdsda/mad-libs-project/refs/heads/main/story/story1.txt'
response = requests.get(url)
csv_data = response.text


# 빈칸을 처리하는 함수
def fill_in_blanks():
    global csv_data
    current_blank = ""
    # 빈칸이 있는 부분을 찾아서 처리하는 함수
    def process_blank():
        global csv_data
        nonlocal current_blank
        first_index = csv_data.index('{')
        second_index = csv_data.index('}')
        current_blank = csv_data[first_index+1:second_index]  # 빈칸 내용 추출

        input_window = tk.Toplevel(window)
        input_window.title(f"{current_blank}을(를) 입력하세요")

        label = tk.Label(input_window, text=f"{current_blank}을(를) 입력하세요:")
        label.pack(pady=10)

        entry = tk.Entry(input_window)
        entry.pack(pady=10)

        def submit_input():
            user_input = entry.get()  # 사용자가 입력한 값
            global csv_data
            csv_data = csv_data.replace(csv_data[first_index:second_index + 1], user_input, 1)
            input_window.destroy()  # 입력 창 닫기
            # 다음 빈칸 처리
            if '{' in csv_data:
                process_blank()
            else:
                # 빈칸이 모두 채워졌을 때 종료
                messagebox.showinfo("완료", "빈칸이 모두 채워졌습니다!")
                update_story()  # 스토리 갱신
                
        submit_button = tk.Button(input_window, text="입력 완료", command=submit_input)
        submit_button.pack(pady=10)

        entry.focus_set()
        entry.bind("<Return>", lambda event: submit_input()) 

    process_blank()  # 빈칸 처리 시작

# 스토리를 텍스트 박스에 업데이트하는 함수
def update_story():
    story_text.delete(1.0, tk.END)  # 기존 텍스트 지우기
    story_text.insert(tk.END, csv_data)  # 갱신된 스토리 삽입

# tkinter 윈도우 설정
window = tk.Tk()
window.title("Mad Libs 게임")

# 스토리 출력용 텍스트 박스
story_text = tk.Text(window, height=30, width=100)
story_text.pack(pady=20)

story_text.insert(tk.END, "Mad Libs 게임입니다! '시작' 버튼을 눌러 빈칸을 채우세요!")

# '시작' 버튼
start_button = tk.Button(window, text="시작", command=fill_in_blanks)
start_button.pack(pady=20)

window.mainloop()
