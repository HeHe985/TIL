# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        name = input('이름을 입력하세요: ')
        if name == '':
            return None
        else:
            try:
                self.user_data.update({'name': name, 'age': int(input('나이를 입력하세요: '))})
            except ValueError:
                print('나이는 숫자로 입력해야 합니다.')
                return False
            else:
                return True

    def display_user_info(self):
        
        if self.user_data == {}:
            print('사용자 정보가 입력되지 않았습니다.')
        else:
            print('사용자정보:')
            print(f"이름: {self.user_data.get('name')}")
            print(f"나이: {self.user_data.get('age')}")
        

user = UserInfo()
result = user.get_user_info()

if result is True:
    user.display_user_info()
elif result is None:
    user.display_user_info()
