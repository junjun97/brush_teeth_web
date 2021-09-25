import json
import os
from google.cloud import storage
from datetime import datetime, timedelta
import pytz

user_id = "mcl_user"
bucket_name = "mcl_byt"

def read_json(temp):  # 임시파일에 있는 temp를 json으로 읽어와 반환
    with open(user_id + '/' + 'temp' , 'r',encoding="utf-8-sig") as f:
        json_data = json.load(f)
    return json_data

def read_json_member(name):  # 임시파일에 있는 temp를 json으로 읽어와 반환
    with open(user_id + '/' + name , 'r',encoding="utf-8-sig") as f:
        json_data = json.load(f)
    return json_data


def save_file(setting, member_name):  # 파일 이름을 현재 시간으로 저장
    now = datetime.utcnow()
    UTC = pytz.timezone('UTC')
    now_utc = now.replace(tzinfo=UTC)
    KST = pytz.timezone('Asia/Seoul')
    createDirectory(user_id)
    now_kst = now_utc.astimezone(KST)
    with open(user_id +"/" + member_name, 'w', encoding='UTF-8-sig') as make_file:
        #json.dump(setting, make_file, indent='\t')
        make_file.write(json.dumps(setting, ensure_ascii=False, indent='\t'))
    return 0


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            f = open("temp", 'w', encoding="UTF-8-sig")
            f.close()
    except :
        pass


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'byt_key.json'
storage_client = storage.Client()
def UPLOAD(bucket_name, source_file_name, destination_blob_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print("PI {} ---> GCP {} COMPLETE".format(source_file_name , destination_blob_name))

def DOWNLOAD(bucket_name, source_blob_name,destination_file_name):
    #set_bucket_public_iam(bucket_name)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    #print("GCP {} ---> PI {} COMPLETE".format(source_blob_name , destination_file_name))

def copy_blob(
    bucket_name, blob_name, destination_bucket_name, destination_blob_name):
    """Copies a blob from one bucket to another with a new name."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"
    # destination_bucket_name = "destination-bucket-name"
    # destination_blob_name = "destination-object-name"

    storage_client = storage.Client()

    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name
    )

    print(
        "Blob {} in bucket {} copied to blob {} in bucket {}.".format(
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name,
        )
    )


def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    print("Blob {} deleted.".format(blob_name))


def rename_blob(bucket_name, blob_name, new_name):
    """Renames a blob."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"
    # new_name = "new-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    new_blob = bucket.rename_blob(blob, new_name)

    print("Blob {} has been renamed to {}".format(blob.name, new_blob.name))



def member_list_in_bucket(bucket_name): # 버킷안에 저장된 재생목록 이름들을 불러냄

    blobs = storage_client.list_blobs(bucket_name)
    list_blob = []

    except_str = str(user_id + "/")  # 제외시킬 문자열
    for blob in blobs:
        if blob.name.startswith(except_str):
            blob.name = blob.name.replace(except_str, '')
            if blob.name == '':
                pass
            else:
                list_blob.append(blob.name)

    return list_blob


def directory_list():   # 디렉토리가 '/'로 끝나는 특징을 사용해 디렉토리 이름만 추출
    play_list_name = member_list_in_bucket(bucket_name)
    list_name = []
    for i in range(len(play_list_name)):
        if play_list_name[i][-1:] == '/':
            list_name.append(play_list_name[i][:-1])
    return list_name


def data_in_member_list(member_name):  # 해당 멤버의 양치질 json 데이터 가져옴
    blobs = storage_client.list_blobs(bucket_name)
    list_blob = []

    except_str = str(user_id + "/" + member_name + "/")  # 제외시킬 문자열
    for blob in blobs:
        if blob.name.startswith(except_str):
            blob.name = blob.name.replace(except_str, '')
            if blob.name == '':
                pass
            else:
                list_blob.append(blob.name)
    return list_blob