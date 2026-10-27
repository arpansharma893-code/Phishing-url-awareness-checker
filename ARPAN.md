# EWB Phishing URL Awareness Checker

## Overview
Phishing is a trick where an attacker sends a fake link to steal passwords, card numbers or OTPs. The fake link often looks like a real website address.
This project is a small Python program that reads the text of a URL and shows simple warning signs. It does not open the link or use the internet.

## Features
- Detects an @ symbol in the URL
- Flags unusually long URLs (over 100 characters)
- Flags IP-address hostnames
- Flags many hostname segments (5 or more)
- Flags punycode-style hostnames (xn--)
- Flags the HTTP scheme
- Loop: can check many URLs without restarting (type q to quit)
- "REVIEW CAREFULLY" summary with the number of warnings
- Safe handling of wrong input (no crash)

## Requirements
Python 3.10 or later. No extra packages.

## How to Run
Windows: `python phishing_checker.py`

Mac/Linux: `python3 phishing_checker.py`

## Example Output
```
EWB Phishing URL Awareness Checker
Text checks only - this program does not open URLs.

Enter a sample URL (or type q to quit): http://192.0.2.10/account

Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.
Never enter passwords from unexpected links.

Enter a sample URL (or type q to quit): q
Goodbye! Stay alert online.
```

## Testing
| # | Input | Expected | Actual | Result |
|---|-------|----------|--------|--------|
| 1 | https://www.example.com/login | No warning signs | No listed warning signs found | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | IP address and HTTP warnings | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | @ symbol and HTTP warnings | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Many hostname segments warning | PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | Punycode warning | PASS |

The full table is in `tests/test_samples.md`.

## Screenshots
![Sample run](screenshots/sample_run.png)
![Test results](screenshots/test_results.png)

## Improvements
1. **Loop with quit** - The first version closed after one URL. I added a `while True` loop so many URLs can be checked in one run. Typing `q` stops the program. I tested it by entering several URLs and then `q`.
2. **Review carefully summary** - I added the function `has_warnings()` to tell real warnings from information messages. When there are real warnings, the program prints how many were found. I tested it with the five sample URLs.
3. **Handling malformed input** - The input `http://[bad` used to crash with a ValueError. I added try/except so the program prints "This text is not a valid URL format." instead. I tested it with that input and re-ran all five tests.

## Limitations
This is an educational tool. It only reads URL text. It does not visit URLs, scan for malware or prove that a URL is safe. No warning signs found does NOT mean a URL is safe.

## Ethical Use
Use sample strings only. Do not collect credentials. Do not use this project to deceive anyone or to test websites without permission.

## Author
[Your name], [your batch or course], EWB Courses
