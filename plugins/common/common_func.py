def get_sftp():
    print('sftp 작업 시작')

def regist(name, sex, *args):
    print(f"이름: {name}")
    print(f"성별: {sex}")
    print(f"기타 options: {args}")
    print('등록 완료')

def regist2(name, sex, *args, **kwargs):
    print(f"이름: {name}")
    print(f"성별: {sex}")
    print(f"기타 options: {args}")
    email = kwargs.get('email') or None
    phone = kwargs.get('phone') or None
    if email:
        print(f"email: {email}")
    if phone:
        print(f"phone: {phone}")