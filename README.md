# Orthophonie Chez Soi
Public files for Orthophonie chez soi, Mélodie Gagnon.  These consist mainly of HTML email templates.

<https://mathieugouin.github.io/orthophoniechezsoi>

## Notes

### HTML
* `<p class="class1 class2">hello</p>` More than one class can be selected (space separated).

### CSS
* `element` (ex: p)
* `#id`
* `.class` (ex: .myClass)
* `element.class` (ex: p.myClass)
* grouping (`,`)
* descendant selector (`space`)
* child selector (`>`)
* adjacent sibling selector (`+`)
* general sibling selector (`~`)

### Development
#### Sync common templates
* `python html_update.py`

#### Github workspace
* `python -m http.server`
* Click "Open in Browser"
* Optional:
  * Open command palette
  * `Simple Browser: Show`
  * Enter the previous URL (from Open in Browser)