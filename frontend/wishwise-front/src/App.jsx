import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login.jsx";
import Wishlists from "./pages/Wishlists";
import Layout from "./components/Layout";
import Register from "./pages/Register";
import AddGift from "./pages/AddGift";


function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/wishlists/my" element={<Wishlists />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/wishlists/:id/add-gift" element={<AddGift />} />

        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
