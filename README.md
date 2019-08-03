# Nothi
HTML generator from json data of irc logs. Supports basic searching and tagging

## How to use
- Create a `data.json` file containing all irclogs in the format as shown in `data.json.example`
- Run `python3 create_html.py`. This will create a `dist/` folder with index.html and all necessary css and js files
- Run `python3 -m http.server`.
- Visit `localhost:8000/dist/` from your favourite browser.
