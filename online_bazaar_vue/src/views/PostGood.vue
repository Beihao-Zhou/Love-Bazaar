<template>
    <div class="page-post-good">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sell My Good</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Product Name:</label>
                        <div class="control">
                            <input class="input" type="text" placeholder="e.g. women coat" v-model="name">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Category:</label>
                        <div class="control">
                            <div class="select" >
                            <select v-model="category">
                                <option disabled value="">Please select one</option>
                                <option value=1>Books</option>
                                <option value=2>Clothing</option>
                            </select>
                            </div>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Description:</label>
                        <div class="control">
                            <textarea class="textarea" placeholder="The good is wonderful!" v-model="description"></textarea>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Price: ($)</label>
                        <div class="control">
                            <input type="number" class="input" min="0" placeholder="e.g. 10" v-model="price">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Quantity Available:</label>
                        <div class="control">
                            <input type="number" class="input" min="1" placeholder="e.g. 1" v-model="quantity">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Image:</label>
                        <div class="control">
                            <div class="file is-danger has-name is-boxed">
                                <label class="file-label">
                                    <input class="file-input" type="file" ref="image" @change="handleImageUpload()">
                                    <span class="file-cta">
                                    <span class="file-icon">
                                        <i class="fas fa-cloud-upload-alt"></i>
                                    </span>
                                    <span class="file-label">
                                        Product Image...
                                    </span>
                                    </span>
                                    <span class="file-name" v-if="image">
                                        {{image.name}}
                                    </span>
                                    <span class="file-name" v-else>
                                        Product 2022-01-01 at 15.54.25.png
                                    </span>
                                </label>
                            </div>
                        </div>
                    </div>

                    <div class="field mt-5">
                        <div class="control">
                            <label class="checkbox">
                            <input type="checkbox" id="agree" unchecked>
                            I agree to the <a href="#">terms and conditions</a> and understand that all revenues of my goods would be donated to charity. 
                            </label>
                        </div>
                    </div>

                    <div class="notification is-danger is-light" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <button class="button is-danger">Submit</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'PostGood', 
    data() {
        return {
            name: '', 
            category: 0, 
            description: '', 
            price: 0,
            quantity: 1,
            image: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Sell | Online Bazaar'
    },
    methods: {
        handleImageUpload(){
            this.image = this.$refs.image.files[0];
        },
        submitForm() {

            this.errors = []

            if(this.name === '') {
                this.errors.push('The product name is missing')
            }

            if(this.category === 0) {
                this.errors.push('The category is missing')
            }

            if(this.description === '') {
                this.errors.push('The description is missing')
            }

            if(this.price <= 0) {
                this.errors.push('The price is missing')
            }

            if (!document.getElementById('agree').checked) {
                this.errors.push('Please agree with the terms. ')
            }
            

            if(!this.errors.length) {

                let formData = new FormData();

                formData.append("image", this.image);
                formData.append("name", this.name);
                formData.append("category", Number(this.category));
                formData.append("description", this.description);
                formData.append("price", this.price);
                formData.append("quantity", this.quantity);
            
                for (var key of formData.entries()) {
                    console.log(key[0] + ', ' + key[1]);
                }

                axios
                    .post("api/v1/goods/", formData,
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                    .then(response => {
                        toast({
                            message: "Sales posted!", 
                            type: 'is-success', 
                            dismissible: true, 
                            pauseOnHover: true, 
                            duration: 2000, 
                            position: 'bottom-right',
                        })

                        this.$router.push('/my-account')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
            }
            
        }
    }
}
</script>