from bs4 import BeautifulSoup
import requests
import argparse
import os
import sys
import toml


def init_loglist(year):
    baseurl = 'https://dgplug.org/irclogs/{}/'.format(year)
    soup = BeautifulSoup(requests.get(baseurl).text, 'lxml')

    links = [link.get('href') for link in soup.find_all('a') if 'Logs' in link.get('href')]

    logs = []
    for i, link in enumerate(links):
        logs.append({
            "title": "IRC Log {} - {}".format(year, str(i+1).zfill(2)),
            "link": baseurl + link,
            "date": link[5:15],
            "tags": [],
            "speakers": [],
        })

    return logs


def save_log_toml(logs, filename):
    assert type(logs) == list, "logs must be a list of logs"
    toml.dump({'logs': logs}, open(filename, 'w'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create an initial toml file for dgplug logs")
    parser.add_argument("--year", help="The year that should be initialized")
    parser.add_argument("--output", help="The filename to save the output to, defaults to './<year>_logs.toml'")
    args = parser.parse_args()
    if args.year is None:
        parser.print_help()
        sys.exit(1)

    if args.output is None:
        args.output = "{}_logs.toml".format(args.year)

    logs = init_loglist(args.year)
    save_log_toml(logs, args.output)
