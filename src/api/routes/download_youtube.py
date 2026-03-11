# routes / main.py ou youtube.py

from typing import Optional

from fastapi import APIRouter, BackgroundTasks, HTTPException, Query, status

from src.services.downloader import VideoDownloader

router = APIRouter(prefix="/api", tags=["download"])

downloader = VideoDownloader("downloads")


@router.get("/download-yt", status_code=status.HTTP_202_ACCEPTED)
async def start_video_download(
    background_tasks: BackgroundTasks,
    url: str = Query(..., description="URL do YouTube"),
    num_parts: Optional[int] = Query(
        4, ge=1, le=12, description="Quantas partes dividir"
    ),
):
    """
    Inicia o download em background e retorna imediatamente.
    Cliente deve fazer polling em outra rota para verificar status.
    """
    if not url:
        raise HTTPException(400, "URL é obrigatória")

    task_id = downloader.process_in_background(
        url=url,
        num_parts=int(num_parts),
        background_tasks=background_tasks,
    )

    return {
        "status": "accepted",
        "message": "Download iniciado em background",
        "task_id": task_id,
        "poll_url": f"/api/download-status/{task_id}",
        "estimated_time": "depende do tamanho do vídeo",
    }


# Opcional: Rota para baixar apenas áudio
@router.get("/download-audio")
async def download_audio_endpoint(
    url: str = Query(..., description="URL do vídeo do YouTube"),
):
    """
    Baixa apenas o áudio do vídeo em MP3
    """
    try:
        # Aqui você pode criar um método específico no downloader
        # ou usar o mesmo com opção de áudio
        import asyncio

        result = await asyncio.to_thread(
            downloader.download_audio,
            url,  # Você precisaria criar este método
        )

        return {
            "message": "Download de áudio concluído",
            "data": result,
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


# Opcional: Rota para verificar informações antes de baixar
@router.get("/video-info")
async def video_info_endpoint(
    url: str = Query(..., description="URL do vídeo do YouTube"),
):
    """
    Retorna informações do vídeo sem baixar
    """
    try:
        import yt_dlp

        def get_info_sync(url):
            with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
                return ydl.extract_info(url, download=False)

        import asyncio

        info = await asyncio.to_thread(get_info_sync, url)

        return {
            "title": info.get("title"),
            "duration": info.get("duration"),
            "uploader": info.get("uploader"),
            "view_count": info.get("view_count"),
            "description": (
                info.get("description")[:1000] + "..."
                if info.get("description")
                else None
            ),
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


@router.get("/create/titles")
async def create_titles_endpoint(
    url: str = Query(..., description="URL do vídeo do YouTube"),
    num_titles: int = Query(5, description="Número de títulos para gerar", ge=1, le=10),
):
    """
    Rota para criar títulos a partir do vídeo

    - **url**: URL do vídeo do YouTube
    - **num_titles**: Número de títulos para gerar (1-10, padrão: 5)
    """
    try:
        target = GetInfoVideo(url=url)
        result = await target.create_titles(num_titles=num_titles)

        return result

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
