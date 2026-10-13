# NOLAP GIFTS

Personalised animated gift pages for the people you love. A gift is one private link that opens like a small mobile app: a login screen, a story, photos, videos, a song, and messages that appear slowly enough to read.

First gift: an 8 month anniversary page for Queen Toria, at `/g/toria-8m-k7q2x9/`.

## Run locally

    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    DEBUG=1 python manage.py runserver

Open http://localhost:8000/g/toria-8m-k7q2x9/

## Deploy (Railway)

Set `SECRET_KEY` and, if needed, `ALLOWED_HOSTS`. `nixpacks.toml` runs `collectstatic`; `Procfile` runs gunicorn. There is no database yet.

## Layout

- `apps/gifts/views.py` has the gift registry. Each gift has an unguessable slug.
- `templates/gifts/anniversary.html` is the gift page (single file: markup, styles, script).
- `static/gifts/toria/` holds that gift's photos, video and song.

Gift pages are served with `noindex` and `robots.txt` disallows `/g/`.

## Music note

The song file is the owner's own upload for a private gift. A public product must use licensed or royalty-free music. See PLAN.md.
