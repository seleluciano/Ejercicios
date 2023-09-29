<template>
  <div>
    <div>
      <h1>LISTA DE COMPRAS</h1>
      <p>Ingrese un nuevo item</p>
      <input v-model="nuevoitem" @keyup.enter="guardar" />
      <p>Ingrese la cantidad</p>
      <input v-model="cantidad" @keyup.enter="guardar" type="number" />
      <button v-on:click="guardar()">CONFIRMAR</button>
    </div>
    <h2>CARRITO</h2>
    <ul>
      <li v-for="item in items" :key="item.id">Objeto: {{ item.objeto }} Cantidad: {{ item.cant }}
        <button v-on:click="eliminar(item.id)">ELIMINAR</button>
      </li>
    </ul>
  </div>
</template>
<script>
/* eslint-disable */
export default {
  name: 'App',
  data: function () {
    return {
      nuevoitem: '',
      cantidad: '',
      items: []
    }
  },
  methods: {
    uuidv4() {
      return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
      });
    },
    guardar() {
      if (!this.nuevoitem || !this.cantidad || this.cantidad <= 0) {
        alert('Por favor, complete ambos campos con valores válidos.');
        return;
      }

      var nuevoId = this.uuidv4();
      this.items.push({
        objeto: this.nuevoitem,
        cant: parseFloat(this.cantidad),
        id: nuevoId
      });

      this.nuevoitem = '';
      this.cantidad = '';
    },
    eliminar(itemID) {
      this.items = this.items.filter((item) => item.id !== itemID);
    }
  }
}
</script>
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: aquamarine;
  width: 100%;
  height: 80%;
}

h1,
p,
h2,
button {
  color: black;
  font-family: cursive;
}

input {
  background-color: rgb(128, 156, 247);
}
</style>