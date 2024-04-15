import json
import os


def get_student_info(student_id: str) -> dict:
    with open('students.json', 'r', encoding='utf-8') as file:
        students_data = json.load(file)
        for student in students_data:
            if student["student_id"] == student_id:
                return student
        raise ValueError(f"學號 {student_id} 找不到.")


def add_course(student_id: str):
    with open('students.json', 'r+', encoding='utf-8') as file:
        students_data = json.load(file)
        for student in students_data:
            if student["student_id"] == student_id:
                course_name = input("請輸入要新增課程的名稱: ").strip()

                if not course_name:
                    raise ValueError("課程名稱不可空白.")

                course_score_str = input("請輸入要新增課程的分數: ").strip()

                if not course_score_str:
                    raise ValueError("課程分數不可空白.")

                if not course_score_str.isdigit():
                    raise ValueError("請輸入有效的數字.")

                course_score = float(course_score_str)

                student["courses"].append({"name": course_name, "score": course_score})
                file.seek(0)
                json.dump(students_data, file, indent=4, ensure_ascii=False)
                file.truncate()
                return "課程已成功新增."
        raise ValueError(f"學號 {student_id} 找不到.")

def calculate_average_score(student_data: dict) -> float:
    courses = student_data.get("courses", [])
    if not courses:
        return 0.0
    return sum(course["score"] for course in courses) / len(courses)

if os.path.isfile('students.json'):
    while True:
        print("***************選單***************")
        print("1. 查詢指定學號成績")
        print("2. 新增指定學號的課程名稱與分數")
        print("3. 顯示指定學號的各科平均分數")
        print("4. 離開")
        print("**********************************")

        choice = input("請選擇操作項目：").strip()

        if choice == "1":
            student_id = input("請輸入學號: ").strip()
            try:
                student_info = get_student_info(student_id)
                print("=>學生資料:", json.dumps(student_info, indent=2, ensure_ascii=False))
            except ValueError as e:
                print("=>發生錯誤:", e)
        elif choice == "2":
            student_id = input("請輸入學號: ").strip()
            try:
                result = add_course(student_id)
                print("=>" + result)
            except ValueError as e:
                print("=>" + str(e))
        elif choice == "3":
            student_id = input("請輸入學號: ").strip()
            try:
                student_info = get_student_info(student_id)
                average_score = calculate_average_score(student_info)
                print("=>各科平均分數:", average_score)
            except ValueError as e:
                print("=>發生錯誤:", e)
        elif choice == "4":
            print("=>程式結束。")
            break
        else:
            print("=>請輸入有效的選項。")
else:
    print("檔案不存在。")
