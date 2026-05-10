# Animal Animation 과제 

- [_GitHub 바로가기_](https://github.com/jeongiryang/Algorithm_animal-animation_tool.git)

 - **과목:** 알고리즘
 - **학번:**  2022 2017
 - **이름:** 정이량


 ---

## 1. 과제 개요
본 과제는 주어진 999개의 좌표 데이터(points.txt)와 본인의 학번을 활용하여 총 1,000개의 점을 특정 규칙에 맞게 화면에 렌더링하는 프로그램을 구현하는 것.

---

## 2. 과제 요구사항

강의 자료에서 제시된 핵심 요구사항을 분석하여 설계에 반영하였다.

| [01] 과제 기본 요건 | [02] 점 렌더링 세부 규칙 |
| :---: | :---: |
| ![Homework Overview](./screenshots/요구사항1.png) | ![Point Rules](./screenshots/요구사항2.png)  |
| ▲ 1,000개의 점 표시 및 50의 배수 강조 | ▲ 가는 점(Radius 1), 굵은 점(Radius 3) 구분 |

| [03] 입력 데이터 분석 | [04] 학번 기반 특수 점 계산 |
| :---: | :---: |
| ![Input Data](./screenshots/요구사항3.png)  | ![Red Point Formula](./screenshots/요구사항4.png)  |
| ▲ points.txt (0 ~ 1000 범위의 999개 좌표) | ▲ 마지막 붉은 점: $x = (\text{학번}) \pmod{999}$, $y = (\text{학번}) \pmod{998}$ |

| [05] 제출 주의사항 |
| :---: |
| ![Submission Info](./screenshots/요구사항5.png)  |
| ▲ 소스 코드와 실행 결과 캡처를 하나의 HWP/PDF로 통합 제출 |

---

## 3. 디렉토리 구조

```text
Assignment_Animal_Animation/
 ┣ src/          # 애니메이션 스크립트를 생성하는 파이썬 소스 코드
 ┣ data/         # 입력 데이터 (points.txt)
 ┣ screenshot/   # 과제 제출용 실행 결과 캡처 이미지 모음
 ┗ README.md     # 결과 간단 보고서
 ```

---

## 4. 실행 방법

1. data 폴더 안에 points.txt 파일이 정상적으로 위치해 있는지 확인
2. 터미널 또는 명령 프롬프트에서 src 폴더로 이동
3. 아래 명령어를 입력하여 프로그램을 실행
   ```bash
   python script_generator.py
   ```