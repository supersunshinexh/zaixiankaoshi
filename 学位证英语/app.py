import streamlit as st
import json
import os
import sys

# 设置页面配置
st.set_page_config(
    page_title="英语学位考试模拟系统",
    page_icon="🎓",
    layout="wide"
)


# ================= 辅助函数：核心路径修复 =================
def get_resource_path(relative_path):
    """
    获取资源文件的绝对路径。
    使用 __file__ 确保永远相对于 app.py 所在的目录寻找文件，
    而不是相对于 Streamlit 的运行根目录。
    """
    # 1. 兼容 PyInstaller 打包后的环境
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    # 2. 正常运行环境 (本地或 Streamlit Cloud)
    # 获取 app.py 当前所在的文件夹路径 (即 '学位证英语' 文件夹)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, relative_path)


def load_data(filename='data_full.json'):
    # 使用修复后的路径函数
    file_path = get_resource_path(filename)

    if not os.path.exists(file_path):
        # 打印路径方便调试
        st.error(f"❌ 找不到文件: {file_path}")
        st.error("请确保 data_full.json 和 app.py 在同一个文件夹内！")
        return {}

    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


# 初始化 Session State
if 'current_paper' not in st.session_state:
    st.session_state.current_paper = None
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

# 1. 选择试卷
if all_data:
    paper_list = list(all_data.keys())
    selected_paper = st.sidebar.selectbox(
        "请选择试卷",
        paper_list,
        index=None,
        placeholder="点击选择..."
    )

    # 切换试卷时重置状态
    if selected_paper != st.session_state.current_paper:
        st.session_state.current_paper = selected_paper
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.answer_submitted = False
        st.session_state.user_answers = {}
        st.rerun()

# 2. 题目导航 (仅在已选择试卷时显示)
if st.session_state.current_paper:
    questions = all_data[st.session_state.current_paper]
    total_q = len(questions)

    st.sidebar.markdown("---")
    st.sidebar.subheader("📍 题目导航")


    def on_nav_change():
        new_index = st.session_state.q_nav - 1
        if new_index != st.session_state.question_index:
            st.session_state.question_index = new_index
            st.session_state.answer_submitted = False


    current_q_num = st.sidebar.selectbox(
        "跳转到题目:",
        options=range(1, total_q + 1),
        index=st.session_state.question_index,
        key="q_nav",
        on_change=on_nav_change,
        format_func=lambda x: f"第 {x} 题"
    )

    current_type = questions[st.session_state.question_index].get('type', '未知')
    st.sidebar.info(f"当前题型: {current_type}")

# ================= 主界面逻辑 =================

if not st.session_state.current_paper:
    st.title("🎓 英语学位考试全真模拟系统")
    st.markdown("""
    ### 欢迎使用！
    👈 **请在左侧侧边栏选择一套试卷开始练习。**
    """)
else:
    # 获取当前题目数据
    questions = all_data[st.session_state.current_paper]
    total_q = len(questions)
    current_idx = st.session_state.question_index

    # --- 考试结束界面 ---
    if current_idx >= total_q:
        st.balloons()
        st.title("🎉 测试结束！")

        accuracy = (st.session_state.score / total_q) * 100

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
        q_data = questions[current_idx]

        # 1. 顶部进度条
        progress = (current_idx + 1) / total_q
        st.progress(progress, text=f"当前进度: {current_idx + 1}/{total_q} - [{q_data.get('type', 'Unknown')}]")

        # 2. 显示阅读材料 (如果有)
        if 'context' in q_data and q_data['context']:
            with st.expander("📖 阅读文章 / 背景材料 (点击展开/收起)", expanded=True):
                st.markdown(f"*{q_data['context']}*")

        st.divider()

        # 3. 显示题目
        st.subheader(f"Question {q_data['id']}")
        st.write(f"**{q_data['question']}**")

        # 4. 答题区域

        # === 客观题 (选择题) ===
        if 'options' in q_data:
            options_dict = q_data['options']
            option_keys = sorted(options_dict.keys())
            formatted_options = [f"{k}. {options_dict[k]}" for k in option_keys]

            user_choice_full = st.radio(
                "请选择答案:",
                formatted_options,
                index=None,
                key=f"q_{current_idx}_radio",
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
                # 保持显示用户的选择和答案状态
                saved_choice = st.session_state.get(f"q_{current_idx}_radio")
                if saved_choice:
                    user_c = saved_choice.split('.')[0]
                    correct_c = q_data['answer'].strip().upper()
                    if user_c == correct_c:
                        st.success("✅ 你已回答正确")
                    else:
                        st.error(f"❌ 你选择了 {user_c}，正确答案是 {correct_c}")
                        if q_data.get('explanation'):
                            st.info(f"💡 解析: {q_data['explanation']}")

        # === 主观题 (翻译题) ===
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

                eval_key = f"self_eval_{st.session_state.current_paper}_{current_idx}"

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
                eval_key = f"self_eval_{st.session_state.current_paper}_{current_idx}"
                if eval_key in st.session_state:
                    can_proceed = True

            if can_proceed:
                st.divider()
                if st.button("➡️ 下一题", type="primary"):
                    st.session_state.question_index += 1
                    st.session_state.answer_submitted = False
                    st.rerun()