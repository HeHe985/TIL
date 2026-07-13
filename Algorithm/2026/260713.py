'''
프로그래머스
코딩테스트 연습 2018 KAKAO BLIND RECRUITMENT [1차] 뉴스 클러스터링
https://school.programmers.co.kr/learn/courses/30/lessons/17677
'''


def make_set(s):
    dic = {}
    
    # 소문자 통일
    s = s.lower()
    
    # make 다중집합
    for i in range(len(s) - 1):
        pair = s[i:i + 2]
        if pair.isalpha():
            if pair in dic:
                dic[pair] += 1
            else:
                dic[pair] = 1

    return dic

def solution(str1, str2):
    
    da1 = make_set(str1)
    da2 = make_set(str2)
    
    intersaction = 0
    union = 0
    
    # 교집합
    for i in da1:
        if i in da2:
            intersaction += min(da1[i], da2[i])
    
    # 합집합
    keys = set(da1.keys()) | set(da2.keys())
    
    for k in keys:
        union += max(da1.get(k, 0), da2.get(k, 0))
    
    if union == 0:
        return 65536
    
    
    answer = int(intersaction / union * 65536)
    return answer
