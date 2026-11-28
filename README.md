# Cachebolt

**A local Redis and Memcached traffic replay proxy that lets backend developers record production cache access patterns and replay them locally to test hit-rate regressions.**

<!-- THE PROBLEM: 2-3 concrete lines on the annoying thing this removes. -->

## Example

```bash
docker-compose up -d
cachebolt replay
```

## Install

```bash
pip install -e ".[dev]"
```

## Usage

<!-- The 2-4 commands people actually need, one line each. -->

## How it works

<!-- 3-6 bullets: what it checks, computes or produces. -->

## Limitations

<!-- Honest and short: what it does NOT do, known gaps. -->

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
