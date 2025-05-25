import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

const apiClient = axios.create({
    baseURL: API_BASE_URL,
    headers: { "Content-Type": "application/json" }
});

export const fetchWishlists = async () => {
    const response = await apiClient.get("/wishlists");
    return response.data;
};

export const createWishlist = async (title) => {
    const response = await apiClient.post("/wishlists", { title });
    return response.data;
};

export const addGift = async (wishlistId, title) => {
    await apiClient.post(`/wishlists/${wishlistId}/gifts`, { title });
};

export const deleteGift = async (wishlistId, giftId) => {
    await apiClient.delete(`/wishlists/${wishlistId}/gifts/${giftId}`);
};
