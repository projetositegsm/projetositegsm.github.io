from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html")

data = {
    "social_links": [
        {"img": "imgs/btn_facebook.png", "url": "#"},
        {"img": "imgs/btn_instagram.png", "url": "#"},
        {"img": "imgs/btn_linkedin.png", "url": "#"},
    ],
}

with open("index.html", "w") as file:
    html_content = template.render(data=data)
    file.write(html_content.encode("utf-8"))
