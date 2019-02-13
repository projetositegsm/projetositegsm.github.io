import React, { useState } from 'react';

const ProductCard = props => {
  const { index } = props;
  const {
    area_description,
    area_localization,
    title,
    location,
    status,
    imageSrcs,
    firstImg,
    description: { list }
  } = props.product;

  const [expandedImg, setExpandedImg] = useState(firstImg);

  return (
    <div className="product-card">
      <div className="section product-images">
        <img
          src={expandedImg}
          className="expanded-img"
        />
        <div className="thumbnails-row">
          {imageSrcs.map((imageSrc, idx) =>
            <div className="thumbnail-col">
              <img
                src={imageSrc}
                onClick={() => setExpandedImg(imageSrc)}
              />
            </div>
          )}
        </div>
      </div>
      <div className="section product-description">
        <div className="title">
          <h3>{title}</h3>
          <p className="localization">{location}</p>
          <p className="status" dangerouslySetInnerHTML={{ __html: status }}></p>
        </div>
        <div className="description-list">
          <ul>
            {list.map((desc, idx) =>
              <li key={idx} dangerouslySetInnerHTML={{ __html: desc }}></li>
            )}
          </ul>
        </div>
        <div className="additional-details">
          <p className="area-description" dangerouslySetInnerHTML={{ __html: area_description }}></p>
          {area_localization.map((a_l, idx) =>
            <p className="area-localization" dangerouslySetInnerHTML={{ __html: a_l }}></p>
          )}
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
