with open('Vivaldi7.9Stable/Javascripts/BeautyMedia.js', 'r') as f:
    js_content = f.read()

# Increase specificity by using #tab-... instead of [id="tab-..."]
js_content = js_content.replace('[id="tab-${tabId}"]', '#tab-${tabId}')

with open('Vivaldi7.9Stable/Javascripts/BeautyMedia.js', 'w') as f:
    f.write(js_content)
