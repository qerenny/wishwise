import React from "react";
import { Link } from "react-router-dom";

function Layout({ children }) {
  return (
    <div>
      <header style={{
        backgroundColor: "#007BFF",
        padding: "15px 20px",
        boxShadow: "0 4px 8px rgba(0,0,0,0.1)",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center"
      }}>
        <h1 style={{ color: "white", margin: 0 }}>WishWise 🎁</h1>
        <nav>
          <Link to="/" style={linkStyle}>Главная</Link>
          <Link to="/login" style={linkStyle}>Вход</Link>
          <Link to="/register" style={linkStyle}>Регистрация</Link>
          <Link to="/wishlists/my" style={linkStyle}>Мои вишлисты</Link>
        </nav>
      </header>

      {/* Здесь будет отображаться содержимое страниц! */}
      <main style={{ padding: "20px", maxWidth: "900px", margin: "auto" }}>
        {children}
      </main>
    </div>
  );
}

const linkStyle = {
  color: "white",
  textDecoration: "none",
  padding: "10px 15px",
  margin: "0 5px",
  borderRadius: "8px",
  backgroundColor: "rgba(255, 255, 255, 0.2)",
  transition: "0.3s"
};

export default Layout;
