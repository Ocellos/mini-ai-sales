import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [sales, setSales] = useState([]);
  const [form, setForm] = useState({
    jumlah_penjualan: "",
    harga: "",
    diskon: "",
  });
  const [result, setResult] = useState("");

  // Fetch sales data
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/sales")
      .then(res => setSales(res.data))
      .catch(err => console.error(err));
  }, []);

  // Handle form input
  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  // Handle predict
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("http://127.0.0.1:8000/predict", {
        jumlah_penjualan: Number(form.jumlah_penjualan),
        harga: Number(form.harga),
        diskon: Number(form.diskon)
      });

      setResult(res.data.prediction);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="container">
      <h1>📊 Sales Dashboard</h1>

      {/* TABLE */}
      <h2>Data Penjualan</h2>
      <table className="table">
        <thead>
          <tr>
            <th>Nama</th>
            <th>Penjualan</th>
            <th>Harga</th>
            <th>Diskon</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {sales.map((item, index) => (
            <tr key={index}>
              <td>{item.product_name}</td>
              <td>{item.jumlah_penjualan}</td>
              <td>{item.harga}</td>
              <td>{item.diskon}</td>
              <td
                style={{
                  color: item.status === "Laris" ? "green" : "red",
                  fontWeight: "bold"
                }}
              >
                {item.status}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* FORM */}
      <h2>Prediksi Produk</h2>
      <form className="form" onSubmit={handleSubmit}>
        <input
          name="jumlah_penjualan"
          placeholder="Jumlah Penjualan"
          onChange={handleChange}
          required
        />
        <input
          name="harga"
          placeholder="Harga"
          onChange={handleChange}
          required
        />
        <input
          name="diskon"
          placeholder="Diskon (%)"
          onChange={handleChange}
          required
        />
        <button type="submit">Predict</button>
      </form>

      {/* RESULT */}
      {result && (
        <div className="result">
          <p style={{ color: result === "Laris" ? "green" : "red" }}>
            Hasil Prediksi: {result}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;