# VALUE REMOVABLE

A lightweight Python URL parameter filtering tool for bug bounty hunters and web application security testers.

**Author:** Vignesh V  
**Alias:** vigneshthehunter

## Overview

VALUE REMOVABLE filters URLs that contain selected redirect-related parameter names and blanks their query values. It is useful for organizing URL lists during authorized web security assessments.

**Input**
```text
https://example.com/page?url=https://google.com&id=10
```

**Output**
```text
https://example.com/page?url=&id=
```

When a URL contains at least one selected parameter, the tool blanks all query parameter values while preserving parameter names and duplicate parameter occurrences.

## Features

- Scan a single URL or a text file containing URLs.
- Match parameter names without case sensitivity.
- Blank query values while preserving parameter names.
- Remove duplicate normalized results.
- Optionally save results to an output file.
- Uses Python's standard library; no third-party packages required.

## Requirements

- Python 3.8 or later.

## Installation

```bash
git clone https://github.com/vignesh8772/parameter-value-removable.git
cd parameter-value-removable
```

## Usage

Scan a single URL:

```bash
python3 filecall.py -u "https://example.com/?redirect=https://example.org&id=10"
```

Scan URLs from a file:

```bash
python3 filecall.py -i urls.txt
```

Save results to a file:

```bash
python3 filecall.py -i urls.txt -o results.txt
```

Show help:

```bash
python3 filecall.py -h
```

## Input file example

Create a file named `urls.txt`:

```text
https://example.com/page?url=https://google.com&id=10
https://example.org/login?next=/dashboard&user=vignesh
https://example.net/search?q=security
```

Only URLs containing one or more configured parameter names are included.

## Security note

Finding a parameter such as `redirect`, `url`, or `next` does **not** prove that a website has an Open Redirect vulnerability. Always validate findings safely and only test systems you own or are explicitly authorized to assess. Respect the scope and rules of each bug bounty program.

## License

No license has been specified yet.
