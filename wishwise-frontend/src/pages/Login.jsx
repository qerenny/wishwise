import React, { useState } from "react";
import axios from "axios";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(""); // Очистить ошибки перед новым запросом

    try {
      const response = await axios.post("https://your-api-url/users/login", {
        email,
        password,
      });

      console.log("Успешный вход:", response.data);
      // Здесь можно сохранить токен и перенаправить пользователя
    } catch (err) {
      setError("Ошибка входа. Проверьте email и пароль.");
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "50px" }}>
      <h2>Вход</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
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
          type="password"
          placeholder="Пароль"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          style={{ display: "block", marginBottom: "10px", padding: "10px", width: "100%" }}
        />
        <button type="submit" style={{ padding: "10px 20px", backgroundColor: "#007BFF", color: "white", border: "none", cursor: "pointer" }}>
          Войти
        </button>
      </form>
    </div>
  );
}

export default Login;

