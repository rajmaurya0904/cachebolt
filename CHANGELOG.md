# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-11-28

- Initial release of **Cachebolt**.
- Provides a local proxy for Redis and Memcached traffic replay, allowing developers to record production cache access patterns and replay them locally to assess hit‑rate regressions.
- Includes a simple version marker and package scaffolding.

### Known limitations
- Only basic proxy functionality is implemented; advanced features such as TLS support, detailed metrics, and extensive protocol coverage are not yet available.
- No comprehensive test suite beyond import smoke test.
