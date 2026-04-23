# Changelog

All notable changes to `nekosbest` are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Dates listed before a git commit existed for a release are taken from the
version-bump commit timestamp. For releases older than the project's
changelog-keeping practice, entries are reconstructed from the commit
history and may be less detailed than newer entries.

## [1.2.0] - 2026-04-23

### Added

- `Client` now supports the async context manager protocol. Prefer
  `async with Client() as client: ...` so the underlying HTTP session is
  closed cleanly even if an exception is raised.
- `Client.close()` for explicit cleanup when the context manager pattern
  is not used.
- `HttpClient.close()` for parity at the transport layer.
- `Dimensions`, a frozen dataclass exposing `width: int` and `height: int`.
- `Result.dimensions: Optional[Dimensions]`, populated when the API
  response includes a `dimensions` object with `width` and `height`.
- `__all__` on the top-level `nekosbest` package, pinning the public API.
- `ClientError` is now re-exported from the top-level `nekosbest` package,
  alongside `NekosBestBaseError`, `NotFound`, `APIError`, `Client`,
  `Result`, and `Dimensions`.

### Changed

- `HttpClient` now lazily creates its `aiohttp.ClientSession` on the first
  request and reuses it across subsequent requests. Previously a new
  session was created per call.
- `APIError` now carries a descriptive message
  (`"nekos.best API returned unexpected status code <code>."`). The
  `err.code` attribute is preserved for existing call sites.
- `APIError.__init__` signature is now `code: Optional[int] = None` (was
  `code: int = None`, which was inconsistent with its default).
- `ClientError` raised from connection failures now chains the underlying
  `aiohttp.ClientConnectionError` via `__cause__`, so
  `except ClientError as err: err.__cause__` exposes the real cause.
- User-Agent header now reflects the running Python version at runtime,
  computed from `sys.version_info`, instead of a hard-coded value that
  could drift from the installed interpreter.
- README: modernized the Example to use `asyncio.run` and the current
  `"neko"` category, added a Recommended usage section demonstrating
  `async with`, and added an Exception handling section.

### Fixed

- User-Agent string no longer drifts from the actual running Python
  version.

### Internal

- Added a `pytest` + `pytest-asyncio` + `aioresponses` test harness.
- Added regression tests covering session lifecycle, User-Agent
  composition, exception chaining, and the public API surface.

## [1.1.15] - 2026-03-09

### Added

- New categories: `bleh`, `blowkiss`, `carry`, `clap`, `confused`,
  `kabedon`, `lappillow`, `nya`, `salute`, `shake`, `shocked`, `sip`,
  `spin`, `teehee`, `wag`.

## [1.1.14] - 2026-01-21

### Added

- New endpoints.

### Changed

- Internal: categories list tidied and reordered.

## [1.1.13] - 2025-03-17

### Added

- New endpoints.
- Python 3.13 added to the supported-versions classifiers.

### Removed

- Python 3.8 from the supported-versions classifiers.

## [1.1.12] - 2024-02-07

### Changed

- Updated `aiohttp` requirement range.

## [1.1.11] - 2023-08-18

### Added

- New categories: `nope`, `handshake`, `lurk`, `peck`, `yawn`.

## [1.1.10] - 2023-01-02

### Added

- New categories: `nod`, `nom`, `nope`.

## [1.1.9] - 2022-07-26

### Added

- `husbando` and `yeet` endpoints.

## [1.1.8] - 2022-05-09

### Fixed

- `Result` no longer returns `None` when `amount == 1`.

## [1.1.7] - 2022-05-03

### Added

- New endpoints.

## [1.1.6] - 2022-03-26

### Added

- `waifu` endpoint.

## [1.1.5] - 2022-02-25

Stable release of the `1.1.5a` line.

### Added

- `kitsune` endpoint.

### Changed

- When `amount == 1`, a single `Result` is still returned (a previously
  planned breaking change to always return a list was deferred; see
  `1.2.0` changelog above for the ergonomic pattern in practice).

## [1.1.5a] - 2022-02-16

### Added

- Support for nekos.best API v2.

## [1.1.4] - 2022-01-30

### Changed

- Code simplifications (community contribution — thanks @NekoFanatic).

## [1.1.3] - 2022-01-09

### Added

- `anime_name` field on `Result` (and included in `__repr__`).

### Breaking (since 1.1.0)

- `nekosbest.Result.source_details` was removed. Source details are now
  flattened onto `Result` directly.
- `nekosbest.Results` and `nekosbest.SourceDetails` were removed.

Migration:

```py
# Before (<= 1.0.20)
result.source_details.artist_name

# After (>= 1.1.0)
result.artist_name
```

## [1.0.20] - 2021-07-25

### Added

- Source details on `Result` (via `source_details`).

## [1.0.11] - 2021-06-10

### Changed

- Updated to nekos.best API v1 and the new result model. See the 1.1.x
  migration note above for the follow-up cleanup.
- `Client` now raises a helpful `ValueError` listing valid categories
  when an unknown category is passed.

## [1.0.1] - 2021-05-30

### Changed

- Updated Discord invitation link and PyPI badge.

## [1.0.0] - 2021-05-06

### Added

- `amount` parameter on `Client.get_image`.
- Docstrings on `Result`; custom `__repr__`.

### Breaking

- `Client.teardown` was removed. It is no longer needed to pass it when
  closing the client.
- `HttpClient.session` was removed as a public attribute.

Migration:

```py
# Before (0.x.x)
await client.teardown(bot)

# After (1.0.0+)
# No teardown needed.
```

## [0.1.1] - 2021-02-13

### Added

- New categories.
- README updates.

## [0.1.0] - 2021-02-09

Initial release.
