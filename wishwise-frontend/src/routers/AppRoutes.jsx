import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Home from "../pages/Home";
import Wishlists from "../pages/Wishlists";
import Gifts from "../pages/Gifts";
import Reservations from "../pages/Reservations";
import Register from "./pages/Register";


const AppRoutes = () => {
    return (
        <Router>
            <nav className="flex justify-center space-x-6 py-4 bg-blue-600 text-white">
                <Link to="/">Главная</Link>
                <Link to="/wishlists">Вишлисты</Link>
                <Link to="/gifts">Подарки</Link>
                <Link to="/reservations">Бронирования</Link>
            </nav>

            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/wishlists" element={<Wishlists />} />
                <Route path="/gifts" element={<Gifts />} />
                <Route path="/reservations" element={<Reservations />} />
                <Route path="/register" element={<Register />} />

            </Routes>
        </Router>
    );
};

export default AppRoutes;
