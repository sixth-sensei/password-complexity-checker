## Overview
This script checks and scores a given password for comformity with standard and some extended password policies; runs it against a custom password list consisting of common, default and leaked passwords for possible matches.

<p align="center">
  <img src="https://github.com/sixth-sensei/password-complexity-checker/assets/31647166/d4e3854b-7640-42c5-8d04-4bec3d7e2879" width="auto" title="Script screenshot">
</p>

## How to use
**Step 1:** Initialize Git LFS on your machine with `git lfs install` in order to get the raw pass-list file.

**Step 2:** Clone repository using `git lfs clone` or `git clone` although the former is deprecated but still works.

**Step 3:** Install dependencies

**Step 4:** Simply run `python password_checker.py` or `python3 password_checker.py` depending on your terminal configuration.

voila!


## Dependencies
The following python modules are required for this script to run properly:

* Rich module: If not installed, run `pip install rich` or `python -m pip install rich`
* Emoji module: if not installed, run `pip install emoji` or `python -m pip install emoji`
* Colorama module: If not installed, run `pip install colorama` or `python -m pip install colorama`


**This tool is targeted at the following:**
* System Admins: For user accounts audits
* Cybersecurity enthusiasts: For online accounts security foolproof