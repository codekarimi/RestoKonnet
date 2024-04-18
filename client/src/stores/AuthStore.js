import { defineStore } from "pinia";
import axios from "axios";


export const useAuthStore = defineStore('auth', {
    state: () => ({
        isAuthenticated: false,
        currentUser: null,
    }),
    actions: {
        async login_customer(custPhone_no) {
            const formData = new FormData()
            formData.append('phone_no', custPhone_no)
            try {
                const response = await axios.post('https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/customer_login', formData);
                const user_data = await axios.get(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/customers/${response.data.id}`)
                this.isAuthenticated = true;
                this.currentUser = user_data.data
                // localStorage.setItem('token', response.data.access_token);
                localStorage.setItem('customer_id', response.data.id)
                localStorage.removeItem('vendor_id');
                return (response.data)
    
            } catch (error) {
                alert(error)
                console.log("Login Failed:", error)
            }

        },
        logout() {
            this.isAuthenticated = false;
            this.currentUser = null
        },
    },
    persist: true,
})