function ProductCard({ product }) {
  return (
    <div className="card h-100 shadow-sm">
      <img src={product.thumbnail} className="card-img-top" alt={product.title} />
      <div className="card-body d-flex flex-column">
        <h5>{product.title}</h5>
        <p className="text-muted">{product.brand}</p>
        <p className="fw-bold">${product.price}</p>
        <button className="btn btn-dark mt-auto">Add to Cart</button>
      </div>
    </div>
  );
}
export default ProductCard;