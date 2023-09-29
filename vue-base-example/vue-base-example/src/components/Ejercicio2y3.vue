<template>
<div>
  <h1>Calculadora</h1>
  <p>INGRESE DOS VALORES</p>
     <input v-model="num1" type="number"/>
     <input v-model="num2" type="number"/>
     <div>
      <button v-on:click="operacion(1)">SUMA</button>
      <p v-if="op==1">La suma es {{resultado}}</p>
      <button v-on:click="operacion(2)">RESTA</button>
      <p v-if="op==2">La resta es {{resultado}}</p>
      <button v-on:click="operacion(3)">DIVISION</button>
      <p v-if="op==3">La division es {{resultado}}</p>
      <button v-on:click="operacion(4)">MULTIPLICACION</button>
      <p v-if="op==4">La multiplicacion es {{resultado}}</p>
     </div>
    </div>
</template>

<script>
/* eslint-disable */
export default {
    name: 'App',
    data: function () {
      return {
        num1:0,
        num2:0,
        resultado:undefined,
        op:0
      }
    },
    methods: {
    operacion(op) {
      this.op = op;
      const n1 = parseFloat(this.num1);
      const n2 = parseFloat(this.num2);

      if (!isNaN(n1) && !isNaN(n2)) {
        if (op === 1) {
          this.resultado = n1 + n2;
        } else if (op === 2) {
          this.resultado = n1 - n2;
        } else if (op === 3) {
          this.resultado = n1 * n2;
        } else if (op === 4) {
          this.resultado = n1 / n2;
        }
      } else {
        alert('Por favor ingrese números válidos')
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