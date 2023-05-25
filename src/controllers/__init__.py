from fastapi import APIRouter
from src.controllers.youtube_downloader import youtube_route


route_collector = APIRouter()


route_collector.include_router(youtube_route, prefix="youtube/")
