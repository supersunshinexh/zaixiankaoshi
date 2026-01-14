import json
import os

# 存放所有3套试卷的完整数据
full_data = {
    "2025模拟卷1": [],
    "2025模拟卷2": [],
    "2025模拟卷3": []
}

def add_q(paper, q_id, q_type, question, options=None, answer=None, context=None, explanation=""):
    q_data = {
        "id": q_id,
        "type": q_type,
        "question": question,
        "answer": answer,
        "explanation": explanation
    }
    if options: q_data["options"] = options
    if context: q_data["context"] = context  # 这里将存放完整的阅读文章
    full_data[paper].append(q_data)

# =======================================================
#                      试卷 1 数据 (完整版)
# =======================================================
p1 = "2025模拟卷1"

# --- Part I Reading Comprehension ---

# Passage One
txt_p1_r1 = """Passage One
People like sellers or advertisers love to tell us that advertising will save us money. They tell us that placing ads in and on everything from video games to toilet paper will help us to save much money. The advertising pays the cost of part of the item or service, allowing the seller or provider to charge less than they would. But I disagree.

A couple of years ago, I bought a Kindle, an e-reader. I decided to choose one with the ads or "Special Offers" as Amazon called it. The price was lower and there were promises of money-saving offers, with basic ads.

Well, things were good for about six months. I did receive some offers such as a 10% off, or the opportunity to buy certain books for $1. Then the offers disappeared when the Kindle Fire came out. Suddenly, most of the special offers were limited to Kindle Fire owners. Now there are very few offers for them, either. The only things I now receive are true ads: Things for me to look at, but they hold no value.

The advertising no longer benefits me. To be honest, it makes me mad. I fell for the trick, the "Advertising will save you money". I had thought that it would be different with the Kindle. But it wasn't. Once they needed to sell a different product, those buyers got left behind. Though sellers say they make less money, those holding the newer product can't receive all the special offers. Sure, you pay a little less for the mode that ads display, but the money-saving promise is long gone."""

add_q(p1, 1, "Reading", "The author decided to buy the Kindle with ads mainly because of",
      {"A": "its high quality", "B": "its good after-sales service", "C": "its low price and promised offers", "D": "its offer to give money-saving advice"}, "C", txt_p1_r1, "作者提到 'The price was lower and there were promises of money-saving offers'。")
add_q(p1, 2, "Reading", "After the author owned the Kindle,",
      {"A": "he could buy any book for $1", "B": "he was asked to buy a Kindle Fire", "C": "he didn't receive any special offers", "D": "he ended up receiving ads of no value"}, "D", txt_p1_r1, "文中提到 'The only things I now receive are true ads... they hold no value'。")
add_q(p1, 3, "Reading", "The underlined words 'fell for' in Paragraph 4 means",
      {"A": "was inspired by", "B": "was fooled by", "C": "was confused about", "D": "was worried about"}, "B", txt_p1_r1, "fell for the trick 意为“上了当，受骗”，即 was fooled by。")
add_q(p1, 4, "Reading", "The writer tries to tell us",
      {"A": "advertising has its own sales theory.", "B": "advertising wastes consumers' time.", "C": "advertising helps consumers save money.", "D": "advertising doesn't benefit consumers as it says."}, "D", txt_p1_r1, "作者通过自己的经历反驳了“广告能省钱”的说法。")
add_q(p1, 5, "Reading", "Things were good for about _____ months.",
      {"A": "six", "B": "ten", "C": "two", "D": "one"}, "A", txt_p1_r1, "文中明确提到 'things were good for about six months'。")


# Passage Two
txt_p1_r2 = """Passage Two
Grown-ups are often surprised by how well they remember something they learned as children but have never practiced ever since. A man who has not had a chance to go swimming for years can still swim as well as ever when he gets back in the water. He can get on a bicycle after many years and still ride away. He can play catch and hit a ball as well as his son. A mother who has not thought about the words for years can teach her daughter the poem that begins "Twinkle, twinkle, little star" or remember the story of Cinderella or Goldilocks and the Three Bears.

One explanation is the law of overlearning, which can be stated as follows: Once we have learned something, additional learning trials(尝试) increase the length of time we will remember it.

In childhood we usually continue to practice such skills as swimming, bicycle riding, and playing baseball long after we have learned them. We continue to listen to and remind ourselves of words such as "Twinkle, twinkle, little star" and childhood tales such as Cinderella and Goldilocks. We not only learn but overlearn.

The multiplication tables(乘法口诀表) are an exception to the general rule that we forget rather quickly the things that we learn in school, because they are another of the things we overlearn in childhood.

The law of overlearning explains why cramming(突击学习) for an examination, though it may result in a passing grade, is not a satisfactory way to learn a college course. By cramming, a student may learn the subject well enough to get by on the examination, but he is likely soon to forget almost everything he learned. A little overlearning, on the other hand, is really necessary for one's future development."""

add_q(p1, 6, "Reading", "What is the main idea of paragraph 1?",
      {"A": "People remember well what they learned in childhood.", "B": "Children have a better memory than grown-ups.", "C": "Poem reading is a good way to learn words.", "D": "Stories for children arc easy to remember."}, "A", txt_p1_r2, "第一段举例说明成年人能很好地记得童年学过的东西。")
add_q(p1, 7, "Reading", "The author explains the law of overlearning by",
      {"A": "presenting research findings", "B": "selling down general rules", "C": "making a comparison", "D": "using examples"}, "D", txt_p1_r2, "作者通过游泳、骑车、背诗等例子来解释过度学习定律。")
add_q(p1, 8, "Reading", "According to the author, being able to use multiplication tables is",
      {"A": "a result of overlearning", "B": "a special case of cramming", "C": "a skill to deal with math problems", "D": "a basic step towards advanced studies"}, "A", txt_p1_r2, "文中提到乘法表是我们在童年时期 'overlearn' 的事物之一。")
add_q(p1, 9, "Reading", "What does the word 'they' in Paragraph 4 refer to?",
      {"A": "Commonly accepted rules.", "B": "The multiplication tables.", "C": "Things easily forgotten.", "D": "School subjects."}, "B", txt_p1_r2, "They 指代前面的 'The multiplication tables'。")
add_q(p1, 10, "Reading", "What is the author's opinion on cramming?",
      {"A": "It leads to failure in college exams.", "B": "It's helpful only in a limited way.", "C": "It's possible to result in poor memory.", "D": "It increases students' learning interest."}, "B", txt_p1_r2, "作者认为突击学习只能应付考试，很快就会忘，所以只有有限的帮助。")


# Passage Three
txt_p1_r3 = """Passage Three
We spend most of our time with friends whom we like. Well, who would stay with a person one doesn't like? What kind of people are welcomed by others, then?

There are people that naturally attract you. By being with them just once, you start to like them. If you wonder why they attract people and want to be a person like them, you should learn how to develop the traits that they have.

Firstly, everybody wants to be happy, and nobody wants to spend their time with a sad person. Well, you see, there is what you call mood linkage. If you are with a jolly(愉快的)person, you are more probably to be happy. When people choose to spend time with a person, they are more likely to choose those who are cheerful. So if you are a happy person, many people will want to spend their time with you.

Next, everybody needs someone to give encouragement to them, because sometimes in our lives we experience failure, sadness, problems and other bad things. So if you always choose to cheer others up with encouraging words or actions, they will be willing to spend time with you.

Lastly, you are not a friend if you don't lend a hand to your friends when they need help. You should always be helpful to them, no matter what it costs, because when you need help, they will be there for you, too.

It feels good if people want to be your friends because of your character. So if you want to attract friends, I suggest you learn to develop these traits."""

add_q(p1, 11, "Reading", "Why does the writer raise two questions in Paragraph 1?",
      {"A": "Because the writer hasn't decided what to write about.", "B": "Because the writer wants to show off his ideas.", "C": "Because the writer wants to make Paragraph 1 more logical.", "D": "Because the writer wants to draw readers' attention to the article."}, "D", txt_p1_r3, "开头提问是为了吸引读者的注意力并引出话题。")
add_q(p1, 12, "Reading", "The writer mentions all the following that attracts others, EXCEPT",
      {"A": "being a happy person", "B": "being polite", "C": "being encouraging", "D": "being helpful"}, "B", txt_p1_r3, "文中提到了快乐(happy/cheerful)、鼓励(encouraging)、乐于助人(helpful)，未提及 polite。")
add_q(p1, 13, "Reading", "Which of the following shows the right structure of the passage?",
      {"A": "1-2-3-4", "B": "1-(234)-5", "C": "1-2-3", "D": "1-2345"}, "D", txt_p1_r3, "文章结构为总（引入）-分（三个特点）-总（总结）。(注：选项根据原题意推断，通常为总分总结构)")
add_q(p1, 14, "Reading", "The best title for the passage is",
      {"A": "How To Be An Attractive Person", "B": "How To Introduce The Traits Of Oneself", "C": "How To Live A Happy Life", "D": "How To Find A Real Friend"}, "A", txt_p1_r3, "文章主要讲如何培养特质来吸引朋友。")
add_q(p1, 15, "Reading", "The writer suggest us at the end of the passage: 'if you want to attract friends, I suggest you learn to develop these ____'",
      {"A": "mood", "B": "encouragement", "C": "traits", "D": "friends"}, "C", txt_p1_r3, "最后一句: learn to develop these traits.")


# Passage Four
txt_p1_r4 = """Passage Four
One evening in February 2007, a student named Paula Ceely brought her car to a stop on a remote road in Wales. She got out to open a metal gate that blocked her path. That's when she heard the whistle sounded by the driver of a train. Her Renault Clio was parked across a railway line. Seconds later, she watched the train drag her car almost a kilometre down the railway tracks.

Ceely's near miss made the news because she blamed it on he GPS (导航仪). She had never driven the route before. It was dark and raining heavily. Ceely was relying on her GPS, but it made no mention of the crossing. "I put my complete trust in the device and it led me right into the path of a speeding train," she told the BBC.

Who is to blame here? Rick Stevenson, who tells Ceely's story in his book When Machines Fail Us, points the finger at the limitations of technology. We put our faith in digital devices, he says, but our digital helpers are too often not up to the job. They are filled with small problems. And it's not just GPS devices: Stevenson takes us on a tour of digital disasters involving everything from mobile phones to wireless keyboards.

The problem with his argument in the book is that it's not clear why he only focuses on digital technology, while there may be a number of other possible causes. A map-maker might have left the crossing off a paper map. Maybe we should blame Ceely for not paying attention. Perhaps the railway authorities are at fault for poor singalling system. Or maybe someone has studied the relative dangers and worked out that there really is something specific wrong with the GPS equipment. But Stevenson doesn't say.

It's a problem that runs through the book. In a section on cars, Stevenson gives an account of the advanced techniques that criminals use to defeat computer-based locking systems for cars. He offers two independent sets of figures on car theft; both show a small rise in some parts of the country. He says that once again not all new locks have proved reliable. Perhaps, but maybe it's also due to the shortage of policemen on the streets. Or changing social circumstances. Or some combination of these factors.

The game between humans and their smart devices is amusing and complex. It is shaped by economics and psychology and the cultures we live in. Somewhere in the mix of those forces there may be a way for a wiser use of technology. If there is such a way, it should involve more than just an awareness of the shortcomings of our machines. After all, we have lived with them for thousands of years. They have probably been fooling us for just as long."""

add_q(p1, 16, "Reading", "What did Paula Ceely think was the cause of her accident?",
      {"A": "She was not familiar with the road.", "B": "It was dark and raining heavily then.", "C": "The railway workers failed to give the signal.", "D": "Her GPS device didn't tell her about the crossing."}, "D", txt_p1_r4, "她把事故归咎于 GPS (she blamed it on her GPS)。")
add_q(p1, 17, "Reading", "The phrase 'near miss' (Paragraph 2) can best be replaced by",
      {"A": "close hit", "B": "heavy loss", "C": "narrow escape", "D": "big mistake"}, "C", txt_p1_r4, "near miss 指险些发生的事故，即死里逃生 (narrow escape)。")
add_q(p1, 18, "Reading", "Which of the following would Rick Stevenson most probably agree with?",
      {"A": "Modern technology is what we can't live without.", "B": "Digital technology often falls short of our expectation.", "C": "Digital devices are more reliable than they used to be.", "D": "GPS error is not the only cause for Ceely's accident."}, "B", txt_p1_r4, "Stevenson 认为数字助手经常无法胜任工作 (not up to the job)。")
add_q(p1, 19, "Reading", "In the writer's opinion, Stevenson's argument is",
      {"A": "one-sided", "B": "reasonable", "C": "puzzling", "D": "well-based"}, "A", txt_p1_r4, "作者认为 Stevenson 只关注技术限制而忽略其他原因，观点片面 (one-sided)。")
add_q(p1, 20, "Reading", "What is the real concern of the writer of this article?",
      {"A": "The major causes of traffic accidents and car thefts.", "B": "The relationship between human and technology.", "C": "The shortcomings of digital devices we use.", "D": "The human unawareness of technical problems."}, "B", txt_p1_r4, "作者在最后一段探讨了人与智能设备之间复杂的关系。")


# --- Part II Vocabulary (21-60) ---
p1_vocab = [
    (21, "B", "The tourists protested _____ the bad service at the restaurant.", {"A":"on","B":"against","C":"with","D":"of"}),
    (22, "B", "In this factory the machines are not regulated _____ but are jointly controlled by a central computer system.", {"A":"independently","B":"individually","C":"indifferently","D":"irregularly"}),
    (23, "D", "Are there _____ forms of life on other planets?", {"A":"clever","B":"wise","C":"talented","D":"intelligent"}),
    (24, "A", "Many women still feel that they are being _____ by a male culture, particularly in the professional services sector.", {"A":"held back","B":"held forth","C":"held on","D":"held out"}),
    (25, "D", "Britain was _____ by the Romans in AD 43.", {"A":"concentrated","B":"connected","C":"confused","D":"conquered"}),
    (26, "D", "Doing your homework is a sure way to improve your test scores, and this is especially true _____ it comes to classroom tests.", {"A":"before","B":"as","C":"since","D":"when"}),
    (27, "D", "Although his _____ ideas were difficult to understand, I managed to go through the whole book.", {"A":"practical","B":"concrete","C":"superficial","D":"abstract"}),
    (28, "D", "The exchange of the government delegations _____ a better understanding between the two countries.", {"A":"adds to","B":"keeps to","C":"amounts to","D":"contributes to"}),
    (29, "A", "Nothing can _____ missing such a wonderful opportunity.", {"A":"make up for","B":"make up with","C":"keep up for","D":"keep up with"}),
    (30, "C", "The speaker gave a very successful speech with _____.", {"A":"pension","B":"possession","C":"passion","D":"procession"}),
    (31, "D", "It is often the case _____ anything is possible for those who hang on to hope.", {"A":"why","B":"what","C":"as","D":"that"}),
    (32, "B", "More efforts, as reported, _____ in the years ahead to accelerate the supply-side structural reform.", {"A":"are made","B":"will be made","C":"are being made","D":"have been made"}),
    (33, "C", "Many young people, most _____ were well-educated, headed for remote regions to chase their dreams.", {"A":"of which","B":"of them","C":"of whom","D":"of those"}),
    (34, "A", "---Can you tell us your _____ for happiness and a long life? \n---Living every day to the full, definitely.", {"A":"recipe","B":"record","C":"range","D":"receipt"}),
    (35, "C", "He did not _____ easily, but was willing to accept any constructive advice for a worthy cause.", {"A":"approach","B":"wrestle","C":"compromise","D":"communicate"}),
    (36, "D", "_____ some people are motivated by a need for success, others are motivated by a fear of failure.", {"A":"Because","B":"If","C":"Unless","D":"While"}),
    (37, "A", "If it _____ for his invitation the other day, I should not be here now.", {"A":"had not been","B":"should not be","C":"were not to be","D":"should not have been"}),
    (38, "B", "In art criticism, you must assume the artist has a secret message _____ within the work.", {"A":"to hide","B":"hidden","C":"hiding","D":"being hidden"}),
    (39, "D", "Dashan, who _____ crosstalk, the Chinese comedic tradition, for decades, wants to mix it up with the Western stand-up tradition.", {"A":"will be learning","B":"is learning","C":"had been learning","D":"has been learning"}),
    (40, "B", "Many businesses started up by college students have _____ thanks to the comfortable climate for business creation.", {"A":"fallen off","B":"taken off","C":"turned off","D":"left off"}),
    (41, "B", "Oh, I can't believe! There is a UFO _____ on the earth.", {"A":"land","B":"landing","C":"lands","D":"landed"}),
    (42, "C", "At forty he was _____ of his profession.", {"A":"kept up","B":"on top","C":"at the top","D":"on the top"}),
    (43, "C", "The thief stole food from the supermarket and was _____ by the policemen.", {"A":"catch","B":"catching","C":"caught","D":"called"}),
    (44, "C", "People in western countries use forks and _____ to have a meal in a restaurant.", {"A":"chopsticks","B":"eggs","C":"knives","D":"hands"}),
    (45, "D", "The company went _____ because it couldn't sell its products.", {"A":"wrong","B":"stock","C":"depart","D":"bankrupt"}),
    (46, "D", "Let's ask _____ some questions and think about them before we make a big decision.", {"A":"himself","B":"herself","C":"myself","D":"ourselves"}),
    (47, "C", "The doctor gave the little girl some pills to _____ her pain.", {"A":"release","B":"slow","C":"ease","D":"relax"}),
    (48, "C", "I've recently been to a very _____ museum in India, the International Museum of Toilets.", {"A":"strong","B":"usual","C":"unusual","D":"common"}),
    (49, "C", "Bob faces a difficult _____ between becoming a professional basketball player and going to university.", {"A":"choose","B":"choosing","C":"choice","D":"decide"}),
    (50, "B", "Wounds that are _____ to the air heal more quickly.", {"A":"took","B":"exposed","C":"observed","D":"discovered"}),
    (51, "A", "In such a big country like China the agricultural development will and must _____ economic development in the coming years.", {"A":"precede","B":"process","C":"provide","D":"possess"}),
    (52, "A", "My mother is an excellent housewife and she likes to keep everything _____.", {"A":"in place","B":"out of place","C":"on place","D":"at place"}),
    (53, "C", "It is not the right way you _____ speak with your parents.", {"A":"are going to","B":"must","C":"are supposed to","D":"can"}),
    (54, "D", "To be frank, your project is not _____ with our company's long-term aims; we can't approve it.", {"A":"competitive","B":"comparative","C":"convertible","D":"compatible"}),
    (55, "A", "I end up getting my heart _____. For so many years, I was never expressive with my feelings.", {"A":"hardened","B":"hardening","C":"hardens","D":"being hardened"}),
    (56, "C", "'Marquis,' said the boy, turning to the man, his eyes _____ wide, and his right hand raised.", {"A":"turned...opened","B":"turning...opening","C":"opened","D":"opening"}),
    (57, "D", "He was taken on for a three-month trial period before being accepted as a _____ member of staff.", {"A":"lasting","B":"eternal","C":"persistent","D":"permanent"}),
    (58, "C", "First reported in 1981, almost 38,000 individuals in the United States had _____ AIDS by the end of 1986.", {"A":"infected","B":"contacted","C":"contracted","D":"affected"}),
    (59, "B", "If the story did _____ to be true, though, I think he might be pushing his luck.", {"A":"turn on","B":"turn out","C":"turn up","D":"turn over"}),
    (60, "D", "It is difficult to know what horses have _____ and they must find us equally frustrating to understand.", {"A":"over mind","B":"to mind","C":"up mind","D":"in mind"})
]
for i, ans, q, opts in p1_vocab:
    add_q(p1, i, "Vocabulary", q, opts, ans)

# --- Part III Cloze ---
txt_p1_cloze = """Every time I travel around the mountains in Yukon Territory by car, I often notice a road sign that says, "A fed bear is a dead bear." 61, I did not get it. Why is a fed bear a dead one? According to a friend, many travelers used to throw their food from their cars for the bears. 62 the bears turned to the roadside for food and finally lost their ability to take care of themselves. When winter came, fewer travelers took trips to the mountains, which 63 less food for the bears, some of them died of hunger. So the Canadian government 64 warning signs along the road, advising people not to feed the bears.

This reminded me 65 a scientific experiment. Some white mice were divided into two groups. One group 66 their days only eating and sleeping. 67 fed only with half the amount of food they need, had to search for food. Half a year later, scientists found that the mice that had to search for their own food were 68, while the fully fed ones were either ill or dead. It was clear that the underfed white mice, in the process of searching for their food, had kept healthy by exercising in finding food.

Many over-concerned(过度关注的)parents are feeding their children like bears or white mice. At present, children depend on others too much, and are not 69 to think independently and act for themselves. 70 placed in strange environments, they are lost, confused, and helpless. Parents do not understand how to achieve their children's long-term success. They forget the most important thing--that is how to make their children grow into independent adults, so that they can face challenges and succeed in the future."""

cloze_p1 = [
    (61, "C", "A. After all B. Above all C. At first D. In the end"),
    (62, "A", "A. Slowly B. Normally C. Actually D. Generally"),
    (63, "B", "A. explained B. meant C. offered D. required"),
    (64, "D", "A. made up B. took up C. kept up D. put up"),
    (65, "C", "A. for B. to C. of D. about"),
    (66, "B", "A. lived B. spent C. took D. made"),
    (67, "C", "A. Another B. Other C. The others D. The other"),
    (68, "B", "A. popular B. healthy C. lazy D. sick"),
    (69, "C", "A. allowed B. supposed C. encouraged D. used"),
    (70, "C", "A. Until B. Unless C. Once D. After")
]
for i, ans, txt in cloze_p1:
    q_text = f"Cloze {i} (Select the best option)"
    ops = {"A":"A","B":"B","C":"C","D":"D"}
    explanation_txt = f"选项: {txt}"
    add_q(p1, i, "Cloze", q_text, ops, ans, txt_p1_cloze, explanation_txt)

# --- Part IV & V Translation ---
p1_trans = [
    (71, "Every weekend, she volunteers at the local library to help children with their reading.", "每个周末，她都在当地图书馆做志愿者，帮助孩子们阅读。"),
    (72, "The professor emphasized the importance of critical thinking in his lecture yesterday.", "教授在昨天的讲座中强调了批判性思维的重要性。"),
    (73, "Due to the heavy rain, the outdoor concert has been postponed until next Saturday.", "由于大雨，户外音乐会已推迟至下周六。"),
    (74, "Learning a new language requires patience and consistent practice.", "学习一门新语言需要耐心和持续的练习。"),
    (75, "The city government is planning to build more bike lanes to promote eco-friendly transportation.", "市政府正计划修建更多自行车道，以推广环保出行方式。"),
    (76, "每天早晨，爷爷都会在公园里打太极拳。", "Every morning, Grandpa practices Tai Chi in the park."),
    (77, "昨天的会议上，我们讨论了如何提高团队合作效率。", "At yesterday's meeting, we discussed how to improve teamwork efficiency."),
    (78, "如果你需要帮助，可以随时联系我。", "If you need help, feel free to contact me anytime."),
    (79, "这家超市的水果和蔬菜既新鲜又便宜。", "The fruits and vegetables in this supermarket are both fresh and affordable."),
    (80, "医生建议我每天至少喝八杯水。", "The doctor advised me to drink at least eight glasses of water daily.")
]
for i, q, a in p1_trans:
    add_q(p1, i, "Translation", q, None, a)


# =======================================================
#                      试卷 2 数据 (完整版)
# =======================================================
p2 = "2025模拟卷2"

# --- Reading ---
# Passage One
txt_p2_r1 = """Passage One
More attention was paid to the quality of production in France at the time of Rene Coty. Charles Deschanel was then the financial minister. He stressed that workmanship and quality were more important than quantity for industrial production. It would be necessary to produce quality goods for the international market to compete with those produced in other countries. The French economy needed a larger share of the international market to balance its import and export trade.

French industrial and agricultural production was still inadequate to meet the immediate needs of the people, let alone long-ranged developments. Essential imports had stretched the national credit to the breaking point. Rents were tightly controlled, but the extreme inflation affected general population most severely through the cost of food. Food costs took workers as much as 80 per cent of their income. Wages, it is true, had risen. Extensive family allowances(津贴) and benefits were paid by the state, and there was full time and overtime employment. Taken together, these factors enabled the working class to exist but allowed them no sense of security. In this discouraging situation, workmen were willing to work overseas for higher wages.

The government was reluctant to let workers leave the country. It was feared that this migration of workers would deplete(用尽) the labor force. The lack of qualified workers might affect the improvement in the quality of industrial products produced. Qualified workers employed abroad would only increase the quantity of quality goods produced in foreign countries. Also the quantity of quality goods produced in France would not be able to increase as part of its qualified labor force moved to other countries."""

add_q(p2, 1, "Reading", "Charles Deschanel stressed better quality in production because",
      {"A": "they wanted to produce much more products", "B": "they wanted to balance their import and export trade", "C": "they wanted to compete with those goods produced in other countries", "D": "they believed they must do that way"}, "C", txt_p2_r1, "文中提到 'compete with those produced in other countries'。")
add_q(p2, 2, "Reading", "According to the passage, French production",
      {"A": "was inadequate to meet the needs of the French people", "B": "was enough for the local market", "C": "was increasing", "D": "was flooding the international market with inferior products"}, "A", txt_p2_r1, "文中明确说 'was still inadequate to meet the immediate needs of the people'。")
add_q(p2, 3, "Reading", "Which of the following was NOT true in France?",
      {"A": "Wages had increased.", "B": "There was overtime employment.", "C": "The state paid family allowances.", "D": "Food costs were low."}, "D", txt_p2_r1, "文中说 'Food costs took workers as much as 80 per cent'，所以费用很高，D 选项说低是不对的。")
add_q(p2, 4, "Reading", "In this discouraging economic situation, workmen were",
      {"A": "working harder to produce more products", "B": "anxious to work abroad", "C": "saving some money to get over the difficulty", "D": "often unable to find work"}, "B", txt_p2_r1, "文中说 'workmen were willing to work overseas'，即渴望去国外工作。")
add_q(p2, 5, "Reading", "The French government was reluctant to let the workers leave the country because",
      {"A": "it would affect the increase in quantity of exports", "B": "it would affect the improvement of quality in industrial production", "C": "it would damage the imports", "D": "it would enlarge the working force"}, "B", txt_p2_r1, "文中提到 'The lack of qualified workers might affect the improvement in the quality'。")


# Passage Two
txt_p2_r2 = """Passage Two
Almost two million young workers in the UK have to live with their parents because they cannot buy a house or rent a room. Newspapers in Britain call them the "clipped wing generation" because they are like birds who have had their wings cut. House prices in the UK are now so high that many young people cannot afford to buy one. This means a quarter of young adults have to live with their parents or grandparents. A poll found that 48 percent of the people said the biggest problem was housing costs. Britain has a long history of young people moving away from the family home when they start working. Rising house prices are now making this more and more difficult to do.

A 32-year-old woman said she has been saving money for over ten years to pay the deposit for a new apartment. She said it was very difficult because the more she saves, the more house prices go up. She is worried about the future if she can't buy her own home. She told reporters why she didn't want to leave the family home and rent, saying, "If I move out now, the reality is I'll be stuck paying expensive rents for the rest of my life... The thought that I'm going to be living like a teenager into my late 30s or even 40s is really disheartening."

A charity for homeless people said Britain's government needed to build more homes and sell them at a price that is low enough for younger people."""

add_q(p2, 6, "Reading", "According to paragraph one, young workers in the UK have to live with their parents because",
      {"A": "they can't afford to buy a house or rent a room", "B": "they are like birds whose wings have been cut", "C": "they move away from the family home when they start working", "D": "they have to save money for a new department"}, "A", txt_p2_r2, "第一句就说明了原因：cannot buy a house or rent a room。")
add_q(p2, 7, "Reading", "Among 10,000 young adults, how many of them have to live with their parents or grandparents?",
      {"A": "30", "B": "40", "C": "2,500", "D": "4,800"}, "C", txt_p2_r2, "文中说 'a quarter' (四分之一) 的年轻人必须和父母住。10000 的 1/4 是 2500。")
add_q(p2, 8, "Reading", "Why is it difficult for the 32-year-old woman to buy her own house?",
      {"A": "She has to pay for costs of daily life.", "B": "She doesn't have a very good job.", "C": "Her husband doesn't agree.", "D": "The housing prices have been rising all the time."}, "D", txt_p2_r2, "文中说 'the more she saves, the more house prices go up'。")
add_q(p2, 9, "Reading", "What does the underlined word 'disheartening' in paragraph two mean?",
      {"A": "Fascinating.", "B": "Unbelievable.", "C": "Frustrating.", "D": "Exciting."}, "C", txt_p2_r2, "disheartening 意为令人沮丧的，即 Frustrating。")
add_q(p2, 10, "Reading", "What can we infer from this passage?",
      {"A": "Young workers in the UK don't like living with their parents.", "B": "Young adults in the UK are under too much pressure.", "C": "The government will lower the housing prices in the future.", "D": "Only a small number of young people in the UK have problems paying for their housing costs."}, "B", txt_p2_r2, "通篇都在讲高房价给年轻人带来的困境，B 选项最符合推断。")


# Passage Three
txt_p2_r3 = """Passage Three
In many British schools, the pupils usually wear their school uniforms to school on weekdays. However, recently the students at LVS Ascot Junior School in England wore something quite different. What they wore was what people wear when they go to bed - pyjamas (睡衣). They did this not only for fun, but for a local charity called Christopher's Smile.

Christopher's Smile was set up in 2008 by Karen & Kevin Capel whose only son Christopher died of cancer at a young age. They hope their charity will help pay for more research into children's cancers. Since then, the charity has raised a lot of money and gotten more and more volunteers. Every year, thousands of people take part in different activities such as charity walk or run to show their support for Christopher's Smile.

The students of Grade 6 at LVS Ascot Junior School also wanted to do something for the sick children. They organized the event "Pyjama Day" to support Christopher's Smile. "We wanted to raise money for our charity in a way that the whole school could join in it, so each pupil paid £1 to wear his or her pyjamas to school on Pyjama Day," said the young organizers. Both the students and their teachers took part in the event with great interest. Together they not only raised some money, but also had a good time."""

add_q(p2, 11, "Reading", "Who set up Christopher's Smile?",
      {"A": "LVS Ascot Junior School's teachers.", "B": "The local government.", "C": "LVS Ascot Junior School's students.", "D": "Christopher's parents."}, "D", txt_p2_r3, "文中说是 'Karen & Kevin Capel whose only son Christopher died'，即 Christopher 的父母。")
add_q(p2, 12, "Reading", "What is the purpose of setting up Christopher's Smile?",
      {"A": "To tell people some knowledge about children's cancers.", "B": "To have fun for the students in LVS Ascot Junior School.", "C": "To help the local government do more things for students.", "D": "To raise money for more research into children's cancers."}, "D", txt_p2_r3, "文中明确说是 'help pay for more research into children's cancers'。")
add_q(p2, 13, "Reading", "Which of the following is TRUE?",
      {"A": "It has been 14 years since Christopher's Smile was set up.", "B": "Few pupils wear school uniforms to school on weekdays in Britain.", "C": "In LVS Ascot Junior School, only students join in the event 'Pyjama Day'.", "D": "All students in England need to wear pyjamas to school on Pyjama Day."}, "A", txt_p2_r3, "原文说2008年建立。这套题是2025年模拟题，2025-2008=17年。但根据选项和试卷年份（可能是旧题新编），如果题目原意是2022年左右，则是14年。Keys 选 A。")
add_q(p2, 14, "Reading", "The best title for the passage may be",
      {"A": "The Christopher's Smile", "B": "Fun and charity", "C": "The Pyjama Day", "D": "Children's cancers"}, "C", txt_p2_r3, "文章主要围绕 'Pyjama Day' 这个活动展开。")
add_q(p2, 15, "Reading", "Which of following is NOT TRUE?",
      {"A": "Since then, the charity has raised a lot of money and gotten more and more volunteers.", "B": "The people took part in the activity just for fun.", "C": "Both the students and their teachers took part in the event with great interest.", "D": "Every year, thousands of people take part in different activities such as charity walk or run to show their support for Christopher's Smile."}, "B", txt_p2_r3, "文中说 'not only for fun, but for a local charity'，所以 'just for fun' 是错的。")


# Passage Four
txt_p2_r4 = """Passage Four
My mother is a kind and gentle woman. She is very busy from morning till night. As a teacher she works diligently and efficiently. As a mother, she takes good care of us and gives us every comfort. I have an elder brother. He and I both love her dearly and she loves us.

My mother has been teaching maths at a middle school in my hometown. She goes to the school early in the morning and does not return home until late in the afternoon. She loves her students and cares for them. She treats them with patience and teaches them well. For her excellent qualities and very good teaching results, she is always praised and respected by both her students and colleagues alike. And she has been chosen or elected as a model teacher several times.

My mother is a thrifty and industrious woman. She never buys expensive or fancy dresses for herself; she goes occasionally to buy some inexpensive and high-quality clothes for us. She never goes luxurious restaurants to enjoy expensive meals. She lives a busy yet simple life, without any complaints. As soon as she comes hack from school, she sets about doing housework: sweeping the living room and bedrooms or cleaning the furniture, putting everything in good order. Besides, she prepares nice dishes for us to eat. She seems to be on the go all the time. As she has been very busy working hard every day, she looks older than she really is. Her face is wrinkled, and her hair has turned silver white. But she looks as cheerful and happy as ever.

Often she says to us, "Work while you work, and play while you play. That is the way to be happy and gay. If you do not work, you will become lazy and of no use to society." What a piece of good advice this is! I never forget it and always bear it in my mind. This advice of hers will always serve as a guide to my action. My mother is great indeed, and I always feel proud of her."""

add_q(p2, 16, "Reading", "What kind of person is the writer's mother?",
      {"A": "A person who often complains about her work.", "B": "A person who is too busy to take care of her children.", "C": "A person who loves both her children and her students.", "D": "A person who works with low efficiency."}, "C", txt_p2_r4, "文中提到她既是好妈妈也是好老师。")
add_q(p2, 17, "Reading", "Why is the writer's mother always praised and respected by both her students and colleagues?",
      {"A": "Because she has been teaching for a long time.", "B": "Because she goes to school early and return home late.", "C": "Because she loves her children very much.", "D": "Because she treats students well and teaches well."}, "D", txt_p2_r4, "文中说 'For her excellent qualities and very good teaching results...'。")
add_q(p2, 18, "Reading", "What does the writer's mother usually do when she gets home from school?",
      {"A": "She starts doing housework.", "B": "She helps her kids with homework.", "C": "She has a good rest.", "D": "She continues her work at school."}, "A", txt_p2_r4, "文中说 'As soon as she comes hack from school, she sets about doing housework'。")
add_q(p2, 19, "Reading", "Which word is closest to the meaning of the underlined word 'industrious' in paragraph three?",
      {"A": "Busy.", "B": "Serious.", "C": "Hard-working.", "D": "Patient."}, "C", txt_p2_r4, "industrious 意为勤奋的，即 Hard-working。")
add_q(p2, 20, "Reading", "The writer writes this passage to",
      {"A": "tell others his mother is a good teacher", "B": "show his love to his mother", "C": "ask people to remember the words of mothers'", "D": "remind young people to take care of their mothers"}, "B", txt_p2_r4, "文章充满了对母亲的爱和自豪 (I always feel proud of her)。")


# --- Vocab (21-60) ---
p2_vocab = [
    (21, "B", "If I _____ you, I would take the job offer without hesitation.", {"A":"am","B":"were","C":"will be","D":"had been"}),
    (22, "A", "_____ the rain, the football match would have been postponed.", {"A":"Had it not been for","B":"If it would not be for","C":"Unless it had been for","D":"Should it not be for"}),
    (23, "A", "The professor recommended that the students _____ more attention to experimental data.", {"A":"pay","B":"paid","C":"would pay","D":"must pay"}),
    (24, "D", "He is the only person _____ knows the combination to the safe.", {"A":"whom","B":"whose","C":"which","D":"who"}),
    (25, "D", "The new policy aims to _____ the gap between rich and poor.", {"A":"narrow","B":"shrink","C":"reduce","D":"all of the above"}),
    (26, "A", "A club is a place to make frequent _____ with friends.", {"A":"contact","B":"control","C":"contract","D":"context"}),
    (27, "D", "The poet is regarded as the _____ figure in literacy circles.", {"A":"most","B":"leader","C":"misleading","D":"leading"}),
    (28, "A", "The horse was injured on one of its _____ legs.", {"A":"rear","B":"side","C":"behind","D":"near"}),
    (29, "B", "Coal and oil are important _____ materials for the manufacture of plastics.", {"A":"nature","B":"raw","C":"crude","D":"sore"}),
    (30, "C", "She only received _____ injuries in the accident.", {"A":"major","B":"junior","C":"minor","D":"shorter"}),
    (31, "A", "The successful series was first co-hosted by Buck Owens and Roy Clark, and later on they appeared only occasionally, _____ for various guest hosts.", {"A":"having made room","B":"have made room","C":"making rooms","D":"having made a room"}),
    (32, "B", "It was the promise of better job opportunities _____ the inconvenience of moving away and leaving her friends.", {"A":"via","B":"versus","C":"for","D":"except"}),
    (33, "D", "Joining a global effort, Hong Kong has fully taken up its obligations... to decrease substances that _____ the ozone layer.", {"A":"depict","B":"remove","C":"complete","D":"deplete"}),
    (34, "C", "One study's findings suggested that just looking at photos of green settings was enough to _____ positive benefits.", {"A":"sustain","B":"retain","C":"attain","D":"contain"}),
    (35, "D", "Can you help me with my homework? I'm _____.", {"A":"stick","B":"struck","C":"stricken","D":"stuck"}),
    (36, "D", "Fresh watermelons are _____ available in most groceries in summer.", {"A":"very","B":"rarely","C":"likely","D":"readily"}),
    (37, "B", "Firms can no longer safely _____ that every employee walking in the door has similar beliefs or expectations.", {"A":"suppose","B":"assume","C":"presume","D":"postulate"}),
    (38, "A", "On her feet she wore linen stockings and prison shoes, and round her head was tied a white handkerchief, _____ a few locks of black hair were brushed.", {"A":"from under which","B":"from which","C":"out of which","D":"under which"}),
    (39, "B", "To be considered chronically homeless, persons _____ in a place not meant for human habitation...", {"A":"must be sleeping","B":"must have been sleeping","C":"should have been sleeping","D":"should sleep"}),
    (40, "B", "Don't _____ that people can achieve their success without painstaking effort.", {"A":"resume","B":"assume","C":"assure","D":"consume"}),
    (41, "B", "Wounds that are _____ to the air heal more quickly.", {"A":"took","B":"exposed","C":"observed","D":"discovered"}),
    (42, "C", "His _____, considering his world-wide fame in his field, was endearing.", {"A":"protest","B":"mission","C":"modesty","D":"compliment"}),
    (43, "D", "He _____ the book from the floor.", {"A":"took up","B":"look up","C":"save up","D":"picked up"}),
    (44, "A", "They tried to _____ the nervous old woman that flying was safe.", {"A":"assure","B":"conform","C":"confirm","D":"persuade"}),
    (45, "C", "The doctor gave the little girl some pills to _____ her pain.", {"A":"release","B":"slow","C":"ease","D":"relax"}),
    (46, "A", "The disease is _____ by sneezing and fever.", {"A":"accompanied","B":"companied","C":"designed","D":"produced"}),
    (47, "B", "Her _____ was obvious when her face turned red and her lips trembled.", {"A":"grace","B":"fluster","C":"haste","D":"politeness"}),
    (48, "D", "The company went _____ because it couldn't sell its products.", {"A":"wrong","B":"stock","C":"depart","D":"bankrupt"}),
    (49, "A", "He _____ the dangers of setting out without proper equipment.", {"A":"pointed out","B":"believed in","C":"prayed on","D":"relate"}),
    (50, "C", "At forty he was _____ of his profession.", {"A":"kept up","B":"on top","C":"at the top","D":"on the top"}),
    (51, "C", "Paper money was in _____ use in China when Marco Polo visited the country in _____ thirteenth century.", {"A":"the, /","B":"the, the","C":"/, the","D":"/, /"}),
    (52, "A", "---I want someone to write the composition for me.\n---No. As a student, you _____ depend on yourself.", {"A":"shall","B":"will","C":"can","D":"may"}),
    (53, "B", "The escaped prisoner, _____, looked up and stared in the direction where the noise came from.", {"A":"alarming","B":"alarmed","C":"having alarmed","D":"to be alarmed"}),
    (54, "C", "They were given the task according to their _____ abilities.", {"A":"respectful","B":"respectable","C":"respective","D":"respecting"}),
    (55, "C", "It is commonly believed that young graduates who _____ employment will have to work hard to succeed.", {"A":"attend","B":"search","C":"seek","D":"attempt"}),
    (56, "B", "The lecture mainly deals with the trouble young children have _____ right from wrong.", {"A":"distinguished","B":"distinguishing","C":"to distinguish","D":"to be distinguished"}),
    (57, "D", "Mr. Li is such a considerate person _____ all his colleagues like to work with.", {"A":"that","B":"so","C":"which","D":"as"}),
    (58, "B", "The _____ moment when the Berlin Wall came down is the theme of this _____ movie.", {"A":"historical, historic","B":"historic, historical","C":"historical, history","D":"history, historical"}),
    (59, "B", "_____ to loud noises for a long time will have one's hearing _____.", {"A":"Exposed, harmed","B":"Being exposed, harmed","C":"Exposing, being harmed","D":"Expose, be harmed"}),
    (60, "D", "If a shop has chairs _____ women can park their men, women will spend more time in the shop.", {"A":"that","B":"which","C":"when","D":"where"})
]
for i, ans, q, opts in p2_vocab:
    add_q(p2, i, "Vocabulary", q, opts, ans)

# --- Cloze ---
txt_p2_cloze = """It was a rainy Monday morning. As I hurried towards the classroom, my shoes got 61 in the mud. "Great way to start the week," I muttered. Inside, the classroom was noisy. My best friend, Li Ming, waved me over. "You look 62! Here," he said, tossing me a towel. "Dry your hair before Ms. Wang arrives."

Ms. Wang, our English teacher, is strict but 63. Today, she announced a surprise quiz. My heart sank-I'd forgotten to study! As the papers were 64, I glanced at Li Ming's answers. Copying them felt wrong, but fear of failure 65 me.

After class, Ms. Wang called me to her desk. "I noticed you struggling," she said gently. "Cheating never solves problems. Next time, come to me for help." Her words stung, but I knew she was right.

That afternoon, I stayed late to study. The rain had stopped, and sunlight streamed through the windows. Li Ming joined me, 66 a cup of hot chocolate. "Told you Ms. Wang isn't so bad," he grinned. "She just wants us to 67."

We studied until the library closed. Walking home, I felt lighter. The quiz score didn't matter anymore; I'd learned a bigger lesson about 68. The next day, Ms. Wang returned our quizzes. To my surprise, I'd passed! "Good effort," she wrote in red ink. I glanced at Li Ming, who winked. "See? Honesty 69."

As weeks passed, I visited Ms. Wang for extra help. Slowly, my grades improved. One afternoon, she handed me a book. "For your 70," she said. "You've come a long way.\""""

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
    q_text = f"Cloze {i} (Select the best option)"
    ops = {"A":"A","B":"B","C":"C","D":"D"}
    explanation_txt = f"选项: {txt}"
    add_q(p2, i, "Cloze", q_text, ops, ans, txt_p2_cloze, explanation_txt)

# --- Translation ---
p2_trans = [
    (71, "The local government has organized free job training programs to help recent graduates improve their employment prospects.", "当地政府组织了免费职业培训项目，帮助应届毕业生提升就业机会。"),
    (72, "Many students find it challenging to balance part-time work with their academic responsibilities.", "许多学生发现很难兼顾兼职工作和学业。"),
    (73, "The new library on campus provides a quiet study space equipped with advanced digital resources.", "校园里的新图书馆提供了安静的自习空间，并配备了先进的数字资源。"),
    (74, "Regular physical exercise is proven to boost concentration and reduce stress among high school students.", "事实证明，定期锻炼能提高高中生的注意力并减轻压力。"),
    (75, "The popularity of online learning platforms surged during the pandemic, offering flexible alternatives to traditional classrooms.", "在疫情期间，在线学习平台的受欢迎程度激增，为传统课堂提供了灵活的替代方案。"),
    (76, "春节期间，家人通常会团聚在一起吃年夜饭。", "During the Spring Festival, families usually reunite for a big feast on New Year's Eve."),
    (77, "手机支付改变了人们的消费方式，现在很少有人带现金出门。", "Mobile payment has changed how people spend money; few now carry cash when going out."),
    (78, "坚持每天锻炼半小时，能有效改善睡眠质量。", "Exercising for half an hour daily can effectively improve sleep quality."),
    (79, "越来越多的人选择骑自行车上班，以减少交通拥堵和空气污染。", "More and more people choose to cycle to work to reduce traffic jams and air pollution."),
    (80, "学校图书馆新购置了大量英文原版书籍，方便学生借阅。", "The school library has acquired numerous original English books for students to borrow.")
]
for i, q, a in p2_trans:
    add_q(p2, i, "Translation", q, None, a)


# =======================================================
#                      试卷 3 数据 (完整版)
# =======================================================
p3 = "2025模拟卷3"

# --- Reading ---
# Passage One
txt_p3_r1 = """Passage One
Is a nearby neighbor better than a faraway cousin? An American lady, Anna Lane, believes it's true. Her kind neighbors once helped her out when she was in a big trouble.

Mrs. Lane was living alone in a city in Texas, US. The woman in her 70s could do a lot of housework herself. However, she was too old to mow( ) her lawn. Then a big trouble found her. She let the grass grow over 18 inches high and it broke the law in her city. As a result, she was in danger of paying lots of money or even going to prison!

Luckily, her neighbors, the Adams brothers, heard the news about her on TV. They decided to do something to help. "We haven't met her yet, but she's 75 years old and she needs some help," said Sam Adams, one of the boys. "That's the least we could do."

The Adams brothers took their mowers (machines which are used to mow grass) and came to Mrs. Lane's house to mow her lawn without telling her. Once they got started, other neighbors saw what was going on and joined in the effort. Together they worked hard in the sun and finished mowing the whole lawn in about two hours.

When Mrs. Lane saw what her neighbors did for her, she was surprised and moved to tears. "I cannot believe this," she said. "They were so kind to spend two hours helping me and I didn't even know their names." As for the Adams brothers, they said they would always be ready to help her."""

add_q(p3, 1, "Reading", "What can we know about Mrs. Lane?",
      {"A": "She was 70 years old", "B": "She could not do her housework", "C": "She was living with her children", "D": "She could not cut the grass on the lawn"}, "D", txt_p3_r1, "文中提到 'she was too old to mow her lawn'。")
add_q(p3, 2, "Reading", "Mrs. Lane in danger of prison because",
      {"A": "she broke the education law in her city", "B": "the grass on her lawn was over 18 inches high", "C": "the news about her on TV was made up by her", "D": "she didn't pay enough money to her neighbors"}, "B", txt_p3_r1, "文中提到 'grass grow over 18 inches high... broke the law... danger of... going to prison'。")
add_q(p3, 3, "Reading", "Who mowed the lawn?",
      {"A": "the Adams brothers", "B": "Sam Adams and Mrs. Lane", "C": "the Adams brothers and Mrs. Lane", "D": "the Adams brothers and other neighbors"}, "D", txt_p3_r1, "文中说 Adams brothers 开始，然后 'other neighbors... joined'，所以是D。")
add_q(p3, 4, "Reading", "Which of the following TRUE?",
      {"A": "The Adams brothers knew Mrs. Lane very well.", "B": "Mrs. Lane knew some of her neighbors' names.", "C": "Mrs. Lane didn't expect her neighbors would help her.", "D": "The Adams brothers used Mrs. Lane's mowers to cut the grass."}, "C", txt_p3_r1, "Mrs. Lane 说 'I cannot believe this'，说明她没料到。")
add_q(p3, 5, "Reading", "Mrs. Lane was living alone in a city in ____, US.",
      {"A": "Texas", "B": "Indiana", "C": "Georgia", "D": "Washington"}, "A", txt_p3_r1, "文中明确说是 'living alone in a city in Texas, US'。")


# Passage Two
txt_p3_r2 = """Passage Two
Your next Saturday night takeaway could be brought to you by a robot after a major food delivery company announced plans to use automated vehicles to transport meals. Europe's biggest online takeaway food company Just Eat has partnered with Starship Technologies to deliver food with robots on the streets of London later this month.

"Nobody has ever done deliveries with land-based robots," said Allan Martinson, the chief operating officer of Starship. The robot courier can travel up to 4 miles per hour for about 10 miles. It uses a GPS signal and nine cameras to navigate (确定方向). Instead of a person arriving at their door, customers could find themselves receiving a notification on their phone that says a robot is on its way and a code to unlock the automated courier. "Put the code in, the robot opens up, and there's your food," said David Buttress, chief manager of Just Eat.

The robot, which has so far been tested in Greenwich, Milton Keynes and Glastonbury, costs 1 to transport within 3 miles, compared with the £3 to £6 it costs for a human courier. To date 30 robots have driven nearly 5,000 miles without getting into an accident or finding themselves picked on by passers-by. They have driven in more than 40 cities around the world, including London and Tallinn, Estonia.

An initial worry was how the public would react to robots. But Martinson said the public has been calm when passing the delivery machine on the streets. "The most surprising reaction has been the lack of reaction," said Martinson. Another significant fear was that people would disrupt (扰乱) the robots, or try to steal them and their contents. To prevent this, the robot is fitted with nine cameras, two way audio, and movement sensors that send a warning if it is lifted off the ground. And it opens only with a pass code provided to the customer via a notification. "It's much easier to shoplift than it is to steal a robot," said Martinson."""

add_q(p3, 6, "Reading", "Which of the following can replace the underlined word 'courier' in Paragraph 2?",
      {"A": "deliverer", "B": "collector", "C": "provider", "D": "guide"}, "A", txt_p3_r2, "courier 意为信使、递送员，即 deliverer。")
add_q(p3, 7, "Reading", "According to the text, the Starship robot",
      {"A": "opens up upon hearing the code", "B": "travels 10 miles per hour at most", "C": "finds its way by means of GPS and cameras", "D": "sends a message to the customer upon arrival"}, "C", txt_p3_r2, "文中说 'It uses a GPS signal and nine cameras to navigate'。")
add_q(p3, 8, "Reading", "The test of Starship robots shows that",
      {"A": "they are easy to operate", "B": "the robot delivery is appreciated in big cities", "C": "the robot delivery is cheaper than human delivery", "D": "they can travel for 10 hours continuously"}, "C", txt_p3_r2, "文中提到 'costs 1 ... compared with the £3 to £6 it costs for a human'。")
add_q(p3, 9, "Reading", "Which of the following is one of the worries about Starship robots?",
      {"A": "Safety of the robot delivery.", "B": "Accuracy of the robot delivery", "C": "Peoples indifference to the robots.", "D": "People's concern about public traffic."}, "A", txt_p3_r2, "文中提到的 'disrupt... or try to steal them' 属于安全隐患。")
add_q(p3, 10, "Reading", "Which of the following would be the best title for the text?",
      {"A": "Great Improvement of Just Eat", "B": "Global Trend of Food Companies", "C": "New Robots to Move on the road", "D": "Delivery Robots to Replace Takeaway Drivers"}, "D", txt_p3_r2, "文章主要讲外卖配送机器人。")


# Passage Three
txt_p3_r3 = """Passage Three
Lisa was a businesswoman who often traveled by plane. One day her husband Sam drove her to the airport and he stayed with her waiting for the security check before the plane took off. They found the line took longer than before. This was due to a man in front of them. Because of strict safety concern, his package was not allowed on the plane. Even though the man begged again and again for a long time, it was no use. He was asked to throw the package into the nearest rubbish bin, and so he did.

Seeing the man's sad expression, Lisa, before parting from her husband, asked him to do something strange. After the plane landed, she quickly called Sam to see if he had taken the package back. Sam took some photos of what was inside the package. On seeing the photos, she understood why the man was so sad. It was a glass snowball with a picture of a little girl. On the bottom of it was carved with "We love you Katie. 01/25/2016."

Lisa and her husband went online to look for its owner. The photos were shared more than 48,000 times in a week! Soon, with the help of a global supermarket, they found the person who had bought the snow globe: Richard Milton, and with the help of an express company, they returned the package to him.

Richard, grandpa of Katie, was moved to tears. The true story behind the snowball was that the words on it did not represent a date of birth. It was the date of Katie's adoption. The globe was to show everyone how welcome Katie was in her new family. Whenever Lisa and Sam look back on the whole event, they are filled with great pride, for what they saved is not only a gift but also love."""

add_q(p3, 11, "Reading", "What happened during the security check?",
      {"A": "A man had got to abandon his package.", "B": "A man in front forgot to bring his luggage.", "C": "Lisa was asked to throw her package away.", "D": "Lisa got impatient while waiting in the line."}, "A", txt_p3_r3, "前排男子被迫丢弃包裹 (asked to throw the package)。")
add_q(p3, 12, "Reading", "What was the main reason why the man's package was not allowed on the plane?",
      {"A": "It contained a dangerous item.", "B": "It exceeded the weight limit.", "C": "It violated safety regulations.", "D": "It was not properly packaged."}, "C", txt_p3_r3, "文中说是 'Because of strict safety concern'，即违反安全规定。")
add_q(p3, 13, "Reading", "What strange thing did Lisa ask Sam to do?",
      {"A": "To take photos of the airport.", "B": "To find the nearest rubbish bin.", "C": "To put away the sad man's package.", "D": "To beg the security officials for help."}, "C", txt_p3_r3, "她让丈夫把那个包裹捡回来/收好 (taken the package back)。")
add_q(p3, 14, "Reading", "Why was the snowball so important according to the passage?",
      {"A": "It recorded Katie's birthday.", "B": "It was valuable and expensive.", "C": "It meant family's love to Katie.", "D": "It was very popular on the Internet."}, "C", txt_p3_r3, "文中说 'show everyone how welcome Katie was in her new family'，代表了家人的爱。")
add_q(p3, 15, "Reading", "Which of the following may be the best title of the passage?",
      {"A": "Katie's birthday gift", "B": "Return of a snow globe", "C": "Security check in the U.S.", "D": "A lost package in an airport"}, "B", txt_p3_r3, "文章讲的是归还雪球的故事。")


# Passage Four
txt_p3_r4 = """Passage Four
The concept of "mindfulness" has gained traction in recent years as a tool for improving mental health and focus. Mindfulness involves intentionally paying attention to the present moment without judgment. Practices like meditation, deep breathing, and even simple activities such as savoring a cup of tea can be forms of mindfulness.

Research suggests that mindfulness reduces stress by lowering cortisol levels, the body's primary stress hormone. It also enhances emotional regulation, helping individuals respond to challenges calmly rather than reacting impulsively. For example, a study found that college students who practiced mindfulness for eight weeks reported lower anxiety levels and improved sleep quality.

Critics argue that mindfulness is merely a trend and lacks scientific rigor. However, numerous peer-reviewed studies support its benefits. Neuroimaging studies show that long-term mindfulness practice can thicken the prefrontal cortex, the brain region responsible for decision-making and attention.

Despite its advantages, mindfulness is not a one-size-fits-all solution. Some individuals struggle with the stillness required for meditation, finding it frustrating rather than calming. Experts recommend starting with short sessions (5-10 minutes daily) and gradually increasing duration as comfort grows."""

add_q(p3, 16, "Reading", "What is the primary purpose of mindfulness, as described in the passage?",
      {"A": "To replace traditional medicine.", "B": "To improve mental health and focus.", "C": "To increase physical strength.", "D": "To promote technological advancement."}, "B", txt_p3_r4, "第一句：'as a tool for improving mental health and focus'。")
add_q(p3, 17, "Reading", "How does mindfulness reduce stress, according to the passage?",
      {"A": "By increasing cortisol levels.", "B": "By lowering cortisol levels.", "C": "By eliminating all challenges.", "D": "By encouraging impulsive reactions."}, "B", txt_p3_r4, "文中说 'reduces stress by lowering cortisol levels'。")
add_q(p3, 18, "Reading", "The word 'traction' in paragraph 1 most nearly means:",
      {"A": "popularity", "B": "confusion", "C": "rejection", "D": "criticism"}, "A", txt_p3_r4, "gain traction 意为获得关注、变得流行 (popularity)。")
add_q(p3, 19, "Reading", "What does the example of college students illustrate?",
      {"A": "Mindfulness is only effective for young people.", "B": "Mindfulness can improve anxiety and sleep.", "C": "Mindfulness requires eight weeks to work.", "D": "Mindfulness is a replacement for therapy."}, "B", txt_p3_r4, "文中说学生 'reported lower anxiety levels and improved sleep quality'。")
add_q(p3, 20, "Reading", "What is a potential challenge for beginners practicing mindfulness?",
      {"A": "Immediate improvement in focus.", "B": "Difficulty staying still or calm.", "C": "Enhanced social connections.", "D": "Guaranteed reduction in stress."}, "B", txt_p3_r4, "文中提到 'Some individuals struggle with the stillness required'。")


# --- Vocab (21-60) ---
p3_vocab = [
    (21, "C", "The team's performance was greatly _____ by the heavy rain.", {"A":"injured","B":"governed","C":"affected","D":"harmed"}),
    (22, "C", "But as an American, I constantly found myself _____ when it came to seeing guests off at the door.", {"A":"quiet","B":"shocked","C":"tongue-tied","D":"surprised"}),
    (23, "C", "She only received _____ injuries in the accident.", {"A":"major","B":"junior","C":"minor","D":"shorter"}),
    (24, "D", "Even when she became rich and famous, she never forgot her _____ background.", {"A":"noble","B":"modest","C":"brilliant","D":"humble"}),
    (25, "A", "He taught his children to be _____ of other cultures.", {"A":"respectful","B":"respectable","C":"respective","D":"respect"}),
    (26, "A", "This advice will _____ throughout your life.", {"A":"hold true","B":"go against","C":"go through","D":"slip into"}),
    (27, "A", "Those gifts of rare books that were given to us were deeply _____.", {"A":"appreciated","B":"approved","C":"appealed","D":"applied"}),
    (28, "D", "The poet is regarded as the _____ figure in literacy circles.", {"A":"most","B":"leader","C":"misleading","D":"leading"}),
    (29, "A", "His work involves _____ journeys.", {"A":"occasional","B":"full","C":"occasion","D":"artificial"}),
    (30, "C", "There are plastic and wooden garden chairs but the _____ are more expensive.", {"A":"late","B":"lately","C":"latter","D":"back"}),
    (31, "B", "---I have tried very hard to find a solution to the problem, but in vain.\n---Why not consult with Frank? You see, _____.", {"A":"great minds think alike","B":"two heads are better than one","C":"a bird in the hand is worth two in the bush","D":"it's better to think twice before doing something"}),
    (32, "D", "The newly built café, the walls of _____ are painted light green, is really a peaceful place...", {"A":"that","B":"it","C":"what","D":"which"}),
    (33, "A", "---Is everyone here? \n---Not yet. Look, there _____ the rest of our guests!", {"A":"come","B":"comes","C":"is coming","D":"are coming"}),
    (34, "B", "George is going to talk about the geography of his country, but I'd rather he _____ more on its culture.", {"A":"focus","B":"focused","C":"would focus","D":"had focused"}),
    (35, "A", "---I prefer shutting myself in and listening to music all day on Sundays.\n---That's _____ I don't agree. You should have a more active life.", {"A":"where","B":"how","C":"when","D":"what"}),
    (36, "C", "The teacher _____ him that he had the talent to study music.", {"A":"guaranteed","B":"pledged","C":"convinced","D":"promised"}),
    (37, "B", "The villagers were _____ that the fast development in science... would facilitate their lives...", {"A":"deceived","B":"informed","C":"shown","D":"upheld"}),
    (38, "C", "The local government has taken every measure to _____ that every kid at the age of six can attend school.", {"A":"assure","B":"insure","C":"ensure","D":"secure"}),
    (39, "A", "In a sudden _____ of anger, the man tore up everything within reach.", {"A":"burst","B":"attack","C":"split","D":"blast"}),
    (40, "D", "To our great sorrow, none of the villagers _____ the earthquake.", {"A":"outlived","B":"sustained","C":"underwent","D":"survived"}),
    (41, "D", "When he tried to make a _____ he found that the hotel was completely filled...", {"A":"complaint","B":"claim","C":"decision","D":"reservation"}),
    (42, "D", "She has written a _____ of modern English literature.", {"A":"supervision","B":"indication","C":"selection","D":"survey"}),
    (43, "D", "Ancient Egyptians knew of means to _____ dead bodies from decay.", {"A":"conserve","B":"reserve","C":"deserve","D":"preserve"}),
    (44, "A", "Make sure the wound is _____ dirt before applying the bandage.", {"A":"free from","B":"out of","C":"away from","D":"prevented"}),
    (45, "B", "Professor Martin is always very _____ to the reaction of the audience when he gives lectures.", {"A":"sentimental","B":"sensitive","C":"sensible","D":"positive"}),
    (46, "C", "_____ customer satisfaction, the policy cannot be criticized.", {"A":"Superior to","B":"Prior to","C":"In terms of","D":"Along with"}),
    (47, "A", "Don't _____ this news to the public until we give you information.", {"A":"release","B":"relieve","C":"retain","D":"relate"}),
    (48, "C", "It was _____ that he'd find out her secret sooner or later.", {"A":"feasible","B":"discouraged","C":"inevitable","D":"denied"}),
    (49, "B", "The shabby houses in the back street were in striking _____ with the skyscrapers in the center of the city.", {"A":"comparison","B":"contrast","C":"contrary","D":"contract"}),
    (50, "D", "Which _____ of shoes do you prefer?", {"A":"bind","B":"band","C":"bond","D":"brand"}),
    (51, "A", "After living in a house with a garden, it's hard to _____ living in a flat.", {"A":"adapt to","B":"devote to","C":"lead to","D":"add to"}),
    (52, "D", "_____ you so long a time, I miss you very much.", {"A":"Having not seen","B":"Not seeing","C":"Have not seen","D":"Not having seen"}),
    (53, "B", "Linda gave us a vivid _____ of her trip to Mountain Lu Shan after her return.", {"A":"explanation","B":"account","C":"idea","D":"imagination"}),
    (54, "A", "All their hopes _____ the next generation now.", {"A":"concentrate on","B":"attract on","C":"look on","D":"fascinate on"}),
    (55, "C", "Over the years of hard work, her beauty had _____ a lot.", {"A":"changed","B":"damaged","C":"faded","D":"disappeared"}),
    (56, "B", "A tiny baby soon learns to _____ his mother's face from other adult's.", {"A":"disapprove","B":"distinguish","C":"separate","D":"recognize"}),
    (57, "A", "Many people here are _____ by his _____ story.", {"A":"moved; moving","B":"moving; moved","C":"moved; moved","D":"moving; moving"}),
    (58, "D", "_____ the expert stressed at the meeting, students' study should focus on the 45-minute lessons.", {"A":"It","B":"What","C":"That","D":"As"}),
    (59, "C", "It _____ us greatly that they took so long to answer our requirement.", {"A":"interrupted","B":"disturbed","C":"annoyed","D":"troubled"}),
    (60, "B", "When you make a speech, you should try to get your idea _____.", {"A":"off","B":"across","C":"away","D":"aside"})
]
for i, ans, q, opts in p3_vocab:
    add_q(p3, i, "Vocabulary", q, opts, ans)

# --- Cloze ---
txt_p3_cloze = """In today's fast-paced world, maintaining a healthy lifestyle has become increasingly challenging. Many people struggle to balance work, family, and personal time, often sacrificing their well-being in the process. However, small changes can make a 61 difference.

One key aspect is physical activity. Experts recommend at least 30 minutes of moderate exercise daily, such as 62 or cycling. Yet, studies show that nearly 60% of adults fail to meet this 63. Sedentary lifestyles are linked to various health issues, including obesity and heart disease. To 64 this, even short breaks from sitting-like stretching or walking-can help.

Nutrition also plays a vital role. A 65 diet rich in fruits, vegetables, and whole grains provides essential nutrients. Avoiding processed foods and excessive sugar is equally important. For instance, replacing sugary drinks with water can 66 reduce calorie intake.

Mental health is another 67 component. Chronic stress weakens the immune system and affects sleep quality. Practices like meditation or mindfulness can alleviate stress and improve 68.

Finally, adequate sleep cannot be overlooked. Most adults need 7-9 hours nightly, but 69 schedules often lead to sleep deprivation. Prioritizing sleep enhances focus, mood, and overall health.

In conclusion, adopting a holistic approach to health-combining exercise, nutrition, mental care, and rest-is 70 for long-term well-being."""

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
    q_text = f"Cloze {i} (Select the best option)"
    ops = {"A":"A","B":"B","C":"C","D":"D"}
    explanation_txt = f"选项: {txt}"
    add_q(p3, i, "Cloze", q_text, ops, ans, txt_p3_cloze, explanation_txt)

# --- Translation ---
p3_trans = [
    (71, "The Lantern Festival, which falls on the 15th day of the first lunar month, marks the end of the Spring Festival celebrations.", "元宵节在农历正月十五，标志着春节庆祝活动的结束。"),
    (72, "With the rapid development of mobile internet, smartphones have become an indispensable part of people's daily lives.", "随着移动互联网的迅猛发展，智能手机已成为人们日常生活中不可或缺的一部分。"),
    (73, "Many universities now offer online learning platforms, allowing students to access course materials anytime and anywhere.", "如今许多大学都提供在线学习平台，让学生可以随时随地获取课程资料。"),
    (74, "The government has launched a campaign to promote waste sorting, aiming to reduce environmental pollution.", "政府发起了一项推广垃圾分类的活动，旨在减少环境污染。"),
    (75, "Despite the challenges, young entrepreneurs are increasingly choosing to start their own businesses in rural areas.", "尽管面临挑战，年轻创业者越来越多地选择在农村地区创业。"),
    (76, "这本书不仅内容有趣，而且语言通俗易懂，适合初学者阅读。", "This book is not only interesting but also easy to understand, making it suitable for beginners."),
    (77, "许多城市正在推广垃圾分类，以减少环境污染和资源浪费。", "Many cities are promoting waste sorting to reduce environmental pollution and resource waste."),
    (78, "如果你坚持每天练习英语口语，很快就会看到进步。", "If you keep practicing English speaking every day, you will see progress soon."),
    (79, "互联网的普及让人们可以随时随地获取信息和知识。", "The popularity of the Internet enables people to access information and knowledge anytime, anywhere."),
    (80, "他虽然年轻，但已经积累了丰富的工作经验。", "Although he is young, he has already accumulated rich work experience.")
]
for i, q, a in p3_trans:
    add_q(p3, i, "Translation", q, None, a)


if __name__ == "__main__":
    with open("data_full.json", "w", encoding="utf-8") as f:
        json.dump(full_data, f, indent=4, ensure_ascii=False)
    print("✅ 成功生成 data_full.json！")
    print("包含 3 套卷子，阅读文章和题目已修正为完整版。")