# 파일명: script.py

def create_script():
    # 본인 학번 설정 
    student_id = 20222017
    
    input_file = 'points.txt'
    output_file = 'animal_output.txt'

    try:
        # 1. 기존 좌표 데이터 파일 읽기
        with open(input_file, 'r') as f:
            lines = f.readlines()

        script_lines = []

        # 2. 999개의 점 처리 루프
        # points.txt에 있는 좌표를 하나씩 읽어서 circle 명령어로 변환함 [cite: 61]
        for i, line in enumerate(lines):
            coords = line.split()
            if len(coords) < 2:
                continue
            
            x = int(coords[0])
            y = int(coords[1])

            # 조건 확인: x 또는 y가 50의 배수이면 radius를 3으로 크게 잡음 [cite: 3, 4]
            # 배수가 아니면 일반 점 크기인 1로 설정함 [cite: 10]
            if x % 50 == 0 or y % 50 == 0:
                radius = 3
            else:
                radius = 1
            
            # AnimalScript 형식에 맞춰 circle 생성 (검은색 기본값) [cite: 10, 12]
            # p0, p1... 식으로 id를 부여해서 중복되지 않게 함
            command = f'circle "p{i}" ({x}, {y}) radius {radius} filled'
            script_lines.append(command)

        # 3. 마지막 1000번째 점 (붉은 점) 추가
        # 문제에 제시된 공식: x = 학번 % 999, y = 학번 % 998 
        red_x = student_id % 999
        red_y = student_id % 998
        
        # 붉은 점은 fillColor red 속성을 추가하고 눈에 띄게 radius 3으로 고정함 [cite: 14, 54]
        red_dot_cmd = f'circle "red_dot" ({red_x}, {red_y}) radius 3 filled fillColor red'
        script_lines.append(red_dot_cmd)

        # 4. 최종 파일 저장
        with open(output_file, 'w') as out:
            out.write('\n'.join(script_lines))

        print(f"성공: {output_file} 파일이 생성됨.")
        print(f"계산된 붉은 점 좌표: ({red_x}, {red_y})")

    except FileNotFoundError:
        print(f"오류: {input_file} 파일을 찾을 수 없음.")

if __name__ == "__main__":
    create_script()