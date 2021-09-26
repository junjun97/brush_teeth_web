from django.http import HttpResponse
from django.shortcuts import render
from home.gcp import *
import json
from PIL import Image
import cv2
import numpy as np
import matplotlib.pylab as plt
# Create your views here.

def read_json():  # 임시파일에 있는 temp를 json으로 읽어와 반환
    with open('mcl_user' + '/send', 'r',encoding="utf-8-sig") as f:
        json_data = json.load(f)
    return json_data

def member1(request):



    list_member = directory_list()
    data = {}

    download_data = {
        "weakness": {
            "stop": 1,
            "horizon": 2,
            "vertical": 4,
            "left_up_in": 5,
            "left_up_out": 1200,
            "left_down_in": 500,
            "left_down_out": 7,
            "right_up_in": 8,
            "right_up_out": 30,
            "right_down_in": 20,
            "right_down_out": 3
        },
        "score": "100"
    }
    weakness_data = download_data['weakness']
    weakness = {}
    weakness = download_data['weakness']
    data["score"] = download_data['score']
    save_file(data, 'send')
    UPLOAD("mcl_byt", "mcl_user/send", user_id + "/" + list_member[0] + "/32")


    score_list = [30, 80, 65, 30, 75, 20, 10, 5, 88, 88, 8, 91, 9]

    sorted_weakness = sorted(weakness.items(), key=lambda x: x[1])



    weakness_key = []
    weakness_value = []

    for i in range(5):
        max_list_in = [k for k, v in weakness.items() if max(weakness.values()) == v]
        print(max_list_in)
        weakness_key.append(max_list_in[0])
        weakness_value.append(weakness[max_list_in[0]])
        del (weakness[max_list_in[0]])

    for i in range(5):
        weakness_data[weakness_key[i]] = weakness_value[i]


    list_dict = {
        'score_list': score_list,
        'weakness_key': weakness_key,
        'weakness_value': weakness_value
    }
    context = json.dumps(list_dict)


    max_list_in_dic = {}
    max_list_in = [k for k in weakness_data if 'in' in k]

    for i in range(4):
        weakness_data[max_list_in[i]]
        max_list_in_dic[max_list_in[i]] = weakness_data[max_list_in[i]]

    max_list_in_dic

    max_list_out_dic = {}
    max_list_out = [k for k in weakness_data if 'out' in k]

    for i in range(4):
        weakness_data[max_list_out[i]]
        max_list_out_dic[max_list_out[i]] = weakness_data[max_list_out[i]]

    max_list_out_dic

    max_list_in = [k for k, v in max_list_in_dic.items() if max(max_list_in_dic.values()) == v]  #
    max_list_out = [k for k, v in max_list_out_dic.items() if max(max_list_out_dic.values()) == v]  #

    img_in = cv2.imread("home/static/org2.png")
    img_out = cv2.imread("home/static/org1.jpg")
    img4 = cv2.imread("home/static/left_up_in.png")
    img5 = cv2.imread("home/static/left_up_out.png")
    img6 = cv2.imread("home/static/left_down_in.png")
    img7 = cv2.imread("home/static/left_down_out.png")
    img8 = cv2.imread("home/static/right_up_in.png")
    img9 = cv2.imread("home/static/right_up_out.png")
    img10 = cv2.imread("home/static/right_down_in.png")
    img11 = cv2.imread("home/static/right_down_out.png")

    # for i in range(len(max_list)):

    in_change = 0
    out_change = 0

    temp_result_in = img_in

    if ('left_up_in' in max_list_in):
        img_result_in = {'img_result': img_in + img4}
        temp_result_in = temp_result_in + img4
        in_change = 1

    if ('left_down_in' in max_list_in):
        img_result_in = {'img_result': temp_result_in + img6}
        temp_result_in = temp_result_in + img6
        in_change = 1

    if ('right_up_in' in max_list_in):
        img_result_in = {'img_result': temp_result_in + img8}
        temp_result_in = temp_result_in + img8
        in_change = 1

    if ('right_down_in' in max_list_in):
        img_result_in = {'img_result': temp_result_in + img10}
        temp_result_in = temp_result_in + img10
        in_change = 1

    if (in_change == 0):
        img_result_in = {'img_result': img_in}

    temp_result_out = img_out
    if ('left_up_out' in max_list_out):
        img_result_out = {'img_result': img_out + img5}
        temp_result_out = temp_result_out + img5
        out_change = 1

    if ('left_down_out' in max_list_out):
        img_result_out = {'img_result': temp_result_out + img7}
        temp_result_out = temp_result_out + img7
        out_change = 1

    if ('right_up_out' in max_list_out):
        img_result_out = {'img_result': temp_result_out + img9}
        temp_result_out = temp_result_out + img9
        out_change = 1

    if ('right_down_out' in max_list_out):
        img_result_out = {'img_result': temp_result_out + img11}
        temp_result_out = temp_result_out + img11
        out_change = 1

    if (out_change == 0):
        img_result_out = {'img_result': img_out}

    for i, (k, v) in enumerate(img_result_in.items()):
        plt.title(k)
        plt.xticks([]);
        plt.yticks([])

    plt.imsave("home/static/result_in.png", v[:, :, ::-1])

    for i, (k, v) in enumerate(img_result_out.items()):
        plt.title(k)
        plt.xticks([]);
        plt.yticks([])

    plt.imsave("home/static/result_out.png", v[:, :, ::-1])

    # UPLOAD("mcl_byt", "mcl_user/hi.txt", "inf/hi.txt")
    return render(request, 'member1.html', {'context': context})


def member2(request):



    list_member = directory_list()
    data = {}

    download_data = {
        "weakness": {
            "stop": 1,
            "horizon": 2,
            "vertical": 4,
            "left_up_in": 5000,
            "left_up_out": 10,
            "left_down_in": 500,
            "left_down_out": 7,
            "right_up_in": 8,
            "right_up_out": 30,
            "right_down_in": 20,
            "right_down_out": 3
        },
        "score": "100"
    }
    weakness_data = download_data['weakness']
    weakness = {}
    weakness = download_data['weakness']
    data["score"] = download_data['score']
    save_file(data, 'send')
    UPLOAD("mcl_byt", "mcl_user/send", user_id + "/" + list_member[0] + "/32")


    score_list = [30, 80, 65, 30, 75, 20, 10, 5, 88, 88, 8, 91, 9]

    sorted_weakness = sorted(weakness.items(), key=lambda x: x[1])



    weakness_key = []
    weakness_value = []

    for i in range(5):
        max_list_in = [k for k, v in weakness.items() if max(weakness.values()) == v]
        print(max_list_in)
        weakness_key.append(max_list_in[0])
        weakness_value.append(weakness[max_list_in[0]])
        del (weakness[max_list_in[0]])

    for i in range(5):
        weakness_data[weakness_key[i]] = weakness_value[i]


    list_dict = {
        'score_list': score_list,
        'weakness_key': weakness_key,
        'weakness_value': weakness_value
    }
    context = json.dumps(list_dict)


    max_list_in_dic = {}
    max_list_in = [k for k in weakness_data if 'in' in k]

    for i in range(4):
        weakness_data[max_list_in[i]]
        max_list_in_dic[max_list_in[i]] = weakness_data[max_list_in[i]]

    max_list_in_dic

    max_list_out_dic = {}
    max_list_out = [k for k in weakness_data if 'out' in k]

    for i in range(4):
        weakness_data[max_list_out[i]]
        max_list_out_dic[max_list_out[i]] = weakness_data[max_list_out[i]]

    max_list_out_dic

    max_list_in = [k for k, v in max_list_in_dic.items() if max(max_list_in_dic.values()) == v]  #
    max_list_out = [k for k, v in max_list_out_dic.items() if max(max_list_out_dic.values()) == v]  #

    img_in = cv2.imread("home/static/org2.png")
    img_out = cv2.imread("home/static/org1.jpg")
    img4 = cv2.imread("home/static/left_up_in.png")
    img5 = cv2.imread("home/static/left_up_out.png")
    img6 = cv2.imread("home/static/left_down_in.png")
    img7 = cv2.imread("home/static/left_down_out.png")
    img8 = cv2.imread("home/static/right_up_in.png")
    img9 = cv2.imread("home/static/right_up_out.png")
    img10 = cv2.imread("home/static/right_down_in.png")
    img11 = cv2.imread("home/static/right_down_out.png")

    # for i in range(len(max_list)):

    in_change = 0
    out_change = 0

    temp_result_in = img_in

    if ('left_up_in' in max_list_in):
        img_result_in = {'img_result': img_in + img4}
        temp_result_in = temp_result_in + img4
        in_change = 1

    if ('left_down_in' in max_list_in):
        img_result_in = {'img_result': temp_result_in + img6}
        temp_result_in = temp_result_in + img6
        in_change = 1

    if ('right_up_in' in max_list_in):
        img_result_in = {'img_result': temp_result_in + img8}
        temp_result_in = temp_result_in + img8
        in_change = 1

    if ('right_down_in' in max_list_in):
        img_result_in = {'img_result': temp_result_in + img10}
        temp_result_in = temp_result_in + img10
        in_change = 1

    if (in_change == 0):
        img_result_in = {'img_result': img_in}

    temp_result_out = img_out
    if ('left_up_out' in max_list_out):
        img_result_out = {'img_result': img_out + img5}
        temp_result_out = temp_result_out + img5
        out_change = 1

    if ('left_down_out' in max_list_out):
        img_result_out = {'img_result': temp_result_out + img7}
        temp_result_out = temp_result_out + img7
        out_change = 1

    if ('right_up_out' in max_list_out):
        img_result_out = {'img_result': temp_result_out + img9}
        temp_result_out = temp_result_out + img9
        out_change = 1

    if ('right_down_out' in max_list_out):
        img_result_out = {'img_result': temp_result_out + img11}
        temp_result_out = temp_result_out + img11
        out_change = 1

    if (out_change == 0):
        img_result_out = {'img_result': img_out}

    for i, (k, v) in enumerate(img_result_in.items()):
        plt.title(k)
        plt.xticks([]);
        plt.yticks([])

    plt.imsave("home/static/result_in.png", v[:, :, ::-1])

    for i, (k, v) in enumerate(img_result_out.items()):
        plt.title(k)
        plt.xticks([]);
        plt.yticks([])

    plt.imsave("home/static/result_out.png", v[:, :, ::-1])

    # UPLOAD("mcl_byt", "mcl_user/hi.txt", "inf/hi.txt")
    return render(request, 'member2.html', {'context': context})


def member3(request):

    list_member = directory_list()
    data = {}

    download_data = {
        "weakness": {
            "stop": 1,
            "horizon": 2,
            "vertical": 4,
            "left_up_in": 5,
            "left_up_out": 1200,
            "left_down_in": 500,
            "left_down_out": 7,
            "right_up_in": 8,
            "right_up_out": 30,
            "right_down_in": 50000,
            "right_down_out": 3000
        },
        "score": "100"
    }
    weakness_data = download_data['weakness']
    weakness = {}
    weakness = download_data['weakness']
    data["score"] = download_data['score']
    save_file(data, 'send')
    UPLOAD("mcl_byt", "mcl_user/send", user_id + "/" + list_member[0] + "/32")


    score_list = [30, 80, 65, 30, 75, 20, 10, 5, 88, 88, 8, 91, 9]

    sorted_weakness = sorted(weakness.items(), key=lambda x: x[1])



    weakness_key = []
    weakness_value = []

    for i in range(5):
        max_list_in = [k for k, v in weakness.items() if max(weakness.values()) == v]
        print(max_list_in)
        weakness_key.append(max_list_in[0])
        weakness_value.append(weakness[max_list_in[0]])
        del (weakness[max_list_in[0]])

    for i in range(5):
        weakness_data[weakness_key[i]] = weakness_value[i]


    list_dict = {
        'score_list': score_list,
        'weakness_key': weakness_key,
        'weakness_value': weakness_value
    }
    context = json.dumps(list_dict)


    max_list_in_dic = {}
    max_list_in = [k for k in weakness_data if 'in' in k]

    for i in range(4):
        weakness_data[max_list_in[i]]
        max_list_in_dic[max_list_in[i]] = weakness_data[max_list_in[i]]

    max_list_in_dic

    max_list_out_dic = {}
    max_list_out = [k for k in weakness_data if 'out' in k]

    for i in range(4):
        weakness_data[max_list_out[i]]
        max_list_out_dic[max_list_out[i]] = weakness_data[max_list_out[i]]

    max_list_out_dic

    max_list_in = [k for k, v in max_list_in_dic.items() if max(max_list_in_dic.values()) == v]  #
    max_list_out = [k for k, v in max_list_out_dic.items() if max(max_list_out_dic.values()) == v]  #

    img_in = cv2.imread("home/static/org2.png")
    img_out = cv2.imread("home/static/org1.jpg")
    img4 = cv2.imread("home/static/left_up_in.png")
    img5 = cv2.imread("home/static/left_up_out.png")
    img6 = cv2.imread("home/static/left_down_in.png")
    img7 = cv2.imread("home/static/left_down_out.png")
    img8 = cv2.imread("home/static/right_up_in.png")
    img9 = cv2.imread("home/static/right_up_out.png")
    img10 = cv2.imread("home/static/right_down_in.png")
    img11 = cv2.imread("home/static/right_down_out.png")

    # for i in range(len(max_list)):

    in_change = 0
    out_change = 0

    temp_result_in = img_in

    if ('left_up_in' in max_list_in):
        img_result_in = {'img_result': img_in + img4}
        temp_result_in = temp_result_in + img4
        in_change = 1

    if ('left_down_in' in max_list_in):
        img_result_in = {'img_result': temp_result_in + img6}
        temp_result_in = temp_result_in + img6
        in_change = 1

    if ('right_up_in' in max_list_in):
        img_result_in = {'img_result': temp_result_in + img8}
        temp_result_in = temp_result_in + img8
        in_change = 1

    if ('right_down_in' in max_list_in):
        img_result_in = {'img_result': temp_result_in + img10}
        temp_result_in = temp_result_in + img10
        in_change = 1

    if (in_change == 0):
        img_result_in = {'img_result': img_in}

    temp_result_out = img_out
    if ('left_up_out' in max_list_out):
        img_result_out = {'img_result': img_out + img5}
        temp_result_out = temp_result_out + img5
        out_change = 1

    if ('left_down_out' in max_list_out):
        img_result_out = {'img_result': temp_result_out + img7}
        temp_result_out = temp_result_out + img7
        out_change = 1

    if ('right_up_out' in max_list_out):
        img_result_out = {'img_result': temp_result_out + img9}
        temp_result_out = temp_result_out + img9
        out_change = 1

    if ('right_down_out' in max_list_out):
        img_result_out = {'img_result': temp_result_out + img11}
        temp_result_out = temp_result_out + img11
        out_change = 1

    if (out_change == 0):
        img_result_out = {'img_result': img_out}

    for i, (k, v) in enumerate(img_result_in.items()):
        plt.title(k)
        plt.xticks([]);
        plt.yticks([])

    plt.imsave("home/static/result_in.png", v[:, :, ::-1])

    for i, (k, v) in enumerate(img_result_out.items()):
        plt.title(k)
        plt.xticks([]);
        plt.yticks([])

    plt.imsave("home/static/result_out.png", v[:, :, ::-1])

    # UPLOAD("mcl_byt", "mcl_user/hi.txt", "inf/hi.txt")
    return render(request, 'member3.html', {'context': context})

def member4(request):



    list_member = directory_list()
    data = {}

    download_data = {
        "weakness": {
            "stop": 1,
            "horizon": 2,
            "vertical": 4,
            "left_up_in": 5,
            "left_up_out": 1200,
            "left_down_in": 500,
            "left_down_out": 7000,
            "right_up_in": 8000,
            "right_up_out": 30,
            "right_down_in": 20,
            "right_down_out": 3
        },
        "score": "100"
    }
    weakness_data = download_data['weakness']
    weakness = {}
    weakness = download_data['weakness']
    data["score"] = download_data['score']
    save_file(data, 'send')
    UPLOAD("mcl_byt", "mcl_user/send", user_id + "/" + list_member[0] + "/32")


    score_list = [30, 80, 65, 30, 75, 20, 10, 5, 88, 88, 8, 91, 9]

    sorted_weakness = sorted(weakness.items(), key=lambda x: x[1])



    weakness_key = []
    weakness_value = []

    for i in range(5):
        max_list_in = [k for k, v in weakness.items() if max(weakness.values()) == v]
        print(max_list_in)
        weakness_key.append(max_list_in[0])
        weakness_value.append(weakness[max_list_in[0]])
        del (weakness[max_list_in[0]])

    for i in range(5):
        weakness_data[weakness_key[i]] = weakness_value[i]


    list_dict = {
        'score_list': score_list,
        'weakness_key': weakness_key,
        'weakness_value': weakness_value
    }
    context = json.dumps(list_dict)


    max_list_in_dic = {}
    max_list_in = [k for k in weakness_data if 'in' in k]

    for i in range(4):
        weakness_data[max_list_in[i]]
        max_list_in_dic[max_list_in[i]] = weakness_data[max_list_in[i]]

    max_list_in_dic

    max_list_out_dic = {}
    max_list_out = [k for k in weakness_data if 'out' in k]

    for i in range(4):
        weakness_data[max_list_out[i]]
        max_list_out_dic[max_list_out[i]] = weakness_data[max_list_out[i]]

    max_list_out_dic

    max_list_in = [k for k, v in max_list_in_dic.items() if max(max_list_in_dic.values()) == v]  #
    max_list_out = [k for k, v in max_list_out_dic.items() if max(max_list_out_dic.values()) == v]  #

    img_in = cv2.imread("home/static/org2.png")
    img_out = cv2.imread("home/static/org1.jpg")
    img4 = cv2.imread("home/static/left_up_in.png")
    img5 = cv2.imread("home/static/left_up_out.png")
    img6 = cv2.imread("home/static/left_down_in.png")
    img7 = cv2.imread("home/static/left_down_out.png")
    img8 = cv2.imread("home/static/right_up_in.png")
    img9 = cv2.imread("home/static/right_up_out.png")
    img10 = cv2.imread("home/static/right_down_in.png")
    img11 = cv2.imread("home/static/right_down_out.png")

    # for i in range(len(max_list)):

    in_change = 0
    out_change = 0

    temp_result_in = img_in

    if ('left_up_in' in max_list_in):
        img_result_in = {'img_result': img_in + img4}
        temp_result_in = temp_result_in + img4
        in_change = 1

    if ('left_down_in' in max_list_in):
        img_result_in = {'img_result': temp_result_in + img6}
        temp_result_in = temp_result_in + img6
        in_change = 1

    if ('right_up_in' in max_list_in):
        img_result_in = {'img_result': temp_result_in + img8}
        temp_result_in = temp_result_in + img8
        in_change = 1

    if ('right_down_in' in max_list_in):
        img_result_in = {'img_result': temp_result_in + img10}
        temp_result_in = temp_result_in + img10
        in_change = 1

    if (in_change == 0):
        img_result_in = {'img_result': img_in}

    temp_result_out = img_out
    if ('left_up_out' in max_list_out):
        img_result_out = {'img_result': img_out + img5}
        temp_result_out = temp_result_out + img5
        out_change = 1

    if ('left_down_out' in max_list_out):
        img_result_out = {'img_result': temp_result_out + img7}
        temp_result_out = temp_result_out + img7
        out_change = 1

    if ('right_up_out' in max_list_out):
        img_result_out = {'img_result': temp_result_out + img9}
        temp_result_out = temp_result_out + img9
        out_change = 1

    if ('right_down_out' in max_list_out):
        img_result_out = {'img_result': temp_result_out + img11}
        temp_result_out = temp_result_out + img11
        out_change = 1

    if (out_change == 0):
        img_result_out = {'img_result': img_out}

    for i, (k, v) in enumerate(img_result_in.items()):
        plt.title(k)
        plt.xticks([]);
        plt.yticks([])

    plt.imsave("home/static/result_in.png", v[:, :, ::-1])

    for i, (k, v) in enumerate(img_result_out.items()):
        plt.title(k)
        plt.xticks([]);
        plt.yticks([])

    plt.imsave("home/static/result_out.png", v[:, :, ::-1])

    # UPLOAD("mcl_byt", "mcl_user/hi.txt", "inf/hi.txt")
    return render(request, 'member4.html', {'context': context})


