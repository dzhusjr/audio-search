"""Shared processing steps, called the same way from Celery, Kafka consumers
or serverless handlers (phase 1/2/3 only change the transport)."""


def transcribe(track_path: str) -> str:
    raise NotImplementedError


def classify_genre(track_path: str) -> dict:
    raise NotImplementedError


def embed_text(text: str) -> list[float]:
    raise NotImplementedError
