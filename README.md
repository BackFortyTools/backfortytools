# Back Forty Tools

Free calculators for the farm, the barn and the woods. Live at https://backfortytools.com (GitHub Pages, deployed from `main`).

## Layout
- `index.html` and `<slug>/index.html` are generated. Don't edit them by hand.
- `_src/site.css` shared styles; `_src/build.py` page shell, schema and sitemap; `_src/tool_NN_*.py` one module per calculator (markup, copy, FAQ, gear links, script).
- `CNAME` sets the custom domain. `sitemap.xml` and `robots.txt` are generated/static.

## Add a tool
1. Copy an existing `_src/tool_NN_*.py`, change slug, copy, formulas and gear links.
2. Add it to `TOOLS` in `_src/tool_00_home.py`.
3. `python3 _src/build.py`, commit, push. Pages deploys in about a minute.

## Affiliate links
Gear sections use `rel="sponsored nofollow"` search links to Tractor Supply and Amazon as placeholders. Replace with tracked links from the affiliate programs once approved (search the modules for `tractorsupply.com` and `amazon.com/s?`).
