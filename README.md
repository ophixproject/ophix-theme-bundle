# ophix-theme-bundle

A bundle of demonstration color-palette themes for Ophix Project Servers:

- Apurplexy
- Bloobs
- Chocolatte
- Eucalypty
- Ice Queen
- Quicksilver
- Sakura
- Stone Cold
- Tealifique

All 9 themes install inactive on `migrate`. Activate whichever one you want with:

```bash
ophix-manage set_theme "Sakura"
```

Or via **Admin Interface → Themes** in the admin UI.

## Installation

```bash
pip install ophix-theme-bundle
ophix-manage migrate
ophix-manage set_theme "Sakura"
```
