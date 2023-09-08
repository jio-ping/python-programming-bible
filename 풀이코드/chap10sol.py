##### 프로그래밍의 정석, 파이썬 - 실습 및 연습 문제 풀이
##### 10장 예외 처리
##### 작성자: 도경구 (확인 2020/12/27)

### 실습 10.1 - 예외 발생시켜 보기 (p.463)
# 개별 확인

### 실습 10.2 - 실수 입력 확인 (p.471)

def input_float():
    while True:
        try:
            x = float(input("실수 입력: "))
        except ValueError:
            print("정수 또는 실수를 주셔야 합니다.")
        else:
            return x
            break
        finally:
            print(":‑)")

# # Test code
# print(input_float(), "를 주셨습니다.")

### 실습 10.3 - 조합 계산 서비스 구현 (p.474-476)

def comb_pascal(n, r):
    vector = [1 for _ in range(r+1)]
    for _ in range(1, n - r + 1):
        for j in range(1, r + 1):
            vector[j] = vector[j-1] + vector[j]
    return vector[r]

# print("This program computes combination of two natural numbers, n and r.")
# print("Press Control-C to quit.")
# while True:
#     try:
#         n = int(input("Enter n: "))
#         assert n >= 0
#         r = int(input("Enter r: "))
#         assert r >= 0
#         print(n, "C", r, " = ", comb_pascal(n,r), sep='')
#     except ValueError:
#         print("Must be a number.")
#     except AssertionError:
#         print("Must be a natural number.")
#     except KeyboardInterrupt:
#         print("Goodbye!")
#         break


### 실습 10.4 - 실수 입력 확인 (범위 제한) (p.477-478)

class OutOfBoundOne(Exception): pass

def input_float():
    while True:
        try:
            x = float(input("실수 입력: "))
            if not (-0.1 <= x <= 1.0):
                raise OutOfBoundOne
        except ValueError:
            print("정수 또는 실수를 주셔야 합니다.")
        except OutOfBoundOne:
            print("허용 범위는 -0.1 ~ 1.0 입니다.")
        else:
            return x
            break
        finally:
            print(":‑)")

# # Test code
# print(input_float(), "를 주셨습니다.")


#### 연습 문제

### 10.1 - 퍼즐게임 미니 스도쿠 예외 처리 추가 (p.478)


### 10.2 - 카드게임 블랙잭 예외 처리 추가 (p.478)


