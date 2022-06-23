#!/usr/bin/env python3

"""Create a project list for a given GitHub organisation"""

__version__ = "0.0.0"

import argparse
import logging
import os
import sys
from datetime import datetime

from docxtpl import DocxTemplate, RichText
from dotenv import load_dotenv
from github import Github

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

load_dotenv()
ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
g = Github(ACCESS_TOKEN)

doc = DocxTemplate(os.path.join("templates", "base_template.docx"))
non_forks = []


def generate_project_list(organization: str) -> None:
    org = g.get_organization(organization)
    repositories = org.get_repos()

    for repo in repositories:
        if repo.fork is False:
            logging.info(f"Now processing {repo.name} ...")
            project = RichText(
                repo.name, url_id=doc.build_url_id(repo.html_url)
            )  # noqa: E501
            contents = repo.get_contents("")
            has_setup_py = any(
                item.path for item in contents if item.path == "setup.py"
            )
            non_forks.append((project, repo, has_setup_py))


def create_docx_file(organization: str) -> None:
    context = {
        "repos": non_forks,
    }
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_dir = "dist"
    os.makedirs(output_dir, exist_ok=True)

    logging.info("Now creating your docx file ...")

    doc.render(context)
    doc.save(
        os.path.join(output_dir, f"{organization}_projects_{timestamp}.docx")
    )  # noqa: E501


def main(args=None):
    """Console script for create_project_list."""
    if not args:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="create-project-list",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.version = __version__
    parser.add_argument("-v", "--version", action="version")

    parser.add_argument(
        "-o",
        "--org",
        dest="organization",
        required=True,
        help="the GitHub organization (slug) for which you'd like to generate the projects list",  # noqa: E501
    )

    args = parser.parse_args(args)

    generate_project_list(args.organization)
    create_docx_file(args.organization)


if __name__ == "__main__":
    main()
