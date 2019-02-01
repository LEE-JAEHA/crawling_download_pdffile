import urllib.request

# URL 저장 경로 지정하기
url = "찾고싶은 url"

# 저장할 파일이름
savename = "파일 경로 및 파일 명"

# 다운로드
urllib.request.urlretrieve(url, savename)
print("저장완료")