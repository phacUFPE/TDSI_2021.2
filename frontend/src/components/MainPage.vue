<template>
  <div class="main">
    <div>
      <h1>Register Product:</h1>
        <b>Name: </b>
        <input
          v-model="product.name"
          :disabled="disabled"
          class="input-space"
        >
        <br />
        <b>Price: </b>$
        <input
          v-model="product.price"
          :disabled="disabled"
          type="number"
          step="0.01"
          min="0"
        >
      <br /><br />
      <button
        :disabled="disabled"
        class="button-space"
        @click.prevent="register(FAILURE_URL)"
      >
        Register
      </button>
      <button
        :disabled="disabled"
        @click.prevent="clearFields"
      >
        Clear
      </button>
    </div>
    <div class="class-space">
      <h1 class="border-bottom">Registered Products:</h1>
      <span v-if="!products.length">No products registered.</span>
      <div
        v-else
        v-for="(product, index) in products"
        :key="index"
      >
        <div align="left" class="border-bottom">
          <h3 class="margin-left">Product #{{index + 1}}</h3><br />
          <b class="margin-left">Name: </b><span>{{ product.name }}</span><br />
          <b class="margin-left">Price: </b><span>{{ product.price }}</span><br />
          <b class="margin-left">Created: </b><span>{{ product.created }}</span><br />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { BACKUP_URL, FAILURE_URL, MESSAGES } from '@/utils/contants'

export default {
  name: 'MainPage',
  data: function () {
    return {
      disabled: false,
      products: [],
      product: {
        name: '',
        price: 0
      }
    }
  },
  created () {
    this.FAILURE_URL = FAILURE_URL
  },
  mounted () {
    this.getProducts()
  },
  methods: {
    /**
     * Sends the register request to the product endpoint.
     * @param URL
     */
    register (URL) {
      let created = false
      this.disabled = true
      axios.post(URL, this.product)
        .then(() => {
          created = true
          window.alert(MESSAGES.PRODUCT_CREATED)
        })
        .finally(() => {
          this.getProducts()
        })
      if (!created && URL !== BACKUP_URL) {
        this.register(BACKUP_URL)
      } else {
        this.disabled = false
      }
    },

    /**
     * Gets all products registered.
     */
    getProducts () {
      axios.get(BACKUP_URL)
        .then((response) => {
          this.products = response.data.data
        })
    },

    /**
     * Clear the product input fields
     */
    clearFields () {
      this.product = {
        name: '',
        price: 0
      }
    }
  }
}
</script>

<style scoped>
.margin-left {
  margin-left: 2rem;
}

.border-bottom {
  padding-bottom: 1rem;
  border-bottom: 2px dashed black;
}

.class-space {
  margin-top: 1rem;
}

.input-space {
  margin-bottom: 1rem;
}

.button-space {
  margin-right: 1rem;
}
</style>
