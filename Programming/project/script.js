(function(){
  const cart = {};
  const cartCountEl = document.getElementById('cartCount');
  const cartButton = document.getElementById('cartButton');
  const cartDrawer = document.getElementById('cartDrawer');
  const closeCart = document.getElementById('closeCart');
  const overlay = document.getElementById('overlay');
  const cartItemsEl = document.getElementById('cartItems');
  const cartTotalEl = document.getElementById('cartTotal');
  const checkoutBtn = document.getElementById('checkout');
  const searchInput = document.getElementById('search');

  function updateCartCount(){
    const count = Object.values(cart).reduce((s,i)=>s+i.qty,0);
    cartCountEl.textContent = count;
  }

  function renderCart(){
    cartItemsEl.innerHTML = '';
    const keys = Object.keys(cart);
    let total = 0;
    if(keys.length===0){
      cartItemsEl.innerHTML = '<p class="empty">Your cart is empty.</p>';
    }
    keys.forEach(id=>{
      const item = cart[id];
      total += item.price * item.qty;
      const div = document.createElement('div');
      div.className = 'cart-item';
      div.innerHTML = `
        <div class="ci-left">
          <div class="ci-name">${item.name}</div>
          <div class="ci-price">$${(item.price).toFixed(2)}</div>
        </div>
        <div class="ci-right">
          <input type="number" min="1" value="${item.qty}" data-id="${id}" class="ci-qty" />
          <button class="ci-remove" data-id="${id}">Remove</button>
        </div>
      `;
      cartItemsEl.appendChild(div);
    });
    cartTotalEl.textContent = total.toFixed(2);
    updateCartCount();
  }

  function openCart(){
    cartDrawer.classList.add('open');
    overlay.classList.add('show');
    renderCart();
  }
  function closeCartDrawer(){
    cartDrawer.classList.remove('open');
    overlay.classList.remove('show');
  }

  document.addEventListener('click', e=>{
    if(e.target.matches('.add-to-cart')){
      const btn = e.target;
      const id = btn.dataset.id;
      const name = btn.dataset.name;
      const price = parseFloat(btn.dataset.price);
      if(!cart[id]) cart[id] = {id,name,price,qty:0};
      cart[id].qty += 1;
      updateCartCount();
    }
    if(e.target === cartButton) openCart();
    if(e.target === closeCart || e.target === overlay) closeCartDrawer();
    if(e.target.matches('.ci-remove')){
      const id = e.target.dataset.id;
      delete cart[id];
      renderCart();
    }
  });

  document.addEventListener('change', e=>{
    if(e.target.matches('.ci-qty')){
      const id = e.target.dataset.id;
      const val = parseInt(e.target.value,10) || 1;
      if(cart[id]){
        cart[id].qty = val;
        renderCart();
      }
    }
  });

  checkoutBtn.addEventListener('click', ()=>{
    if(Object.keys(cart).length===0){
      alert('Your cart is empty.');
      return;
    }
    alert('Checkout demo — total: $' + cartTotalEl.textContent);
    // clear cart
    Object.keys(cart).forEach(k=>delete cart[k]);
    renderCart();
    closeCartDrawer();
  });

  searchInput.addEventListener('input', e=>{
    const q = e.target.value.toLowerCase();
    document.querySelectorAll('.product').forEach(p=>{
      const title = p.querySelector('.title').textContent.toLowerCase();
      p.style.display = title.includes(q) ? '' : 'none';
    });
  });

  // initial render
  updateCartCount();
})();
