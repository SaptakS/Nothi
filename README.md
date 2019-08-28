# Nothi
HTML generator from json data of irc logs. Supports basic searching and tagging

## How to use
- Create a `data.toml` file containing all irclogs in the format as shown in `data.toml.example`
- Install python dependencies with `pip install -r requirements.txt`
- Run `python3 create_html.py`. This will create a `dist/` folder with index.html and all necessary css and js files
- Run `python3 -m http.server`.
- Visit `localhost:8000/dist/` from your favourite browser.
