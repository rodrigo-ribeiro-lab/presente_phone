import streamlit as st
from datetime import datetime
from pathlib import Path

# ------------------------------
# CONFIGURAÇÕES INICIAIS
# ------------------------------
st.set_page_config(page_title="Nossa História ❤️", layout="wide")

st.markdown("""
<style>
/* Corações caindo */
@keyframes fall {
  0% {transform: translateY(-100px);}
  100% {transform: translateY(800px);}
}
.heart {
  position: fixed;
  font-size: 24px;
  animation: fall linear infinite;
  color: #FF69B4;
  user-select: none;
  pointer-events: none;
}

.section-note {
  margin-bottom: 0.75rem;
  color: #6b7280;
}

[data-testid="stAppViewContainer"] .main .block-container {
  padding-top: 0.5rem;
  padding-bottom: 2rem;
}

[data-testid="stAppViewContainer"] .stMainBlockContainer {
  padding-top: 0rem;
}

.cover-card {
  max-width: 760px;
  margin: 1.5rem auto 1.5rem auto;
  padding: 2.5rem 2rem;
  border-radius: 24px;
  background: linear-gradient(135deg, rgba(255, 240, 245, 0.95), rgba(255, 250, 252, 0.92));
  border: 1px solid rgba(255, 105, 180, 0.18);
  box-shadow: 0 20px 45px rgba(255, 105, 180, 0.14);
  text-align: center;
}

.cover-eyebrow {
  margin-bottom: 1rem;
  color: #be185d;
  font-size: 0.95rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-weight: 700;
}

.cover-line {
  margin: 0.85rem 0;
  font-size: 1.2rem;
  line-height: 1.7;
  color: #3f3f46;
}

.cover-hero {
  max-width: 750px;
  margin: 0.5rem auto 1.25rem auto;
}

.cover-shell {
  margin-top: -2.5rem;
}
</style>
""", unsafe_allow_html=True)

import random
for i in range(20):
    st.markdown(f'<div class="heart" style="left:{random.randint(0,100)}%; animation-duration:{random.randint(5,15)}s;">❤️</div>', unsafe_allow_html=True)


def centered_image(image_path, caption=None, ratio=(1, 1.8, 1)):
    left, center, right = st.columns(ratio)
    with center:
        st.image(image_path, caption=caption, use_container_width=True)


def image_row(images, captions=None):
    if captions is None:
        captions = [None] * len(images)
    columns = st.columns(len(images), gap="medium")
    for column, image_path, caption in zip(columns, images, captions):
        with column:
            st.image(image_path, caption=caption, use_container_width=True)


def column_image(column, image_path, caption=None):
    with column:
        st.image(image_path, caption=caption, use_container_width=True)

# ------------------------------
# VARIÁVEIS PRINCIPAIS
# ------------------------------
nome = "Vi"
data_conhecemos = datetime(2025, 12, 30)
hoje = datetime.now()
dias_juntos = (hoje - data_conhecemos).days

# ------------------------------
# TELA INICIAL
# ------------------------------
# Música de fundo
audio_path = Path("audio/'City of Stars' (Duet ft. Ryan Gosling, Emma Stone) - La La Land Original Motion Picture Soundtrack [GTWqwSNQCcg].mp3")
hero_image_path = Path("fotos/gato.jpeg")
with st.container():
    st.markdown('<div class="cover-shell">', unsafe_allow_html=True)
    st.title(f"Feliz Aniversário, {nome} ❤️")
    st.subheader(f"Estamos escrevendo nossa história há {dias_juntos} dias")

    if hero_image_path.exists():
        st.markdown('<div class="cover-hero">', unsafe_allow_html=True)
        centered_image(str(hero_image_path), ratio=(0.7, 2.6, 0.7))
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="cover-card">
            <div class="cover-eyebrow">Seu presente de aniversário</div>
            <p class="cover-line">Tem uma coisinha feita com carinho.</p>
            <p class="cover-line">Antes de começar, respira fundo e de play na música.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if audio_path.exists():
        st.audio(str(audio_path), format="audio/mp3", loop=True)
    else:
        st.warning("Adicione o arquivo em audio/musica.mp3 para tocar a música.")
    st.markdown('</div>', unsafe_allow_html=True)

if st.button("Abrir seu presente", key="start_story_button", use_container_width=True):
    st.session_state.start = True

if 'start' not in st.session_state:
    st.stop()

if "show_second_date" not in st.session_state:
    st.session_state.show_second_date = False

if "show_third_date" not in st.session_state:
    st.session_state.show_third_date = False

# ------------------------------
# LINHA DO TEMPO
# ------------------------------
st.header("Nossa Jornada")

# Primeiro Date
with st.container(border=True):
    st.subheader("💕 30/01 – Primeiro Date")
    st.write("🍽️ Poke | 🎬 Sinners | 🎮 Jogos online")
    st.write("No nosso primeiro encontro, decidimos assistir a um filme juntos online. Você escolheu 'Sinners'. Foi muito divertido assistir ao filme juntos, mesmo em lugares diferentes consegui sentir sua presença.")
    st.write("Eu lembro como eu estava nervoso nesse dia, foi a primeira vez que nos vimos por vídeo. Eu queria te impressionar e por isso fiquei um tempo pensando em qual roupa eu ia usar.")
    st.write("Como você percebeu, em determinados momentos do filme, me pagava olhando só para você e até esquecia a televisão, eu me perdia no seu olhar.")
    image_row(
        ["fotos/sinners.jpeg", "fotos/poke.jpeg", "fotos/uno.jpeg"],
        ["Filme da noite", "Nosso poke", "Uno para fechar"],
    )
    st.write("Comemos poke enquanto assistíamos o filme. Foi um momento especial, nossa primeira refeição juntos.")
    st.write("E para fechar a noite, jogamos Uno. Foi bem divertido ganhar de você e rir das nossas jogadas. Mal podia esperar para o próximo encontro! ❤️")

if st.button("Mostrar a próxima Lembrança", key="show_second_date_button"):
    st.session_state.show_second_date = True

if not st.session_state.show_second_date:
    st.stop()

# Segundo Date
with st.container(border=True):
    st.subheader("💕 28/02 – Segundo Date")
    st.write("🍜 Coreano | 🎬 La La Land | 🌍 Passeio pelo Street View")
    st.write("No nosso segundo encontro, decidimos vivenciar a culinária coreana. Foi divertido experimentar novos sabores com você. No começo eu estava um pouco cético quanto à essa escolha, mas decidi confiar em seu gosto e adorei o prato.")
    st.write("Enquanto comíamos, decidimos assistir La La Land. Como você sabe, é um filme que eu gostaria muito de assistir com uma pessoa especial, e foi maravilhoso ver com você!")
    coreano, filme = st.columns(2, gap="large")
    column_image(coreano, "fotos/coreano.jpeg", "Jantar coreano")
    column_image(filme, "fotos/lalaland.jpg", "La La Land")
    st.write(" ")
    st.write("Nesse encontro pudemos ver mais do passado e o presente um do outro, nos lugares que passamos nossa vida e onde moramos.")
    image_row(
        ["fotos/casa.jpeg", "fotos/vicrp.jpeg"],
        ["Um pedacinho da minha história", "Um pedacinho da sua"],
    )

if st.button("Mostrar a próxima Lembrança", key="show_third_date_button"):
    st.session_state.show_third_date = True

if not st.session_state.show_third_date:
    st.stop()

# Terceiro Date
with st.container(border=True):
    st.subheader("💕 14/03 – Terceiro Date")
    st.write("🍜 Tailandesa | 📺 Lupin | 🎮 Resident Evil | 🃏 Uno | 🎨 Desenho | 🌎 Viagens planejadas")
    st.write("Nesse encontro (que encontro...), decidimos tirar mais fotos, para registrarmos melhor os nossos momentos juntos.")
    st.write("Lembro quando abrimos a câmera, você estava tão linda... Me deixou sem palavras.")
    st.write("Decidimos experimentar a culinária tailandesa. A comida estava deliciosa. Mais uma vez você acertou em cheio na escolha.")
    jantar, serie = st.columns(2, gap="large")
    column_image(jantar, "fotos/thai.jpeg", "Jantar tailandês")
    column_image(serie, "fotos/lupin.jpeg", "Nossa série")
    st.write("Amei o nosso jogo de desenhar o personagem um do outro. Aqui estão as comparações de expectativa x realidade:")
    primeira_expectativa, primeira_realidade = st.columns(2, gap="large")
    column_image(primeira_expectativa, "fotos/mario.jpeg", "Mario: expectativa")
    column_image(primeira_realidade, "fotos/mario_realidade.jpeg", "Mario: realidade")
    segunda_expectativa, segunda_realidade = st.columns(2, gap="large")
    column_image(segunda_expectativa, "fotos/char_expectativa.jpeg", "Charmander: expectativa")
    column_image(segunda_realidade, "fotos/char_realidade.jpeg", "Charmander: realidade")
    st.write("Pra finalizar a noite, decidimos fazer comida japonesa. Eu amei a calma e paciência que você teve pra me ensinar a fazer sushi, desde o arroz até enrolar o Temaki desconstruído (foi a porposta do chef)")
    centered_image("fotos/sushi.jpeg", caption="Japones juntos", ratio=(0.8, 2.2, 0.8))

# ------------------------------
# VIAGENS DOS SONHOS
# ------------------------------
st.header("🎨 Viagens dos Sonhos")
st.write("Com a barriga cheia, decidimos planejar nossas viagens dos sonhos. Muitos lugares incríveis para conhecer juntos.")
with st.container(border=True):
    st.write("**2026/2027** • Holanda, França, Bélgica e Alemanha")
    holanda, paris = st.columns(2, gap="large")
    column_image(holanda, "fotos/holanda.jpeg", "Holanda")
    column_image(paris, "fotos/paris.jpeg", "Paris")
    st.write("**2027** • Brasil e América do Sul")
    brasil, america = st.columns(2, gap="large")
    column_image(brasil, "fotos/ubatuba.jpeg", "Brasil")
    column_image(america, "fotos/peru.jpeg", "América do Sul")
    st.write("**2028** • Olimpíadas em Los Angeles e passeio pela California")
    la28, golden = st.columns(2, gap="large")
    column_image(la28, "fotos/la28.jpeg", "Los Angeles 2028")
    column_image(golden, "fotos/california.jpeg", "California")

# ------------------------------
# QUIZ INTERATIVO
# ------------------------------
st.header("🎮 Quiz do Casal")
st.write("Vamos ver se você lembra dos nossos momentos juntos? Responda o quiz corretamente e veja se consegue ganhar o presentinho especial no final! ❤️")
score = 0

q1 = st.radio("Quando foi nosso primeiro date?", ["30/01", "28/02", "14/03"], key="q1")
q2 = st.radio("Qual filme vimos juntos no segundo encontro?", ["La La Land", "Sinners", "Lupin"], key="q2")
q3 = st.radio("Quem ganhou mais no Uno?", ["Você", "Eu", "Empatamos"], key="q3")
q4 = st.radio("Qual foi o cardápio do almoço do nosso terceiro date?", ["Pad Thai", "Som Tum", "Khao Pad"], key = "q4")
q5 = st.radio("Qual a minha cor favorita?", ["Azul", "Vermelho", "Verde"], key = "q5")
q6 = st.radio("Qual o nome da música que está tocando?", ["Another Day of Sun", "City of Stars", "Start a Fire"], key = "q6")
q7 = st.radio("Qual a personagem de Genshin mais subestimada?", ["Noelle", "Barbara", "Amber"], key = "q7")

if st.button("Verificar respostas", key="check_quiz_button"):
    if q1 == "30/01":
        score += 1
    if q2 == "La La Land":
        score += 1
    if q3 == "Empatamos":
        score += 1
    if q4 == "Pad Thai":
        score += 1
    if q5 == "Vermelho":
        score += 1
    if q6 == "City of Stars":
        score += 1
    if q7 == "Amber":
        score += 1
    
    if score == 7:
        st.success("🎉 Parabéns! Você acertou tudo e ganhou o presente final!")
        st.session_state.quiz_done = True
    else:
        st.warning(f"Você acertou {score}/7. Tente novamente! ❤️")

if 'quiz_done' not in st.session_state or not st.session_state.quiz_done:
    st.stop()

# ------------------------------
# CARTA FINAL
# ------------------------------
st.header("💌 Cartinha")
st.write("""
Vi, este foi o meu presentinho pra você, espero que você tenha gostado. Fiz ele com muito carinho e tentei ao máximo, através dele, mostrar como tenho me divertido com você.
Desde que você apareceu, a minha vida mudou o sentido, se tornou mais colorida e alegre, como eu digo, você é para mim, como o Sol aparecendo depois de um longo frio e solitário inverno. A vida com você tem mais sabor, eu vejo o futuro com outros olhos e imagino e planejo coisas boas pra gente.
Você é uma mulher incrível, determinada e inteligente! Por favor lembre disso sempre, pense em tudo o que batalhou e ainda batalha, sempre pensando em evoluir e nunca ficar estagnada.
O seu sorriso é a coisa mais bonita, eu acordo todos os dias pensando o que posso fazer para colocar ele no seu rosto novamente.
Desejo muita saúde, paz, alegrias e muito eu te enchendo :) nesse seu novo ciclo! Que você consiga realizar tudo o que você almeja, e pode contar comigo ao seu lado te apoiando!
Eu te amo muito minha linda e sou muito grato e feliz pelo carinho que você tem por mim. E vamos por mais, fazer novas atividades e continuar construindo nossas memórias para preencher esse website!
Espero que você aproveite muito o seu dia e que faça dele um dia especial, assim como voce faz os meus todos os dias! ❤️
""")
