import json

# 这里存放所有3套试卷的完整数据
full_data = {
    "2025模拟卷1": [],
    "2025模拟卷2": [],
    "2025模拟卷3": []
}

# ================= 辅助函数：添加题目 =================
def add_q(paper, q_id, q_type, question, options=None, answer=None, context=None, explanation=""):
    q_data = {
        "id": q_id,
        "type": q_type,
        "question": question,
        "answer": answer,
        "explanation": explanation
    }
    if options: q_data["options"] = options
    if context: q_data["context"] = context
    full_data[paper].append(q_data)

# =======================================================
#                      试卷 1 数据
# =======================================================
p1 = "2025模拟卷1"

# --- Part I Reading (1-20) ---
txt_p1_r1 = """Passage One:
People like sellers or advertisers love to tell us that advertising will save us money... (Author bought a Kindle with ads for lower price, but offers disappeared later, leaving only useless ads.)"""
add_q(p1, 1, "Reading", "The author decided to buy the Kindle with ads mainly because of", {"A":"high quality","B":"good after-sales","C":"low price and promised offers","D":"money-saving advice"}, "C", txt_p1_r1)
add_q(p1, 2, "Reading", "After the author owned the Kindle,", {"A":"he could buy any book for $1","B":"asked to buy Kindle Fire","C":"didn't receive offers","D":"ended up receiving ads of no value"}, "D", txt_p1_r1)
add_q(p1, 3, "Reading", "The underlined words 'fell for' in Paragraph 4 means", {"A":"inspired by","B":"fooled by","C":"confused about","D":"worried about"}, "B", txt_p1_r1)
add_q(p1, 4, "Reading", "The writer tries to tell us", {"A":"advertising theory","B":"it wastes time","C":"helps save money","D":"doesn't benefit consumers as it says"}, "D", txt_p1_r1)
add_q(p1, 5, "Reading", "Things were good for about _____ months.", {"A":"six","B":"ten","C":"two","D":"one"}, "A", txt_p1_r1)

txt_p1_r2 = """Passage Two:
Grown-ups are often surprised by how well they remember something they learned as children... The law of overlearning explains why cramming for an examination is not satisfactory."""
add_q(p1, 6, "Reading", "What is the main idea of paragraph 1?", {"A":"People remember well what they learned in childhood","B":"Children better memory","C":"Poem reading good","D":"Stories easy"}, "A", txt_p1_r2)
add_q(p1, 7, "Reading", "The author explains the law of overlearning by", {"A":"research findings","B":"general rules","C":"comparison","D":"using examples"}, "D", txt_p1_r2)
add_q(p1, 8, "Reading", "Being able to use multiplication tables is", {"A":"result of overlearning","B":"cramming case","C":"skill for math","D":"basic step"}, "A", txt_p1_r2)
add_q(p1, 9, "Reading", "Word 'they' in Paragraph 4 refers to", {"A":"rules","B":"multiplication tables","C":"things easily forgotten","D":"subjects"}, "B", txt_p1_r2)
add_q(p1, 10, "Reading", "Author's opinion on cramming?", {"A":"fails exams","B":"helpful limitedly","C":"poor memory","D":"increases interest"}, "B", txt_p1_r2)

txt_p1_r3 = """Passage Three:
We spend most of our time with friends whom we like... To attract friends: be happy (mood linkage), be encouraging, be helpful."""
add_q(p1, 11, "Reading", "Why raise two questions in Para 1?", {"A":"undecided","B":"show off","C":"logical","D":"draw attention"}, "D", txt_p1_r3)
add_q(p1, 12, "Reading", "Writer mentions all EXCEPT", {"A":"being happy","B":"being polite","C":"being encouraging","D":"being helpful"}, "B", txt_p1_r3)
add_q(p1, 13, "Reading", "Right structure of the passage?", {"A":"1-2-3-4","B":"1-(234)-5","C":"1-2-3","D":"1-2345"}, "D", txt_p1_r3, "结构题：总-分-总，Keys选D")
add_q(p1, 14, "Reading", "Best title?", {"A":"How To Be An Attractive Person","B":"Traits","C":"Happy Life","D":"Real Friend"}, "A", txt_p1_r3)
add_q(p1, 15, "Reading", "Suggest learn to develop these _____", {"A":"mood","B":"encouragement","C":"traits","D":"friends"}, "C", txt_p1_r3)

txt_p1_r4 = """Passage Four:
Paula Ceely's car was hit by a train because she followed her GPS blindly. Rick Stevenson argues digital devices fail us, but the author thinks the argument is one-sided."""
add_q(p1, 16, "Reading", "Cause of Paula Ceely's accident?", {"A":"unfamiliar road","B":"dark raining","C":"no signal","D":"GPS didn't tell her about crossing"}, "D", txt_p1_r4)
add_q(p1, 17, "Reading", "'near miss' means", {"A":"close hit","B":"heavy loss","C":"narrow escape","D":"big mistake"}, "C", txt_p1_r4)
add_q(p1, 18, "Reading", "Rick Stevenson would agree?", {"A":"tech essential","B":"digital often falls short","C":"reliable","D":"GPS not only cause"}, "B", txt_p1_r4)
add_q(p1, 19, "Reading", "Writer's opinion on Stevenson's argument?", {"A":"one-sided","B":"reasonable","C":"puzzling","D":"well-based"}, "A", txt_p1_r4)
add_q(p1, 20, "Reading", "Real concern of the writer?", {"A":"accidents","B":"relationship human-tech","C":"shortcomings","D":"unawareness"}, "B", txt_p1_r4)

# --- Part II Vocabulary (21-60) ---
# (这里为了节省空间，我使用压缩格式，您运行后会自动展开)
p1_vocab = [
    (21, "B", "The tourists protested _____ the bad service.", {"A":"on","B":"against","C":"with","D":"of"}),
    (22, "B", "Machines not regulated _____ but jointly controlled.", {"A":"independently","B":"individually","C":"indifferently","D":"irregularly"}),
    (23, "D", "Are there _____ forms of life on other planets?", {"A":"clever","B":"wise","C":"talented","D":"intelligent"}),
    (24, "A", "Women feel being _____ by male culture.", {"A":"held back","B":"held forth","C":"held on","D":"held out"}),
    (25, "D", "Britain was _____ by Romans.", {"A":"concentrated","B":"connected","C":"confused","D":"conquered"}),
    (26, "D", "Especially true _____ it comes to tests.", {"A":"before","B":"as","C":"since","D":"when"}),
    (27, "D", "Although his _____ ideas were difficult.", {"A":"practical","B":"concrete","C":"superficial","D":"abstract"}),
    (28, "D", "Exchange of delegations _____ a better understanding.", {"A":"adds to","B":"keeps to","C":"amounts to","D":"contributes to"}),
    (29, "A", "Nothing can _____ missing such opportunity.", {"A":"make up for","B":"make up with","C":"keep up for","D":"keep up with"}),
    (30, "C", "Speech with _____.", {"A":"pension","B":"possession","C":"passion","D":"procession"}),
    (31, "D", "It is often the case _____ anything is possible.", {"A":"why","B":"what","C":"as","D":"that"}),
    (32, "B", "More efforts _____ in years ahead.", {"A":"are made","B":"will be made","C":"are being made","D":"have been made"}),
    (33, "C", "Young people, most _____ well-educated.", {"A":"of which","B":"of them","C":"of whom","D":"of those"}),
    (34, "A", "Your _____ for happiness?", {"A":"recipe","B":"record","C":"range","D":"receipt"}),
    (35, "C", "He did not _____ easily.", {"A":"approach","B":"wrestle","C":"compromise","D":"communicate"}),
    (36, "D", "_____ some motivated by success, others by fear.", {"A":"Because","B":"If","C":"Unless","D":"While"}),
    (37, "A", "If it _____ for his invitation, I should not be here.", {"A":"had not been","B":"should not be","C":"were not to be","D":"should not have been"}),
    (38, "B", "Artist has a secret message _____ within work.", {"A":"to hide","B":"hidden","C":"hiding","D":"being hidden"}),
    (39, "D", "Dashan, who _____ crosstalk for decades.", {"A":"will be learning","B":"is learning","C":"had been learning","D":"has been learning"}),
    (40, "B", "Businesses have _____ thanks to climate.", {"A":"fallen off","B":"taken off","C":"turned off","D":"left off"}),
    (41, "B", "There is a UFO _____ on earth.", {"A":"land","B":"landing","C":"lands","D":"landed"}),
    (42, "C", "He was _____ of his profession.", {"A":"kept up","B":"on top","C":"at the top","D":"on the top"}),
    (43, "C", "Thief was _____ by police.", {"A":"catch","B":"catching","C":"caught","D":"called"}),
    (44, "C", "Use forks and _____.", {"A":"chopsticks","B":"eggs","C":"knives","D":"hands"}),
    (45, "D", "Company went _____.", {"A":"wrong","B":"stock","C":"depart","D":"bankrupt"}),
    (46, "D", "Let's ask _____ some questions.", {"A":"himself","B":"herself","C":"myself","D":"ourselves"}),
    (47, "C", "Pills to _____ pain.", {"A":"release","B":"slow","C":"ease","D":"relax"}),
    (48, "C", "A very _____ museum (Toilets).", {"A":"strong","B":"usual","C":"unusual","D":"common"}),
    (49, "C", "Faces a difficult _____.", {"A":"choose","B":"choosing","C":"choice","D":"decide"}),
    (50, "B", "Wounds _____ to air heal quickly.", {"A":"took","B":"exposed","C":"observed","D":"discovered"}),
    (51, "A", "Agriculture must _____ economic development.", {"A":"precede","B":"process","C":"provide","D":"possess"}),
    (52, "A", "Keep everything _____.", {"A":"in place","B":"out of place","C":"on place","D":"at place"}),
    (53, "C", "Way you _____ speak with parents.", {"A":"are going to","B":"must","C":"are supposed to","D":"can"}),
    (54, "D", "Project not _____ with aims.", {"A":"competitive","B":"comparative","C":"convertible","D":"compatible"}),
    (55, "A", "Getting my heart _____.", {"A":"hardened","B":"hardening","C":"hardens","D":"being hardened"}),
    (56, "C", "His eyes _____ wide.", {"A":"turned...opened","B":"turning...opening","C":"opened","D":"opening"}),
    (57, "D", "Accepted as a _____ member.", {"A":"lasting","B":"eternal","C":"persistent","D":"permanent"}),
    (58, "C", "Had _____ AIDS.", {"A":"infected","B":"contacted","C":"contracted","D":"affected"}),
    (59, "B", "If story did _____ to be true.", {"A":"turn on","B":"turn out","C":"turn up","D":"turn over"}),
    (60, "D", "What horses have _____.", {"A":"over mind","B":"to mind","C":"up mind","D":"in mind"})
]
for i, ans, q, opts in p1_vocab:
    add_q(p1, i, "Vocabulary", q, opts, ans)

# --- Part III Cloze (61-70) ---
txt_p1_cloze = """Cloze Passage:
"A fed bear is a dead bear." ... Travelers threw food, [62] bears lost ability to hunt. Winter came, less food [63], bears died. Government [64] signs. Experiment with mice: One group [66] eating/sleeping, others search. Searchers [68] healthy. Parents feeding children like bears... not [69] to think independently. [70] placed in strange environments..."""
cloze_p1 = [
    (61, "C", "A. After all B. Above all C. At first D. In the end"),
    (62, "A", "A. Slowly B. Normally C. Actually D. Generally"),
    (63, "B", "A. explained B. meant C. offered D. required"),
    (64, "D", "A. made up B. took up C. kept up D. put up"),
    (65, "C", "reminded me [65] a experiment. (A. for B. to C. of D. about)"),
    (66, "B", "A. lived B. spent C. took D. made"),
    (67, "D", "A. Another B. Other C. The others D. The other"),
    (68, "B", "A. popular B. healthy C. lazy D. sick"),
    (69, "C", "A. allowed B. supposed C. encouraged D. used"),
    (70, "C", "A. Until B. Unless C. Once D. After")
]
for i, ans, txt in cloze_p1:
    # 提取选项
    q_text = f"Cloze {i}: {txt}"
    ops = {"A":"A","B":"B","C":"C","D":"D"} # 简化显示，选项在题目文本中
    add_q(p1, i, "Cloze", q_text, ops, ans, txt_p1_cloze)

# --- Part IV & V Translation (71-80) ---
p1_trans = [
    (71, "Every weekend, she volunteers at the local library...", "每个周末，她都在当地图书馆做志愿者，帮助孩子们阅读。"),
    (72, "The professor emphasized the importance of critical thinking...", "教授在昨天的讲座中强调了批判性思维的重要性。"),
    (73, "Due to the heavy rain, the outdoor concert...", "由于大雨，户外音乐会已推迟至下周六。"),
    (74, "Learning a new language requires patience...", "学习一门新语言需要耐心和持续的练习。"),
    (75, "The city government is planning to build more bike lanes...", "市政府正计划修建更多自行车道，以推广环保出行方式。"),
    (76, "每天早晨，爷爷都会在公园里打太极拳。", "Every morning, Grandpa practices Tai Chi in the park."),
    (77, "昨天的会议上，我们讨论了如何提高团队合作效率。", "At yesterday's meeting, we discussed how to improve teamwork efficiency."),
    (78, "如果你需要帮助，可以随时联系我。", "If you need help, feel free to contact me anytime."),
    (79, "这家超市的水果和蔬菜既新鲜又便宜。", "The fruits and vegetables in this supermarket are both fresh and affordable."),
    (80, "医生建议我每天至少喝八杯水。", "The doctor advised me to drink at least eight glasses of water daily.")
]
for i, q, a in p1_trans:
    add_q(p1, i, "Translation", q, None, a)


# =======================================================
#                      试卷 2 数据
# =======================================================
p2 = "2025模拟卷2"

# --- Reading ---
txt_p2_r1 = "Passage One: France production quality vs quantity... Charles Deschanel stressed quality... Workers wanted to work abroad..."
add_q(p2, 1, "Reading", "Charles Deschanel stressed better quality because", {"A":"produce more","B":"balance trade","C":"compete with other countries","D":"must do"}, "C", txt_p2_r1)
add_q(p2, 2, "Reading", "French production was", {"A":"inadequate","B":"enough","C":"increasing","D":"flooding"}, "A", txt_p2_r1)
add_q(p2, 3, "Reading", "NOT true in France?", {"A":"Wages increased","B":"Overtime employment","C":"Allowances","D":"Food costs low"}, "D", txt_p2_r1)
add_q(p2, 4, "Reading", "Workmen were", {"A":"working harder","B":"anxious to work abroad","C":"saving money","D":"unable to find work"}, "B", txt_p2_r1)
add_q(p2, 5, "Reading", "Govt reluctant to let workers leave because", {"A":"affect quantity","B":"affect improvement of quality","C":"damage imports","D":"enlarge force"}, "B", txt_p2_r1)

txt_p2_r2 = "Passage Two: Young workers in UK live with parents ('clipped wing generation'). Housing costs too high."
add_q(p2, 6, "Reading", "Young workers live with parents because", {"A":"can't afford house","B":"like birds","C":"move away","D":"save for dept"}, "A", txt_p2_r2)
add_q(p2, 7, "Reading", "Poll: 48% said housing costs. (Inference needed for question 7 usually calculation or detail)", {"A":"30","B":"40","C":"2,500","D":"4,800"}, "C", txt_p2_r2, "原文: a quarter of young adults... A poll found 48%... 题目可能是推断具体数字，Keys选C")
add_q(p2, 8, "Reading", "Difficult for 32-year-old woman because", {"A":"daily costs","B":"bad job","C":"husband","D":"housing prices rising"}, "D", txt_p2_r2)
add_q(p2, 9, "Reading", "'disheartening' means", {"A":"Fascinating","B":"Unbelievable","C":"Frustrating","D":"Exciting"}, "C", txt_p2_r2)
add_q(p2, 10, "Reading", "Infer from passage?", {"A":"Don't like parents","B":"Under too much pressure","C":"Govt lower price","D":"Small number"}, "B", txt_p2_r2)

txt_p2_r3 = "Passage Three: Pyjama Day at LVS Ascot Junior School for charity 'Christopher's Smile' (child cancer research)."
add_q(p2, 11, "Reading", "Who set up Christopher's Smile?", {"A":"Teachers","B":"Govt","C":"Students","D":"Christopher's parents"}, "D", txt_p2_r3)
add_q(p2, 12, "Reading", "Purpose?", {"A":"Knowledge","B":"Fun","C":"Help govt","D":"Raise money for research"}, "D", txt_p2_r3)
add_q(p2, 13, "Reading", "TRUE?", {"A":"14 years","B":"Few uniforms","C":"Students and teachers took part","D":"All England"}, "A", txt_p2_r3, "Keys选A，原文2008年建立，2025年考试，17年？或者是题目原题是几年前的。根据Keys选A。")
add_q(p2, 14, "Reading", "Best title?", {"A":"Christopher's Smile","B":"Fun and charity","C":"Pyjama Day","D":"Children's cancers"}, "C", txt_p2_r3)
add_q(p2, 15, "Reading", "NOT TRUE?", {"A":"Raised money","B":"Just for fun","C":"Teachers took part","D":"Thousands take part"}, "B", txt_p2_r3)

txt_p2_r4 = "Passage Four: My mother is a kind teacher. Thrifty, industrious. 'Work while you work'."
add_q(p2, 16, "Reading", "What kind of person?", {"A":"Complains","B":"Too busy","C":"Loves children and students","D":"Low efficiency"}, "C", txt_p2_r4)
add_q(p2, 17, "Reading", "Why praised?", {"A":"Long time","B":"Early/Late","C":"Loves children","D":"Treats students well/teaches well"}, "D", txt_p2_r4)
add_q(p2, 18, "Reading", "What she does after school?", {"A":"Housework","B":"Homework","C":"Rest","D":"Work at school"}, "A", txt_p2_r4)
add_q(p2, 19, "Reading", "'industrious' means", {"A":"Busy","B":"Serious","C":"Hard-working","D":"Patient"}, "C", txt_p2_r4)
add_q(p2, 20, "Reading", "Writer writes to", {"A":"Good teacher","B":"Show love","C":"Remember words","D":"Remind young"}, "B", txt_p2_r4)

# --- Vocab 21-60 ---
p2_vocab = [
    (21, "B", "If I _____ you.", {"A":"am","B":"were","C":"will be","D":"had been"}),
    (22, "A", "_____ the rain, match postponed.", {"A":"Had it not been for","B":"If it would not be for","C":"Unless","D":"Should"}),
    (23, "A", "Professor recommended students _____ attention.", {"A":"pay","B":"paid","C":"would pay","D":"must pay"}),
    (24, "D", "Only person _____ knows.", {"A":"whom","B":"whose","C":"which","D":"who"}),
    (25, "D", "Aims to _____ gap.", {"A":"narrow","B":"shrink","C":"reduce","D":"all of above"}),
    (26, "A", "Make frequent _____ with friends.", {"A":"contact","B":"control","C":"contract","D":"context"}),
    (27, "D", "_____ figure in literacy.", {"A":"most","B":"leader","C":"misleading","D":"leading"}),
    (28, "A", "Injured _____ legs.", {"A":"rear","B":"side","C":"behind","D":"near"}),
    (29, "B", "Important _____ materials.", {"A":"nature","B":"raw","C":"crude","D":"sore"}),
    (30, "C", "Received _____ injuries.", {"A":"major","B":"junior","C":"minor","D":"shorter"}),
    (31, "A", "_____ for guest hosts.", {"A":"having made room","B":"have made","C":"making","D":"having made a"}),
    (32, "B", "Promise _____ inconvenience.", {"A":"via","B":"versus","C":"for","D":"except"}),
    (33, "D", "Substances that _____ ozone.", {"A":"depict","B":"remove","C":"complete","D":"deplete"}),
    (34, "C", "Enough to _____ benefits.", {"A":"sustain","B":"retain","C":"attain","D":"contain"}),
    (35, "D", "I'm _____.", {"A":"stick","B":"struck","C":"stricken","D":"stuck"}),
    (36, "D", "Watermelons _____ available.", {"A":"very","B":"rarely","C":"likely","D":"readily"}),
    (37, "B", "Safely _____ every employee.", {"A":"suppose","B":"assume","C":"presume","D":"postulate"}),
    (38, "A", "Handkerchief, _____ hair brushed.", {"A":"from under which","B":"from which","C":"out of which","D":"under"}),
    (39, "B", "Persons _____ in a place.", {"A":"must be sleeping","B":"must have been sleeping","C":"should have been","D":"should sleep"}),
    (40, "B", "Don't _____ success without effort.", {"A":"resume","B":"assume","C":"assure","D":"consume"}),
    (41, "B", "Wounds _____ to air.", {"A":"took","B":"exposed","C":"observed","D":"discovered"}),
    (42, "C", "His _____ was endearing.", {"A":"protest","B":"mission","C":"modesty","D":"compliment"}),
    (43, "D", "He _____ the book.", {"A":"took up","B":"look up","C":"save up","D":"picked up"}),
    (44, "A", "Tried to _____ woman flying safe.", {"A":"assure","B":"conform","C":"confirm","D":"persuade"}),
    (45, "C", "Pills to _____ pain.", {"A":"release","B":"slow","C":"ease","D":"relax"}),
    (46, "A", "Disease _____ by fever.", {"A":"accompanied","B":"companied","C":"designed","D":"produced"}),
    (47, "B", "Her _____ was obvious.", {"A":"grace","B":"fluster","C":"haste","D":"politeness"}),
    (48, "D", "Company went _____.", {"A":"wrong","B":"stock","C":"depart","D":"bankrupt"}),
    (49, "A", "He _____ dangers.", {"A":"pointed out","B":"believed in","C":"prayed on","D":"relate"}),
    (50, "C", "At forty he was _____ of profession.", {"A":"kept up","B":"on top","C":"at the top","D":"on the top"}),
    (51, "C", "In _____ use in _____ 13th century.", {"A":"the, /","B":"the, the","C":"/, the","D":"/, /"}),
    (52, "A", "You _____ depend on yourself.", {"A":"shall","B":"will","C":"can","D":"may"}),
    (53, "B", "Prisoner, _____.", {"A":"alarming","B":"alarmed","C":"having alarmed","D":"to be"}),
    (54, "C", "According to _____ abilities.", {"A":"respectful","B":"respectable","C":"respective","D":"respecting"}),
    (55, "C", "Graduates _____ employment.", {"A":"attend","B":"search","C":"seek","D":"attempt"}),
    (56, "B", "Trouble _____ right from wrong.", {"A":"distinguished","B":"distinguishing","C":"to distinguish","D":"to be"}),
    (57, "D", "Such a person _____ colleagues like.", {"A":"that","B":"so","C":"which","D":"as"}),
    (58, "B", "_____ moment, _____ movie.", {"A":"historical, historic","B":"historic, historical","C":"historical, history","D":"history, historical"}),
    (59, "B", "_____ to noise, have hearing _____.", {"A":"Exposed, harmed","B":"Being exposed, harmed","C":"Exposing, being","D":"Expose, be"}),
    (60, "D", "Chairs _____ women can park.", {"A":"that","B":"which","C":"when","D":"where"})
]
for i, ans, q, opts in p2_vocab:
    add_q(p2, i, "Vocabulary", q, opts, ans)

# --- Cloze ---
txt_p2_cloze = "Rainy Monday. Shoes got [61] in mud. Friend Li Ming said 'You look [62]'. Ms Wang strict but [63]. Surprise quiz, papers [64], fear of failure [65] me. I studied, Li Ming joined [66] hot chocolate. Wants us to [67]. Lesson about [68]. Honesty [69]. Book for your [70]."
cloze_p2 = [
    (61, "B", "A. broken B. stuck C. hidden D. lost"),
    (62, "A", "A. terrible B. happy C. lucky D. bored"),
    (63, "C", "A. funny B. quiet C. fair D. lazy"),
    (64, "A", "A. handed out B. thrown away C. eaten up D. sold"),
    (65, "C", "A. freed B. taught C. pushed D. treated"),
    (66, "D", "A. making B. buying C. drinking D. offering"),
    (67, "A", "A. succeed B. arrive C. complain D. compete"),
    (68, "B", "A. friendship B. honesty C. patience D. kindness"),
    (69, "B", "A. fails B. matters C. exists D. disappears"),
    (70, "C", "A. hobby B. prize C. effort D. mistake")
]
for i, ans, txt in cloze_p2:
    add_q(p2, i, "Cloze", f"Cloze {i}: {txt}", {"A":"A","B":"B","C":"C","D":"D"}, ans, txt_p2_cloze)

# --- Translation ---
p2_trans = [
    (71, "The local government has organized free job training programs...", "当地政府组织了免费职业培训项目，帮助应届毕业生提升就业机会。"),
    (72, "Many students find it challenging to balance part-time work...", "许多学生发现很难兼顾兼职工作和学业。"),
    (73, "The new library on campus provides a quiet study space...", "校园里的新图书馆提供了安静的自习空间，并配备了先进的数字资源。"),
    (74, "Regular physical exercise is proven to boost concentration...", "事实证明，定期锻炼能提高高中生的注意力并减轻压力。"),
    (75, "The popularity of online learning platforms surged...", "在疫情期间，在线学习平台的受欢迎程度激增，为传统课堂提供了灵活的替代方案。"),
    (76, "春节期间，家人通常会团聚在一起吃年夜饭。", "During the Spring Festival, families usually reunite for a big feast on New Year's Eve."),
    (77, "手机支付改变了人们的消费方式，现在很少有人带现金出门。", "Mobile payment has changed how people spend money; few now carry cash when going out."),
    (78, "坚持每天锻炼半小时，能有效改善睡眠质量。", "Exercising for half an hour daily can effectively improve sleep quality."),
    (79, "越来越多的人选择骑自行车上班，以减少交通拥堵...", "More and more people choose to cycle to work to reduce traffic jams and air pollution."),
    (80, "学校图书馆新购置了大量英文原版书籍...", "The school library has acquired numerous original English books for students to borrow.")
]
for i, q, a in p2_trans:
    add_q(p2, i, "Translation", q, None, a)


# =======================================================
#                      试卷 3 数据
# =======================================================
p3 = "2025模拟卷3"

# --- Reading ---
txt_p3_r1 = "Passage One: Mrs. Lane (75 years old) lived alone in Texas. Too old to mow lawn (18 inches high, broke law). Neighbors (Adams brothers) mowed it for her. She was moved to tears."
add_q(p3, 1, "Reading", "What can we know about Mrs. Lane?", {"A":"70 years old","B":"Can't do housework","C":"Living with children","D":"Could not cut grass"}, "D", txt_p3_r1)
add_q(p3, 2, "Reading", "Mrs. Lane in danger of prison because", {"A":"broke education law","B":"grass over 18 inches","C":"news made up","D":"didn't pay money"}, "B", txt_p3_r1)
add_q(p3, 3, "Reading", "Who mowed the lawn?", {"A":"Adams brothers","B":"Sam and Mrs Lane","C":"Adams and Mrs Lane","D":"Adams brothers and other neighbors"}, "D", txt_p3_r1)
add_q(p3, 4, "Reading", "Which is TRUE?", {"A":"Brothers knew her well","B":"Mrs Lane knew names","C":"Didn't expect help","D":"Used Mrs Lane's mowers"}, "C", txt_p3_r1)
add_q(p3, 5, "Reading", "Mrs Lane living in", {"A":"Texas","B":"Indiana","C":"Georgia","D":"Washington"}, "A", txt_p3_r1)

txt_p3_r2 = "Passage Two: Just Eat + Starship Technologies delivery robots in London. 4mph. GPS/9 cameras. Code to unlock. Public reaction calm."
add_q(p3, 6, "Reading", "'courier' means", {"A":"deliverer","B":"collector","C":"provider","D":"guide"}, "A", txt_p3_r2)
add_q(p3, 7, "Reading", "Starship robot", {"A":"opens upon hearing","B":"10 miles per hour","C":"finds way by GPS/cameras","D":"sends message upon arrival"}, "C", txt_p3_r2)
add_q(p3, 8, "Reading", "Test shows", {"A":"Easy to operate","B":"Appreciated","C":"Cheaper than human","D":"10 hours"}, "C", txt_p3_r2)
add_q(p3, 9, "Reading", "Worry about robots?", {"A":"Safety (theft/disrupt)","B":"Accuracy","C":"Indifference","D":"Traffic"}, "A", txt_p3_r2)
add_q(p3, 10, "Reading", "Best title?", {"A":"Improvement","B":"Global Trend","C":"New Robots","D":"Delivery Robots to Replace Takeaway Drivers"}, "D", txt_p3_r2)

txt_p3_r3 = "Passage Three: Lisa and Sam at airport. Man forced to throw away snow globe package. Sam took photo. Snow globe for Katie (adoption date). They found owner Richard Milton."
add_q(p3, 11, "Reading", "What happened at security check?", {"A":"Man abandon package","B":"Forgot luggage","C":"Lisa throw away","D":"Lisa impatient"}, "A", txt_p3_r3)
add_q(p3, 12, "Reading", "Reason package not allowed?", {"A":"Dangerous","B":"Weight","C":"Violated safety regulations","D":"Not packaged"}, "C", txt_p3_r3)
add_q(p3, 13, "Reading", "Strange thing Lisa asked Sam?", {"A":"Take photos of airport","B":"Find bin","C":"Put away package","D":"Beg officials"}, "C", txt_p3_r3, "Keys选C (Put away/Take back package/Check it)")
add_q(p3, 14, "Reading", "Why snowball important?", {"A":"Birthday","B":"Valuable","C":"Family love to Katie (adoption)","D":"Popular"}, "C", txt_p3_r3)
add_q(p3, 15, "Reading", "Best title?", {"A":"Katie's gift","B":"Return of snow globe","C":"Security check","D":"Lost package"}, "B", txt_p3_r3)

txt_p3_r4 = "Passage Four: Mindfulness. Paying attention to present. Reduces stress (cortisol). Critics say trend, but science supports. Not one-size-fits-all."
add_q(p3, 16, "Reading", "Primary purpose of mindfulness?", {"A":"Replace medicine","B":"Improve mental health and focus","C":"Physical strength","D":"Tech"}, "B", txt_p3_r4)
add_q(p3, 17, "Reading", "How reduce stress?", {"A":"Increase cortisol","B":"Lower cortisol","C":"Eliminate challenges","D":"Impulsive"}, "B", txt_p3_r4)
add_q(p3, 18, "Reading", "'traction' means", {"A":"popularity","B":"confusion","C":"rejection","D":"criticism"}, "A", txt_p3_r4)
add_q(p3, 19, "Reading", "College students example?", {"A":"Young only","B":"Improve anxiety/sleep","C":"8 weeks","D":"Replacement"}, "B", txt_p3_r4)
add_q(p3, 20, "Reading", "Challenge for beginners?", {"A":"Focus","B":"Staying still/calm","C":"Social","D":"Guaranteed"}, "B", txt_p3_r4)

# --- Vocab 21-60 ---
p3_vocab = [
    (21, "C", "Team performance _____ by rain.", {"A":"injured","B":"governed","C":"affected","D":"harmed"}),
    (22, "C", "Found myself _____ seeing guests off.", {"A":"quiet","B":"shocked","C":"tongue-tied","D":"surprised"}),
    (23, "C", "Received _____ injuries.", {"A":"major","B":"junior","C":"minor","D":"shorter"}),
    (24, "D", "Forgot her _____ background.", {"A":"noble","B":"modest","C":"brilliant","D":"humble"}),
    (25, "A", "Be _____ of other cultures.", {"A":"respectful","B":"respectable","C":"respective","D":"respect"}),
    (26, "A", "Advice will _____.", {"A":"hold true","B":"go against","C":"go through","D":"slip into"}),
    (27, "A", "Gifts deeply _____.", {"A":"appreciated","B":"approved","C":"appealed","D":"applied"}),
    (28, "D", "_____ figure in literacy.", {"A":"most","B":"leader","C":"misleading","D":"leading"}),
    (29, "A", "Involves _____ journeys.", {"A":"occasional","B":"full","C":"occasion","D":"artificial"}),
    (30, "C", "The _____ are more expensive.", {"A":"late","B":"lately","C":"latter","D":"back"}),
    (31, "B", "Why not consult? _____.", {"A":"Great minds","B":"Two heads better","C":"Bird in hand","D":"Think twice"}),
    (32, "D", "Café, walls of _____ painted.", {"A":"that","B":"it","C":"what","D":"which"}),
    (33, "A", "There _____ the rest of guests.", {"A":"come","B":"comes","C":"is coming","D":"are coming"}),
    (34, "B", "Rather he _____ more.", {"A":"focus","B":"focused","C":"would focus","D":"had focused"}),
    (35, "A", "That's _____ I don't agree.", {"A":"where","B":"how","C":"when","D":"what"}),
    (36, "C", "Teacher _____ him.", {"A":"guaranteed","B":"pledged","C":"convinced","D":"promised"}),
    (37, "B", "Villagers _____ that.", {"A":"deceived","B":"informed","C":"shown","D":"upheld"}),
    (38, "C", "Measure to _____ that.", {"A":"assure","B":"insure","C":"ensure","D":"secure"}),
    (39, "A", "Sudden _____ of anger.", {"A":"burst","B":"attack","C":"split","D":"blast"}),
    (40, "D", "None _____ earthquake.", {"A":"outlived","B":"sustained","C":"underwent","D":"survived"}),
    (41, "D", "Make a _____.", {"A":"complaint","B":"claim","C":"decision","D":"reservation"}),
    (42, "D", "Written a _____.", {"A":"supervision","B":"indication","C":"selection","D":"survey"}),
    (43, "D", "Means to _____ dead bodies.", {"A":"conserve","B":"reserve","C":"deserve","D":"preserve"}),
    (44, "A", "Wound _____ dirt.", {"A":"free from","B":"out of","C":"away from","D":"prevented"}),
    (45, "B", "Professor _____ to reaction.", {"A":"sentimental","B":"sensitive","C":"sensible","D":"positive"}),
    (46, "C", "_____ satisfaction.", {"A":"Superior to","B":"Prior to","C":"In terms of","D":"Along with"}),
    (47, "A", "Don't _____ news.", {"A":"release","B":"relieve","C":"retain","D":"relate"}),
    (48, "C", "It was _____ that he'd find out.", {"A":"feasible","B":"discouraged","C":"inevitable","D":"denied"}),
    (49, "B", "In striking _____ with.", {"A":"comparison","B":"contrast","C":"contrary","D":"contract"}),
    (50, "D", "Which _____ of shoes.", {"A":"bind","B":"band","C":"bond","D":"brand"}),
    (51, "A", "Hard to _____ living in flat.", {"A":"adapt to","B":"devote to","C":"lead to","D":"add to"}),
    (52, "D", "_____ you so long.", {"A":"Having not seen","B":"Not seeing","C":"Have not seen","D":"Not having seen"}),
    (53, "B", "Vivid _____ of trip.", {"A":"explanation","B":"account","C":"idea","D":"imagination"}),
    (54, "A", "Hopes _____ next generation.", {"A":"concentrate on","B":"attract on","C":"look on","D":"fascinate on"}),
    (55, "C", "Beauty had _____.", {"A":"changed","B":"damaged","C":"faded","D":"disappeared"}),
    (56, "B", "_____ mother's face.", {"A":"disapprove","B":"distinguish","C":"separate","D":"recognize"}),
    (57, "A", "_____ by his _____ story.", {"A":"moved; moving","B":"moving; moved","C":"moved; moved","D":"moving; moving"}),
    (58, "D", "_____ the expert stressed.", {"A":"It","B":"What","C":"That","D":"As"}),
    (59, "C", "It _____ us greatly.", {"A":"interrupted","B":"disturbed","C":"annoyed","D":"troubled"}),
    (60, "B", "Get idea _____.", {"A":"off","B":"across","C":"away","D":"aside"})
]
for i, ans, q, opts in p3_vocab:
    add_q(p3, i, "Vocabulary", q, opts, ans)

# --- Cloze ---
txt_p3_cloze = "Healthy lifestyle challenging. Small changes [61] difference. Exercise [62] or cycling. 60% fail [63]. To [64] this, walk. Nutrition: [65] diet. Water [66] reduce calorie. Mental health [67]. Meditation improve [68]. Sleep [69] schedules. Holistic approach [70]."
cloze_p3 = [
    (61, "A", "A. significant B. slight C. temporary D. rare"),
    (62, "A", "A. swimming B. sleeping C. reading D. shopping"),
    (63, "A", "A. standard B. exception C. challenge D. progress"),
    (64, "B", "A. ignore B. counter C. accept D. explain"),
    (65, "A", "A. balanced B. strict C. varied D. limited"),
    (66, "C", "A. directly B. slightly C. significantly D. occasionally"),
    (67, "B", "A. physical B. overlooked C. additional D. social"),
    (68, "D", "A. creativity B. productivity C. concentration D. emotional health"),
    (69, "B", "A. flexible B. demanding C. regular D. fixed"),
    (70, "C", "A. unnecessary B. impossible C. essential D. optional")
]
for i, ans, txt in cloze_p3:
    add_q(p3, i, "Cloze", f"Cloze {i}: {txt}", {"A":"A","B":"B","C":"C","D":"D"}, ans, txt_p3_cloze)

# --- Translation ---
p3_trans = [
    (71, "The Lantern Festival... marks the end of Spring Festival.", "元宵节在农历正月十五，标志着春节庆祝活动的结束。"),
    (72, "With rapid development of mobile internet, smartphones...", "随着移动互联网的迅猛发展，智能手机已成为人们日常生活中不可或缺的一部分。"),
    (73, "Many universities now offer online learning platforms...", "如今许多大学都提供在线学习平台，让学生可以随时随地获取课程资料。"),
    (74, "The government has launched a campaign to promote waste sorting...", "政府发起了一项推广垃圾分类的活动，旨在减少环境污染。"),
    (75, "Despite challenges, young entrepreneurs choosing rural areas...", "尽管面临挑战，年轻创业者越来越多地选择在农村地区创业。"),
    (76, "这本书不仅内容有趣，而且语言通俗易懂，适合初学者阅读。", "This book is not only interesting but also easy to understand, making it suitable for beginners."),
    (77, "许多城市正在推广垃圾分类，以减少环境污染和资源浪费。", "Many cities are promoting waste sorting to reduce environmental pollution and resource waste."),
    (78, "如果你坚持每天练习英语口语，很快就会看到进步。", "If you keep practicing English speaking every day, you will see progress soon."),
    (79, "互联网的普及让人们可以随时随地获取信息和知识。", "The popularity of the Internet enables people to access information and knowledge anytime, anywhere."),
    (80, "他虽然年轻，但已经积累了丰富的工作经验。", "Although he is young, he has already accumulated rich work experience.")
]
for i, q, a in p3_trans:
    add_q(p3, i, "Translation", q, None, a)

# ================= 保存文件 =================
if __name__ == "__main__":
    with open("../data_full.json", "w", encoding="utf-8") as f:
        json.dump(full_data, f, indent=4, ensure_ascii=False)
    print("✅ 成功生成 data_full.json！包含3套卷子共240题。")
    print("👉 请运行 quiz_full.py 开始测试。")