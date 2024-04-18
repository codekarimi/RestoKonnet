import { createRouter, createWebHistory } from "vue-router"
// import { useAuthStore } from '../stores/AuthStore'
import LandingView from "../views/Landing.vue"
import Cust_SignInView from "../views/Cust_SignIn.vue"
import Cust_SignUpView from "../views/Cust_SignUp.vue"
import Vend_SignUpView from "../views/Vend_SignUp.vue"
import Vend_SignInView from "../views/Vend_SignIn.vue"
import HomeView from "../views/Home.vue"
import VendorHomeView from "../views/VendHome.vue"
import RestaurantView from "../views/Restaurant.vue"
import DashboardView from "../views/Dashboard.vue"
import { IStaticMethods } from "preline/preline";

window.HSStaticMethods = /** @type {IStaticMethods} */ ({});

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "landing page",
            component: LandingView
        },

        {
            path: "/customerSignIn",
            name: "Customer Sign In page",
            component: Cust_SignInView
        },

        {
            path: "/customerSignUp",
            name: "Customer Sign Up page",
            component: Cust_SignUpView
        },

        {
            path: "/customers/:d",
            name: "Home page",
            component: HomeView
        },

        {
            path: "/vendors/:d",
            name: "Vendor Home page",
            component: VendorHomeView
        },

        {
            path: "/restaurants/:d",
            name: "Restaurant page",
            component: RestaurantView
        },

        {
            path: "/vendorSignUp",
            name: "Vendor Sign Up page",
            component: Vend_SignUpView
        },

        {
            path: "/vendorSignIn",
            name: "Vendor Sign In page",
            component: Vend_SignInView
        },

        {
            path: "/vendors/:d/restaurants",
            name: "Dashboard page",
            component: DashboardView
        }
    ]
});

router.afterEach((to, from, failure) => {
    if (!failure) {
        setTimeout(() => {
            window.HSStaticMethods.autoInit();
        }, 100)
    }
});

// const authStore = useAuthStore();


// router.beforeEach((to, from, next) => {
//     const requiresAuth = to.meta.requiresAuth;

//     if (requiresAuth && !authStore.isAuthenticated) {
//       next('/login'); // Redirect to login page if not authenticated
//     } else {
//       next();
//     }
// });



export default router