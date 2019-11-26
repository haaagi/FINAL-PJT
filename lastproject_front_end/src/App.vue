<template>
  <div id="app">
      <navbar />
      <router-link to="/">Home</router-link> 
      <router-link to="/about">About</router-link>
      <router-link to="/moviedetail">moviedetail</router-link>
      


    <router-view/>

  </div>
</template>

<script>
import navbar from './components/navbar';

export default {
  name: 'App',  
  components: {
    navbar,
  },
}
</script>


<style>

</style>
