import json
import os
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_data(filename='data_full.json'):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, filename)
    if not os.path.exists(file_path):
        print(f"❌ 错误：找不到文件 {filename}，请务必先运行 generate_full_data.py")
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def run_quiz():
    all_papers = load_data()
    if not all_papers: return

    while True:
        clear_screen()
        print("=" * 40)
        print("      英语学位考试全真模拟系统")
        print("=" * 40)
        # 列出所有试卷
        paper_names = list(all_papers.keys())
        for idx, name in enumerate(paper_names, 1):
            print(f"  {idx}. {name} (80题)")
        print("  Q. 退出")
        print("-" * 40)

        choice = input("👉 请选择试卷 (输入序号): ").strip().upper()
        if choice == 'Q': break

        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(paper_names):
            print("输入无效，请重试。")
            time.sleep(1)
            continue

        selected_paper_name = paper_names[int(choice) - 1]
        questions = all_papers[selected_paper_name]
        start_exam(selected_paper_name, questions)


def start_exam(paper_name, questions):
    score = 0
    total = len(questions)
    wrong_ids = []

    # 用于记录当前显示的阅读文章，避免重复打印
    current_context = ""

    print(f"\n🚀 开始 {paper_name} 测试！")
    input("按回车键开始...")

    for idx, q in enumerate(questions, 1):
        clear_screen()
        print(f"【{paper_name}】 进度 {idx}/{total}  [{q['type']}]")
        print("-" * 60)

        # 1. 如果有阅读文章/完形段落，且与上一题不同，则显示
        if 'context' in q and q['context']:
            if q['context'] != current_context:
                print(f"\n📖 阅读/背景材料:\n{q['context']}")
                print("-" * 60)
                current_context = q['context']

        # 2. 显示题目
        print(f"题目 {q['id']}: {q['question']}")

        # 3. 处理不同题型
        user_correct = False

        # === 客观题 (选择题) ===
        if 'options' in q and q['options']:
            # 排序显示选项
            sorted_opts = sorted(q['options'].items())
            print()
            for k, v in sorted_opts:
                print(f"  {k}. {v}")
            print()

            while True:
                user_ans = input("👉 你的答案 (A/B/C/D): ").strip().upper()
                if user_ans in ['A', 'B', 'C', 'D']: break

            correct_ans = q['answer'].strip().upper()
            if user_ans == correct_ans:
                print("✅ 正确！")
                user_correct = True
            else:
                print(f"❌ 错误！正确答案是: {correct_ans}")

        # === 主观题 (翻译) ===
        else:
            print("\n(这是一个主观题，请在心里翻译或写在纸上)")
            input("👉 思考完毕后，按回车键查看参考答案...")
            print("-" * 30)
            print(f"参考答案: {q['answer']}")
            print("-" * 30)

            # 自我评分
            while True:
                self_eval = input("🤔 你觉得自己答对了吗？(Y=对/N=错): ").strip().upper()
                if self_eval in ['Y', 'N']: break

            if self_eval == 'Y':
                user_correct = True
                print("✅ 已标记为正确。")
            else:
                print("❌ 已标记为错误。")

        # 4. 统计与解析
        if user_correct:
            score += 1
        else:
            wrong_ids.append(q['id'])
            if 'explanation' in q and q['explanation']:
                print(f"💡 解析: {q['explanation']}")
            time.sleep(1)  # 错题停留一下

        input("\n按回车继续...")

    # 结算
    clear_screen()
    print("=" * 40)
    print(f"  {paper_name} 测试结束")
    print("=" * 40)
    print(f"得分: {score} / {total}")
    if wrong_ids:
        print("错题 ID:", wrong_ids)
    input("按回车键返回主菜单...")


if __name__ == "__main__":
    run_quiz()