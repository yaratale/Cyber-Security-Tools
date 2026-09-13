# 🛡️ Cyber Security Tools: Infrastructure Password Validator

## Project Overview
This repository contains a practical **Python-based Security Script** designed to evaluate password strength against corporate network complexity requirements. 

Instead of relying on basic text validation, this script uses explicit boolean logic to cross-reference user inputs against standard security architecture baselines.

## How It Works (The Logic Breakdown)
The validator assesses five core security metrics to prevent automated brute-force attacks:
1. **Length Verification:** Minimum of 8 characters.
2. **Numerical Density:** Ensures at least one integer (`0-9`) is present.
3. **Casing Variance:** Verifies both uppercase (`A-Z`) and lowercase (`a-z`) implementation.
4. **Cryptographic Special Characters:** Scans for standard punctuation inputs.

## Academic Integration
- **A-Level Mathematics Application:** The scoring mechanism utilizes set logic and item counting metrics to calculate compliance values (`strength_score`), mapping directly to algorithmic logic models.
- **Digital Technology Alignment:** This project mirrors the validation concepts used in secure data-entry architecture and relational database access controls studied in class.
