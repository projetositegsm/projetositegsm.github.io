import React from 'react';

const Footer = props => {
  const { socialLinks, contact } = props;

  return (
    <div className="container">
      <div className="row">
        <div className="col-12">
          <div className="tk-footer">
            <img className="footer-logo" src="imgs/logo_footer.png" />
            <div className="address-n-contact-wrapper">
              <div className="address-wrapper">
                <h3 className="contact-title">CONTATO</h3>
                <p className="contact">
                  {contact.addressLineOne}
                  <br />
                  {contact.addressLineTwo}
                </p>
                <p className="contact">{contact.number}</p>
                <a className="email" href={`mailto:${contact.email}`}>
                  {contact.email}
                </a>
              </div>
              <div className="social-contacts">
                {socialLinks.map((social, idx) =>
                  <a
                    href={social.url}
                    target="_blank"
                  >
                    <img src={social.img} />
                  </a>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Footer;
