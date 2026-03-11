"""
Brain IA - Agente para gerar títulos de vídeos
Usa Groq API para criar títulos virais baseados em informações do vídeo
"""

import json
import logging
import os
import re
from typing import Dict, List, Optional

from openai import OpenAI

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


class Brain:
    """
    Agente de IA para gerar títulos virais para vídeos.
    Versão melhorada para títulos únicos e variados.
    """

    def __init__(self):
        """Inicializa o agente com configuração da API"""
        # Configuração da API
        self.API_KEY = os.getenv("GROQ_API_KEY") or os.getenv("GLOK_API")

        if not self.API_KEY:
            logger.warning("⚠️ GROQ_API_KEY não encontrada no ambiente")
            self.client = None
        else:
            self.client = OpenAI(
                api_key=self.API_KEY,
                base_url="https://api.groq.com/openai/v1",
            )

        # Limites de uso
        self.daily_limit = 200
        self.requests_today = 0
        self.last_reset = None

        # Template melhorado para títulos ÚNICOS e VARIADOS
        self.prompt_template = """
            Gere {count} títulos DIFERENTES e CRIATIVOS para cortes deste vídeo.

            INFORMAÇÕES DO VÍDEO:
            - Título original: {title}
            - Canal: {uploader}
            - Duração: {duration} segundos
            - Visualizações: {view_count}
            - Descrição: {description}

            REGRAS IMPORTANTES:
            1. ✅ TODOS os títulos devem ser COMPLETAMENTE DIFERENTES entre si
            2. ✅ NÃO repita palavras ou estruturas nos títulos
            3. ✅ Cada título deve ter um ângulo/abordagem ÚNICA
            4. ✅ Máximo 60 caracteres por título
            5. ✅ Use 1-2 emojis no máximo (opcional)
            6. ✅ Crie curiosidade e engajamento
            7. ✅ Seja direto e impactante

            EXEMPLOS DE VARIAÇÃO (NÃO USE ESTES, APENAS COMO REFERÊNCIA):
            - "O segredo que ele revelou 🤯" (abordagem: mistério)
            - "Você não vai acreditar no que aconteceu..." (abordagem: surpresa)
            - "A verdade chocante sobre isso" (abordagem: revelação)
            - "Por que isso está mudando tudo" (abordagem: impacto)
            - "Nunca tinha visto isso antes!" (abordagem: exclusividade)

            FORMATO DE RESPOSTA (APENAS JSON VÁLIDO):
        """

        logger.info("🧠 Brain IA inicializado (modo títulos únicos)")

    def _check_rate_limit(self) -> bool:
        """Verifica limite de requisições de forma simples"""
        from datetime import datetime

        today = datetime.now().date()

        if self.last_reset != today:
            self.requests_today = 0
            self.last_reset = today

        if self.requests_today >= self.daily_limit:
            logger.warning(f"⚠️ Limite diário atingido: {self.daily_limit}")
            return False

        return True

    def generate_titles(self, video_info: Dict[str, any], count: int = 5) -> List[str]:
        """
        Gera títulos ÚNICOS e VARIADOS baseado nas informações do vídeo.

        Args:
            video_info: Dicionário com informações do vídeo
            count: Número de títulos para gerar

        Returns:
            Lista de títulos únicos gerados
        """
        if not self.client:
            logger.error("❌ Cliente API não configurado")
            return self._generate_fallback_titles(video_info, count)

        if not video_info:
            logger.error("❌ Informações do vídeo vazias")
            return self._generate_fallback_titles(video_info, count)

        if not self._check_rate_limit():
            return self._generate_fallback_titles(video_info, count)

        try:
            # Prepara o prompt com as informações do vídeo
            description = video_info.get("description", "")[:300]  # Aumentei para 300
            if description and description.endswith("..."):
                description = description[:-3]

            # Formata duração em minutos
            duration_sec = video_info.get("duration", 0)
            duration_min = f"{duration_sec // 60}:{duration_sec % 60:02d}"

            prompt = self.prompt_template.format(
                count=count * 2,  # Pede o dobro para ter opções
                title=video_info.get("title", "Sem título")[:100],
                uploader=video_info.get("uploader", "Desconhecido"),
                duration=duration_min,
                view_count=self._format_number(video_info.get("view_count", 0)),
                description=description or "Sem descrição disponível",
            )

            # Chama a API
            response = self.client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "system",
                        "content": "Você é um especialista em criar títulos virais ÚNICOS e DIVERSIFICADOS para YouTube. Responda apenas com o JSON contendo a lista de títulos, garantindo que todos sejam diferentes entre si.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.9,  # Aumentei a temperatura para mais criatividade
                max_tokens=500,
            )

            self.requests_today += 1

            # Processa a resposta
            content = response.choices[0].message.content.strip()
            all_titles = self._extract_titles(content)

            if all_titles:
                # Remove duplicatas (case insensitive)
                seen = set()
                unique_titles = []

                for title in all_titles:
                    title_lower = title.lower().strip()
                    if title_lower not in seen and len(title) <= 70:
                        seen.add(title_lower)
                        unique_titles.append(title)

                # Retorna apenas a quantidade solicitada
                final_titles = unique_titles[:count]

                if len(final_titles) < count:
                    logger.warning(
                        f"⚠️ Apenas {len(final_titles)} títulos únicos gerados, completando com fallback"
                    )
                    fallback = self._generate_fallback_titles(
                        video_info, count - len(final_titles)
                    )
                    final_titles.extend(fallback)

                logger.info(f"✅ {len(final_titles)} títulos únicos gerados")
                return final_titles

            return self._generate_fallback_titles(video_info, count)

        except Exception as e:
            logger.error(f"❌ Erro ao gerar títulos: {e}")
            return self._generate_fallback_titles(video_info, count)

    def _extract_titles(self, content: str) -> List[str]:
        """Extrai títulos da resposta da API"""
        # Tenta parsear JSON diretamente
        try:
            titles = json.loads(content)
            if isinstance(titles, list):
                return [str(t).strip('" ') for t in titles if t]
        except:
            pass

        # Tenta encontrar lista JSON no texto
        json_match = re.search(r"\[(.*?)\]", content, re.DOTALL)
        if json_match:
            try:
                # Tenta parsear o JSON encontrado
                json_str = json_match.group(0)
                titles = json.loads(json_str)
                if isinstance(titles, list):
                    return [str(t).strip('" ') for t in titles if t]
            except:
                # Se falhar, tenta extrair manualmente
                items = re.findall(r'"([^"]+)"', json_match.group(1))
                if items:
                    return [item.strip() for item in items if item]

        # Fallback: extrai linhas que parecem títulos
        titles = []
        lines = content.split("\n")

        for line in lines:
            # Remove números, marcadores e espaços
            clean_line = re.sub(r"^[\d\-\*\.\"\']+\s*", "", line).strip(" \"'")
            clean_line = re.sub(r"[,\[\]]$", "", clean_line)

            # Se a linha não estiver vazia e tiver tamanho razoável
            if clean_line and 15 < len(clean_line) < 70:
                # Verifica se parece um título (tem palavras, não é código)
                if re.search(r"[a-zA-ZÀ-ÿ]{3,}", clean_line):
                    titles.append(clean_line)

        return titles[:10]  # Limita a 10 títulos

    def _generate_fallback_titles(self, video_info: Dict, count: int) -> List[str]:
        """Gera títulos fallback criativos quando a API falha"""
        base_title = video_info.get("title", "Vídeo")
        uploader = video_info.get("uploader", "")

        templates = [
            f"🔥 O SEGREDO que {uploader} revelou",
            f"😱 VOCÊ NÃO VAI ACREDITAR - {base_title[:30]}",
            f"⚡ A VERDADE sobre {base_title[:25]}",
            f"🎯 Por que {base_title[:20]} está bombando",
            f"💥 O que {uploader} NÃO te contou",
            f"🚀 A MELHOR parte de {base_title[:20]}",
            f"👀 Isso mudou TUDO - {base_title[:25]}",
            f"📌 O momento CHOCANTE de {base_title[:20]}",
        ]

        # Embaralha os templates
        import random

        random.shuffle(templates)

        # Retorna a quantidade solicitada
        return templates[:count]

    def _format_number(self, num: int) -> str:
        """Formata números grandes de forma legível"""
        if num >= 1_000_000:
            return f"{num/1_000_000:.1f}M"
        elif num >= 1_000:
            return f"{num/1_000:.1f}K"
        return str(num)

    def get_stats(self) -> Dict:
        """Retorna estatísticas simples de uso"""
        from datetime import datetime

        today = datetime.now().date()

        return {
            "requests_hoje": self.requests_today,
            "limite_diario": self.daily_limit,
            "disponivel": self.daily_limit - self.requests_today,
            "data": str(today),
        }
