#!/usr/bin/env python3
"""
Script para baixar o modelo faster-whisper-tiny.
Execute UMA VEZ para baixar o modelo tiny (75MB).
"""

import os
from pathlib import Path


def download_tiny_model():
    """Baixa o modelo faster-whisper-tiny para o cache."""

    print("=" * 60)
    print("🔧 DOWNLOAD DO MODELO FASTER-WHISPER-TINY")
    print("=" * 60)

    # Define o cache directory (mesmo local do small)
    cache_dir = os.path.expanduser("~/.cache/whisper-models/")
    os.makedirs(cache_dir, exist_ok=True)

    print(f"📁 Cache directory: {cache_dir}")

    # Desabilita modo offline para download
    os.environ.pop("HF_HUB_OFFLINE", None)
    os.environ.pop("TRANSFORMERS_OFFLINE", None)

    print("\n📥 Iniciando download do modelo TINY (75 MB)...")
    print("   Isso deve levar apenas alguns segundos...")

    try:
        from faster_whisper import WhisperModel

        print("   ⏳ Baixando...")

        # Baixa o modelo tiny
        model = WhisperModel(
            "tiny",  # ← Modelo tiny!
            device="cpu",
            compute_type="int8",
            download_root=cache_dir,
            local_files_only=False,  # Permite download
        )

        print("✅ Download do TINY concluído com sucesso!")

        # Mostra onde foi salvo
        print("\n📂 Arquivos do TINY:")
        tiny_found = False
        for root, dirs, files in os.walk(cache_dir):
            for file in files:
                if file.endswith(".bin") and "tiny" in root.lower():
                    file_path = os.path.join(root, file)
                    size_mb = os.path.getsize(file_path) / (1024 * 1024)
                    print(f"   ✅ {file_path}")
                    print(f"   Tamanho: {size_mb:.1f} MB")
                    tiny_found = True

        if not tiny_found:
            # Procura em qualquer lugar
            for root, dirs, files in os.walk(cache_dir):
                for file in files:
                    if (
                        file.endswith(".bin")
                        and os.path.getsize(file_path) < 100 * 1024 * 1024
                    ):  # < 100MB
                        file_path = os.path.join(root, file)
                        size_mb = os.path.getsize(file_path) / (1024 * 1024)
                        print(f"   ✅ Possível tiny: {file_path}")
                        print(f"   Tamanho: {size_mb:.1f} MB")

        return True

    except Exception as e:
        print(f"\n❌ Erro durante o download: {e}")
        return False


def list_all_models():
    """Lista todos os modelos baixados."""
    print("\n" + "=" * 60)
    print("📋 MODELOS BAIXADOS NO CACHE")
    print("=" * 60)

    cache_dir = os.path.expanduser("~/.cache/whisper-models/")

    for root, dirs, files in os.walk(cache_dir):
        for file in files:
            if file.endswith(".bin"):
                file_path = os.path.join(root, file)
                size_mb = os.path.getsize(file_path) / (1024 * 1024)
                # Identifica o modelo pelo tamanho
                if size_mb > 400:
                    model_type = "SMALL (488MB)"
                elif size_mb > 100:
                    model_type = "BASE (142MB)"
                elif size_mb > 50:
                    model_type = "TINY (75MB)"
                else:
                    model_type = "DESCONHECIDO"

                print(f"\n📁 {model_type}")
                print(f"   Arquivo: {file_path}")
                print(f"   Tamanho: {size_mb:.1f} MB")


if __name__ == "__main__":
    print("🚀 DOWNLOAD DO MODELO TINY\n")

    # Primeiro lista o que já tem
    list_all_models()

    print("\n" + "=" * 60)
    resposta = input("🤔 Deseja baixar o modelo TINY? (s/N): ")

    if resposta.lower() == "s":
        success = download_tiny_model()

        if success:
            print("\n" + "=" * 60)
            print("✅ TUDO PRONTO! Agora você pode:")
            print("   1. Usar 'tiny' no seu transcriber.py")
            print("   2. Testar com: python3 src/services/transcriber.py")
            print("=" * 60)

            # Mostra resultado final
            list_all_models()
        else:
            print("\n" + "=" * 60)
            print("❌ FALHA NO DOWNLOAD. Tente novamente.")
            print("   Verifique sua internet e tente de novo.")
            print("=" * 60)
    else:
        print("\n❌ Download cancelado.")
