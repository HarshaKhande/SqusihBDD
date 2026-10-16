SQUISH PYTHON POM + DATA-DRIVEN + BDD FRAMEWORK
================================================

WHAT IS INCLUDED
----------------
POM:
  suite_SquishFramework\shared\scripts\pages\login_page.py
  suite_SquishFramework\shared\scripts\pages\home_page.py

DATA DRIVEN:
  suite_SquishFramework\shared\testdata\login_data.csv
  suite_SquishFramework\tst_login_data_driven\test.py

BDD:
  suite_SquishFramework\tst_login_bdd\test.feature
  suite_SquishFramework\tst_login_bdd\test.py
  suite_SquishFramework\shared\steps\login_steps.py

HOOKS:
  suite_SquishFramework\shared\scripts\bdd_hooks.py

UTILITIES:
  suite_SquishFramework\shared\scripts\common.py

OBJECT MAP:
  suite_SquishFramework\shared\scripts\names.py

HOW TO RUN
==========
1. Extract the ZIP.
2. Double-click START_DEMO_SITE.bat.
3. Confirm http://127.0.0.1:8000 opens in Edge/Chrome.
4. Keep the server window open.
5. Open Squish IDE -> File -> Open Test Suite.
6. Select suite_SquishFramework.
7. Configure a supported browser / Edge WebDriver if required.
8. Run tst_login_data_driven.
9. Run tst_login_bdd.

FRAMEWORK FLOW
==============
Data Driven:
CSV -> test.py -> Page Objects -> Object Map -> Web AUT

BDD:
Feature -> Step Definitions -> Page Objects -> Object Map -> Web AUT

For your own application, update BASE_URL in shared\scripts\config.py and replace the sample object definitions in names.py with objects recorded/picked from your AUT.
