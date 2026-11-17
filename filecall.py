#!/usr/bin/env python3
"""VALUE REMOVABLE - URL parameter filter for authorized security testing."""

import argparse
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse


PARAMETERS = {
    "url", "redirect", "target_url", "targeturl",
    "redir", "redirect_uri", "return", "return_to",
    "next", "continue", "r", "r_url", "go", "goto",
    "backurl", "successurl", "ref", "referrer",
    "view", "next_to",
}


def banner():
    print(r"""
 __     __    _   _   _   _ _____
 \ \   / /   | | | | | | | | ____|
  \ \ / /__  | | | | | | | |  _|
   \ V / _ \ | | | | | |_| | |___
    \_/\___/  |_| |_|  \___/|_____|

             VALUE REMOVABLE
       Author : Vignesh V
       Alias  : vigneshthehunter
       Purpose: URL Parameter Filtering
""")


def filter_urls(urls):
    """Return unique URLs with values blanked if a target parameter is present."""
    results = set()
    parameter_names = {name.lower() for name in PARAMETERS}

    for raw_url in urls:
        url = raw_url.strip()
        if not url:
            continue

        parsed = urlparse(url)
        query_pairs = parse_qsl(parsed.query, keep_blank_values=True)

        has_target_parameter = any(
            key.lower() in parameter_names for key, _ in query_pairs
        )
        if not has_target_parameter:
            continue

        # Blank every query value, preserving parameter names and duplicates.
        cleaned_query = urlencode([(key, "") for key, _ in query_pairs])
        cleaned_url = urlunparse((
            parsed.scheme,
            parsed.netloc,
            parsed.path,
            parsed.params,
            cleaned_query,
            parsed.fragment,
        ))
        results.add(cleaned_url)

    return sorted(results)


def main():
    parser = argparse.ArgumentParser(
        description="Find selected URL parameters and blank query values."
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("-i", "--input", help="Read URLs from a text file.")
    source.add_argument("-u", "--url", help="Check one URL.")

    parser.add_argument(
        "-o", "--output",
        help="Write results to a file (otherwise print to the terminal).",
    )
    args = parser.parse_args()

    banner()

    if args.input:
        try:
            with open(args.input, "r", encoding="utf-8") as file:
                urls = file.readlines()
        except OSError as error:
            parser.error(f"could not read input file: {error}")
    else:
        urls = [args.url]

    results = filter_urls(urls)
    if not results:
        print("[-] No matching parameters found.")
        return

    print(f"[+] Matching unique URLs: {len(results)}")

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as file:
                file.write("\n".join(results) + "\n")
        except OSError as error:
            parser.error(f"could not write output file: {error}")
        print(f"[+] Results saved to: {args.output}")
    else:
        print("\n[+] Cleaned URLs:")
        for result in results:
            print(result)


if __name__ == "__main__":
    main()
