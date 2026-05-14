# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Setup for Phase 3 (Next.js Frontend)

## [0.2.0] - 2026-05-06

### Added
- **Phase 2 Complete:** CLI Diagnostic Agent (`envforge-agent`).
- OS detection for Windows, Linux, and WSL2.
- GPU detection via `nvidia-smi`.
- CUDA toolkit, cuDNN, and NCCL version detection.
- Python installation scanner.
- RAM and CPU profiling.
- CLI commands: `envforge diagnose`, `envforge verify`, and `envforge fix`.
- Test suite with multi-platform fixtures.
- Documentation updates for CLI Agent deep-dive.

## [0.1.0] - 2026-05-06

### Added
- **Phase 1 Complete:** Core Backend implementation.
- FastAPI server with async PostgreSQL database (SQLAlchemy 2.0).
- Pure, deterministic Compatibility Engine for resolving package versions.
- Jinja2 Template Engine with a strict regex-based `SafetyFilter`.
- Generation of `setup.sh`, `setup.ps1`, `requirements.txt`, `Dockerfile`, and `devcontainer.json`.
- REST API endpoints for profiles, diagnostics, and script generation.
- Idempotent YAML seed service with 6 starter profiles (e.g., `pytorch-cuda`, `yolov8`).
- AI Layer skeleton with mock provider and Pydantic schemas.
- Comprehensive documentation suite (Architecture, ADRs, Workflows).
