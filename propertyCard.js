const template = document.createElement('template');
template.innerHTML = `
      <style>
       :host {
         display: flex;
         align-items: center;
         width: 45%;
         height: 180px;
         background-color: #d4d4d4;
         border: 1px solid #d5d5d5;
         box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.1);
         border-radius: 10px;
         overflow: hidden;
         padding: 10px;
         box-sizing: border-box;
         font-family: 'Poppins', sans-serif;
         margin: 10px;
       }
       .image {
         flex: 0 0 auto;
         width: 160px;
         height: 160px;
         vertical-align: middle;
         border-radius: 5px;
       }
       .container {
         box-sizing: border-box;
         padding: 20px;
         height: 160px;
       }
       .container > .price {
         font-size: 20px;
         font-weight: 600;
         line-height: 1;
         margin: 0;
         margin-bottom: 5px;
       }
       .container > .type {
         font-size: 12px;
         opacity: 0.75;
         line-height: 1;
         margin: 0;
         margin-bottom: 15px;
       }
       .container > .button {
         padding: 10px 25px;
         font-size: 12px;
         border-radius: 5px;
         text-transform: uppercase;
       }
       @media only screen and (max-width: 600px) {
         :host {
          width: 100%;
         }
         .container {
            background-color: red;
         }
       }
      </style>
      
      <div class="container">
        <p class="price"></p>
        <p class="type"></p>
        <p class="location"></p>
        <button><a class="url" target="_blank">See It</a></button>
      </div>
`;
class PropertyCard extends HTMLElement {
  constructor() {
    super();
    this._shadowRoot = this.attachShadow( { mode: 'open' } );
    var content = template.content.cloneNode(true);
    this._shadowRoot.appendChild(content);

    this.$price = this._shadowRoot.querySelector('.container>.price');
    this.$type = this._shadowRoot.querySelector('.container>.type');
    this.$location = this._shadowRoot.querySelector('.container>.location');
    this.$url = this._shadowRoot.querySelector('.container .url');
  }
 
  static get observedAttributes() {
    return ['price', 'type', 'url', 'location'];
  }
 
  attributeChangedCallback(name, oldVal, newVal) {
    this[name] = newVal;
    this.render();
  }
 
  render() {
    this.$price.innerHTML = this.price;
    this.$type.innerHTML = this.type;
    this.$location.innerHTML = this.location;
    this.$url.href = this.url;
  }
}
window.customElements.define('property-card', PropertyCard);




