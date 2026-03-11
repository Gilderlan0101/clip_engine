## 📝 **README.md CORRIGIDO**

```markdown
# 🎬 Clip Engine

<div align="center">
  <img src="https://img.shields.io/badge/python-3.11%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/status-active--development-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/year-2026-orange" alt="Year">

  **Transforme vídeos longos em Shorts/Reels incríveis automaticamente!** 🚀
</div>

---

## 📋 Sobre o Projeto

Clip Engine é um motor inteligente que processa vídeos automaticamente para criar clipes prontos para **YouTube Shorts**, **Instagram Reels** e **TikTok**.

Ele faz todo o trabalho pesado para você:

- 🎯 **Detecta quem está falando** e dá zoom automático na pessoa certa
- 📝 **Gera legendas palavra por palavra** com emojis e censura automática
- 🎨 **Aplica efeitos visuais** com imagens engraçadas nos momentos certos
- ⚡ **Processa em lote** vários clipes de uma vez
- 🤖 **Usa IA** para identificar falantes e transcrever áudio

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| **🎯 Zoom inteligente** | Acompanha automaticamente quem está falando |
| **📝 Legendas dinâmicas** | Palavra por palavra com emojis 🎉 e censura 🔞 |
| **😄 Memes automáticos** | Imagens engraçadas aparecem em palavras-chave |
| **🎬 Corte automático** | Divide vídeos longos em clipes de 60s |
| **🧠 Detecção de falantes** | Identifica múltiplas pessoas em cena |
| **⚡ Processamento rápido** | Otimizado com O(log n) para performance |
| **🛡️ Censura inteligente** | Bloqueia palavras ofensivas automaticamente |

---

## 🎥 **VEJA O RESULTADO!**

Aqui está um exemplo real do Clip Engine em ação:

<div align="center">
  <video src="processed_videos/final_clips/exemple.mp4" width="320" controls>
    Seu navegador não suporta a tag de vídeo.
  </video>
  <p><i>Preview do processamento automático</i></p>
</div>

**▶️ Para assistir o vídeo de exemplo:**

```bash
# Pelo terminal (Linux/Mac)
vlc processed_videos/final_clips/exemple.mp4

# Ou apenas abra a pasta e clique no arquivo
nautilus processed_videos/final_clips/
```

### Preview do resultado:

```
┌─────────────────────────────────────┐
│                                     │
│    🧔 FALANDO: "E aí galera!"      │
│                                     │
│    📝 LEGENDA: E AÍ GALERA 😂       │
│                                     │
│    ✨ MEME: [CARAMBA!] aparece      │
│                                     │
│    🔍 ZOOM: No falante da vez       │
│                                     │
│    🎬 DURAÇÃO: 60s (formato Shorts) │
│                                     │
└─────────────────────────────────────┘
```

---

## 🚀 Como Instalar

### Pré-requisitos

- Python 3.11 ou superior
- FFmpeg instalado no sistema
- Git

### Passo a Passo

```bash
# 1. Clone o repositório
git clone https://github.com/Gilderlan0101/clip_engine.git
cd clip_engine

# 2. Crie um ambiente virtual
python3.11 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate    # Windows

# 3. Instale as dependências
# Opção 1: Com pip
pip install -r requirements.txt

# Opção 2: Com poetry (recomendado)
pip install poetry
poetry install

# 4. Verifique se o FFmpeg está instalado
ffmpeg -version

# Se não tiver o FFmpeg:
# Ubuntu/Debian: sudo apt install ffmpeg
# Mac: brew install ffmpeg
# Windows: baixe de ffmpeg.org
```

---

## 🎮 Como Usar

### 1️⃣ **Processar um vídeo completo**

```bash
# Coloque seu vídeo na pasta downloads/
python src/utils/ffm_peg.py --video meu_video.mp4
```

### 2️⃣ **Personalizar clipes**

```bash
# Gera 15 clipes de 45 segundos cada
python src/utils/ffm_peg.py --video meu_video.mp4 --num-shots 15 --duration 45
```

### 3️⃣ **Processar sem legendas (apenas cortes)**

```bash
python src/utils/ffm_peg.py --video meu_video.mp4 --no-subtitles
```

### 4️⃣ **Apenas gerar legendas para um clipe já existente**

```bash
python src/services/transcriber.py
```

### 5️⃣ **Processar em lote (mais rápido!)**

```bash
python src/utils/ffm_peg.py --video meu_video.mp4 --batch-size 4
```

---

## 📁 Estrutura de Pastas

```
clip_engine/
├── downloads/               # Vídeos baixados do YouTube
├── processed_videos/
│   ├── raw_clips/          # Clipes brutos sem legendas
│   └── final_clips/        # Vídeos finais COM legendas
│       └── exemple.mp4     # Vídeo de exemplo
├── imagens_efeitos/         # Memes para efeitos visuais
│   ├── comprimentar.jpeg
│   ├── legal.jpeg
│   └── timido.jpeg
├── src/                     # Código fonte
│   ├── controllers/         # Lógica principal
│   ├── services/           # Serviços (transcrição, etc)
│   └── utils/              # Utilitários (ffm_peg.py)
├── requirements.txt         # Dependências pip
├── pyproject.toml          # Configuração poetry
└── README.md               # Este arquivo
```

---

## ⚙️ Personalização

### Adicionar novos memes:

```bash
# 1. Coloque suas imagens em imagens_efeitos/
# 2. Edite src/services/transcriber.py

# Exemplo:
imagens_efeitos/
├── comprimentar.jpeg   # Aparece com "oi", "olá"
├── legal.jpeg          # Aparece com "top", "brabo"
└── timido.jpeg         # Aparece com "tímido", "vergonha"
```

### Configurar palavras censuradas:

```python
# Em src/services/transcriber.py
BAD_WORDS = {
    "suicidio": "sui***",
    "morte": "mo**e",
    # Adicione suas palavras aqui
}
```

---

## 📦 Dependências Principais

- **opencv-python** - Visão computacional
- **mediapipe** - Detecção de faces
- **faster-whisper** - Transcrição de áudio
- **moviepy** - Edição de vídeo
- **yt-dlp** - Download do YouTube
- **fastapi** - API REST
- **numpy** - Cálculos numéricos

---

## 🧠 Performance

O código foi otimizado com algoritmos eficientes:

| Operação | Complexidade | Ganho |
|----------|--------------|-------|
| Detecção de falantes | O(log n) | 1000x mais rápido |
| Busca por posição | O(log n) | 50x mais rápido |
| Transcrição | O(n) otimizado | 4x mais rápido |

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

1. Fork o projeto
2. Crie sua branch (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request


---

## 👨‍💻 Autor

**Gilderlan0101**
- GitHub: [@Gilderlan0101](https://github.com/Gilderlan0101)
- Email: lansilva007gg@gmail.com

---

## ⭐ Mostre seu apoio

Se este projeto te ajudou, dê uma estrela no GitHub!

---

<div align="center">
  Feito com ❤️ e ☕ para a comunidade open source em 2026
</div>
```

