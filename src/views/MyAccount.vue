<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My Account</h1>
                <button @click="logout" class="button is-danger">Log out</button>
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="is-size-3 has-text-centered">My Sales</h2>
            </div>

            <ProductBox 
                v-for="good in goods" 
                v-bind:key="good.id" 
                v-bind:product="good" />

            <div class="column is-12">
                <router-link to="/my-account/post-good" class="button is-danger">Add Another Good for Sale</router-link>
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="is-size-3 has-text-centered">My Orders</h2>

                <OrderSummary
                    v-for="order in orders"
                    v-bind:key="order.id"
                    v-bind:order="order" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import OrderSummary from '../components/OrderSummary.vue'
import ProductBox from '../components/ProductBox.vue'

export default {
    name: 'MyAccount', 
    components: {
        OrderSummary, 
        ProductBox
    },
    data() {
        return {
            orders: [], 
            goods: []
        }
    },
    mounted() {
        document.title = 'My account | Online Bazaar'

        this.getMyOrders()
        this.getMyGoods()
    },
    methods: {
        logout() {
            axios.defaults.headers.common['Authorization'] = ''

            localStorage.removeItem('token')
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')

            this.$router.push('/')
        }, 
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/orders/')
                .then(response => {
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading',false)
        }, 
        async getMyGoods() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/goods/')
                .then(response => {
                    this.goods = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading',false)
        }
    }
}
</script>