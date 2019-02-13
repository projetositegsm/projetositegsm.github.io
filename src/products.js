import React from 'react';
import ReactDOM from 'react-dom';

import ProductCard from './ProductCard';
import Footer from './Footer';

const data = window.globalData;

ReactDOM.render(
  <React.Fragment>
    {data.products.map((product, idx) =>
      <ProductCard product={product} index={idx} />
    )}
  </React.Fragment>,
  document.getElementById('react-product'),
);

ReactDOM.render(
  <Footer socialLinks={data.social_links} contact={data.contact} />,
  document.getElementById('gsm-contatos'),
);
