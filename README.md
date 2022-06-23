# create-project-list

[![Continuous Integration](https://github.com/engineervix/create-project-list/actions/workflows/main.yml/badge.svg)](https://github.com/engineervix/create-project-list/actions/workflows/main.yml)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [About](#about)
- [Dependencies](#dependencies)
- [Usage](#usage)
  - [First things first](#first-things-first)
  - [Run the script](#run-the-script)
- [Customize](#customize)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## About

This is a little python script that generates a list of projects for a given GitHub organisation, and saves this information as a table in a **.docx** document

The table is structured as follows:

| No. | Name | Description | Language | Stars | Forks | Last updated | Has `setup.py` ? |
| --- | ---- | ----------- | -------- | ----- | ----- | ------------ | ---------------- |
| 1   |      |             |          |       |       |              |                  |
| 2   |      |             |          |       |       |              |                  |
| 3   |      |             |          |       |       |              |                  |
| ... |      |             |          |       |       |              |                  |

## Dependencies

- [PyGithub](https://github.com/PyGithub/PyGithub) -- a Python library to access the [GitHub REST API](https://docs.github.com/en/rest).
- [python-dotenv](https://github.com/theskumar/python-dotenv) -- Reads key-value pairs from a .env file and can set them as environment variables
- [docxtpl](https://github.com/elapouya/python-docx-template) -- Use a **.docx** document as a [Jinja2](https://jinja.palletsprojects.com) template

## Usage

### First things first

- Clone the repo, create a virtual environment and install the dependencies (`pip install -r requirements.txt`).
- Create a [GitHub personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token), and save it in a `.env` file as `GITHUB_ACCESS_TOKEN=....`. You can make a copy of the provided `.env.sample`:

```bash
cp -v .env.sample .env
```

### Run the script

Make it executable:

```bash
chmod +x ./create_project_list.py
```

Simply pass the organization name to the script:

```bash
./create_project_list.py -o [organization]
```

or

```bash
./create_project_list.py --org [organization]
```

## Customize

If you want additional info for each repo, feel free to customize the script as well as the [template](templates/base_template.docx) to your liking.

Please refer to the [PyGithub docs](https://pygithub.readthedocs.io/en/latest/) for more info. I also created a text file in the **docs** directory to serve as quick reference for methods/properties available for a repo instance, fir example, `repo.html_url` for a repo's URL.
