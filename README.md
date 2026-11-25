# Audio Search

Pet project: upload audio tracks, process them with local models (STT, genre,
embeddings), and search them by name, lyrics or meaning.

Real goal is learning: the same processing pipeline gets built three ways —
Celery + RabbitMQ, Kafka, and serverless (Knative/OpenFaaS) — to compare how
each manages concurrency, scaling and failure.

## Status

Phase 1: skeleton + Celery pipeline + Elasticsearch search + local Kubernetes
(k3d/kind). See `docs/specs/` and `docs/plans/` for the spec-driven work log.

## Stack

- API: FastAPI
- Processing: Celery + RabbitMQ (phase 1), Kafka and serverless come later
- Storage: PostgreSQL (metadata), MinIO (audio), Elasticsearch (search index)
- Models: Whisper-class STT, HuggingFace genre classifier, text embeddings —
  each its own local service
- Deploy: Docker Compose first, then a local Kubernetes cluster

## Non-goals (v1)

- Mobile app, cloud AI APIs, hosting someone else's music catalog, training
  custom models, production hosting/SLA.
