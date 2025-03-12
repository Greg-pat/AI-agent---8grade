import streamlit as st
import openai

# Konfiguracja klucza API (dodawany przez sekrety w Streamlit)
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Sprawdź swoją wypowiedź!", page_icon="✍️", layout="centered")

st.title("✍️ Sprawdź swoją wypowiedź na egzamin ósmoklasisty!")

st.write("""
Wpisz swoją pracę (np. e-mail, zaproszenie, wpis na bloga), a asystent AI sprawdzi ją i podpowie, co poprawić, aby zdobyć maksymalną liczbę punktów! 💪
""")

user_input = st.text_area("Twoja wypowiedź:", height=200)

if st.button("✅ Sprawdź moją pracę"):
    if user_input.strip() == "":
        st.error("Proszę wpisać swoją wypowiedź.")
    else:
        with st.spinner("Analizuję Twoją pracę..."):

            # Przygotowanie promptu dla AI
            prompt = f"""
Jesteś nauczycielem języka angielskiego, oceniasz wypowiedź pisemną ucznia 8 klasy zgodnie z kryteriami egzaminu ósmoklasisty:
1. Zgodność z poleceniem (0-3 pkt)
2. Spójność i logika (0-2 pkt)
3. Zakres środków językowych (0-2 pkt)
4. Poprawność językowa (0-3 pkt)

Podaj:
- Liczbę punktów z każdej kategorii.
- Co jest dobre.
- Co trzeba poprawić (z przykładami).
- Lepszą wersję wypowiedzi (dostosowaną do poziomu A2+/B1).

Oto wypowiedź ucznia:
\"\"\"{user_input}\"\"\"
"""

            # Wysłanie zapytania do OpenAI GPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=700
            )

            reply = response['choices'][0]['message']['content']

            # Wyświetlenie odpowiedzi AI
            st.subheader("📝 Twoja ocena i poprawki:")
            st.write(reply)

            st.success("Super! Teraz popraw swoją pracę i zdobywaj punkty na egzaminie! 🚀")