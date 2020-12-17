import os
import requests #리퀘 모듈 다운받아야함

def restart(): #다시 시작하기위해 만든 함수
  answer = str(input("Do you want to start over? y/n ")).lower()
  if answer == "y" or answer =="n":
    if answer == "n":
        print("k. bye!")
        return
    elif answer == "y":
      main()
  else:
    print("That's not a valid answer")
    restart()


def main():# 전체적인 코드의 몸통
  os.system('clear')# cls랑 같다.
  print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
  urls = str(input()).lower().split(",")
  for url in urls:
    url = url.strip()
    if "." not in url:
      print(url, "is not a valid URL.")
    else:
      if "http" not in url:
        url = f"http://{url}"
      try:
        request = requests.get(url)
        if request.status_code == 200:
          print(url,"is up!")
        else:
          print(url, "is down!")
      except:
          print(url, "is down!")
  restart() #함수 불러옴


main() #함수 불러옴
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
