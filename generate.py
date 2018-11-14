from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html")

data = {
    "sections": [
        { "title": "QUEM SOMOS", "id": "gsm-quem-somos" },
        { "title": "ATUAÇÃO", "id": "gsm-atuacao" },
        { "title": "CASES", "id": "gsm-cases" },
        { "title": "PRODUTOS", "id": "gsm-products" },
        { "title": "CONTATO", "id": "gsm-contatos" },
    ],
    "social_links": [
        {"img": "imgs/btn_facebook.png", "url": "#"},
        {"img": "imgs/btn_instagram.png", "url": "#"},
        {"img": "imgs/btn_linkedin.png", "url": "#"},
    ],
    "cases": [
        {
            "thumb": "01_Alphaville Burle Marx_4_bx.jpg",
            "img": "01_Alphaville Burle Marx_4.jpg",
            "label": "Alphaville<br />burle marx",
            "description": "Alphaville - Burle Marx",
        },
        {
            "thumb": "02_Alphaville Jacuhy_1_bx.jpg",
            "img": "02_Alphaville Jacuhy_1.jpg",
            "label": "Alphaville<br />Jacuhy",
            "description": "Alphaville - Jacuhy 1",
        },
        {
            "thumb": "03_Alphaville Barra da Tijuca_8_bx.jpg",
            "img": "03_Alphaville Barra da Tijuca_8.jpg",
            "label": "Alphaville<br />Barra da Tijuca",
            "description": "Alphaville - Barra da Tijuca",
        },
        {
            "thumb": "04_Alphaville Jacuhy_IMG_0179_bx.jpg",
            "img": "04_Alphaville Jacuhy_IMG_0179.jpg",
            "label": "Alphaville<br />Jacuhy",
            "description": "Alphaville - Jacuhy 2",
        },
        {
            "thumb": "05_Alphaville Jacuhy_IMG_0470_bx.jpg",
            "img": "05_Alphaville Jacuhy_IMG_0470.jpg",
            "label": "Alphaville<br />Jacuhy",
            "description": "Alphaville - Jacuhy 3",
        },
        {
            "thumb": "06_Dona Carolina_4_bx.jpg",
            "img": "06_Dona Carolina_4.jpg",
            "label": "Dona<br />Carolina",
            "description": "Dona Carolina",
        },
        {
            "thumb": "07_City Parque Itu_7_bx.jpg",
            "img": "07_City Parque Itu_7.jpg",
            "label": "City<br />Parque Itu",
            "description": "City Parque Itu",
        },
        {
            "thumb": "08_Jardins da Cidade_5_bx.jpg",
            "img": "08_Jardins da Cidade_5.jpg",
            "label": "Jardins<br />da Cidade",
            "description": "Jardins da Cidade",
        },
        {
            "thumb": "09_Tracos da Cidade_3_bx.jpg",
            "img": "09_Tracos da Cidade_3.jpg",
            "label": "Traços<br />da Cidade",
            "description": "Traços da Cidade",
        },
        {
            "thumb": "10_Camacari_BA_4_bx.jpg",
            "img": "10_Camacari_BA_4.jpg",
            "label": "Camaçari<br />(BA)",
            "description": "Camaçari (BA)",
        },
        {
            "thumb": "11_Guarapari_ES_12_bx.jpg",
            "img": "11_Guarapari_ES_12.jpg",
            "label": "Guarapari<br />(ES)",
            "description": "Guarapari (ES)",
        },
        {
            "thumb": "12_Macapa_AP_2_bx.jpg",
            "img": "12_Macapa_AP_2.jpg",
            "label": "Macapá<br />(AP)",
            "description": "Macapá (AP) 1",
        },
        {
            "thumb": "13_Campina Grande_bx.jpg",
            "img": "13_Campina Grande.jpg",
            "label": "Campina<br />Grande",
            "description": "Campina Grande",
        },
        {
            "thumb": "14_Macapa_AP_7_bx.jpg",
            "img": "14_Macapa_AP_7.jpg",
            "label": "Macapá<br />(AP)",
            "description": "Macapá (AP) 2"
        },
        {
            "thumb": "15_PROFISSIONAIS 2017_DJI_0109 ok_bx.jpg",
            "img": "15_PROFISSIONAIS 2017_DJI_0109 ok.jpg",
            "label": "Profissionais<br />2017",
            "description": "Profissionais 2017",
        }
    ]
}

with open("index.html", "w") as file:
    html_content = template.render(data=data)
    file.write(html_content)
