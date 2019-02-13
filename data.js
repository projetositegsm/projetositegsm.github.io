/*
 * Este arquivo contém as informações relativas as sessões de produto e de contato.
 * Qualquer alteração neste arquivo irá alterar as informações exibidas no website.
 * Para modificar este arquivo você precisa estar logado(a) no site www.github.com
 * e clicar no ícone de edição (Edit this file).
 *
 * 
 * MODIFICAÇÕES NA SESSÃO DE PRODUTOS E CONTATO:
 *   Basta realizar as alterações neste mesmo arquivo ('data.js').
 *
 *
 * MODIFICAÇÕES EM OUTRAS SESSÕES DO SITE:
 *   Modificações de texto em outras sessões do site podem ser realizadas modificando
 *   o arquivo 'index.html'. Basta procurar no arquivo o texto que você deseja modificar
 *   e modificá-lo.
 *
 *
 * MODIFICAÇÕES NA SESSÃO DE CASES:
 *   Modificações na sessão de cases não é suportada de maneira fácil. Contudo é possível
 *   fazer modificações de texto procurando no arquivo 'index.html' o texto que você deseja
 *   modificar e modificá-lo.
  * */

window.globalData = {
  /*
   * Informações de contato
  * */
  contact: {
    addressLineOne: 'Rua Sebastião Lanza, 317',
    addressLineTwo: 'CEP 13805-027 - Mogi Mirim/SP.',
    number: '+55 11 5096-4265',
    email: 'contato@silveiramarques.com',
  },
  social_links: [
    {
      img: 'imgs/btn_facebook.png',
      url:
        'https://www.facebook.com/Silveira-Marques-Engenharia-369667870472927/'
    },
    {
      img: 'imgs/btn_instagram.png',
      url: 'https://www.instagram.com/silveiramarqueseng/'
    },
    {
      img: 'imgs/btn_linkedin.png',
      url: 'https://www.linkedin.com/company/silveira-marques-engenharia/'
    }
  ],


  /*
   * Informações de produtos
   *
   * Observações:
   * - Para alterar o status de uma obra, basta modificar o campo 'status'.
   * - O campo 'imageSrcs' representa as imagens pequenas que aparecem no card do produto.
   *   -->> Tal campo suporta apenas 5 imagens <<--.
   * - Caso seja necessário alterar alguma imagem, não esquecer de colocar o nome dela na lista
   *   'imageSrcs' e também de fazer o upload da nova imagem.
  * */
  products: [
    {
      title: 'Portal San Giovanni',
      location: 'Itatiba / SP',
      status: 'Entrega em <strong>novembro de 2019</strong>',
      area_description: 'Terreno: 380m<sup>2</sup> | Casa: 300m<sup>2</sup>',
      area_localization: [
        'Quadra K - Lote 2',
        'Quadra M - Lote 8',
        'Quadra S1 - Lote 6'
      ],
      firstImg: 'imgs/products/Itatiba_01.jpg',
      imageSrcs: [
        'imgs/products/Itatiba_01.jpg',
        'imgs/products/Itatiba_02.jpg',
        'imgs/products/Itatiba_03.jpg',
        'imgs/products/Itatiba_04.jpg',
        'imgs/products/Itatiba_05.jpg'
      ],
      description: {
        list: [
          '- <strong>3 Suítes</strong> com mezanino',
          '- <strong>2 Vagas</strong> para auto',
          '- <strong>Sala de estar e Escritório</strong> reversível',
          '- <strong>Sala de Jantar e Cozinha</strong> integrados com área de lazer'
        ]
      }
    },
    {
      title: 'Parque da Imprensa',
      location: 'Mogi Mirim / SP',
      status: 'Finalizado. <strong>Pronta entrega</strong>',
      area_description: 'Terreno: 300,00m<sup>2</sup> | Casa: 155m<sup>2</sup>',
      area_localization: [],
      firstImg: 'imgs/products/Mogi_01.jpg',
      imageSrcs: [
        'imgs/products/Mogi_01.jpg',
        'imgs/products/Mogi_02.jpg',
        'imgs/products/Mogi_03.jpg',
        'imgs/products/Mogi_04.jpg',
        'imgs/products/Mogi_05.jpg'
      ],
      description: {
        list: [
          '- <strong>3 Dormitórios</strong> (sendo 1 suíte)',
          '- <strong>2 Vagas</strong> para auto',
          '- <strong>TV, Sala de Jantar e Cozinha</strong> integrados com área de lazer'
        ]
      }
    },
    {
      title: 'Alphaville Rio Costa do Sol',
      location: 'Rio das Ostras / RJ',
      status: 'Em desenvolvimento',
      area_description: 'Terreno: 460m<sup>2</sup> | Casa: 330m<sup>2</sup>',
      area_localization: ['Residencial 1 - Quadra O - Lote 7'],
      firstImg: 'imgs/products/Rio_02.jpg',
      imageSrcs: [
        'imgs/products/Rio_02.jpg',
        'imgs/products/Rio_03.jpg',
        'imgs/products/Rio_04.jpg',
        'imgs/products/Rio_05.jpg'
      ],
      description: {
        list: [
          '- <strong>4 Dormitórios</strong> (sendo 2 suítes) com mezanino',
          '- <strong>2 Vagas</strong> para auto',
          '- <strong>Escritório</strong> reversível',
          '- <strong>Sala de Estar, TV, Sala de Jantar e Cozinha</strong> integrados com área de lazer'
        ]
      }
    },
    {
      title: 'Alphaville Jacuhy',
      location: 'Vitória / ES',
      status: 'Entrega em <strong>novembro de 2019</strong>',
      area_description: 'Terreno: 460m<sup>2</sup> | Casa: 330m<sup>2</sup>',
      area_localization: ['Residencial 4 - Quadra L - Lote 13'],
      firstImg: 'imgs/products/Vitoria_01.jpg',
      imageSrcs: [
        'imgs/products/Vitoria_01.jpg',
        'imgs/products/Vitoria_02.jpg',
        'imgs/products/Vitoria_03.jpg',
        'imgs/products/Vitoria_04.jpg',
        'imgs/products/Vitoria_05.jpg'
      ],
      description: {
        list: [
          '- <strong>4 Dormitórios</strong> (sendo 2 suítes) com mezanino',
          '- <strong>2 Vagas</strong> para auto',
          '- <strong>Escritório</strong> reversível',
          '- <strong>Sala de Estar, TV, Sala de Jantar e Cozinha</strong> integrados com área de lazer'
        ]
      }
    }
  ]
};
