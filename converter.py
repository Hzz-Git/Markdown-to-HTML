import markdown
import sys
import os

def markdown_to_html(input_file, output_file):
    # Read Markdown content
    with open(input_file, 'r', encoding='utf-8') as md_file:
        markdown_text = md_file.read()

    # Convert to HTML
    html_content = markdown.markdown(markdown_text)

    # Write to an HTML file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"Converted '{input_file}' to '{output_file}' successfully!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python converter.py <input_markdown_file> <output_html_file>")
    else:
        input_md = sys.argv[1]
        output_html = sys.argv[2]

        if not os.path.exists(input_md):
            print(f"Error: File '{input_md}' not found!")
        else:
            markdown_to_html(input_md, output_html)
