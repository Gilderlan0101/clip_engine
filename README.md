🎬 Clip Engine

<div align="center">
<img src="https://img.shields.io/badge/python-3.11%2B-blue" alt="Python Version">
<img src="https://img.shields.io/badge/license-MIT-green" alt="License">
<img src="https://img.shields.io/badge/status-active--development-brightgreen" alt="Status">
<img src="https://img.shields.io/badge/year-2026-orange" alt="Year">

<h3>Transforme vídeos longos em Shorts/Reels incríveis automaticamente! 🚀</h3>
</div>

📋 Sobre o Projeto

Clip Engine é um motor inteligente que processa vídeos automaticamente para criar clipes prontos para YouTube Shorts, Instagram Reels e TikTok.

Ele faz todo o trabalho pesado para você:

🎯 Detecta quem está falando e aplica zoom automático dinâmico.

📝 Gera legendas interativas palavra por palavra com emojis e censura automática.

🎨 Efeitos visuais dinâmicos com inserção de imagens baseadas em contexto.

⚡ Processamento em lote otimizado para alta performance.

🤖 IA Avançada para transcrição (Whisper) e detecção facial (MediaPipe).

🎥 VEJA O RESULTADO!

Aqui está um exemplo real do processamento automático do Clip Engine:

<div align="center">
<video src="processed_videos/final_clips/exemple.mp4" width="320" controls>
Seu navegador não suporta a tag de vídeo. Você pode baixar o vídeo em <a href="processed_videos/final_clips/exemple.mp4">neste link</a>.
</video>
<p><i>Preview: Zoom automático + Legendas dinâmicas + Memes contextuais</i></p>
</div>

✨ Funcionalidades

Funcionalidade

Descrição

🎯 Zoom Inteligente

IA que acompanha o rosto do falante ativo

📝 Legendas Dinâmicas

Estilo "Alex Hormozi" com cores e emojis 🎉

😄 Memes Automáticos

Imagens engraçadas aparecem por gatilhos de palavras

🎬 Corte Automático

Segmentação inteligente em formatos verticais (9:16)

🛡️ Censura Inteligente

Detecta e mascara palavras sensíveis automaticamente

⚡ Performance O(log n)

Algoritmos otimizados para busca e corte rápido

🚀 Como Instalar

Pré-requisitos

Python 3.11+

FFmpeg instalado e configurado no PATH

Git

Passo a Passo

# 1. Clone o repositório
git clone [https://github.com/Gilderlan0101/clip_engine.git](https://github.com/Gilderlan0101/clip_engine.git)
cd clip_engine

# 2. Crie um ambiente virtual
python3.11 -m venv .venv
source .venv/bin/activate  # No Windows use: .venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# Recomendado: Uso do Poetry
# pip install poetry && poetry install


🎮 Como Usar

1️⃣ Processar um vídeo completo

Coloque seu vídeo na pasta downloads/ e execute:

python src/utils/ffm_peg.py --video meu_video.mp4


2️⃣ Personalizar a geração de clipes

# Define quantidade de clipes e duração específica
python src/utils/ffm_peg.py --video meu_video.mp4 --num-shots 10 --duration 60


3️⃣ Apenas Transcrição e Legendas

python src/services/transcriber.py


📁 Estrutura do Projeto

clip_engine/
├── downloads/               # Entrada de vídeos originais
├── processed_videos/
│   ├── raw_clips/           # Segmentos brutos
│   └── final_clips/         # Vídeos finais editados e legendados
├── imagens_efeitos/          # Banco de imagens para memes contextuais
├── src/
│   ├── controllers/         # Orquestração do fluxo
│   ├── services/            # IA, Transcrição e Detecção
│   └── utils/               # Manipulação de vídeo (FFmpeg wrapper)
├── requirements.txt
└── README.md


⚙️ Personalização

Adicionar novos gatilhos visuais (Memes)

Adicione a imagem em imagens_efeitos/.

O sistema mapeia o nome do arquivo para palavras-chave na transcrição.

Lista Negra de Palavras (Censura)

Edite o dicionário BAD_WORDS em src/services/transcriber.py:

BAD_WORDS = {
    "palavra_ruim": "p*******",
    "outra_palavra": "o****_*******"
}


🧠 Performance & Algoritmos

Implementamos lógica de baixo nível para garantir que o processamento não seja o gargalo:

Busca de Frames: O(log n) usando indexação temporal.

Detecção Facial: Processamento paralelo via Mediapipe.

Transcrição: Utilização de faster-whisper com suporte a GPU (CUDA).

🤝 Contribuindo

Faça um Fork.

Crie uma Branch (git checkout -b feature/NovaFuncao).

Dê um Commit (git commit -m 'feat: Adiciona nova função').

Dê um Push (git push origin feature/NovaFuncao).

Abra um Pull Request.

👨‍💻 Autor

Gilderlan0101

GitHub: @Gilderlan0101

Email: lansilva007gg@gmail.com

<div align="center">
<p>Se este projeto foi útil para você, considere dar uma ⭐ no repositório!</p>





Feito com ❤️ e muita ☕ por Gilderlan em 2026
</div>
