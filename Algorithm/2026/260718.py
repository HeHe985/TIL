'''
프로그래머스
코딩테스트 연습 완전탐색 소수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/42839
'''

from itertools import permutations


def is_prime(n):
    if n < 2:
        return False
    # 루트n 까지만 검사
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    nums = set()
    
    # 1부터 모든 개수 다쓴 순열 만들기
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            # 튜플 -> 문자열 -> 정수
            nums.add(int(''.join(p)))
    answer = 0
    
    for num in nums:
        if is_prime(num):
            answer += 1
    return answer