from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from home.gcp import *
import operator

def home(request): # 대시보드
    list_member = directory_list()
    print(list_member)

    # 추가된 양치 데이터 통합하는 과정
    for i in range(len(list_member)):  # 멤버 수 만큼 반복 (최대 4명)
        data_list = data_in_member_list(list_member[i]) # 해당 멤버가 가지고 있는 json 데이터의 리스트
        if os.path.isfile(user_id + "/" + list_member[i]):  # 기존 통합데이터 파일이 존재하는 경우
            data_member = read_json_member(list_member[i]) # 읽어옴
        else: # 기존에 없던 경우
            data_member = [] # 새로만듬
        print("data_member =>")
        print(data_member)
        for j in range(len(data_list)): # 해당 멤버의 양치 data들
            DOWNLOAD(bucket_name, user_id + "/" + list_member[i] + "/" + data_list[j], user_id + "/" + "temp") # 다운받아서
            data = read_json('temp') # 변수로 받아옴
            os.remove(user_id + "/temp") # 지우고
            data_member.append(data) # 통합하고
            delete_blob(bucket_name, user_id + "/" + list_member[i] + "/" + data_list[j]) # 스토리지에도 삭제
        save_file(data_member,list_member[i]) # 개인 -> 통합된 데이터 json 저장


    score_list = [80, 80, 65, 30, 75, 20, 100, 75, 88, 88, 88, 91, 89]
    weakness = {
        "stop": 3,
        "horizon": 2,
        "vertical": 3,
        "left_up_in": 0,
        "left_up_out": 0,
        "left_down_in": 5,
        "left_down_out": 3,
        "right_up_in": 10,
        "right_up_out": 5000,
        "right_down_in": 300,
        "right_down_out": 3
    }
    sorted_weakness = sorted(weakness.items(), key=lambda x: x[1])


    weakness_key = []
    weakness_value = []

    for i in range(5):
        max_list_in = [k for k, v in weakness.items() if max(weakness.values()) == v]
        print(max_list_in)
        weakness_key.append(max_list_in[0])
        weakness_value.append(weakness[max_list_in[0]])
        del(weakness[max_list_in[0]])

    list_dict = {
        'score_list' : score_list,
        'weakness_key' : weakness_key,
        'weakness_value' : weakness_value
    }
    context = json.dumps(list_dict)



    #UPLOAD("mcl_byt", "mcl_user/hi.txt", "inf/hi.txt")
    return render(request, 'index.html', {'context' : context})


