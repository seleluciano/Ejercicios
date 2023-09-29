<template>
    <div>
     <p>Hola {{nombre}}!!</p>
     <input v-model="nombre"/>
    </div>
</template>
<script>
/* eslint-disable */ 
  export default {
    name: 'App',
    data: function () {
      return {
        nombre: 'Sele'
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
p{
    color:black;
    font-family: cursive;
}
input{
   background-color: rgb(128, 156, 247);
}
</style>