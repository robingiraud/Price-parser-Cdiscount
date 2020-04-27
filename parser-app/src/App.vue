<template>
  <div id="app">
    <md-card v-if="toggle && !sending" class="card md-layout-item">
      <h1>Saisir un SKU</h1>
      <md-card-content>
        <md-field>
          <label>SKU Produit</label>
          <md-input v-model="idProduit" type="text"></md-input>
        </md-field>
      </md-card-content>

      <md-button class="md-primary" @click="load">Valider</md-button>
    </md-card>

    <md-card v-if="sending" class="card md-layout-item">
      <pulse-loader></pulse-loader>
    </md-card>
    <md-card v-if="!toggle && !sending" class="card md-layout-item">
      <h1>Prix pour le produit</h1>
      <p>{{ idProduit }}</p>
      <md-card-content>
        <md-field>
          <h1>{{ price }} €</h1>
        </md-field>
      </md-card-content>

      <md-button class="md-primary" @click="toggle = true">Nouvelle recherche</md-button>
    </md-card>
  </div>
</template>

<script>
import axios from 'axios'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

export default {
  name: 'App',
  components: {
    PulseLoader
  },
  data () {
    return {
      sending: false,
      toggle: true,
      idProduit: 'sur4444888884974',
      price: 0
    }
  },
  methods: {
    load () {
      this.sending = true
      axios.post('http://localhost:5000/parse', {idProduit: this.idProduit}, { headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'}
      })
              .then((res) => {
                this.sending = false
                this.toggle = false
                this.price = parseFloat(res.data);
              })
              .catch((error) => {
                console.error(error);
              });
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.card {
  flex: inherit !important;
  width: 300px;
  height: 300px;
  padding: 1em;
}
</style>
