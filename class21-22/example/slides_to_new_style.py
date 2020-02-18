HEADER = """---
marp: true
---
"""

def change_code_format(text):
    text = text.replace("{.python .listing}", "python")
    text = text.replace("{.python}", "python")
    return text

def split_slides(text):
    slides = []
    latest_slide = ""
    for line in text.split('\n'):
        if line[:2] == '# ':
            # This is a new slide
            slides.append(latest_slide)
            latest_slide = ""
        latest_slide += line + "\n"
    slides.append(latest_slide)
    return slides[1:]

def main():
    # Get text of slide deck.
    f = open('../class22.md', 'r')
    slide_text = f.read()
    f.close()

    # Split slide text into slides.
    slides = split_slides(slide_text)

    # Join slides with a ruler
    slides_joined = '---\n'.join(slides)

    # Change code format
    slides_joined = change_code_format(slides_joined)

    # Add the header
    slides_joined = HEADER + slides_joined

    # Write to disk.
    f = open('../class22-out.md', 'w')
    f.write(slides_joined)
    f.close()

main()