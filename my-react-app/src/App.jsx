import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:5000/products';

function ProductManager() {
  const [products, setProducts] = useState([]);
  const [formData, setFormData] = useState({
    prodid: '',
    prodname: '',
    qty: '',
    prodtype: ''
  });

  const [isEditing, setIsEditing] = useState(false);

  // ✅ Fetch products on component mount
  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      const res = await axios.get(API_URL);
      setProducts(res.data);
      console.log(products)
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (isEditing) {
        await axios.put(`${API_URL}/${formData.prodid}`, formData);
      } else {
        await axios.post(API_URL, formData);
      }
      setFormData({ prodid: '', prodname: '', qty: '', prodtype: '' });
      setIsEditing(false);
      fetchProducts(); // Refresh list
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

  const handleEdit = (product) => {
    setFormData(product);
    setIsEditing(true);
  };

  const handleDelete = async (id) => {
    try {
        console.log(`${API_URL}/${id}`)
      await axios.delete(`${API_URL}/${id}`);
      fetchProducts();
    } catch (error) {
      console.error('Error deleting product:', error);
    }
  };

  return (
    <div>
      <h2>Product Manager</h2>
      <form onSubmit={handleSubmit}>
        <input
          name="prodid"
          placeholder="Product ID"
          value={formData.prodid}
          onChange={handleChange}
          disabled={isEditing}
          required
        />
        <input
          name="prodname"
          placeholder="Product Name"
          value={formData.prodname}
          onChange={handleChange}
          required
        />
        <input
          name="qty"
          type="number"
          placeholder="Quantity"
          value={formData.qty}
          onChange={handleChange}
          required
        />
        <input
          name="prodtype"
          placeholder="Product Type"
          value={formData.prodtype}
          onChange={handleChange}
          required
        />
        <button type="submit">{isEditing ? 'Update' : 'Add'} Product</button>
      </form>

      <table border="1" cellPadding="8" style={{ marginTop: '20px' }}>
        <thead>
          <tr>
            <th>ID</th><th>Name</th><th>Quantity</th><th>Type</th><th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {products.map((p) => (
            <tr key={p.prodid}>
              <td>{p.prodid}</td>
              <td>{p.prodname}</td>
              <td>{p.qty}</td>
              <td>{p.prodtype}</td>
              <td>
                <button onClick={() => handleEdit(p)}>Edit</button>
                <button onClick={() => handleDelete(p.prodid)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ProductManager;
