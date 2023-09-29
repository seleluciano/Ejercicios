
<template>
  <div id="app">
    <Ejercicio1 />
    <Ejercicio2y3 />
    <Ejercicio4y5y6 />
  </div>
</template>

<script>
/* eslint-disable */
import Ejercicio1 from './components/Ejercicio1.vue'
import Ejercicio2y3 from './components/Ejercicio2y3.vue'
import Ejercicio4y5y6 from './components/Ejercicio4y5y6.vue'
export default {
  name: 'App',
  components: {
    Ejercicio1,
    Ejercicio2y3,
    Ejercicio4y5y6
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
