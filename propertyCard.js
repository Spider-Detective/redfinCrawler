const template = document.createElement('template');
template.innerHTML = `
      <style>
       :host {
         display: flex;
         align-items: center;
         width: 45%;
         height: auto;
         background-color: #d4d4d4;
         border: 1.5px solid #d5d5d5;
         box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.1);
         border-radius: 10px;
         overflow: hidden;
         padding: 10px;
         box-sizing: border-box;
         font-family: 'Poppins', sans-serif;
         margin: 10px;
       }
       .container {
         display: flex;
         box-sizing: border-box;
         padding: 10px;
         height: auto;
         flex-flow: row wrap;
         align-content: flex-start;
       }
       .container > .price {
         font-size: 20px;
         font-weight: 600;
         line-height: 1;
         margin: 0;
         margin-bottom: 5px;
         flex: 0 0 100%;
       }
       .container > .img-button {
         margin: 10px;
         position: relative;
       }
       .container .image {
         border: 1px solid #d6d6d6;
         margin: 0;
         border-radius: 30px;
         width: 100%;
         opacity: 1;
         transition: .5s ease;
         backface-visibility: hidden;
       }
       .container > .type {
         font-size: 14px;
         line-height: 1;
         margin-bottom: 5px;
         flex: 0 0 70%;

       }
       .container > .hoa {
         font-size: 14px;
         line-height: 1;
         margin-bottom: 5px;
         flex: 0 0 30%;
       }
       .container > .location {
         font-size: 12px;
         opacity: 0.75;
         line-height: 1;
         margin: 0;
         margin-bottom: 10px;
         flex: 0 0 100%;
       }
       .container > .onMarket {
         font-size: 14px;
         opacity: 0.85;
         line-height: 1;
         margin: 0;
         font-style: italic;
         flex: 0 0 100%;
       }
       .container > .schools {
         font-size: 14px;
         list-style: circle;
         padding-left: 15px;
       }
       .container .middle-button {
         padding: 10px 25px;
         font-size: 12px;
         border-radius: 5px;
         text-transform: uppercase;
         transition: .5s ease;
         opacity: 0;
         position: absolute;
         top: 50%;
         left: 50%;
         transform: translate(-50%, -50%);
         -ms-transform: translate(-50%, -50%)
       }
       .container .url {
         text-decoration: none;
         color: black;
       }
       .img-button:hover .image {
         opacity: 0.3;
       }

       .img-button:hover .middle-button {
         opacity: 1;
       }
       
       @media (max-width: 600px) {
         :host {
          width: 100%;
         }
       }
      </style>
      
      <div class="container">
        <p class="price"></p>
        <div class="img-button">
            <img class="image"/>
            <button class="middle-button"><a class="url" target="_blank">See It</a></button>
        </div>
        <p class="location"></p>
        <p class="type"></p>
        <p class="hoa"></p>
        <p class="onMarket"></p>
        <ul class="schools"></ul>
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
    this.$hoa = this._shadowRoot.querySelector('.container .hoa');
    this.$location = this._shadowRoot.querySelector('.container>.location');
    this.$url = this._shadowRoot.querySelector('.container .url');
    this.$onMarket = this._shadowRoot.querySelector('.container>.onMarket');
    this.$img = this._shadowRoot.querySelector('.container .image');
    this.$schools = this._shadowRoot.querySelector('.container>.schools');
  }
 
  static get observedAttributes() {
    // can only use lowercase letter
    return ['price', 'type', 'url', 'location', 
            'onmarket', 'hoa', 'img',
            'schools'];
  }
 
  attributeChangedCallback(name, oldVal, newVal) {
    this[name] = newVal;
    this.render();
  }
 
  render() {
    this.$price.innerHTML = this.price;
    this.$type.innerHTML = this.type;
    this.$location.innerHTML = this.location;
    this.$hoa.innerHTML = this.hoa;
    this.$url.href = this.url;
    this.$onMarket.innerHTML = this.onmarket;
    this.$img.src = this.img;
    this.$schools.innerHTML = this.schools;
  }
}
window.customElements.define('property-card', PropertyCard);




