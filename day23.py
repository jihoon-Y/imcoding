#피클 프로그램 상에서 사용하고있는 데이터를 파일 형태로 저장해주는 것
#파일을 넘겨주고받고 해서 피클로 데이터를 불러와 코드로 또 사용 가능
import pickle
profile_file=open("profile.pickle","wb") #쓰기목적w,바이너리의b 피클 쓸때는 바이너리타입정해줘야한다, 피클에서는 encoding을 따로 설정해줄 필요는 없다.
profile={"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
#profile은 사전형태로, 취미는 리스트형태로 만들었다.
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()

profile_file=open("profile.pickle","rb") #여기서도 바이너리 명시
profile=pickle.load(profile_file) #파일형태를 그대로 가져와서 데이터를 불러와준다
#=file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

#지금까지는 file에 대한 작업을 할 때, 파일을 열고, 처리하고, 닫는 과정을 거쳤는데
#with를 사용하면 좀 더 편리하게 동일작업 가능
import pickle

with open("profile.pickle", "rb") as profile_file: #file정보를 profile_file에 저장
    print(pickle.load(profile_file))
#file을 열어서 profile_file이라는 변수로 저장 해두고, profile_file의 내용을 pickle.load로 불러와서 print로 출력
#이러면 따로 profile_file.close()해줄 필요가 없다. with문을 탈출하며 자동종료.

# with open("study.txt", "w", encoding="utf8") as study_file:
    #file명은 study.txt.로 지정, 먼저 써야하니까 w, 한국어사용하니까 utf8
    #study_file이라는 변수에 지정
    # study_file.write("파이썬을 열심히 공부하고 있어요.")
    #study.txt이 생성되며 그 파일에 지정문구 저장되었다.

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
    #위에 생성된 파일을 불러왔다.