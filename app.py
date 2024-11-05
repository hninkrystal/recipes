import markdown
from flask import Flask
app = Flask(__name__)

@app.route("/") #used for telling Flask what URL should trigger our function
def hello_world():
    return "<p>Hello, World!<p>"

@app.route("/recipe/<recipe_name>") #used for telling Flask what URL should trigger our function
def get_recipe(recipe_name):
    
    try:
        with open(f"recipes\\{recipe_name}.md", "r") as md_file: #read content from markdown file
            md_content = md_file.read() ### READ THE FILE
        
        html_content = markdown.markdown(md_content) #converting markdown to html## convert to html using markdown to html converter
        return html_content #return html to browser
    
    except FileNotFoundError:
        return "<p>Recipe Not Found.</p>"
        ##with open("output.html", "w") as html_file: #write html content to file
            ##html_file.write(html_content)
        ##return html


if __name__ == "__main":
    app.run()