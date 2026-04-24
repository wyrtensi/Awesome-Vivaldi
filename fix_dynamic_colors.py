with open('Vivaldi7.9Stable/Javascripts/BeautyMedia.js', 'r') as f:
    js_content = f.read()

target = """                      html.beautymedia-tabs-animation-enabled .tab#tab-${tabId}.audio-on:not(.active)::before,
                      html.beautymedia-tabs-animation-enabled .tab[data-id="tab-${tabId}"].audio-on:not(.active)::before {"""

replacement = """                      html.beautymedia-tabs-animation-enabled .tab#tab-${tabId}.audio-on:not(.active)::before,
                      html.beautymedia-tabs-animation-enabled .tab[data-id="tab-${tabId}"].audio-on:not(.active)::before,
                      html.beautymedia-tabs-animation-enabled .tab-wrapper[id="tab-${tabId}"] .tab.audio-on:not(.active)::before,
                      html.beautymedia-tabs-animation-enabled .tab-wrapper[data-id="tab-${tabId}"] .tab.audio-on:not(.active)::before {"""

js_content = js_content.replace(target, replacement)

with open('Vivaldi7.9Stable/Javascripts/BeautyMedia.js', 'w') as f:
    f.write(js_content)
