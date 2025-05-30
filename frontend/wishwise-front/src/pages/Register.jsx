import React, { useState } from "react";
import axios from "axios";

function Register() {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

  try {
    const response = await axios.post(
      `${API_BASE_URL}/users/registration`,
      {
        email,
        username,
        password,
      },
      {
        withCredentials: true,
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    console.log("Регистрация успешна:", response.data);
    setSuccess("Регистрация успешна!");
  } catch (err) {
    console.error("Ошибка регистрации:", err?.response || err);
    setError("Ошибка регистрации. Проверьте введённые данные.");
  }
};




  return (
    <div style={{ textAlign: "center", padding: "50px" }}>
      <h2>Регистрация</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {success && <p style={{ color: "green" }}>{success}</p>}
      <form onSubmit={handleSubmit} style={{ maxWidth: "300px", margin: "auto" }}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          style={{ display: "block", marginBottom: "10px", padding: "10px", width: "100%" }}
        />
        <input
          type="text"
          placeholder="Имя пользователя"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          style={{ display: "block", marginBottom: "10px", padding: "10px", width: "100%" }}
        />
        <input
          type="password"
          placeholder="Пароль"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          style={{ display: "block", marginBottom: "10px", padding: "10px", width: "100%" }}
        />
        <button
          type="submit"
          style={{ padding: "10px 20px", backgroundColor: "#007BFF", color: "white", border: "none", cursor: "pointer" }}
        >
          Зарегистрироваться
        </button>
      </form>
    </div>
  );
}

export default Register;
