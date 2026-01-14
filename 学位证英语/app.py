import streamlit as st
import json
import os
import sys
import random

# 设置页面配置
st.set_page_config(
    page_title="英语学位考试模拟系统",
    page_icon="🎓",
    layout="wide"
)


# ================= 辅助函数 =================
def get_resource_path(relative_path):
    """
    获取资源文件的绝对路径 (兼容打包和本地运行)
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, relative_path)


def load_data(filename='data_full.json'):
    file_path = get_resource_path(filename)
    if not os.path.exists(file_path):
        st.error(f"❌ 找不到文件: {file_path}")
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_random_paper(all_data):
    """
    核心逻辑：从所有试卷中随机抽取题目，组成一套符合标准结构的试卷
    结构标准：阅读(4篇/20题) + 词汇(40题) + 完形(1篇/10题) + 翻译(10题)
    """
    # 1. 建立题库池
    reading_pool = {}  # 以文章内容(context)为key分组
    vocab_pool = []
    cloze_pool = {}  # 以文章内容为key分组
    trans_pool = []

    for paper_name, questions in all_data.items():
        for q in questions:
            q_type = q.get('type')

            # 阅读理解：必须按文章分组，不能拆散
            if q_type == 'Reading':
                ctx = q.get('context', 'no_context')
                if ctx not in reading_pool:
                    reading_pool[ctx] = []
                reading_pool[ctx].append(q)

            # 完形填空：必须按文章分组
            elif q_type == 'Cloze':
                ctx = q.get('context', 'no_context')
                if ctx not in cloze_pool:
                    cloze_pool[ctx] = []
                cloze_pool[ctx].append(q)

            # 词汇题：直接放入大池子
            elif q_type == 'Vocabulary':
                vocab_pool.append(q)

            # 翻译题：直接放入大池子
            elif q_type == 'Translation':
                trans_pool.append(q)

    # 2. 随机抽题 (模拟标准试卷结构)
    new_paper = []

    # A. 抽取 4 篇阅读理解
    all_readings = list(reading_pool.values())
    # 如果题库够多就抽4篇，不够就全上
    selected_readings = random.sample(all_readings, min(len(all_readings), 4))
    for passage_qs in selected_readings:
        new_paper.extend(passage_qs)

    # B. 抽取 40 道词汇题
    selected_vocab = random.sample(vocab_pool, min(len(vocab_pool), 40))
    new_paper.extend(selected_vocab)

    # C. 抽取 1 篇完形填空
    all_clozes = list(cloze_pool.values())
    selected_clozes = random.sample(all_clozes, min(len(all_clozes), 1))
    for passage_qs in selected_clozes:
        new_paper.extend(passage_qs)

    # D. 抽取 10 道翻译题
    selected_trans = random.sample(trans_pool, min(len(trans_pool), 10))
    new_paper.extend(selected_trans)

    return new_paper


# ================= 状态初始化 =================
if 'current_paper_id' not in st.session_state:
    st.session_state.current_paper_id = None  # 记录当前选的是哪套卷（字符串）
if 'paper_data' not in st.session_state:
    st.session_state.paper_data = []  # 存储当前正在做的题目列表
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answer_submitted' not in st.session_state:
    st.session_state.answer_submitted = False
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

# ================= 侧边栏 =================
st.sidebar.title("📚 考试菜单")
all_data = load_data()

# 1. 构建菜单选项
menu_options = ["🎲 随机生成试卷 (无限刷题)"]
if all_data:
    menu_options += list(all_data.keys())

# 2. 选择试卷
selected_option = st.sidebar.selectbox(
    "请选择练习模式",
    menu_options,
    index=None,
    placeholder="点击选择..."
)

# 3. 处理试卷切换逻辑
# 如果用户换了选项，或者选了随机且还没生成数据
if selected_option != st.session_state.current_paper_id:
    if selected_option:
        # 重置所有状态
        st.session_state.current_paper_id = selected_option
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.answer_submitted = False
        st.session_state.user_answers = {}

        # 生成题目数据
        if selected_option == "🎲 随机生成试卷 (无限刷题)":
            with st.spinner("正在从题库中随机组卷..."):
                st.session_state.paper_data = generate_random_paper(all_data)
            st.toast("✅ 新的随机试卷已生成！")
        else:
            # 加载固定试卷
            st.session_state.paper_data = all_data[selected_option]

        st.rerun()

# 4. 随机卷的刷新按钮
if st.session_state.current_paper_id == "🎲 随机生成试卷 (无限刷题)":
    if st.sidebar.button("🔄 重新生成一套随机卷"):
        # 清除当前 ID 触发重新生成
        st.session_state.current_paper_id = None
        st.rerun()

# 5. 题目导航
if st.session_state.paper_data:
    questions = st.session_state.paper_data
    total_q = len(questions)

    st.sidebar.markdown("---")
    st.sidebar.subheader("📍 题目导航")


    def on_nav_change():
        new_index = st.session_state.q_nav - 1
        if new_index != st.session_state.question_index:
            st.session_state.question_index = new_index
            st.session_state.answer_submitted = False


    st.sidebar.selectbox(
        "跳转到题目:",
        options=range(1, total_q + 1),
        index=st.session_state.question_index,
        key="q_nav",
        on_change=on_nav_change,
        format_func=lambda x: f"第 {x} 题"
    )

    current_q_obj = questions[st.session_state.question_index]
    st.sidebar.info(f"当前题型: {current_q_obj.get('type', '未知')}")

# ================= 主界面逻辑 =================

if not st.session_state.paper_data:
    st.title("🎓 英语学位考试全真模拟系统")
    st.markdown("""
    ### 欢迎使用！
    👈 **请在左侧侧边栏选择一套试卷开始练习。**

    **💡 推荐尝试：**
    * 选择 **“🎲 随机生成试卷”**，系统会从所有题库中按标准比例随机抽取题目，
      每次生成的试卷都不一样，适合考前突击！
    """)
else:
    # 获取当前题目数据
    questions = st.session_state.paper_data
    total_q = len(questions)
    current_idx = st.session_state.question_index
    q_data = questions[current_idx]

    # --- 考试结束界面 ---
    if current_idx >= total_q:
        st.balloons()
        st.title("🎉 测试结束！")

        # 避免除以零（虽然不太可能）
        if total_q > 0:
            accuracy = (st.session_state.score / total_q) * 100
        else:
            accuracy = 0

        col1, col2, col3 = st.columns(3)
        col1.metric("最终得分", f"{st.session_state.score} / {total_q}")
        col2.metric("正确率", f"{accuracy:.1f}%")

        st.success("恭喜你完成了整套试卷！")

        if st.button("🔄 重新开始本卷"):
            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.answer_submitted = False
            st.rerun()

    else:
        # --- 答题界面 ---

        # 1. 顶部进度条
        progress = min((current_idx + 1) / total_q, 1.0)
        st.progress(progress, text=f"当前进度: {current_idx + 1}/{total_q} - [{q_data.get('type', 'Unknown')}]")

        # 2. 显示阅读材料
        if 'context' in q_data and q_data['context']:
            with st.expander("📖 阅读文章 / 背景材料 (点击展开/收起)", expanded=True):
                st.markdown(f"*{q_data['context']}*")

        st.divider()

        # 3. 显示题目
        # 注意：随机组卷后，原来的 id (如 "1", "2") 可能会乱序，这里显示 "Question + 当前序号" 更自然
        st.subheader(f"Question {current_idx + 1}")
        st.write(f"**{q_data['question']}**")

        # 4. 答题区域

        # === 客观题 ===
        if 'options' in q_data:
            options_dict = q_data['options']
            option_keys = sorted(options_dict.keys())
            formatted_options = [f"{k}. {options_dict[k]}" for k in option_keys]

            # 这里的 key 很重要，加上 current_paper_id 确保切换试卷时控件重置
            radio_key = f"q_{st.session_state.current_paper_id}_{current_idx}_radio"

            user_choice_full = st.radio(
                "请选择答案:",
                formatted_options,
                index=None,
                key=radio_key,
                disabled=st.session_state.answer_submitted
            )

            if not st.session_state.answer_submitted:
                if st.button("提交答案"):
                    if user_choice_full:
                        st.session_state.answer_submitted = True

                        user_choice = user_choice_full.split('.')[0]
                        correct_choice = q_data['answer'].strip().upper()

                        if user_choice == correct_choice:
                            st.session_state.score += 1
                            st.balloons()
                            st.success("✅ 回答正确！")
                        else:
                            st.error(f"❌ 回答错误！正确答案是: **{correct_choice}**")
                            if q_data.get('explanation'):
                                st.info(f"💡 解析: {q_data['explanation']}")
                        st.rerun()
                    else:
                        st.warning("⚠️ 请先选择一个选项！")
            else:
                # 保持显示
                saved_choice = st.session_state.get(radio_key)
                if saved_choice:
                    user_c = saved_choice.split('.')[0]
                    correct_c = q_data['answer'].strip().upper()
                    if user_c == correct_c:
                        st.success("✅ 你已回答正确")
                    else:
                        st.error(f"❌ 你选择了 {user_c}，正确答案是 {correct_c}")
                        if q_data.get('explanation'):
                            st.info(f"💡 解析: {q_data['explanation']}")

        # === 主观题 ===
        else:
            st.text_area("✍️ 在此输入你的翻译 (仅供自测，可选):", disabled=st.session_state.answer_submitted)

            if not st.session_state.answer_submitted:
                if st.button("查看参考答案"):
                    st.session_state.answer_submitted = True
                    st.rerun()
            else:
                st.markdown("### 📝 参考答案:")
                st.success(q_data['answer'])

                st.markdown("**🤔 自我评分:**")
                col_y, col_n = st.columns(2)

                eval_key = f"self_eval_{st.session_state.current_paper_id}_{current_idx}"

                if eval_key not in st.session_state:
                    if col_y.button("我觉得我对了 (得分+1)"):
                        st.session_state.score += 1
                        st.session_state[eval_key] = "correct"
                        st.rerun()
                    if col_n.button("我答错了 (不得分)"):
                        st.session_state[eval_key] = "wrong"
                        st.rerun()
                else:
                    if st.session_state[eval_key] == "correct":
                        st.success("✅ 已记录为正确")
                    else:
                        st.error("❌ 已记录为错误")

        # 5. 下一题按钮
        if st.session_state.answer_submitted:
            can_proceed = False
            if 'options' in q_data:
                can_proceed = True
            else:
                eval_key = f"self_eval_{st.session_state.current_paper_id}_{current_idx}"
                if eval_key in st.session_state:
                    can_proceed = True

            if can_proceed:
                st.divider()
                if st.button("➡️ 下一题", type="primary"):
                    st.session_state.question_index += 1
                    st.session_state.answer_submitted = False
                    st.rerun()