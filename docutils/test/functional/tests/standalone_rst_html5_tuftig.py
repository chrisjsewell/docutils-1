# Default settings for all tests.

settings_overrides = {
    '_disable_config': True,
    'report_level': 2,
    'halt_level': 5,
    'warning_stream': '',
    'input_encoding': 'utf-8',
    'embed_stylesheet': False,
    'auto_id_prefix': '%',
    # avoid "Pygments not found"
    'syntax_highlight': 'none'
}

# Keyword parameters passed to publish_file.
reader_name = 'standalone'
parser_name = 'rst'

# Settings.
settings_overrides['sectsubtitle_xform'] = True
settings_overrides['syntax_highlight'] = 'none'

# Source and destination file names.
test_source = "rst_html5_tuftig.txt"
test_destination = "rst_html5_tuftig.html"

# Keyword parameters passed to publish_file.
writer_name = "html5"

# Settings:
settings_overrides['smart_quotes'] = 'yes'
settings_overrides['footnote_references'] = 'superscript'
settings_overrides['table_style'] = 'booktabs numbered captionbelow'
# local copy of stylesheets:
# (Test runs in ``docutils/test/``, we need relative path from there.)
settings_overrides['stylesheet_dirs'] = ('.', 'functional/input/data')
settings_overrides['stylesheet_path'] = 'minimal.css, tuftig.css'
