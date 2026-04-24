with open('Vivaldi7.9Stable/CSS/BeautyMedia.css', 'r') as f:
    css_content = f.read()

css_content = css_content.replace('display: none !important;', 'visibility: hidden !important;')

with open('Vivaldi7.9Stable/CSS/BeautyMedia.css', 'w') as f:
    f.write(css_content)
