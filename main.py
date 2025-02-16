import requests

#github에 있는 파일을 코드로 불러오는법
url = 'https://raw.githubusercontent.com/wwwdsda/mad-libs-project/refs/heads/main/story/story1.txt'
response = requests.get(url)
csv_data = response.text

#mad-libs의 빈칸은 스토리에 {}로 표시. 빈칸을 채우면 {xx}는 사라짐. 즉 {}이 글에 없을때까지 반복.
blank = ""
print("빈칸을 채우세요! 더 이상 빈칸이 없다면 종료됩니다!")
while(csv_data.find('}') != -1):
    first_index = csv_data.index('{')
    second_index = csv_data.index('}')
    blank = input("{0}를 입력하세요 : ".format(csv_data[first_index+1:second_index])) #빈칸 안에 있는 글을 가져옴
    csv_data = csv_data.replace(csv_data[first_index:second_index+1],blank,1) #같은 타입이라도 다른 빈칸이라 앞에꺼부터 바꿈

print("빈칸을 채운 글 입니다!")
print(csv_data)
