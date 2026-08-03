import { useEffect, useState } from "react";
import Nav from "../nav/Nav";
import { useSelector } from "react-redux";
import { toast } from "react-toastify";
import BASE_URL from "../../Api";
import axiosInstance from "../../axios-config/api";

function CartHistory() {
    const { currentUser } = useSelector((store) => store.user);
    const [orders, setOrders] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (currentUser?.id) {
            fetchOrderHistory();
        }
    }, [currentUser]);

    const fetchOrderHistory = async () => {
        try {
            const response = await axiosInstance.get(`/orders/${currentUser.id}`);
            setOrders(response.data);
        } catch (err) {
            console.error("Failed to load order history", err);
            toast.error("Failed to load order history");
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            <Nav />
            <div className="container mt-4 mb-5">
                <h2 className="mb-3">Cart / Order History</h2>
                {loading ? (
                    <div className="text-center my-5">
                        <div className="spinner-border text-warning" role="status">
                            <span className="sr-only">Loading...</span>
                        </div>
                    </div>
                ) : orders.length === 0 ? (
                    <div className="alert alert-info text-center mt-4">
                        <h4>No order history found!</h4>
                        <p>You haven't placed any orders yet.</p>
                    </div>
                ) : (
                    orders.map((order) => (
                        <div className="card mb-4 shadow-sm" key={order.id}>
                            <div className="card-header bg-dark text-white d-flex justify-content-between align-items-center flex-wrap">
                                <div>
                                    <strong>Order ID: {order.id}</strong> | Placed on:{" "}
                                    {new Date(order.date).toLocaleString()}
                                </div>
                                <div>
                                    <span className="badge bg-warning text-dark me-2">
                                        {order.payment_mode || "COD"}
                                    </span>
                                    <span className="fw-bold text-success" style={{ fontSize: "16px" }}>
                                        Total: {order.totalBillAmount} Rs.
                                    </span>
                                </div>
                            </div>
                            <div className="card-body">
                                <div className="row mb-3">
                                    <div className="col-md-6">
                                        <p className="mb-1"><strong>Name:</strong> {order.name}</p>
                                        <p className="mb-1"><strong>Email:</strong> {order.email}</p>
                                        <p className="mb-1"><strong>Contact:</strong> {order.contact}</p>
                                    </div>
                                    <div className="col-md-6">
                                        <p className="mb-1"><strong>Delivery Address:</strong></p>
                                        <p className="text-muted">{order.address}</p>
                                    </div>
                                </div>
                                <h5>Items Ordered:</h5>
                                <div className="table-responsive">
                                    <table className="table table-bordered align-middle">
                                        <thead className="table-light">
                                            <tr>
                                                <th></th>
                                                <th>Product</th>
                                                <th>Image</th>
                                                <th>Price</th>
                                                <th>Qty</th>
                                                <th>Total Price</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {order.order_items.map((item, index) => (
                                                <tr key={item.id || index}>
                                                    <td>{index + 1}</td>
                                                    <td>
                                                        <strong>{item.title}</strong>
                                                        {item.warranty_information && (
                                                            <div className="small text-muted">
                                                                Warranty: {item.warranty_information}
                                                            </div>
                                                        )}
                                                    </td>
                                                    <td>
                                                        <img
                                                            src={BASE_URL + item.product_image}
                                                            alt={item.title}
                                                            width="45"
                                                            height="45"
                                                            style={{ objectFit: "cover" }}
                                                        />
                                                    </td>
                                                    <td>{item.price} Rs.</td>
                                                    <td>{item.qty}</td>
                                                    <td>{item.totalPrice} Rs.</td>
                                                </tr>
                                            ))}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    ))
                )}
            </div>
        </>
    );
}

export default CartHistory;
