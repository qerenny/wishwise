import React, { useState } from "react";
import axios from "axios";

function AddGift({ wishlistId }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    try {
      await axios.post(`${API_BASE_URL}/${wishlistId}/gifts`, {
        title,
        description,
      });

      setSuccess("Подарок успешно добавлен!");
    } catch (err) {
      setError("Ошибка добавления подарка.");
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h3>Добавить подарок</h3>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {success && <p style={{ color: "green" }}>{success}</p>}
      <form onSubmit={handleSubmit} style={{ maxWidth: "300px", margin: "auto" }}>
        <input
          type="text"
          placeholder="Название подарка"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
          style={{ display: "block", marginBottom: "10px", padding: "10px", width: "100%" }}
        />
        <textarea
          placeholder="Описание подарка"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
          style={{ display: "block", marginBottom: "10px", padding: "10px", width: "100%" }}
        />
        <button type="submit" style={{ padding: "10px 20px", backgroundColor: "#007BFF", color: "white", border: "none", cursor: "pointer" }}>
          Добавить
        </button>
      </form>
    </div>
  );
}

export default AddGift;
