import streamlit as st
import streamlit as st
import random

def get_questions():
    return [
        {"question": "Apa sumber utama karbohidrat dalam makanan pokok Indonesia?", "options": ["Daging", "Nasi", "Susu", "Keju"], "answer": "Nasi"},
        {"question": "Vitamin yang banyak terdapat dalam wortel adalah?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "answer": "Vitamin A"},
        {"question": "Manakah yang termasuk protein nabati?", "options": ["Ayam", "Ikan", "Tahu", "Daging Sapi"], "answer": "Tahu"},
        {"question": "Apa yang harus dilakukan untuk menjaga pola makan sehat?", "options": ["Makan fast food setiap hari", "Minum soda berlebihan", "Konsumsi sayur dan buah", "Makan sebelum tidur"], "answer": "Konsumsi sayur dan buah"},
    ]

def main():
    st.title("🎮 Game Edukasi Pangan")
    st.write("Jawab pertanyaan tentang pangan dan gizi untuk menguji pengetahuanmu!")
    
    if 'score' not in st.session_state:
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.questions = random.sample(get_questions(), len(get_questions()))

    if st.session_state.q_index < len(st.session_state.questions):
        q_data = st.session_state.questions[st.session_state.q_index]
        st.write(f"**{q_data['question']}**")
        choice = st.radio("Pilih jawaban:", q_data["options"], key=f"q{st.session_state.q_index}")
        
        if st.button("Submit"):
            if choice == q_data["answer"]:
                st.session_state.score += 1
                st.success("✅ Jawaban benar!")
            else:
                st.error(f"❌ Jawaban salah! Jawaban yang benar adalah {q_data['answer']}")
            
            st.session_state.q_index += 1
            st.experimental_rerun()
    else:
        st.write(f"### 🎉 Permainan selesai! Skor akhir: {st.session_state.score}/{len(st.session_state.questions)}")
        if st.button("Main lagi"):
            st.session_state.score = 0
            st.session_state.q_index = 0
            st.session_state.questions = random.sample(get_questions(), len(get_questions()))
            st.experimental_rerun()

if __name__ == "__main__":
    main()

