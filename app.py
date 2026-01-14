import streamlit as st
import json
import os

# 设置页面配置（标题、图标、布局）
st.set_page_config(
    page_title="英语学位考试模拟系统",
    page_icon="🎓",
    layout="wide"
)


# ================= 辅助函数 =================
def load_data(filename='data_full.json'):
    if not os.path.exists(filename):
        st.error(f"❌ 找不到文件 {filename}，请先运行 generate_full_data.py 生成题库！")
        return {}
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


# 初始化 Session State (用于记录答题状态)
if 'current_paper' not in st.session_state:
    st.session_state.current_paper = None
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answer_submitted' not in st.session_state:
    st.session_state.answer_submitted = False
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}  # 记录用户的答案

# ================= 侧边栏：选择试卷 =================
st.sidebar.title("📚 考试菜单")
all_data = load_data()

if all_data:
    paper_list = list(all_data.keys())
    selected_paper = st.sidebar.selectbox(
        "请选择试卷",
        paper_list,
        index=None,
        placeholder="点击选择..."
    )

    # 如果切换了试卷，重置状态
    if selected_paper != st.session_state.current_paper:
        st.session_state.current_paper = selected_paper
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.answer_submitted = False
        st.session_state.user_answers = {}
        st.rerun()

# ================= 主界面逻辑 =================

if not st.session_state.current_paper:
    st.title("🎓 英语学位考试全真模拟系统")
    st.markdown("""
    ### 欢迎使用！

    👈 **请在左侧侧边栏选择一套试卷开始练习。**

    本系统包含：
    * 📖 **Reading Comprehension** (阅读理解)
    * 🔤 **Vocabulary & Structure** (词汇与结构)
    * 🧩 **Cloze** (完形填空)
    * 📝 **Translation** (翻译)
    """)
    st.info("💡 提示：答题过程中会自动显示解析，主观题支持自测评分。")

else:
    # 获取当前试卷题目
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
            st.session_state.user_answers = {}
            st.rerun()

    else:
        # --- 答题界面 ---
        q_data = questions[current_idx]

        # 1. 顶部进度条
        progress = (current_idx + 1) / total_q
        st.progress(progress, text=f"当前进度: {current_idx + 1}/{total_q} - [{q_data.get('type', 'Unknown')}]")

        # 2. 显示阅读材料/完形段落 (如果有)
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
            # 将选项转换为列表供 radio 使用
            option_keys = sorted(options_dict.keys())
            formatted_options = [f"{k}. {options_dict[k]}" for k in option_keys]

            # 使用 radio 组件
            user_choice_full = st.radio(
                "请选择答案:",
                formatted_options,
                index=None,
                key=f"q_{current_idx}",
                disabled=st.session_state.answer_submitted
            )

            # 提交按钮
            if not st.session_state.answer_submitted:
                if st.button("提交答案"):
                    if user_choice_full:
                        st.session_state.answer_submitted = True

                        # 提取选项字母 (例如 "A. xxx" -> "A")
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

            # 已提交，显示结果和下一题按钮
            else:
                user_choice = st.session_state.get(f"q_{current_idx}", "").split('.')[0]
                correct_choice = q_data['answer'].strip().upper()

                if user_choice == correct_choice:
                    st.success("✅ 你已回答正确")
                else:
                    st.error(f"❌ 你选择了 {user_choice}，正确答案是 {correct_choice}")
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

                # 自测按钮逻辑
                # 这里为了简化，只有还没自评过才显示按钮
                if f"self_eval_{current_idx}" not in st.session_state:
                    if col_y.button("我觉得我对了 (得分+1)"):
                        st.session_state.score += 1
                        st.session_state[f"self_eval_{current_idx}"] = "correct"
                        st.rerun()
                    if col_n.button("我答错了 (不得分)"):
                        st.session_state[f"self_eval_{current_idx}"] = "wrong"
                        st.rerun()
                else:
                    if st.session_state[f"self_eval_{current_idx}"] == "correct":
                        st.success("✅ 已记录为正确")
                    else:
                        st.error("❌ 已记录为错误")

        # 5. 下一题按钮 (仅在提交后显示)
        if st.session_state.answer_submitted:
            # 翻译题需要先自评才能下一题，或者选择题直接下一题
            if 'options' in q_data or f"self_eval_{current_idx}" in st.session_state:
                st.divider()
                if st.button("➡️ 下一题", type="primary"):
                    st.session_state.question_index += 1
                    st.session_state.answer_submitted = False
                    st.rerun()