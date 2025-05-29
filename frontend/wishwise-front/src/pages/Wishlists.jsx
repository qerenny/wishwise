import React, { useEffect, useState } from "react";
import { fetchWishlists, createWishlist } from "../api";
import { addGift, deleteGift } from "../api";
const Wishlists = () => {
    const [wishlists, setWishlists] = useState([]);
    const [newWishlist, setNewWishlist] = useState("");
    const [giftTitle, setGiftTitle] = useState("");
    const [selectedWishlist, setSelectedWishlist] = useState(null);
    const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

    useEffect(() => {
        fetchWishlists().then(data => setWishlists(data));
    }, []);

    const handleCreate = async () => {
        if (newWishlist.trim()) {
            await createWishlist(newWishlist);
            setNewWishlist("");
            fetchWishlists().then(data => setWishlists(data));
        }
    };

    const handleAddGift = async () => {
        if (giftTitle.trim() && selectedWishlist) {
            await addGift(selectedWishlist.id, giftTitle);
            setGiftTitle("");
        }
    };

    const handleDeleteGift = async (wishlistId, giftId) => {
        await deleteGift(wishlistId, giftId);
        fetchWishlists().then(data => setWishlists(data));
    };

    return (
        <div className="max-w-2xl mx-auto mt-10 p-5 bg-white shadow-lg rounded-lg">
            <h1 className="text-3xl font-bold text-blue-600 mb-5">Ваши вишлисты</h1>

            {/* Форма создания вишлиста */}
            <input
                type="text"
                placeholder="Введите название вишлиста"
                className="border p-2 mt-4 w-full rounded"
                value={newWishlist}
                onChange={(e) => setNewWishlist(e.target.value)}
            />
            <button className="bg-blue-500 text-white px-4 py-2 mt-2 rounded" onClick={handleCreate}>
                Создать вишлист
            </button>

            {/* Список вишлистов */}
            <ul className="mt-4">
                {wishlists.map(wishlist => (
                    <li key={wishlist.id} className="p-3 border-b text-gray-700">
                        {wishlist.title}
                        <button
                            className="ml-2 bg-green-500 text-white px-3 py-1 rounded"
                            onClick={() => setSelectedWishlist(wishlist)}
                        >
                            Добавить подарок
                        </button>
                    </li>
                ))}
            </ul>

            {/* Форма добавления подарка */}
            {selectedWishlist && (
                <div className="mt-5 p-4 bg-gray-100 rounded">
                    <h2 className="text-xl font-bold text-gray-700">Добавить подарок в "{selectedWishlist.title}"</h2>
                    <input
                        type="text"
                        placeholder="Название подарка"
                        className="border p-2 mt-2 w-full rounded"
                        value={giftTitle}
                        onChange={(e) => setGiftTitle(e.target.value)}
                    />
                    <button
                        className="bg-purple-500 text-white px-4 py-2 mt-2 rounded"
                        onClick={handleAddGift}
                    >
                        Добавить подарок
                    </button>
                </div>
            )}
        </div>
    );
};

export default Wishlists;
