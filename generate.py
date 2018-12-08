from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html")

data = {
    "palette": {
        "white": "#FFFFFF",
        "light_green": "#4EBC97",
        "dark_green": "#3D5E53",
        "dark_grey": "#4C4C4C",
        "medium_grey": "#BABABA",
    },
    "typography": {
        "desktop": {
            "header": "font-family: 'Sansation', sans-serif; font-size: 24px; font-weight: 700; line-height: 1;",
            "subheader": "font-family: 'Sansation', sans-serif; font-size: 24px; font-weight: 400; line-height: 1;",
            "text_big": "font-family: 'Sansation', sans-serif; font-size: 20px; font-weight: 400; line-height: 1.1;",
            "text": "font-family: 'Sansation', sans-serif; font-size: 16px; font-weight: 400; line-height: 1;",
        },
        "mobile": {
            "header": "font-family: 'Sansation', sans-serif; font-size: 20px; font-weight: 700; line-height: 1;",
            "subheader": "font-family: 'Sansation', sans-serif; font-size: 20px; font-weight: 400; line-height: 1;",
            "text_big": "font-family: 'Sansation', sans-serif; font-size: 16px; font-weight: 400; line-height: 1.1;",
            "text": "font-family: 'Sansation', sans-serif; font-size: 10px; font-weight: 400; line-height: 1;",
        },
    },
    "products": [
        {
            "title": "Portal San Giovanni",
            "location": "Itatiba/SP",
            "status": "Entrega em <strong>novembro de 2019</strong>",
            "area_description": "Terreno: 300m<sup>2</sup> | Casas: 300m<sup>2</sup>",
            "area_localization": [
                "Quadra K - Lote 2",
                "Quadra M - Lote 8",
                "Quadra S1 - Lote 6",
            ],
            "firstImg": "imgs/products/Itatiba_01.jpg",
            "imageSrcs": [
                "imgs/products/Itatiba_01.jpg",
                "imgs/products/Itatiba_02.jpg",
                "imgs/products/Itatiba_03.jpg",
                "imgs/products/Itatiba_04.jpg",
                "imgs/products/Itatiba_05.jpg"
            ],
            "description": {
                "list": [
                    "<strong>3 Suítes</strong> com mezanino",
                    "<strong>2 Vagas</strong> para auto",
                    "<strong>Sala de estar e Escritório</strong> reversível",
                    "<strong>Sala de Jantar e Cozinha</strong> integrados com área de lazer",
                ]
            }
        },
        {
            "title": "Parque da Imprensa",
            "location": "Mogi Mirim/SP",
            "status": "Finalizado. <strong>Pronta entrega</strong>",
            "area_description": "Terreno: 380m<sup>2</sup> | Casa: 155m<sup>2</sup>",
            "area_localization": [],
            "firstImg": "imgs/products/Mogi_01.jpg",
            "imageSrcs": [
                "imgs/products/Mogi_01.jpg",
                "imgs/products/Mogi_02.jpg",
                "imgs/products/Mogi_03.jpg",
                "imgs/products/Mogi_04.jpg",
                "imgs/products/Mogi_05.jpg",
            ],
            "description": {
                "list": [
                    "<strong>3 Dormitórios</strong> (sendo 1 suíte)",
                    "<strong>2 Vagas</strong> para auto",
                    "<strong>TV, Sala de Jantar e Cozinha</strong> integrados com área de lazer",
                ]
            }
        },
        {
            "title": "Alphaville Rio Costa do Sol",
            "location": "Rio das Ostras/RJ",
            "status": "Em desenvolvimento",
            "area_description": "Terreno: 460m<sup>2</sup> | Casa: 330m<sup>2</sup>",
            "area_localization": [
                "Residencial 1 - Quadra O - Lote 7",
            ],
            "firstImg": "imgs/products/Rio_02.jpg",
            "imageSrcs": [
                "imgs/products/Rio_02.jpg",
                "imgs/products/Rio_03.jpg",
                "imgs/products/Rio_04.jpg",
                "imgs/products/Rio_05.jpg",
            ],
            "description": {
                "list": [
                    "<strong>4 Dormitórios</strong> (sendo 2 suítes) com mezanino",
                    "<strong>2 Vagas</strong> para auto",
                    "<strong>Escritório</strong> reversível",
                    "<strong>Sala de Estar, TV, Sala de Jantar e Cozinha</strong> integrados com área de lazer",
                ]
            }
        },
        {
            "title": "Alphaville Jacuhy",
            "location": "Vitória/ES",
            "status": "Entrega em <strong>novembro de 2019</strong>",
            "area_description": "Terreno: 460m<sup>2</sup> | Casa: 330m<sup>2</sup>",
            "area_localization": [
                "Residencial 4 - Quadra L - Lote 13",
            ],
            "firstImg": "imgs/products/Vitoria_01.jpg",
            "imageSrcs": [
                "imgs/products/Vitoria_01.jpg",
                "imgs/products/Vitoria_02.jpg",
                "imgs/products/Vitoria_03.jpg",
                "imgs/products/Vitoria_04.jpg",
                "imgs/products/Vitoria_05.jpg",
            ],
            "description": {
                "list": [
                    "<strong>4 Dormitórios</strong> (sendo 2 suítes) com mezanino",
                    "<strong>2 Vagas</strong> para auto",
                    "<strong>Escritório</strong> reversível",
                    "<strong>Sala de Estar, TV, Sala de Jantar e Cozinha</strong> integrados com área de lazer",
                ]
            }
        }
    ],
    "sections": [
        { "title": "QUEM SOMOS", "id": "gsm-about" },
        { "title": "ATUAÇÃO", "id": "gsm-areas" },
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
