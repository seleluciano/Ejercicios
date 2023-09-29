<template>
    <div>
     <h1>LISTA DE COMPRAS</h1>
     <p>Ingrese un nuevo item</p>
     <input v-model="nuevoitem"/>
     <button v-on:click="guardar()">CONFIRMAR</button>
    </div>
    <h2>LISTA DE COMPRAS</h2>
    <ul>
      <li v-for="item in items" :key="item">{{ item }}</li>
    </ul>
</template>
<script>
/* eslint-disable */ 
  export default {
    name: 'App',
    data: function () {
      return {
        nuevoitem:undefined,
        items:[]
      }
    },
    methods: {
  guardar() {
    if (this.nuevoitem.trim() !== '') {
      this.items.push(this.nuevoitem);
      this.nuevoitem = '';
    }
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
body{
   background-color:aquamarine; 
   width: 100%;
  height: 80%;
}
h1,p,button{
    color:black;
    font-family: cursive;
}
input{
   background-color: rgb(128, 156, 247);
}
</style>