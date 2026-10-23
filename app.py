
import streamlit as st

st.set_page_config(
    page_title="달빛 아래의 제국",
    page_icon="✦",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(160deg, #21172f, #111629);
    color: #fff3df;
}
h1, h2, h3, p, label {
    color: #fff3df !important;
}
div.stButton > button {
    width: 100%;
    min-height: 55px;
    border: 1px solid #c8a66b;
    border-radius: 14px;
    background: #382944;
    color: #fff3df;
    font-size: 16px;
}
div.stButton > button:hover {
    background: #70517a;
    border-color: #f5d9a0;
}
.story {
    background: #292039;
    border: 1px solid #c8a66b;
    border-radius: 18px;
    padding: 22px;
    line-height: 1.9;
}
</style>
""", unsafe_allow_html=True)

if "scene" not in st.session_state:
    st.session_state.scene = 0
    st.session_state.affection = 0

st.markdown(
    "<p style='text-align:center;letter-spacing:5px'>"
    "THE EMPIRE OF MOONLIGHT</p>",
    unsafe_allow_html=True
)
st.title("✦ 달빛 아래의 제국 ✦")
st.caption("당신의 선택이 운명을 바꿉니다.")

scenes = [
    {
        "name": "황궁의 무도회",
        "portrait": "♛",
        "story": "화려한 샹들리에가 빛나는 황궁. "
                 "세 사람의 시선이 당신에게 향한다. "
                 "누구에게 먼저 다가갈까?",
        "choices": [
            ("금빛 눈동자의 황태자에게 다가간다", 1),
            ("차가운 북부대공에게 말을 건다", 2),
            ("수상한 궁정 마법사를 관찰한다", 3)
        ]
    },
    {
        "name": "레온하르트 · 황태자",
        "portrait": "♔",
        "story": "'나에게 먼저 다가오다니, 흥미롭군요.' "
                 "황태자가 부드러운 미소를 짓는다.",
        "choices": [
            ("미소로 화답한다", 4),
            ("황태자에게 장난스럽게 되묻는다", 4)
        ]
    },
    {
        "name": "카시안 · 북부대공",
        "portrait": "♜",
        "story": "'무도회가 마음에 들지 않습니까?' "
                 "차가운 공작의 목소리에는 묘하게 다정함이 묻어난다.",
        "choices": [
            ("솔직하게 대답한다", 4),
            ("아무것도 아니라며 웃는다", 4)
        ]
    },
    {
        "name": "에델 · 궁정 마법사",
        "portrait": "✧",
        "story": "'드디어 만나게 되었군요.' "
                 "마법사는 당신의 운명을 이미 알고 있는 듯하다.",
        "choices": [
            ("그 말의 의미를 묻는다", 4),
            ("조용히 그의 말을 기다린다", 4)
        ]
    }
]

if st.session_state.scene == 4:
    st.markdown(
        "<div class='story'><h2>✦ 첫 번째 인연 ✦</h2>"
        "그날 밤, 당신의 선택은 새로운 이야기의 시작이 되었다."
        "</div>",
        unsafe_allow_html=True
    )
    st.write("인연 점수:", st.session_state.affection)

    if st.button("처음부터 다시 시작하기"):
        st.session_state.scene = 0
        st.session_state.affection = 0
        st.rerun()

else:
    scene = scenes[st.session_state.scene]

    st.markdown(
        f"<div style='text-align:center;font-size:100px;"
        f"padding:25px'>{scene['portrait']}</div>",
        unsafe_allow_html=True
    )
    st.subheader(scene["name"])

    st.markdown(
        f"<div class='story'>{scene['story']}</div>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("### 당신의 선택은?")

    for i, (label, destination) in enumerate(scene["choices"]):
        if st.button(label, key=f"{st.session_state.scene}_{i}"):
            if st.session_state.scene == 0:
                st.session_state.affection += 1
            else:
                st.session_state.affection += 1

            st.session_state.scene = destination
            st.rerun()
